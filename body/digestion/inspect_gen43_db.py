import json
from pathlib import Path

# 🕵️ GEN 43 DATABASE INSPECTOR
# Role: Inspector
# Mission: Analyze the massive Gen 43 memory dump.

DB_PATH = Path(
    "memory/procedural/gen_1_50_codebase/HFO_2025_11_19/hfo_gem/gen_43/hfo_memory_backup.json"
)


def inspect_db():
    print(f"🕵️ Inspecting {DB_PATH}...")

    if not DB_PATH.exists():
        print(f"❌ Database not found: {DB_PATH}")
        return

    file_size_mb = DB_PATH.stat().st_size / (1024 * 1024)
    print(f"📦 Size: {file_size_mb:.2f} MB")

    try:
        with open(DB_PATH, "r", encoding="utf-8") as f:
            print("🔍 Peeking at structure (Assuming NDJSON)...")

            count = 0
            types = {}
            keys_sample = set()

            # Read first few lines to check if it's NDJSON or a big list
            first_char = f.read(1)
            f.seek(0)

            if first_char == "[":
                print(
                    "⚠️ Detected JSON List (not NDJSON). Loading as standard JSON (might be slow)..."
                )
                data = json.load(f)
                print(f"✅ Loaded {len(data)} items.")
                for obj in data[:3]:
                    count += 1
                    if isinstance(obj, dict):
                        obj_type = obj.get("type", "unknown")
                        types[obj_type] = types.get(obj_type, 0) + 1
                        keys_sample.update(obj.keys())
                        print(f"\n--- Item {count} ---")
                        print(json.dumps(obj, indent=2)[:500] + "...")

                # Count types for the rest
                for obj in data[3:]:
                    if isinstance(obj, dict):
                        obj_type = obj.get("type", "unknown")
                        types[obj_type] = types.get(obj_type, 0) + 1
                        keys_sample.update(obj.keys())

                count = len(data)

            else:
                # Assume NDJSON
                for line in f:
                    line = line.strip()
                    if not line:
                        continue

                    try:
                        obj = json.loads(line)
                        count += 1

                        # Analyze structure
                        if isinstance(obj, dict):
                            # Check for 'type' field or similar
                            obj_type = obj.get("type", "unknown")
                            mem_type = obj.get("memory_type", "unknown")
                            types[mem_type] = types.get(mem_type, 0) + 1
                            keys_sample.update(obj.keys())

                            if count <= 3:
                                print(f"\n--- Item {count} ---")
                                print(json.dumps(obj, indent=2)[:500] + "...")

                    except json.JSONDecodeError:
                        print(f"⚠️ Line {count+1} is not valid JSON.")
                        if count < 5:
                            print(f"Line content: {line[:100]}...")

            print("\n📊 Summary:")
            print(f"Total Items: {count}")
            print(f"Types: {types}")
            print(f"Keys Found: {keys_sample}")

    except Exception as e:
        print(f"❌ Error inspecting DB: {e}")


if __name__ == "__main__":
    inspect_db()
