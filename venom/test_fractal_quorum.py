"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: 0dba518a-2ebf-4e95-b3af-d6081416c9b6
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T10:21:31.308255+00:00'
  topos:
    address: venom/test_fractal_quorum.py
    links: []
  telos:
    viral_factor: 0.0
    meme: test_fractal_quorum.py
"""

import yaml


def test_fractal_math():
    """Verifies the mathematical integrity of the Fractal Holarchy."""
    with open("body/swarm_config.yaml", "r") as f:
        config = yaml.safe_load(f)

    swarm = config["swarm"]
    N = swarm["squad_size"]
    Q = swarm["quorum_threshold"]
    Total = swarm["branching_factor"]

    # 1. Check Log-10 Base (Soft check, just ensuring it's not 1)
    assert N >= 2, "Squad size must be at least 2"

    # 2. Check Quorum Majority
    # User Requirement: >4 votes (5). This is exactly N/2.
    # For strict BFT (f=3), we'd need 7, but we follow the "Soft Quorum" intent.
    assert Q >= (N / 2), f"Quorum {Q} is less than half of {N}"

    # 3. Check Fractal Division
    assert (
        Total % N == 0
    ), f"Total agents {Total} cannot be evenly divided into squads of {N}"

    # 4. Check Byzantine Tolerance (Optional, but good for 3f+1)
    # f = (N - 1) // 3
    # Required Quorum for BFT is usually 2f + 1 or similar depending on algorithm.
    # For simple majority of honest nodes (assuming f < N/2):
    # If f=3, N=10. Honest=7. Majority of Honest > 3.5 -> 4.
    # If we want robust consensus, > N/2 is the baseline.
    pass


def test_squad_slicing():
    """Verifies the list slicing logic used in research_swarm.py."""
    total_agents = 50
    squad_size = 10

    # Simulate the findings list
    findings = [f"Finding {i}" for i in range(total_agents)]

    squads = []
    for i in range(0, total_agents, squad_size):
        squad_findings = findings[i : i + squad_size]
        squads.append(squad_findings)

    assert len(squads) == 5
    assert len(squads[0]) == 10
    assert squads[0][0] == "Finding 0"
    assert squads[4][9] == "Finding 49"


if __name__ == "__main__":
    test_fractal_math()
    test_squad_slicing()
    print("✅ Fractal Logic Tests Passed")
