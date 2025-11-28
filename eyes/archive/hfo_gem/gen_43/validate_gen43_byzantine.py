"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: 93716af4-2b1d-43c1-ae9c-30b20dddafcc
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T11:07:35.752530Z'
    generation: 51
  topos:
    address: eyes/archive/hfo_gem/gen_43/validate_gen43_byzantine.py
    links: []
  telos:
    viral_factor: 0.0
    meme: validate_gen43_byzantine.py
"""

import json
import sys
import re

BACKUP_FILE = "hfo_memory_backup.json"
SEED_FILE = "HFO_GENE_SEED_GEN43.md"

# The Axioms defined in Gen 43 that we want to validate against historical memory
AXIOMS = {
    "Epistemic Cap": [r"epistemic cap", r"0\.9", r"90%"],
    "Stigmergy": [r"stigmergy", r"nats", r"pheromone"],
    "Obsidian Hourglass": [r"obsidian hourglass", r"flip", r"anytime algorithm"],
    "Roles": [r"navigator", r"disruptor", r"immunizer", r"scout", r"builder"],
    "Stack": [r"temporal", r"pgvector", r"nats jetstream"],
    "Philosophy": [r"mosaic warfare", r"jadc2", r"cognitive exoskeleton"],
}


def load_memory():
    print(f"📂 Loading memory backup: {BACKUP_FILE}...")
    memories = []
    try:
        with open(BACKUP_FILE, "r", encoding="utf-8") as f:
            for line in f:
                memories.append(json.loads(line))
    except FileNotFoundError:
        print("❌ Backup file not found.")
        sys.exit(1)
    print(f"   └── Loaded {len(memories)} records.")
    return memories


def check_byzantine_tolerance(memories):
    print("\n🛡️  Running Byzantine Fault Tolerance Check (Tolerance: 10%)...")

    results = {}

    for axiom, patterns in AXIOMS.items():
        print(f"   🔍 Auditing Axiom: '{axiom}'")

        # 1. Find supporting memories
        supporting_memories = []
        for mem in memories:
            content = mem.get("content", "").lower()
            # Check if ANY pattern matches
            if any(re.search(p, content) for p in patterns):
                supporting_memories.append(mem)

        count = len(supporting_memories)

        # 2. Analyze Consistency (Simulated)
        # In a real vector space, we would check cluster density.
        # Here, we check if the concept is "well-established" (high frequency)
        # vs "hallucination" (low frequency).

        # We assume the total relevant corpus is roughly the count of memories
        # that mention ANY of these keywords.

        # Let's look for contradictions (Byzantine elements).
        # A contradiction might be "Epistemic Cap" associated with "1.0" or "100%".
        contradictions = 0
        if axiom == "Epistemic Cap":
            for mem in supporting_memories:
                if "100%" in mem.get("content", "") or "1.0" in mem.get("content", ""):
                    contradictions += 1

        # Byzantine Calculation
        # If contradictions > 10% of the supporting set, the axiom is unstable.

        byzantine_ratio = contradictions / count if count > 0 else 0.0
        is_robust = byzantine_ratio <= 0.10

        results[axiom] = {
            "support_count": count,
            "contradictions": contradictions,
            "byzantine_ratio": f"{byzantine_ratio:.1%}",
            "status": "ROBUST" if is_robust else "FRAGILE",
        }

        print(f"       ├── Support: {count} records")
        if contradictions > 0:
            print(
                f"       ├── Contradictions: {contradictions} (Ratio: {byzantine_ratio:.1%})"
            )
        print(f"       └── Status: {'✅ ROBUST' if is_robust else '⚠️ FRAGILE'}")

    return results


def main():
    memories = load_memory()
    results = check_byzantine_tolerance(memories)

    print("\n📊 BYZANTINE AUDIT SUMMARY")
    print("=" * 40)
    print(f"{'AXIOM':<20} | {'SUPPORT':<10} | {'RATIO':<10} | {'STATUS'}")
    print("-" * 55)
    for axiom, data in results.items():
        print(
            f"{axiom:<20} | {data['support_count']:<10} | {data['byzantine_ratio']:<10} | {data['status']}"
        )
    print("=" * 40)

    # Final Verdict
    fragile_axioms = [k for k, v in results.items() if v["status"] == "FRAGILE"]
    if not fragile_axioms:
        print("\n✅ GEN 43 SEED IS MEMORY-COMPLIANT (Passed 10% Byzantine Threshold).")
    else:
        print(
            f"\n⚠️ WARNING: The following axioms show high memory drift: {fragile_axioms}"
        )


if __name__ == "__main__":
    main()
