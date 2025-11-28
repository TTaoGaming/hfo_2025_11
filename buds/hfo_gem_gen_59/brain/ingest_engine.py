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

from buds.hfo_gem_gen_59.blood.schema import MemoryItem
from buds.hfo_gem_gen_59.brain.librarians import LibrarianCouncil
from buds.hfo_gem_gen_59.memory.database import IronLedger

# Setup Logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger("IngestEngine")

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

class IngestEngine:
    def __init__(self):
        self.council = LibrarianCouncil()
        self.ledger = self.council.ledger # Use the same ledger instance
        self.manifest_path = "buds/hfo_gem_gen_59/ingest_manifest.json"
        self.filter = CanalizationFilter()

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
                # Ignore hidden dirs and pycache
                dirs[:] = [d for d in dirs if not d.startswith('.') and d != '__pycache__']
                
                for file in files:
                    if file.startswith('.'): continue
                    if file.endswith('.pyc'): continue
                    
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
        Main Loop: Scan -> Filter -> Ingest.
        """
        logger.info(f"🚀 Starting Ingestion Engine on: {target}")
        
        files = self.scan_target(target)
        logger.info(f"🔍 Found {len(files)} files in target.")
        
        manifest = self.load_manifest()
        
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
                
                # 5. Ingest (The Heavy Lift)
                logger.info(f"🧠 Ingesting: {file_path}")
                
                # Insert raw item first
                self.ledger.insert(item)
                
                # Run Council (8 Agents + Synthesis)
                await self.council.process_item(item)
                
                manifest[file_path] = "success"
                self.save_manifest(manifest)
                
            except UnicodeDecodeError:
                logger.warning(f"⚠️  Skipping Binary/Non-UTF8: {file_path}")
                manifest[file_path] = "error_encoding"
            except Exception as e:
                logger.error(f"❌ Error processing {file_path}: {e}")
                manifest[file_path] = f"error: {str(e)}"
            
            # Save manifest after each file
            self.save_manifest(manifest)

        logger.info("🏁 Ingestion Complete.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="HFO Gen 59 Ingestion Engine")
    parser.add_argument("target", help="File or Directory to ingest")
    parser.add_argument("--force", action="store_true", help="Force re-ingestion even if hash exists")
    
    args = parser.parse_args()
    
    engine = IngestEngine()
    asyncio.run(engine.process_queue(args.target, args.force))
