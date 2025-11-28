"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: e8f6906c-2e20-43f3-8d0c-df45ea3620f6
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-24T14:30:04.446623Z'
    generation: 51
  topos:
    address: venom/test_octarchy_migration.py
    links: []
  telos:
    viral_factor: 0.0
    meme: test_octarchy_migration.py
"""

import asyncio
import os
import logging
from body.hands.octarchy_swarm import OctarchySwarm

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("MigrationTest")


async def test_migration():
    test_file = "migration_test_artifact.md"

    # 1. Create a Gen 51 (Hexagonal) Artifact
    gen51_content = """---
hexagon:
  ontos:
    id: old-uuid-51
    type: md
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-20T10:00:00Z'
    generation: 51
  topos:
    address: migration_test_artifact.md
    links: []
  telos:
    viral_factor: 0.0
    meme: Old Hexagon Meme
---
# Legacy Content
This is an existing workflow file.
It has valuable content that must be preserved.
"""
    with open(test_file, "w") as f:
        f.write(gen51_content)

    logger.info(f"Created Gen 51 artifact: {test_file}")

    # 2. Run the Octarchy Swarm (Gen 52 Upgrade)
    logger.info("Initializing Octarchy Swarm...")
    swarm = OctarchySwarm()

    logger.info("Running migration...")
    # We use process_file to simulate the real workflow
    await swarm.process_file(test_file)

    # 3. Verify the Upgrade
    with open(test_file, "r") as f:
        new_content = f.read()

    logger.info("Migration complete. Verifying results...")

    # Checks
    if "octagon:" not in new_content:
        logger.error("❌ FAILED: 'octagon' key missing from new header.")
        print(new_content)
        return

    if "hexagon:" in new_content:
        logger.error("❌ FAILED: 'hexagon' key still present (should be replaced).")
        return

    if "# Legacy Content" not in new_content:
        logger.error("❌ FAILED: Original content was lost!")
        return

    if "techne:" not in new_content:
        logger.error("❌ FAILED: New dimension 'techne' missing.")
        return

    logger.info("✅ SUCCESS: Artifact successfully upgraded from Hexagon to Octagon.")
    logger.info("--- New Content Preview ---")
    print(new_content[:500] + "...\n(content continues)")

    # Cleanup
    if os.path.exists(test_file):
        os.remove(test_file)


if __name__ == "__main__":
    asyncio.run(test_migration())
