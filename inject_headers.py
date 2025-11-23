"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: 78329f13-101a-466f-82b0-2b2c4108edc1
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T10:20:43.119351+00:00'
  topos:
    address: inject_headers.py
    links: []
  telos:
    viral_factor: 0.0
    meme: inject_headers.py
"""

import glob
import os
import yaml


def inject_stigmergy_headers():
    feature_files = glob.glob("brain/*.feature")
    venom_files = glob.glob("venom/test_*.py")

    print(f"Found {len(feature_files)} feature files in brain/")

    for feature_path in feature_files:
        feature_name = os.path.basename(feature_path)
        slug = feature_name.replace(".feature", "").replace("-", "_")

        # Determine Status
        matching_test = None
        for vf in venom_files:
            if slug in vf:
                matching_test = vf
                break

        # Special cases mapping
        if not matching_test:
            if "capability_external_tools" in slug:
                if "venom/test_external_tools.py" in venom_files:
                    matching_test = "venom/test_external_tools.py"
            elif "workflow_obsidian_hourglass" in slug:
                if "venom/test_strategy_obsidian_hourglass.py" in venom_files:
                    matching_test = "venom/test_strategy_obsidian_hourglass.py"

        status = "Missing"
        if matching_test:
            with open(matching_test, "r") as f:
                content = f.read()
                if '@pytest.mark.skip(reason="Placeholder")' in content:
                    status = "Placeholder"
                elif "TODO: Implement actual steps" in content:
                    status = "Placeholder"
                elif "TODO: Implement steps" in content:
                    status = "Placeholder"
                elif "def test_" in content:
                    status = "Implemented"
                else:
                    status = "Uncertain"

        # Read Feature File
        with open(feature_path, "r") as f:
            lines = f.readlines()

        # Check if YAML header exists
        has_yaml = False
        if lines and lines[0].strip() == "---":
            # Find end of YAML
            for i, line in enumerate(lines[1:]):
                if line.strip() == "---":
                    has_yaml = True
                    break

        new_lines = []
        if has_yaml:
            # Update existing YAML
            in_yaml = False
            # header_end_idx = 0
            for i, line in enumerate(lines):
                if line.strip() == "---":
                    if not in_yaml:
                        in_yaml = True
                        new_lines.append(line)
                    else:
                        in_yaml = False
                        # Ensure status is updated before closing
                        # We'll just rewrite the whole block to be safe or regex replace
                        # header_end_idx = i
                        break
                elif in_yaml:
                    if line.strip().startswith("status:"):
                        continue  # Skip old status
                    new_lines.append(line)

            # Inject new status
            new_lines.insert(
                len(new_lines) - 1, f"status: {status}\n"
            )  # Insert before closing --- (wait, logic above is tricky)

            # Simpler approach: Parse YAML, update, dump
            # Extract YAML block
            yaml_content = ""
            yaml_end_idx = 0
            for i, line in enumerate(lines[1:]):
                if line.strip() == "---":
                    yaml_end_idx = i + 1
                    break
                yaml_content += line

            try:
                data = yaml.safe_load(yaml_content) or {}
                data["status"] = status
                new_yaml = yaml.dump(data, default_flow_style=False)
                new_lines = (
                    ["---\n"]
                    + [f"{line}\n" for line in new_yaml.splitlines()]
                    + ["---\n"]
                    + lines[yaml_end_idx + 1 :]
                )
            except Exception as e:
                print(f"Error parsing YAML for {feature_name}: {e}")
                new_lines = lines  # Fallback

        else:
            # Create new YAML header
            header = {
                "title": feature_name.replace(".feature", "").replace("_", " ").title(),
                "status": status,
                "type": "Intent",
                "owner": "Swarmlord",
            }
            new_yaml = yaml.dump(header, default_flow_style=False)
            new_lines = (
                ["---\n"]
                + [f"{line}\n" for line in new_yaml.splitlines()]
                + ["---\n\n"]
                + lines
            )

        # Write back
        with open(feature_path, "w") as f:
            f.writelines(new_lines)

        print(f"Updated {feature_name} -> Status: {status}")


if __name__ == "__main__":
    inject_stigmergy_headers()
