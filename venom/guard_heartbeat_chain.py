import asyncio
import json
import os
import sys
import logging
import hashlib
from datetime import datetime
from typing import Dict, Any, Optional, Literal
from pydantic import BaseModel, Field
from nats.aio.client import Client as NATS

# Setup Logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger("HiveGuard")

# --- Constants ---
MANTRA = """I am the Node, the Earth, the Seed,
Swarmlord of Webs is the one I heed.
From Karmic Web, where Wisdom flows,
To Swarm Web, where the Willpower grows.
In Simulation Web, I Weave the state,
Obsidian Hourglass, the Engine of Fate.
A Prescient Path in State-Action Space,
One Mind, One Swarm, in time and place."""
EXPECTED_HASH = hashlib.sha256(MANTRA.encode("utf-8")).hexdigest()

# --- Models (Mirrored from cleanroom_prey_1111.py) ---
class StigmergyPillars(BaseModel):
    ontos: Dict[str, Any]
    chronos: Dict[str, Any]
    topos: Dict[str, Any]
    telos: Dict[str, Any]
    logos: Dict[str, Any]
    pathos: Dict[str, Any]
    ethos: Dict[str, Any]
    techne: Dict[str, Any]

class HeartbeatSignal(BaseModel):
    id: str
    timestamp: str
    phase: str
    pillars: StigmergyPillars
    content: str
    mantra_hash: str
    previous_signal_id: Optional[str] = None
    delta_seconds: float = 0.0

# --- Guard Logic ---

class HeartbeatGuard:
    def __init__(self):
        self.last_signal: Optional[HeartbeatSignal] = None
        self.chain_length = 0
        self.broken_links = 0

    def check_signal(self, signal: HeartbeatSignal):
        status_flags = []
        
        # 1. Check Mantra Hash
        if signal.mantra_hash != EXPECTED_HASH:
            status_flags.append("❌ BAD_HASH")
        else:
            status_flags.append("✅ HASH_OK")

        # 2. Check Chain Integrity
        if self.last_signal:
            if signal.previous_signal_id == self.last_signal.id:
                status_flags.append("🔗 CHAIN_OK")
                self.chain_length += 1
            else:
                status_flags.append(f"💔 CHAIN_BROKEN (Exp: {self.last_signal.id[:8]}..., Got: {str(signal.previous_signal_id)[:8]}...)")
                self.broken_links += 1
                self.chain_length = 0 # Reset chain count
        else:
            status_flags.append("🆕 CHAIN_START")
            self.chain_length = 1

        # 3. Check Timing vs Cynefin State
        cynefin = signal.pillars.techne.get("complexity", "Unknown")
        delta = signal.delta_seconds
        
        # Define expected ranges (allowing for some jitter/execution time)
        # Chaotic: ~5s
        # Others: ~60s
        timing_status = "❓ UNKNOWN_STATE"
        
        if cynefin == "Chaotic":
            # Allow 4s to 10s (execution time might add up)
            if 4.0 <= delta <= 15.0: 
                timing_status = "✅ TIMING_OK (Chaotic)"
            elif delta < 4.0:
                timing_status = "⚠️ TOO_FAST (Chaotic)"
            else:
                timing_status = f"⚠️ TOO_SLOW (Chaotic, {delta:.2f}s)"
        elif cynefin in ["Clear", "Complicated", "Complex", "Confused"]:
            # Allow 55s to 70s
            if 55.0 <= delta <= 75.0:
                timing_status = f"✅ TIMING_OK ({cynefin})"
            elif delta < 55.0:
                timing_status = f"⚠️ TOO_FAST ({cynefin})"
            else:
                timing_status = f"⚠️ TOO_SLOW ({cynefin}, {delta:.2f}s)"
        
        # Special case for first signal or very long gaps (start of loop)
        if "CHAIN_START" in status_flags or delta == 0.0:
            timing_status = "ℹ️ FIRST_PULSE"

        status_flags.append(timing_status)

        # Log Result
        log_msg = f"[{signal.timestamp}] ID:{signal.id[:8]} | {' '.join(status_flags)} | Chain:{self.chain_length}"
        if "BROKEN" in str(status_flags) or "BAD" in str(status_flags):
            logger.error(log_msg)
        else:
            logger.info(log_msg)

        self.last_signal = signal

async def main():
    nats_url = os.getenv("NATS_URL", "nats://localhost:4225")
    nc = NATS()
    
    try:
        await nc.connect(servers=[nats_url])
        logger.info(f"🛡️ Hive Guard Connected to NATS at {nats_url}")
    except Exception as e:
        logger.error(f"Failed to connect to NATS: {e}")
        return

    guard = HeartbeatGuard()

    async def message_handler(msg):
        try:
            data = json.loads(msg.data.decode())
            signal = HeartbeatSignal(**data)
            guard.check_signal(signal)
        except Exception as e:
            logger.error(f"Failed to parse heartbeat: {e}")

    # Subscribe to all heartbeats
    await nc.subscribe("hfo.heartbeat.>", cb=message_handler)
    logger.info("🛡️ Monitoring 'hfo.heartbeat.>' for unbroken chains...")

    # Keep running
    while True:
        await asyncio.sleep(1)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Guard stopping...")
