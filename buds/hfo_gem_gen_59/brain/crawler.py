import os
import sys
import logging
from typing import List

# Add root to path
sys.path.append(os.getcwd())

from buds.hfo_gem_gen_59.brain.scribe import Scribe

# Setup Logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger("RepoCrawler")

class RepoCrawler:
    """
    Crawls the repository and feeds data to the Scribe.
    """
    def __init__(self, root_dir: str = "."):
        self.root_dir = root_dir
        self.scribe = Scribe()
        self.ignored_dirs = {
            ".git", "__pycache__", "venv", "node_modules", ".pytest_cache", 
            "buds/hfo_gem_gen_59/memory" # Don't ingest the DB itself!
        }
        self.allowed_extensions = {".md", ".py", ".yaml", ".json", ".txt", ".sh", ".mmd"}

    def crawl(self, target_dir: str, generation: int = 58):
        """
        Walks the target directory and ingests files.
        """
        logger.info(f"🕷️ Starting Crawl of: {target_dir}")
        count = 0
        errors = 0
        
        for root, dirs, files in os.walk(target_dir):
            # Filter directories
            dirs[:] = [d for d in dirs if d not in self.ignored_dirs]
            
            for file in files:
                if any(file.endswith(ext) for ext in self.allowed_extensions):
                    file_path = os.path.join(root, file)
                    
                    # Skip the DB file explicitly if it wasn't caught by dir filter
                    if "hfo_memory.db" in file_path:
                        continue

                    try:
                        self._ingest_file(file_path, generation)
                        count += 1
                    except Exception as e:
                        logger.error(f"❌ Failed to ingest {file_path}: {e}")
                        errors += 1
        
        logger.info(f"✅ Crawl Complete. Ingested: {count}, Errors: {errors}")

    def _ingest_file(self, file_path: str, generation: int):
        """Reads and ingests a single file."""
        abs_path = os.path.abspath(file_path)
        
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
        except UnicodeDecodeError:
            logger.warning(f"⚠️ Skipping binary/non-utf8 file: {file_path}")
            return

        # Determine Category
        ext = os.path.splitext(file_path)[1]
        category = "code"
        if ext == ".md": category = "documentation"
        elif ext in [".yaml", ".json"]: category = "config"
        
        data = {
            "source_path": abs_path,
            "content": content,
            "generation": generation,
            "category": category,
            "tags": ["auto-crawled", f"ext:{ext}"]
        }
        
        result = self.scribe.ingest(data)
        if result["status"] != "success":
            raise Exception(result["message"])

if __name__ == "__main__":
    # Example Usage: Crawl Gen 55 Brain
    crawler = RepoCrawler()
    target = "buds/hfo_gem_gen_55/brain"
    if os.path.exists(target):
        crawler.crawl(target, generation=55)
    else:
        print(f"Target {target} does not exist.")
