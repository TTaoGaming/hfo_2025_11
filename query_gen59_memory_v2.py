import lancedb
import os
import sys

# Fix for OMP Error
os.environ["KMP_DUPLICATE_LIB_OK"] = "True"

# Target Gen 59 Memory (or Gen 60 if cloned)
GEN_59_DB_PATH = (
    "/home/tommytai3/hive_fleet_obsidian_2025_11/buds/hfo_gem_gen_59/memory/lancedb"
)
GEN_60_DB_PATH = "/home/tommytai3/hive_fleet_obsidian_2025_11/buds/hfo_gem_gen_60/memory/hfo_gen_60_lancedb"

if os.path.exists(GEN_59_DB_PATH):
    db_path = GEN_59_DB_PATH
    print(f"Using Gen 59 Memory: {db_path}")
elif os.path.exists(GEN_60_DB_PATH):
    db_path = GEN_60_DB_PATH
    print(f"Using Gen 60 Memory: {db_path}")
else:
    print("No LanceDB found for Gen 59 or Gen 60.")
    sys.exit(1)

try:
    db = lancedb.connect(db_path)
    print(f"Tables: {db.table_names()}")

    table_name = "hfo_vectors"  # Found in previous run
    if table_name not in db.table_names():
        if len(db.table_names()) > 0:
            table_name = db.table_names()[0]
        else:
            print("No tables found.")
            sys.exit(1)

    print(f"Querying Table: {table_name}")
    tbl = db.open_table(table_name)

    queries = [
        "Obsidian Spider",
        "Hexadex Chant",
        "Obsidian Horizon Hourglass",
        "Fractal Octree",
        "8 Obsidian Roles",
        "Swarmlord of Webs",
    ]

    for q in queries:
        print(f"\n🔍 Querying: '{q}'")
        # Use vector search instead of FTS if FTS index is missing
        # Assuming 'vector' column exists and default embedding is handled or not needed if we just search by text similarity via vector
        # Wait, tbl.search(q) does vector search by default if q is a string and embedding function is set?
        # Or we need to be explicit.
        # If FTS failed, it means it tried FTS.
        # Let's try to force vector search if possible, or just print the schema to see what we have.

        try:
            results = tbl.search(q).limit(3).to_pandas()

            if results.empty:
                print("  No results found.")
                continue

            for index, row in results.iterrows():
                print(
                    f"  [Score: {row['_distance']:.4f}] Source: {row.get('filename', 'Unknown')}"
                )
                content = row.get("content", "")
                snippet = content[:300].replace("\n", " ")
                print(f"  Snippet: {snippet}...")
        except Exception as e:
            print(f"  Search failed: {e}")

except Exception as e:
    print(f"Error querying LanceDB: {e}")
