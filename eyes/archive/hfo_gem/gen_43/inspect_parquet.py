"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: d525e2d2-9e34-4f1e-bbc6-04f43e22545a
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T11:07:35.748696Z'
    generation: 51
  topos:
    address: eyes/archive/hfo_gem/gen_43/inspect_parquet.py
    links: []
  telos:
    viral_factor: 0.0
    meme: inspect_parquet.py
"""

import pandas as pd

try:
    df = pd.read_parquet("hfo_gem/gen_43/adapters/memory.parquet")
    print("Columns found:", df.columns.tolist())
    if len(df) > 0:
        print("First row sample:", df.iloc[0].to_dict())
except Exception as e:
    print(f"Error reading parquet: {e}")
