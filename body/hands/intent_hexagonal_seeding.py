"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: 550e8400-e29b-41d4-a716-446655440000
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T12:00:00Z'
    generation: 51
  topos:
    address: body/hands/intent_hexagonal_seeding.py
    links: []
  telos:
    viral_factor: 0.0
    meme: intent_hexagonal_seeding.py
"""
import os
import uuid
import datetime
import yaml

# Configuration
ROOT_DIR = "/home/tommytai3/hive_fleet_obsidian_2025_11"
EXCLUDE_DIRS = {
    "archive",
    ".git",
    "__pycache__",
    "node_modules",
    "venv",
    ".vscode",
    "audit_trail",  # Skip logs
    "raw_audit_logs",  # Skip raw logs
}
TARGET_EXTENSIONS = {".md", ".py", ".yaml", ".yml", ".feature", ".mmd"}


def get_timestamp():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def generate_uuid():
    return str(uuid.uuid4())


def create_header_dict(filepath, file_type):
    return {
        "hexagon": {
            "ontos": {"id": generate_uuid(), "type": file_type, "owner": "Swarmlord"},
            "chronos": {
                "status": "active",
                "urgency": 0.5,
                "decay": 0.5,
                "created": get_timestamp(),
                # last_touched will be updated on write
            },
            "topos": {"address": filepath, "links": []},
            "telos": {"viral_factor": 0.0, "meme": os.path.basename(filepath)}
            # Logos and Pathos omitted for brevity in seed, can be enriched later
        }
    }


def format_yaml_block(data):
    # Custom YAML dump to match the desired style
    yaml_str = yaml.dump(data, default_flow_style=False, sort_keys=False)
    return f"""# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
{yaml_str}"""


def process_markdown(content, header_block):
    # Check for existing frontmatter
    if content.startswith("---"):
        # Find end of frontmatter
        end_idx = content.find("---", 3)
        if end_idx != -1:
            # Insert into existing frontmatter
            frontmatter = content[3:end_idx]
            if "hexagon:" in frontmatter:
                return (
                    content  # Already has hexagon, skip or update (skipping for safety)
                )

            new_frontmatter = frontmatter.rstrip() + "\n\n" + header_block + "\n"
            return "---" + new_frontmatter + content[end_idx:]

    # No frontmatter, create it
    return f"---\n{header_block}---\n\n{content}"


def process_python(content, header_block):
    # Check for existing docstring
    if '"""' in content[:10] or "'''" in content[:10]:
        # Simple heuristic: Just prepend, user can clean up if double docstrings
        # Ideally we'd parse AST but that's heavy.
        # Let's wrap the header in a docstring
        return f'"""\n{header_block}"""\n\n{content}'

    return f'"""\n{header_block}"""\n\n{content}'


def process_generic(content, header_block):
    # For other files, just prepend as comment if possible, or just text
    # This is a "seed", so we might break some strict parsers (like JSON), but we excluded .json
    return f"{header_block}\n\n{content}"


def process_file(filepath):
    rel_path = os.path.relpath(filepath, ROOT_DIR)
    ext = os.path.splitext(filepath)[1]

    if ext not in TARGET_EXTENSIONS:
        return

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        print(f"Skipping {rel_path}: {e}")
        return

    # Skip if already seeded (basic check)
    if "hexagon:" in content and "ontos:" in content:
        print(f"Skipping {rel_path}: Already seeded.")
        return

    print(f"Seeding {rel_path}...")

    header_data = create_header_dict(rel_path, ext.replace(".", ""))
    header_block = format_yaml_block(header_data)

    new_content = content
    if ext == ".md":
        new_content = process_markdown(content, header_block)
    elif ext == ".py":
        new_content = process_python(content, header_block)
    elif ext == ".yaml" or ext == ".yml":
        # For YAML, we append to top as comment or document separator?
        # YAML supports multiple docs with ---
        # But config files might break.
        # Let's use comments for YAML
        comment_block = "\n".join(["# " + line for line in header_block.split("\n")])
        new_content = f"{comment_block}\n\n{content}"
    elif ext == ".feature":
        # Gherkin comments
        comment_block = "\n".join(["# " + line for line in header_block.split("\n")])
        new_content = f"{comment_block}\n\n{content}"
    else:
        # Default to prepending
        new_content = f"{header_block}\n\n{content}"

    try:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
    except PermissionError:
        print(f"⚠️ Permission denied: {rel_path}. Skipping.")
    except Exception as e:
        print(f"❌ Failed to write {rel_path}: {e}")


def main():
    print("🦅 Starting Hexagonal Seeding...")
    for root, dirs, files in os.walk(ROOT_DIR):
        # Filter directories
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]

        for file in files:
            filepath = os.path.join(root, file)
            process_file(filepath)
    print("✅ Seeding Complete.")


if __name__ == "__main__":
    main()
