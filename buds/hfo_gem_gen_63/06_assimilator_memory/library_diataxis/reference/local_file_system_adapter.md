---
holon:
  id: 60b7a85a-4da3-4fe9-9c3b-7c49691e8483
  type: codex_entry
  quadrant: reference
  source_ref: /home/tommytai3/hive_fleet_obsidian_2025_11/buds/hfo_gem_gen_63/src/adapters/fs_adapter.py
hexagon:
  ontos: owner
  logos: diataxis
---

# LocalFileSystemAdapter Class Documentation

## Class Definition

```python
class LocalFileSystemAdapter(FileSystemPort):
```

### Description
The `LocalFileSystemAdapter` provides an interface for interacting with the local file system, extending the `FileSystemPort` class.

## Initialization

### Function: `__init__`
```python
def __init__(self, base_path: str = "."):
```
- **Inputs:**
  - `base_path` (str): The base directory path for file operations. Defaults to the current directory (`.`).

## Methods

### Method: `write_file`
```python
async def write_file(self, path: str, content: str):
```
- **Inputs:**
  - `path` (str): The relative path where the file will be created.
  - `content` (str): The content to be written to the file.
- **Outputs:**
  - This method does not return anything. It performs a write operation to the file system.

### Method: `read_file`
```python
async def read_file(self, path: str) -> str:
```
- **Inputs:**
  - `path` (str): The relative path of the file to read.
- **Outputs:**
  - Returns the content of the file as a string.

### Logging
The class uses a logger to inform about operations:
- `logger.info(f"💾 Wrote file: {full_path}")` is logged after successful writing of a file.
- `logger.info(f"📖 Read file: {full_path}")` is logged after a file has been read successfully.