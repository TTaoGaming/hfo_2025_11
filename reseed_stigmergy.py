"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: reseed-stigmergy-v1
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 1.0
    decay: 0.0
    created: '2025-11-23T12:00:00Z'
    generation: 51
  topos:
    address: reseed_stigmergy.py
    links: []
  telos:
    viral_factor: 1.0
    meme: reseed_stigmergy.py
"""

import os
import uuid
import datetime
import yaml
import re
from pathlib import Path

# Configuration
CURRENT_GEN = 51
ROOT_DIR = Path(".")
EXCLUDE_DIRS = {
    ".git",
    "__pycache__",
    "venv",
    ".pytest_cache",
    "node_modules",
    "audit_trail",
}
INCLUDE_EXTS = {".py", ".md", ".feature", ".yaml", ".yml"}


def get_timestamp():
    return datetime.datetime.utcnow().isoformat() + "Z"


def generate_header_dict(file_path, existing_header=None):
    file_name = file_path.name
    rel_path = str(file_path.relative_to(ROOT_DIR))

    # Defaults
    header = {
        "ontos": {
            "id": str(uuid.uuid4()),
            "type": file_path.suffix.lstrip("."),
            "owner": "Swarmlord",
        },
        "chronos": {
            "status": "active",
            "urgency": 0.5,
            "decay": 0.5,
            "created": get_timestamp(),
            "generation": CURRENT_GEN,
        },
        "topos": {"address": rel_path, "links": []},
        "telos": {"viral_factor": 0.0, "meme": file_name},
    }

    # Merge existing
    if existing_header:
        # Deep merge logic or simple update
        # We want to preserve ID and Created if possible, but update Generation
        if "ontos" in existing_header:
            header["ontos"].update(existing_header["ontos"])
        if "chronos" in existing_header:
            header["chronos"].update(existing_header["chronos"])
            # Force update generation
            header["chronos"]["generation"] = CURRENT_GEN
        if "topos" in existing_header:
            header["topos"].update(existing_header["topos"])
            header["topos"]["address"] = rel_path  # Ensure address is correct
        if "telos" in existing_header:
            header["telos"].update(existing_header["telos"])

    return header


def format_header_yaml(header_dict):
    # Create the YAML string
    # We wrap it in a structure
    full_dict = {"hexagon": header_dict}
    yaml_str = yaml.dump(full_dict, sort_keys=False, default_flow_style=False)
    return yaml_str.strip()


def process_python_file(file_path):
    content = file_path.read_text()

    # Regex to find existing header block
    # Look for """ ... hexagon: ... """ at the start
    pattern = r'^(\s*"""\s*\n# =+\n# 🤖 THE HEXAGON.*?# =+\nhexagon:.*?""")'
    match = re.search(pattern, content, re.DOTALL | re.MULTILINE)

    existing_header = None
    if match:
        raw_header = match.group(1)
        # Extract YAML part
        try:
            # Remove """ and comments to parse YAML
            yaml_part = raw_header.replace('"""', "").strip()
            # We need to be careful with the comments.
            # The regex captures the whole block.
            # Let's try to extract just the yaml part.
            yaml_match = re.search(r"(hexagon:.*)", yaml_part, re.DOTALL)
            if yaml_match:
                parsed = yaml.safe_load(yaml_match.group(1))
                if "hexagon" in parsed:
                    existing_header = parsed["hexagon"]
        except Exception as e:
            print(f"⚠️ Failed to parse existing header in {file_path}: {e}")

    new_header_dict = generate_header_dict(file_path, existing_header)
    new_header_yaml = format_header_yaml(new_header_dict)

    new_header_block = f'''"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
{new_header_yaml}
"""'''

    if match:
        # Replace existing
        new_content = content.replace(match.group(1), new_header_block)
    else:
        # Prepend
        if content.startswith("#!"):
            # Keep shebang
            lines = content.splitlines()
            new_content = (
                lines[0] + "\n" + new_header_block + "\n" + "\n".join(lines[1:])
            )
        else:
            new_content = new_header_block + "\n\n" + content

    file_path.write_text(new_content)
    print(f"✅ Reseeded {file_path}")


def process_markdown_file(file_path):
    content = file_path.read_text()

    # Check for YAML frontmatter
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            frontmatter = parts[1]
            body = parts[2]

            try:
                data = yaml.safe_load(frontmatter) or {}
                existing_header = data.get("hexagon")

                new_header_dict = generate_header_dict(file_path, existing_header)
                data["hexagon"] = new_header_dict

                new_frontmatter = yaml.dump(
                    data, sort_keys=False, default_flow_style=False
                )
                new_content = f"---\n{new_frontmatter}---\n{body}"
                file_path.write_text(new_content)
                print(f"✅ Reseeded {file_path}")
                return
            except Exception as e:
                print(f"⚠️ Failed to parse frontmatter in {file_path}: {e}")

    # If no frontmatter or failed, prepend
    new_header_dict = generate_header_dict(file_path)
    new_header_yaml = format_header_yaml(new_header_dict)
    new_content = f"---\n{new_header_yaml}\n---\n{content}"
    file_path.write_text(new_content)
    print(f"✅ Reseeded {file_path}")


def process_feature_file(file_path):
    # Feature files often use # comments for headers or just text.
    # But inject_headers.py used YAML frontmatter style?
    # Let's stick to the comment block style for Gherkin if possible,
    # OR use the same logic as Markdown if the parser supports it.
    # Gherkin parsers usually ignore comments.

    content = file_path.read_text()

    # Regex for comment block header
    pattern = r"^(# # =+\n# # 🤖 THE HEXAGON.*?# hexagon:.*?\n#\n)"
    match = re.search(pattern, content, re.DOTALL | re.MULTILINE)

    if match:
        # Parse logic similar to python but with # stripped
        pass  # Too complex to parse reliably with regex for now without strict format

    # For feature files, let's just prepend/replace a commented block
    new_header_dict = generate_header_dict(
        file_path
    )  # We ignore existing for simplicity in this pass or we could try to parse
    new_header_yaml = format_header_yaml(new_header_dict)

    # Comment out the YAML
    commented_yaml = "\n".join([f"# {line}" for line in new_header_yaml.splitlines()])

    new_header_block = f"""# # ==================================================================
# # 🤖 THE HEXAGON (System Generated)
# # ==================================================================
{commented_yaml}
#"""

    if match:
        new_content = content.replace(match.group(1), new_header_block)
    else:
        new_content = new_header_block + "\n\n" + content

    file_path.write_text(new_content)
    print(f"✅ Reseeded {file_path}")


def main():
    print(f"🕸️  Reseeding HFO Stigmergy (Gen {CURRENT_GEN})...")

    for root, dirs, files in os.walk(ROOT_DIR):
        # Exclude dirs
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]

        for file in files:
            file_path = Path(root) / file
            if file_path.suffix not in INCLUDE_EXTS:
                continue

            if file_path.name == "reseed_stigmergy.py":
                continue

            try:
                if file_path.suffix == ".py":
                    process_python_file(file_path)
                elif file_path.suffix in {".md", ".yaml", ".yml"}:
                    process_markdown_file(file_path)
                elif file_path.suffix == ".feature":
                    process_feature_file(file_path)
            except Exception as e:
                print(f"❌ Error processing {file_path}: {e}")


if __name__ == "__main__":
    main()
