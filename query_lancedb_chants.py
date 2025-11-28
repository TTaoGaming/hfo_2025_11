import lancedb
import os

# Fix for OMP Error
os.environ["KMP_DUPLICATE_LIB_OK"] = "True"

db_path = (
    "/home/tommytai3/hive_fleet_obsidian_2025_11/buds/hfo_gem_gen_55/memory/lancedb"
)
try:
    db = lancedb.connect(db_path)  # type: ignore
    table_name = "hfo_stigmergy"
    if table_name in db.table_names():
        tbl = db.open_table(table_name)

        # Search for user quotes or definitions of HFO
        # We'll look for "chant", "poetry", "HFO is", "mental"
        query_text = "chant poetry HFO definition mental workflow"

        results = tbl.search(query_text).limit(10).to_pandas()

        print("--- Search Results ---")
        for index, row in results.iterrows():
            print(f"\n[Score: {row['_distance']:.4f}] File: {row['filename']}")
            # Print a snippet of the content
            content = row["content"]
            snippet = content[:500].replace("\n", " ")
            print(f"Snippet: {snippet}...")

    else:
        print(f"Table '{table_name}' NOT found.")
except Exception as e:
    print(f"Error querying LanceDB: {e}")
