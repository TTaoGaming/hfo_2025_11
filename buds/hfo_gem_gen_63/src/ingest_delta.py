import os
import sys
import logging
from datetime import datetime

# Add root to path
sys.path.append(os.getcwd())

from buds.hfo_gem_gen_63.src.assimilator import Assimilator
from buds.hfo_gem_gen_63.src.config import settings

# Setup Logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger("DeltaIngest")

def run_delta_ingestion():
    logger.info("🕷️ Starting Delta Ingestion (Gen 63)...")
    
    assimilator = Assimilator()
    
    # 1. Ingest the Root Manifests
    root_files = ["AGENTS.md", "README.md"]
    for f in root_files:
        if os.path.exists(f):
            logger.info(f"Ingesting Root File: {f}")
            assimilator.ingest_file(os.path.abspath(f))

    # 2. Ingest Gen 63 Source Code (The Brain)
    gen_63_src = os.path.abspath("buds/hfo_gem_gen_63/src")
    if os.path.exists(gen_63_src):
        logger.info(f"Ingesting Gen 63 Src: {gen_63_src}")
        assimilator.ingest_directory(gen_63_src, extensions=['.py', '.md'])

    # 3. Ingest Gen 63 Brain (The Mind)
    # Note: Gen 63 might not have a 'brain' folder yet, but we check.
    gen_63_brain = os.path.abspath("buds/hfo_gem_gen_63/brain")
    if os.path.exists(gen_63_brain):
        logger.info(f"Ingesting Gen 63 Brain: {gen_63_brain}")
        assimilator.ingest_directory(gen_63_brain, extensions=['.md', '.feature'])

    logger.info("✅ Delta Ingestion Complete. Memory is up to date.")

if __name__ == "__main__":
    run_delta_ingestion()
