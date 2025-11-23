"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: f5103830-869b-4723-936d-b4d6703236d6
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T10:21:31.269653+00:00'
    generation: 51
  topos:
    address: venom/test_truth_finding.py
    links: []
  telos:
    viral_factor: 0.0
    meme: test_truth_finding.py
"""

import asyncio
import ray
import uuid
from body.hands.hydra_swarm import build_hydra_graph, HydraState


async def main():
    print("🦅 HFO Trust Engine: Truth Finding Test")
    print("---------------------------------------")

    # 1. Initialize Ray
    if not ray.is_initialized():
        ray.init(ignore_reinit_error=True)

    # 2. Build the R.A.P.T.O.R. Swarm (Hydra)
    app = build_hydra_graph()

    mission_id = str(uuid.uuid4())
    mission_prompt = (
        "Read the file 'AGENTS.md' in the current directory. "
        "Extract the mnemonic for the R.A.P.T.O.R. stack and explain what each letter stands for. "
        "Also, identify the 'Golden Rule' defined in the file."
    )

    print(f"🆔 Mission ID: {mission_id}")
    print(f"📜 Mission: {mission_prompt}")

    initial_state = HydraState(
        mission_id=mission_id,
        mission=mission_prompt,
        plan=[],
        results=[],
        final_output=None,
    )

    # 3. Execute the Swarm
    print("\n🚀 Launching Swarm...")
    result = await app.ainvoke(initial_state)

    # 4. Analyze Results
    print("\n🏁 Swarm Consensus:")
    if result.get("final_output"):
        print(f"   Score: {result['final_output'].consensus_score}")
        print(f"   Summary:\n{result['final_output'].summary}")
    else:
        print("   ❌ No consensus reached.")


if __name__ == "__main__":
    asyncio.run(main())
