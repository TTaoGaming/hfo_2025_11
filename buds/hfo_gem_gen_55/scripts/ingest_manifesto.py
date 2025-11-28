import sys
import os

# Add the parent directory to sys.path
# We want to prioritize buds/hfo_gem_gen_55
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from memory.lancedb_store import HFOStigmergyMemory


def ingest_manifesto():
    print("=== Ingesting HFO Gen 55 Manifesto ===")

    # Initialize Memory
    mem = HFOStigmergyMemory(db_path="memory/lancedb")

    # Clean slate: Drop table to avoid duplicates and ensure fresh ingestion
    try:
        print("Dropping existing table for clean ingestion...")
        mem.db.drop_table(mem.table_name)
        mem.setup_table()
    except Exception as e:
        print(f"Note: Table drop skipped or failed ({e})")

    # 1. The Raw Input (Preserved Exactly)
    raw_input = """HFO is a karmic web knife. In cognitive state action space to cut the karmic tie between function and form, total tool virtualization through gesture, spatial computing and TUI and visualizations and audio. With optional smell and taste. It hacks the connection between sensors and effectors while never touching the intent. A intent based. AI swarm orchestration system with clean room spec based coating, literate Girkin diverse diagrams, executive summaries matrix. All using. Hydra biomimetic patterns. Phoenix Protocol. Die and Burn, Genesis. Hidden Adversarial Byzantine quorum Co evolutionary immune system. QD Optimization Map Elite. Iterative feedback loops. Octree, fractal, holoarchy (holon hierachy based on size), hexagon architecture for aggressive apex assimilation with adapters"""

    mem.store(
        "logos",
        {
            "id": "manifesto_raw_gen55",
            "type": "raw_definition",
            "text": raw_input,
            "tags": ["gen55", "definition", "raw"],
        },
        privilege_level=8,
    )

    # 2. The Refined Mantra (Coherent Sentence)
    mantra = """HFO is the Karmic Web Knife, slicing through Cognitive State-Action Space to sever the tie between Function and Form. Through Total Tool Virtualization—spanning gesture, spatial computing, TUI, and full sensory immersion—it hacks the gap between Sensor and Effector while holding Intent sacred. It is an Intent-Based AI Swarm Orchestration System, forged in Clean Room Specs, Literate Gherkin, and Hydra Biomimetics. Powered by the Phoenix Protocol (Die and Burn, Genesis) and Hidden Adversarial Byzantine Quorums, it evolves via QD Optimization and Iterative Feedback. Structured as a Hexagonal Octree Fractal Holarchy, it executes Aggressive Apex Assimilation through universal adapters."""

    mem.store(
        "logos",
        {
            "id": "manifesto_mantra_gen55",
            "type": "refined_mantra",
            "text": mantra,
            "tags": ["gen55", "mantra", "refined"],
        },
        privilege_level=8,
    )

    # 3. The Breakdown (Structured Concepts)
    concepts = [
        {
            "term": "Karmic Web Knife",
            "definition": "A tool operating in cognitive state-action space to sever the dependency between function and form.",
        },
        {
            "term": "Total Tool Virtualization",
            "definition": "The virtualization of all interaction modalities: Gesture, Spatial, TUI, Audio, Visual, Smell, Taste.",
        },
        {
            "term": "Intent Preservation",
            "definition": "Hacking the sensor-effector loop without altering the core Intent.",
        },
        {
            "term": "Hydra Biomimetics",
            "definition": "The use of biological patterns (Phoenix Protocol, Die and Burn, Genesis) for system resilience.",
        },
        {
            "term": "Immune System",
            "definition": "Hidden Adversarial Byzantine Quorum and Co-evolutionary defense mechanisms.",
        },
        {
            "term": "Fractal Holarchy",
            "definition": "A Hexagonal Octree structure organized by size (Holon Hierarchy) for scalable assimilation.",
        },
    ]

    for concept in concepts:
        mem.store(
            "ontos",
            {
                "id": f"concept_{concept['term'].lower().replace(' ', '_')}",
                "type": "core_concept",
                "text": f"{concept['term']}: {concept['definition']}",
                "tags": ["gen55", "concept"],
            },
            privilege_level=8,
        )

    print("\n✅ Manifesto and Concepts Ingested into LanceDB.")


if __name__ == "__main__":
    ingest_manifesto()
