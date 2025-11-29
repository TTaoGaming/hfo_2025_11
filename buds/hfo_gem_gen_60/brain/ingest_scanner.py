import os
import sys
import asyncio
import argparse
import logging
import hashlib
import json
from pathlib import Path
from typing import List, Dict

# Add root to path
sys.path.append(os.getcwd())

from buds.hfo_gem_gen_60.blood.schema import MemoryItem
from buds.hfo_gem_gen_60.memory.database import IronLedger
from buds.hfo_gem_gen_60.nerves.stigmergy_client import StigmergyClient

# Setup Logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger("IngestScanner")

class CanalizationFilter:
    """
    Enforces the Law of Canalization.
    Filters out 'AI Slop' and 'Hallucinations' (e.g., 40k lore leaks).
    """
    FORBIDDEN_TERMS = [
        "Genestealers", "Tyranids", "Imperium of Man", "Space Marines", 
        "Chaos Gods", "Warp Storm", "Exterminatus", "Heretic", 
        "As an AI language model", "I cannot fulfill this request",
        "delve into", "rich tapestry", "orchestrate a symphony" # Stylistic slop
    ]

    @staticmethod
    def is_clean(content: str, file_path: str) -> bool:
        # 1. Check for Forbidden Terms
        for term in CanalizationFilter.FORBIDDEN_TERMS:
            if term.lower() in content.lower():
                logger.warning(f"🚫 SLOP DETECTED in {file_path}: Found '{term}'")
                return False
        
        # 2. Check for Minimum Content (Avoid empty files)
        if len(content.strip()) < 10:
            logger.warning(f"🚫 EMPTY FILE in {file_path}")
            return False

        return True

class IngestScanner:
    def __init__(self):
        self.ledger = IronLedger()
        self.manifest_path = "buds/hfo_gem_gen_60/ingest_manifest.json"
        self.filter = CanalizationFilter()
        self.stigmergy = StigmergyClient()

    def compute_hash(self, content: str) -> str:
        return hashlib.sha256(content.encode('utf-8')).hexdigest()

    def scan_target(self, target_path: str) -> List[str]:
        """
        Recursively find all valid files in the target path.
        Ignores hidden files, pycache, and binary files (heuristic).
        """
        files_to_process = []
        path = Path(target_path)

        if path.is_file():
            files_to_process.append(str(path))
        elif path.is_dir():
            for root, dirs, files in os.walk(path):
                # Ignore hidden dirs, pycache, venv, and audit_trail
                dirs[:] = [d for d in dirs if not d.startswith('.') and d not in [
                    '__pycache__', 'venv', 'audit_trail', 'node_modules', 'sandbox', 
                    'site-packages', 'dist', 'build', 'egg-info', 'my_env', 'env'
                ]]
                
                for file in files:
                    if file.startswith('.'): continue
                    if file.endswith('.pyc'): continue
                    if file.endswith('.db'): continue # Skip databases
                    if file.endswith('.bak'): continue # Skip backups
                    if file.endswith('.log'): continue # Skip logs
                    if file.endswith('.png'): continue # Skip images
                    if file.endswith('.jpg'): continue # Skip images
                    if file.endswith('.jpeg'): continue # Skip images
                    if file.endswith('.gif'): continue # Skip images
                    if file.endswith('.svg'): continue # Skip images
                    if file.endswith('.ico'): continue # Skip images
                    if file.endswith('.zip'): continue # Skip archives
                    if file.endswith('.tar.gz'): continue # Skip archives
                    if file.endswith('.whl'): continue # Skip wheels
                    if file.endswith('.lance'): continue # Skip lance files
                    if 'lock' in file: continue # Skip lock files
                    
                    full_path = os.path.join(root, file)
                    files_to_process.append(full_path)
        
        return sorted(files_to_process)

    def load_manifest(self) -> Dict[str, str]:
        """Load the tracking manifest (path -> status)."""
        if os.path.exists(self.manifest_path):
            with open(self.manifest_path, 'r') as f:
                return json.load(f)
        return {}

    def save_manifest(self, manifest: Dict[str, str]):
        """Save the tracking manifest."""
        with open(self.manifest_path, 'w') as f:
            json.dump(manifest, f, indent=2)

    async def process_queue(self, target: str, force: bool = False):
        """
        Main Loop: Scan -> Filter -> Publish to NATS.
        """
        logger.info(f"🚀 Starting Ingestion Scanner on: {target}")
        
        # Connect to NATS
        await self.stigmergy.connect()
        
        files = self.scan_target(target)
        logger.info(f"🔍 Found {len(files)} files in target.")
        
        manifest = self.load_manifest()
        published_count = 0
        
        for file_path in files:
            try:
                # 1. Read Content
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # 2. Compute Hash
                content_hash = self.compute_hash(content)
                
                # 3. Check Status
                # Check DB first (Source of Truth)
                is_processed_db = self.ledger.is_processed(content_hash)
                
                if is_processed_db and not force:
                    logger.info(f"⏭️  Skipping (Already Processed): {file_path}")
                    manifest[file_path] = "skipped"
                    continue
                
                # 4. Canalization Filter (Anti-Slop)
                if not self.filter.is_clean(content, file_path):
                    logger.warning(f"🛑 REJECTED by Canalization: {file_path}")
                    manifest[file_path] = "rejected_slop"
                    continue

                # 5. Create MemoryItem
                item = MemoryItem(
                    source_path=file_path,
                    content=content,
                    generation=59,
                    category="ingested_file",
                    tags=["auto_ingest"]
                )
                item.content_hash = content_hash # Pre-computed
                
                # 6. Ingest (The Light Lift)
                # Insert raw item first to claim it
                try:
                    self.ledger.insert(item)
                except Exception:
                    # Might exist if we are forcing re-ingest
                    pass
                
                # 7. Publish to NATS (Hot Stigmergy)
                logger.info(f"📡 Publishing to NATS: {file_path}")
                await self.stigmergy.publish_ingest(item.model_dump_json())
                published_count += 1
                
                manifest[file_path] = "queued"
                
            except UnicodeDecodeError:
                logger.warning(f"⚠️  Skipping Binary/Non-UTF8: {file_path}")
                manifest[file_path] = "error_encoding"
            except Exception as e:
                logger.error(f"❌ Error processing {file_path}: {e}")
                manifest[file_path] = f"error: {str(e)}"
            
            # Save manifest periodically
            if published_count % 10 == 0:
                self.save_manifest(manifest)

        self.save_manifest(manifest)
        # Don't close if we are in daemon mode (listening loop)
        # But process_queue is designed as a one-off. 
        # We should probably close here if it's a one-off, but for daemon we need to keep connection.
        # Let's handle connection management in the caller or make it robust.
        # For now, let's just close it here, and the daemon will reconnect or use a persistent connection.
        # Actually, StigmergyClient connects/closes. 
        # If we use it in a loop, we should probably keep it open.
        # Let's modify process_queue to NOT close if we are in daemon mode?
        # Or just let it close and reconnect. It's fine for 1-minute pulses.
        await self.stigmergy.close()
        logger.info(f"🏁 Scanner Complete. Published {published_count} items to NATS.")

    async def listen_to_heartbeat(self, target: str):
        """
        Listens for the 1-Minute Pulse to trigger scanning.
        """
        # We need a separate connection for listening
        listener = StigmergyClient()
        await listener.connect()
        
        async def callback(msg):
            try:
                data = json.loads(msg.data.decode())
                logger.info(f"💓 Pulse Received: {data.get('chant_line', 'Unknown')}")
                # Run scan
                logger.info(f"🔍 Triggering Scan on {target}...")
                # We need to run process_queue. 
                # process_queue is async, so we can await it.
                # But process_queue closes the connection at the end.
                # We should probably fix process_queue to not close if we are reusing self.stigmergy?
                # Or just let it close self.stigmergy, but 'listener' is separate.
                # self.stigmergy is initialized in __init__.
                # If process_queue closes it, we need to reconnect in next call.
                # StigmergyClient.publish_ingest calls connect() if not connected?
                # Let's check StigmergyClient.
                # Assuming it handles reconnection or we need to ensure it.
                await self.process_queue(target)
            except Exception as e:
                logger.error(f"Error processing pulse: {e}")

        await listener.subscribe("hfo.pulse.1min", callback)
        logger.info(f"👂 Listening for hfo.pulse.1min to scan {target}...")
        
        # Keep alive
        while True:
            await asyncio.sleep(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="HFO Gen 59 Ingestion Scanner")
    parser.add_argument("--target", default=".", help="File or Directory to ingest")
    parser.add_argument("--force", action="store_true", help="Force re-ingestion even if hash exists")
    parser.add_argument("--daemon", action="store_true", help="Run in daemon mode listening to heartbeat")
    
    args = parser.parse_args()
    
    scanner = IngestScanner()
    
    if args.daemon:
        try:
            asyncio.run(scanner.listen_to_heartbeat(args.target))
        except KeyboardInterrupt:
            logger.info("Scanner Stopped.")
    else:
        asyncio.run(scanner.process_queue(args.target, args.force))
