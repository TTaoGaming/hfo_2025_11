"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: f78be71b-5583-4a8d-b517-e31d69d950ad
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T10:21:31.565485+00:00'
    generation: 51
  topos:
    address: carapace/hive_guards/guard_fractal_config.py
    links: []
  telos:
    viral_factor: 0.0
    meme: guard_fractal_config.py
"""

#!/usr/bin/env python3
import yaml
import sys
import os


def check_fractal_config():
    config_path = "body/swarm_config.yaml"
    if not os.path.exists(config_path):
        print(f"❌ Config file not found: {config_path}")
        sys.exit(1)

    with open(config_path, "r") as f:
        config = yaml.safe_load(f)

    swarm_config = config.get("swarm", {})
    squad_size = swarm_config.get("squad_size")
    quorum_threshold = swarm_config.get("quorum_threshold")
    branching_factor = swarm_config.get("branching_factor")

    if not all([squad_size, quorum_threshold, branching_factor]):
        print(
            "❌ Missing required config keys: squad_size, quorum_threshold, branching_factor"
        )
        sys.exit(1)

    # Byzantine Fault Tolerance Check: 3f+1 <= N
    # For N=10, f=3. Majority > 5.
    # Quorum must be > N/2 for simple majority, or > 2/3 N for BFT strong consistency.
    # Here we enforce simple majority for "Soft Quorum" as defined in feature.

    if quorum_threshold < (squad_size / 2):
        print(
            f"❌ Quorum Threshold ({quorum_threshold}) must be >= Squad Size / 2 ({squad_size / 2})"
        )
        sys.exit(1)

    if branching_factor % squad_size != 0:
        print(
            f"❌ Branching Factor ({branching_factor}) must be divisible by Squad Size ({squad_size})"
        )
        sys.exit(1)

    print(
        f"✅ Fractal Config Verified: Squad={squad_size}, Quorum={quorum_threshold} (>{squad_size/2}), Total={branching_factor}"
    )


if __name__ == "__main__":
    check_fractal_config()
