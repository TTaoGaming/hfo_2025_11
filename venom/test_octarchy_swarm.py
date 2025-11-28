"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: b978f019-7c26-46ce-ab65-69baacc6f427
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-24T14:30:04.434498Z'
    generation: 51
  topos:
    address: venom/test_octarchy_swarm.py
    links: []
  telos:
    viral_factor: 0.0
    meme: test_octarchy_swarm.py
"""

import asyncio
import os
from body.hands.octarchy_swarm import OctarchySwarm


async def test_swarm():
    # Create a dummy file
    test_file = "test_octarchy_artifact.md"
    with open(test_file, "w") as f:
        f.write("# Test Artifact\nThis is a test file to verify the Octarchy Swarm.")

    swarm = OctarchySwarm()

    # Run generation directly on the file
    print(f"Generating header for {test_file}...")
    header = await swarm.generate_header(test_file, "This is a test file content.")

    print("\nGenerated Header:")
    print(header.model_dump_json(indent=2))

    # Apply stigmergy
    swarm.apply_stigmergy(test_file, header)

    # Verify file content
    with open(test_file, "r") as f:
        content = f.read()

    print("\nFinal File Content:")
    print(content)

    # Cleanup
    if os.path.exists(test_file):
        os.remove(test_file)


if __name__ == "__main__":
    asyncio.run(test_swarm())
