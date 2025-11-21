import pandas as pd

try:
    df = pd.read_parquet("hfo_gem/gen_43/adapters/memory.parquet")
    print("Columns found:", df.columns.tolist())
    if len(df) > 0:
        print("First row sample:", df.iloc[0].to_dict())
except Exception as e:
    print(f"Error reading parquet: {e}")
