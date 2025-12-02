---
holon:
  id: 8ff8e1ef-639b-47dc-b9aa-1eecc3511374
  type: codex_entry
  quadrant: reference
  source_ref: /home/tommytai3/hive_fleet_obsidian_2025_11/buds/hfo_gem_gen_63/src/core/ports.py
hexagon:
  ontos: hive_fleet_obsidian
  logos: diataxis
---

# EventBusPort Class

## Overview

`EventBusPort` is an abstract base class designed to represent a port for the Nervous System (Hot Stigmergy).

## Methods

### `connect`

```python
async def connect(self):
    pass
```
- **Description:** Abstract method to establish a connection.

### `publish`

```python
async def publish(self, subject: str, payload: Dict[str, Any]):
    pass
```
- **Inputs:**  
  - `subject` (str): The subject to which the payload is published.  
  - `payload` (Dict[str, Any]): The data payload to publish.
- **Description:** Abstract method to publish data to a specific subject.

### `subscribe`

```python
async def subscribe(self, subject: str, callback: Callable[[Dict[str, Any]], Awaitable[None]]):
    pass
```
- **Inputs:**  
  - `subject` (str): The subject to subscribe to.  
  - `callback` (Callable[[Dict[str, Any]], Awaitable[None]]): A callback function to handle incoming messages.
- **Description:** Abstract method to register a callback for a specific subject.

### `close`

```python
async def close(self):
    pass
```
- **Description:** Abstract method to close the connection.

# FileSystemPort Class

## Overview

`FileSystemPort` is an abstract base class designed to represent a port for the Body (Cold Stigmergy).

## Methods

### `write_file`

```python
async def write_file(self, path: str, content: str):
    pass
```
- **Inputs:**  
  - `path` (str): The path of the file to write to.  
  - `content` (str): The content to write to the file.
- **Description:** Abstract method to write content to a specified file.

### `read_file`

```python
async def read_file(self, path: str) -> str:
    pass
```
- **Inputs:**  
  - `path` (str): The path of the file to read from.
- **Outputs:**  
  - (str): The content read from the file.
- **Description:** Abstract method to read content from a specified file.
