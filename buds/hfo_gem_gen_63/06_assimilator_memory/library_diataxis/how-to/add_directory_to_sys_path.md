---
holon:
  id: 764fa108-3f0c-4f4c-9aa9-2374a18e2571
  type: codex_entry
  quadrant: how-to
  source_ref: /home/tommytai3/hive_fleet_obsidian_2025_11/buds/hfo_gem_gen_63/src/__init__.py
hexagon:
  ontos: hive_fleet_obsidian
  logos: diataxis
---

# How to Add Current Directory to sys.path

This guide will explain how to add the current directory to `sys.path` in Python to ensure that modules in the same directory can be imported successfully.

## Explanation

### Why?
Python needs to know where to look for modules to import. By default, it only looks in certain directories. If your modules are in the current directory, you need to explicitly add that directory to `sys.path` for Python to find them.

### What?
To add the current directory to `sys.path`, you can use the following code snippet:

```python
import os
import sys

# Add the current directory to sys.path to ensure modules can be imported
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
```

## Step-by-Step Instructions
1. **Import the required modules**: Start by importing the `os` and `sys` modules into your script. These modules will help you manipulate the system paths.
   ```python
   import os
   import sys
   ```

2. **Get the current directory**: Use `os.path.abspath(__file__)` to retrieve the absolute path of the current file, and then use `os.path.dirname()` to get the directory name from that path.

3. **Append to `sys.path`**: Use `sys.path.append()` to add the current directory to the module search path.
   ```python
   sys.path.append(os.path.dirname(os.path.abspath(__file__)))
   ```

4. **Verify the import**: You can now import your local modules without any issues as the current directory is added to `sys.path`.

By following these steps, you ensure that any Python module located in the same directory as your script can be imported without any errors.