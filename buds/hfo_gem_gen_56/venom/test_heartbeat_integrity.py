"""
# ==================================================================
# 🧪 VENOM: Heartbeat Integrity Test
# ==================================================================
# Purpose: Verify the "Secure Heartbeat" chain, hash integrity, and
#          Cynefin state transitions (Resting vs Chaotic).
# ==================================================================
"""

import sys
import os
import asyncio
import logging
import hashlib
import importlib.util

# Add the root path to sys.path to import body.hfo_sdk
sys.path.append(os.path.abspath("."))

# Load the agent module dynamically to avoid package conflicts
spec = importlib.util.spec_from_file_location(
    "cleanroom_prey_1111", "buds/hfo_gem_gen_56/body/hands/cleanroom_prey_1111.py"
)
if spec is None or spec.loader is None:
    raise ImportError("Could not load cleanroom_prey_1111")
cleanroom_prey_1111 = importlib.util.module_from_spec(spec)
sys.modules["cleanroom_prey_1111"] = cleanroom_prey_1111
spec.loader.exec_module(cleanroom_prey_1111)

PreyAgent = cleanroom_prey_1111.PreyAgent
MANTRA_HASH = cleanroom_prey_1111.MANTRA_HASH
MANTRA = cleanroom_prey_1111.MANTRA


# Setup Logging
logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger("VenomHeartbeat")


async def test_heartbeat_integrity():
    logger.info("🐍 Venom: Initiating Heartbeat Integrity Test...")

    # 1. Verify Hash Logic
    expected_hash = hashlib.sha256(MANTRA.encode("utf-8")).hexdigest()
    if MANTRA_HASH != expected_hash:
        logger.error(f"❌ Hash Mismatch! Code: {MANTRA_HASH} vs Calc: {expected_hash}")
        return
    logger.info(f"✅ Mantra Hash Verified: {MANTRA_HASH[:8]}...")

    # 2. Setup Agent (Mocking Stigmergy for speed/offline)
    # We use a dummy client that just logs
    class MockStigmergy:
        async def publish(self, subject, payload):
            pass  # No-op for test

        async def connect(self):
            pass

    agent = PreyAgent(
        agent_id="venom_test_subject",
        stigmergy=MockStigmergy(),
        mission="Heartbeat Test",
    )

    # 3. Simulate Heartbeats (Resting -> Chaotic)
    logger.info("\n--- Phase 1: Resting State (Clear) ---")
    agent.current_cynefin_state = "Clear"

    # Emit 3 heartbeats (simulating the internal calls of a loop)
    # We manually call emit_heartbeat to control the flow without running the full LLM loop
    await agent.emit_heartbeat("Perceive", "Scanning environment (Clear)...")
    await asyncio.sleep(0.1)  # Small delay to ensure timestamp diff
    await agent.emit_heartbeat("React", "Planning (Clear)...")
    await asyncio.sleep(0.1)
    await agent.emit_heartbeat("Execute", "Action (Clear)...")

    logger.info("\n--- Phase 2: Chaotic State (Chaotic) ---")
    agent.current_cynefin_state = "Chaotic"

    await agent.emit_heartbeat("Perceive", "Scanning environment (Chaotic)...")
    await asyncio.sleep(0.1)
    await agent.emit_heartbeat("React", "Planning (Chaotic)...")

    # 4. Validate the Chain
    logger.info("\n--- Validating Chain Integrity ---")
    buffer = list(agent.signal_buffer)

    if not buffer:
        logger.error("❌ Signal Buffer is empty!")
        return

    chain_broken = False
    for i, signal in enumerate(buffer):
        # Check Hash
        if signal.mantra_hash != expected_hash:
            logger.error(f"❌ Signal {i} has invalid hash!")
            chain_broken = True

        # Check Chain Link
        if i > 0:
            prev_signal = buffer[i - 1]
            if signal.previous_signal_id != prev_signal.id:
                logger.error(
                    f"❌ Chain Break at {i}! PrevID {signal.previous_signal_id} != {prev_signal.id}"
                )
                chain_broken = True
            else:
                logger.info(
                    f"🔗 Link {i-1}->{i} Verified. Delta: {signal.delta_seconds:.4f}s"
                )
        else:
            logger.info(f"🟢 Genesis Signal {i} (No Prev ID).")

    if not chain_broken:
        logger.info("\n✅ SUCCESS: Heartbeat Chain is Unbroken and Trusted.")
        logger.info(f"   Total Signals: {len(buffer)}")
        logger.info(f"   Mantra Hash: {MANTRA_HASH}")
    else:
        logger.error("\n❌ FAILURE: Heartbeat Chain is Broken or Untrusted.")


if __name__ == "__main__":
    asyncio.run(test_heartbeat_integrity())
