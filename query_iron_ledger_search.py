import sqlite3

DB_PATH = "/home/tommytai3/hive_fleet_obsidian_2025_11/buds/hfo_gem_gen_60/memory/hfo_gen_60_memory.db"

try:
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    queries = [
        "Obsidian Spider",
        "Hexadex Chant",
        "Obsidian Horizon Hourglass",
        "Fractal Octree",
        "8 Obsidian Roles",
        "Swarmlord of Webs",
    ]

    print(f"--- Querying Iron Ledger ({DB_PATH}) ---")

    for q in queries:
        print(f"\n🔍 Searching for: '{q}'")
        # Use LIKE for simple text search
        sql = (
            "SELECT source_path, content FROM memory_items WHERE content LIKE ? LIMIT 3"
        )
        cursor.execute(sql, (f"%{q}%",))
        results = cursor.fetchall()

        if not results:
            print("  No results found.")
            continue

        for row in results:
            source = row[0]
            content = row[1]
            # Find the position of the match to show context
            idx = content.find(q)
            start = max(0, idx - 100)
            end = min(len(content), idx + 300)
            snippet = content[start:end].replace("\n", " ")

            print(f"  [Source: {source}]")
            print(f"  Snippet: ...{snippet}...")

    conn.close()

except Exception as e:
    print(f"Error querying SQLite: {e}")
