---
holon:
  id: 2986b66f-3f9a-47b6-85b6-93a30e5e7cad
  type: codex_entry
  quadrant: reference
  source_ref: /home/tommytai3/hive_fleet_obsidian_2025_11/buds/hfo_gem_gen_63/src/config.py
hexagon:
  ontos: hive_fleet_obsidian
  logos: diataxis
---

# HFO Gen 63 Configuration Settings

This module contains the `Settings` class which configures the HFO Gen 63 application using environment variables or a `.env` file.

## Classes

### `Settings`

- **BaseSettings**: Inherits from Pydantic's `BaseSettings` to simplify loading settings from environment variables.

#### Attributes:
- `ENV`: (str) Environment mode, default set to "dev".
- `GENERATION`: (str) The generation of the application, default is "63".
- `OPENROUTER_API_KEY`: (Optional[str]) API key for OpenRouter, default is `None`.
- `OPENROUTER_MODEL`: (str) Model used for OpenRouter, default is "openai/gpt-4o".
- `LANCEDB_PATH`: (str) File path for LanceDB memory, default is "buds/hfo_gem_gen_63/memory/lancedb".
- `SQLITE_PATH`: (str) File path for SQLite database, default is "buds/hfo_gem_gen_63/memory/hfo.db".
- `NATS_URL`: (str) URL for NATS server, default is "nats://localhost:4225".

#### Configurations (Nested Class):
- **Config**: Contains specific configurations for the `Settings` class:
  - `env_file`: Specifies the file to read environment variables from, default is ".env".
  - `extra`: Allows ignoring extra variables not defined in the model.

## Example Usage
If the script is run as the main module, it will print out the following:
```python
print(f"Loaded Settings for HFO Gen {settings.GENERATION} in {settings.ENV} mode.")
```
This will output the current settings loaded for the application.