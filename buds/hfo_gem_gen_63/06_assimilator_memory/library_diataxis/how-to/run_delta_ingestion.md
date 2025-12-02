---
holon:
  id: 0f76e87d-64b6-4324-9ede-a7c58535d03f
  type: codex_entry
  quadrant: how-to
  source_ref: /home/tommytai3/hive_fleet_obsidian_2025_11/buds/hfo_gem_gen_63/src/ingest_delta.py
hexagon:
  ontos: owner
  logos: diataxis
---

# How to Run Delta Ingestion with HFO Gem Generation 63

Delta Ingestion is the process of bringing new data into a system. In this case, it involves using the `Assimilator` class to ingest files and directories relevant to generation 63 of the HFO gem. Follow the steps below to perform delta ingestion.

## Step-by-Step Instructions

1. **Setup Logging**: Ensure that the logging is configured to capture the process flow.
   ```python
   logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
   logger = logging.getLogger("DeltaIngest")
   ```

2. **Create an Instance of Assimilator**: Instantiate the `Assimilator` class which handles the ingestion of the files and directories.
   ```python
   assimilator = Assimilator()
   ```

3. **Ingest the Root Manifests**: Check for the presence of specific root files and ingest them if they exist. The root files include:
   - `AGENTS.md`
   - `README.md`
   ```python
   root_files = ["AGENTS.md", "README.md"]
   for f in root_files:
       if os.path.exists(f):
           logger.info(f"Ingesting Root File: {f}")
           assimilator.ingest_file(os.path.abspath(f))
   ```

4. **Ingest Gen 63 Source Code**: Ingest the source code located in `buds/hfo_gem_gen_63/src`. Ensure to specify the file extensions you want to include:
   ```python
   gen_63_src = os.path.abspath("buds/hfo_gem_gen_63/src")
   if os.path.exists(gen_63_src):
       logger.info(f"Ingesting Gen 63 Src: {gen_63_src}")
       assimilator.ingest_directory(gen_63_src, extensions=['.py', '.md'])
   ```

5. **Ingest the Gen 63 Brain**: Optionally, if a brain directory exists, ingest that directory as well.
   ```python
   gen_63_brain = os.path.abspath("buds/hfo_gem_gen_63/brain")
   if os.path.exists(gen_63_brain):
       logger.info(f"Ingesting Gen 63 Brain: {gen_63_brain}")
       assimilator.ingest_directory(gen_63_brain, extensions=['.md', '.feature'])
   ```

6. **Complete Process**: Conclude the ingestion process and log the completion.
   ```python
   logger.info("✅ Delta Ingestion Complete. Memory is up to date.")
   ```

By following these steps, you will successfully run Delta Ingestion for HFO Gem Generation 63.