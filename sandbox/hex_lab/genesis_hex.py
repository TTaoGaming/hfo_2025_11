"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: a29f1210-b1b9-4704-89bd-4b02fc687a70
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T10:21:31.614654+00:00'
  topos:
    address: sandbox/hex_lab/genesis_hex.py
    links: []
  telos:
    viral_factor: 0.0
    meme: genesis_hex.py
"""

#!/usr/bin/env python3
import yaml
import uuid
import datetime
from pathlib import Path

# Configuration
SANDBOX_DIR = Path("sandbox/hex_lab")


def generate_hexagon(face_data, file_path):
    """Computes the Hexagon based on the Face and File Context."""

    # 1. ONTOS (Identity)
    ontos = {
        "id": str(uuid.uuid4()),
        "type": "doc" if file_path.suffix == ".md" else "code",
        "owner": "Sandbox.Tester",
    }

    # 2. CHRONOS (Thermodynamics)
    # Simple logic: "test" tag = low urgency
    tags = face_data.get("tags", [])
    urgency = 0.1 if "test" in tags else 0.5
    chronos = {
        "status": "active",
        "urgency": urgency,
        "decay": 0.5,
        "created": datetime.datetime.utcnow().isoformat() + "Z",
    }

    # 3. TOPOS (Connectivity)
    # Simple logic: Map directory structure to address
    # sandbox/hex_lab -> 9.1
    topos = {"address": "9.1.0", "links": []}

    # 4. TELOS (Purpose)
    # Simple logic: Viral factor based on BLUF length
    bluf_len = len(face_data.get("bluf", ""))
    viral = min(1.0, bluf_len / 100)
    telos = {"viral_factor": viral, "meme": face_data.get("title", "Untitled")}

    return {"ontos": ontos, "chronos": chronos, "topos": topos, "telos": telos}


def process_file(file_path):
    print(f"🧬 Processing {file_path}...")
    try:
        content = file_path.read_text()

        # Split YAML frontmatter
        if not content.startswith("---"):
            print("  ❌ No frontmatter found.")
            return

        parts = content.split("---", 2)
        if len(parts) < 3:
            print("  ❌ Invalid frontmatter format.")
            return

        yaml_text = parts[1]
        body = parts[2]

        # Parse Face
        face = yaml.safe_load(yaml_text)
        if "hexagon" in face:
            print("  ✨ Hexagon already exists. Skipping.")
            return

        # Generate Hexagon
        hexagon = generate_hexagon(face, file_path)

        # Merge and Write
        face["hexagon"] = hexagon

        # Reconstruct File
        new_yaml = yaml.dump(face, sort_keys=False, allow_unicode=True)

        # Add comments for visual separation
        new_yaml = new_yaml.replace(
            "hexagon:",
            "\n# ==================================================================\n# 🤖 THE HEXAGON (System Generated)\n# ==================================================================\nhexagon:",
        )

        new_content = f"---\n{new_yaml}---\n{body}"
        file_path.write_text(new_content)
        print("  ✅ Hexagon grown successfully.")

    except Exception as e:
        print(f"  ❌ Error: {e}")


def main():
    print("🧪 Genesis Hexagon Lab")
    print("======================")

    if not SANDBOX_DIR.exists():
        print(f"❌ Sandbox directory {SANDBOX_DIR} not found.")
        return

    for file_path in SANDBOX_DIR.glob("*.md"):
        process_file(file_path)


if __name__ == "__main__":
    main()
