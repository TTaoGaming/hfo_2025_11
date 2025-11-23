"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: ca48dd7d-ef13-4572-bbef-9d13249c6383
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T11:07:35.745925Z'
    generation: 51
  topos:
    address: eyes/archive/hfo_gem/gen_43/debug_unknowns.py
    links: []
  telos:
    viral_factor: 0.0
    meme: debug_unknowns.py
"""

import pandas as pd

try:
    df = pd.read_parquet("hfo_gem/gen_43/adapters/memory.parquet")

    # Check for null or 'Unknown' filenames
    unknowns = df[
        df["filename"].isnull() | (df["filename"] == "Unknown") | (df["filename"] == "")
    ]

    print(f"Total rows: {len(df)}")
    print(f"Unknown filename rows: {len(unknowns)}")

    if len(unknowns) > 0:
        print("\nSample of Unknown rows:")
        # Show source_id, content_snippet, and memory_type for context
        print(
            unknowns[["source_id", "content_snippet", "memory_type"]]
            .head(5)
            .to_string()
        )

        # Check if source_id provides a clue
        print("\nTop source_ids for Unknowns:")
        print(unknowns["source_id"].value_counts().head(5))

except Exception as e:
    print(f"Error: {e}")
