---
holon:
  id: 522ae0aa-8c2c-4ff9-a0eb-9c8f81652b83
  type: codex_entry
  quadrant: how-to
  source_ref: /home/tommytai3/hive_fleet_obsidian_2025_11/buds/hfo_gem_gen_63/src/ingest_repo.py
hexagon:
  ontos: owner
  logos: diataxis
---

# How to Run Repository Ingestion with Assimilator

## Introduction
This document outlines the steps involved in performing a repository ingestion using the `Assimilator` class. The ingestion process is designed to log the activities while excluding specific directories that may not be relevant for ingestion.

## Step-by-Step Instructions

1. **Import Required Modules**  
   In your script, ensure to import the necessary modules as follows:
   ```python
   import os
   import sys
   import logging
   ```

2. **Configure the Logging**  
   Set up logging to capture the ingestion process:
   ```python
   logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
   logger = logging.getLogger("RepoIngest")
   ```

3. **Define the `run_ingestion` Function**  
   Create the function that will handle the ingestion process:
   ```python
   def run_ingestion():
       assimilator = Assimilator()
       # ... Additional code ...
   ```

4. **Get the Current Working Directory**  
   Use `os.getcwd()` to find the root directory:
   ```python
   root_dir = os.getcwd()
   ```

5. **Specify Excluded Directories**  
   Create a list of directories to exclude from ingestion:
   ```python
   exclude_dirs = [
       "__pycache__",
       ".git",
       ".vscode",
       "node_modules",
       "buds/hfo_gem_gen_63",
       "audit_trail",
   ]
   ```

6. **Convert Excluded Directories to Absolute Paths**  
   Make sure the paths are absolute for safety:
   ```python
   exclude_dirs = [os.path.abspath(os.path.join(root_dir, d)) for d in exclude_dirs]
   ```

7. **Log the Ingestion Start**  
   Inform the user that the ingestion is starting:
   ```python
   logger.info(f"🕷️ Starting Full Repo Ingestion from: {root_dir}")
   logger.info(f"🚫 Excluding: {exclude_dirs}")
   ```

8. **Call the Ingest Directory Method**  
   Invoke the `ingest_directory` method of the `assimilator` passing the root directory and extensions to include:
   ```python
   assimilator.ingest_directory(root_dir, extensions=['.md', '.py', '.json', '.yaml', '.feature'], exclude_dirs=exclude_dirs)
   ```

9. **Log Completion Message**  
   Once ingestion is complete, log the completion:
   ```python
   logger.info("✅ Ingestion Complete.")
   ```

10. **Execute the Function in Main**  
    Make sure to call the `run_ingestion` function when the script is executed directly:
    ```python
    if __name__ == "__main__":
        run_ingestion()
    ```

## Conclusion
Following these steps will successfully run the repository ingestion process while adhering to the exclusions defined. Make sure to adjust the `exclude_dirs` list as necessary to suit your project's needs.