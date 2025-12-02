import os
import sys
import logging

# Add root to path
sys.path.append(os.getcwd())

from buds.hfo_gem_gen_63.src.assimilator import Assimilator

# Setup Logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger("RepoIngest")

def run_ingestion():
    assimilator = Assimilator()
    
    root_dir = os.getcwd()
    
    # Exclude the current generation's active memory and build artifacts
    exclude_dirs = [
        "__pycache__",
        ".git",
        ".vscode",
        "node_modules",
        "buds/hfo_gem_gen_63", # Don't ingest self while building self
        "audit_trail", # Logs are noisy
    ]
    
    # Convert to absolute paths for safety
    exclude_dirs = [os.path.abspath(os.path.join(root_dir, d)) for d in exclude_dirs]
    
    logger.info(f"🕷️ Starting Full Repo Ingestion from: {root_dir}")
    logger.info(f"🚫 Excluding: {exclude_dirs}")
    
    assimilator.ingest_directory(root_dir, extensions=['.md', '.py', '.json', '.yaml', '.feature'], exclude_dirs=exclude_dirs)
    
    logger.info("✅ Ingestion Complete.")

if __name__ == "__main__":
    run_ingestion()
