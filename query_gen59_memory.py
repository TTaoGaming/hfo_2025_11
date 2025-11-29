import lancedb
import os
import sys

# Fix for OMP Error
os.environ["KMP_DUPLICATE_LIB_OK"] = "True"

# Target Gen 59 Memory (or Gen 60 if cloned)
# The user asked to query "gen 59 memory".
# Let's check if Gen 59 memory exists, otherwise use Gen 60.
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
    # Check for tables
    print(f"Tables: {db.table_names()}")

    # The table name might vary. In Gen 55 it was 'hfo_stigmergy'.
    # Let's try to find the right table.
    table_name = "hfo_stigmergy"  # Default guess
    if "hfo_memory" in db.table_names():
        table_name = "hfo_memory"
    elif "hfo_stigmergy" in db.table_names():
        table_name = "hfo_stigmergy"
    elif len(db.table_names()) > 0:
        table_name = db.table_names()[0]

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
    print(f"Error querying LanceDB: {e}")
