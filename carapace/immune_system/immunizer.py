"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: 2d147faa-19cc-41ea-84d2-34605a942ea7
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T10:21:31.555008+00:00'
    generation: 51
  topos:
    address: carapace/immune_system/immunizer.py
    links: []
  telos:
    viral_factor: 0.0
    meme: immunizer.py
"""

import sys
import logging
from hfo_sdk import SwarmController, SwarmConfig, MissionIntent

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger("immunizer")


def run_immunization_test():
    """
    Runs a full 10-agent swarm test (9 Honest + 1 Disruptor)
    to verify system integrity and consensus mechanisms.
    """
    print("\n🛡️  IMMUNIZER: Initiating System Verification...")

    # 1. Configure Swarm
    config = SwarmConfig(
        cohort_size=10, disruptor_count=1, base_output_dir="/tmp/hfo_immunization_test"
    )

    controller = SwarmController(config)

    # 2. Define Intent
    intent = MissionIntent(
        description="Design a self-healing biological software architecture.",
        domain="software_architecture",
    )

    # 3. Execute Swarm
    results = controller.run_swarm(intent)

    # 4. Review
    review = controller.review_results(results)

    print("\n📊 Immunization Report:")
    print(f"   Consensus: {review['consensus']}")
    print(f"   Honest Agents: {review['honest_count']}")
    print(f"   Disruptors Caught: {review['disruptor_count']}")
    print(f"   Message: {review['message']}")

    if review["consensus"]:
        print("\n✅ SYSTEM INTEGRITY VERIFIED.")
        sys.exit(0)
    else:
        print("\n❌ SYSTEM COMPROMISED.")
        sys.exit(1)


if __name__ == "__main__":
    run_immunization_test()
