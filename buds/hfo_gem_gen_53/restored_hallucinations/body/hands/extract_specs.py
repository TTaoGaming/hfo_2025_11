"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: extract-specs-001
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 1.0
    decay: 0.0
    created: '2025-11-24T14:10:00+00:00'
    generation: 53
  topos:
    address: body/hands/extract_specs.py
    links: []
  telos:
    viral_factor: 1.0
    meme: The Gherkin Extractor
"""

import os
import re
import logging

# Configure Logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger("SpecExtractor")


def extract_gherkin_from_md(file_path: str, output_dir: str):
    """Reads a Markdown file, finds the Gherkin block, and saves it as a .feature file."""
    try:
        with open(file_path, "r") as f:
            content = f.read()

        # Regex to find ```gherkin ... ``` blocks
        match = re.search(r"```gherkin\n(.*?)\n```", content, re.DOTALL)

        if match:
            gherkin_content = match.group(1)

            # Determine output filename
            filename = os.path.basename(file_path).replace(".md", ".feature")
            output_path = os.path.join(output_dir, filename)

            # Write to temp dir
            with open(output_path, "w") as f:
                f.write(f"# Generated from {file_path}\n")
                f.write(gherkin_content)

            logger.info(f"✅ Extracted: {filename}")
        else:
            logger.warning(f"⚠️ No Gherkin found in: {file_path}")

    except Exception as e:
        logger.error(f"❌ Failed to extract {file_path}: {e}")


def main():
    source_dir = "buds/hfo_gem_gen_53/brain/intents"
    output_dir = "buds/hfo_gem_gen_53/tests/features"

    # Ensure output dir exists
    os.makedirs(output_dir, exist_ok=True)

    logger.info(f"🚀 Starting Spec Extraction from {source_dir}...")

    count = 0
    for root, _, filenames in os.walk(source_dir):
        for filename in filenames:
            if filename.endswith(".md"):
                extract_gherkin_from_md(os.path.join(root, filename), output_dir)
                count += 1

    logger.info(f"🏁 Extraction Complete. Processed {count} files.")


if __name__ == "__main__":
    main()
