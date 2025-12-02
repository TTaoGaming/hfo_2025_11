"""
---
holon:
  id: hfo-049489b0
  type: unknown
  file: cleaner.py
  status: active
---
"""
import os
import sys
import logging
from typing import List

# Add root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.assimilator import Assimilator

# Setup Logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger("Cleaner")

class Cleaner:
    """
    The Cleaner (Gen 63).
    Ensures the system is clean and consistent.
    1. Re-ingests the Brain (Intent) to ensure Memory is fresh.
    2. Checks for 'Ghost Files' (files not in Memory/Intent).
    """
    def __init__(self):
        self.assimilator = Assimilator()
        self.base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    def refresh_memory(self):
        """
        Re-ingests the Brain and Src.
        """
        logger.info("🧼 Refreshing Memory...")
        brain_path = os.path.join(self.base_path, "brain")
        src_path = os.path.join(self.base_path, "src")
        
        self.assimilator.ingest_directory(brain_path)
        self.assimilator.ingest_directory(src_path)
        logger.info("✅ Memory Refreshed.")

    def check_integrity(self):
        """
        Simple integrity check.
        """
        logger.info("🔍 Checking Integrity...")
        # TODO: Implement more advanced checks (e.g., Gherkin vs Code coverage)
        # For now, just ensure critical files exist
        critical_files = [
            "brain/manifesto_gen_63.md",
            "brain/tech_stack_gen63.md",
            "src/config.py",
            "src/stigmergy_loop.py"
        ]
        
        all_good = True
        for f in critical_files:
            full_path = os.path.join(self.base_path, f)
            if not os.path.exists(full_path):
                logger.error(f"❌ Missing Critical File: {f}")
                all_good = False
            else:
                logger.info(f"✅ Found: {f}")
        
        if all_good:
            logger.info("✅ System Integrity Verified.")
        else:
            logger.warning("⚠️ System Integrity Compromised.")

if __name__ == "__main__":
    cleaner = Cleaner()
    cleaner.refresh_memory()
    cleaner.check_integrity()
