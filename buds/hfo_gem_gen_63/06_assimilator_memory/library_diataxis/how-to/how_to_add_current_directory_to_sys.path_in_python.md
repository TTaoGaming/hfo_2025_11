---
holon:
  id: 1d9d6393-552b-4ef0-81af-7004bc44db91
  type: codex_entry
  quadrant: how-to
  source_ref: /home/tommytai3/hive_fleet_obsidian_2025_11/buds/hfo_gem_gen_63/src/__init__.py
hexagon:
  ontos: hive_fleet_obsidian
  logos: diataxis
---

# How to Configure Python Module Import Paths

In Python, to import modules from a specific directory, you might need to modify the system path. This can be done by appending your current directory to `sys.path`. Follow these steps to achieve this:

## Prerequisites
- Ensure you are working within a Python environment where you have access to modify the import paths.

## Step-by-Step Instructions
1. **Create Your Python File**: Open or create a new Python file where you want to manage your module imports.

2. **Import Necessary Modules**: At the top of your file, include the following imports:
   ```python
   import os
   import sys
   ```

3. **Append the Current Directory to sys.path**: Use the following line of code to add the current directory to the list of paths where Python looks for modules:
   ```python
   sys.path.append(os.path.dirname(os.path.abspath(__file__)))
   ```

4. **Verify Changes**: To verify if your path has been updated, you can print the current `sys.path`:
   ```python
   print(sys.path)
   ```
   Check if your current directory is listed.

5. **Import Your Modules**: Now you can safely import your modules as usual, and Python will be able to locate them.

This method is helpful when you have modules located in the same directory as your script and need to ensure they are available for import.