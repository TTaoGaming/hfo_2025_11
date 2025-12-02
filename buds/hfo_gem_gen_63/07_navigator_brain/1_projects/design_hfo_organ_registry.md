---
holon:
  id: hfo-gen63-design-organ-registry
  type: design
  status: draft
  author: Swarmlord
  oracle_token: 15bd0963
  context: buds/hfo_gem_gen_63/memory/short_term/query_result_15bd0963.json
---

# 📐 Design: The Organ Registry (Fractal Octree Mapping)

> **Oracle Token**: `15bd0963` (Verified)
> **Source**: `buds/hfo_gem_gen_63/memory/short_term/query_result_15bd0963.json`

## 1. The Problem
The current `src/` directory is a "Kitchen Sink". It mixes logic, config, sensors, and tools.
This violates the **Fractal Octree** architecture, where every component must belong to one of the 8 Pillars.

## 2. The Solution: Physical Organ Mapping
We will dissolve `src/` and redistribute its contents into 8 specific directories ("Organs").
Each Organ has a strict "Function Format".

### The 8 Pillars (Octants)

| Pillar | Organ (Dir) | Function Format | Description |
| :--- | :--- | :--- | :--- |
| **1. Navigator** | `brain/` | `intent_declarative_gherkin` | `.feature` files, Manifestos, Strategy. |
| **2. Observer** | `eyes/` | `sensor_active_monitor` | Polling scripts, API clients (NATS listeners). |
| **3. Bridger** | `memory/` | `library_diataxis` | Documentation, LanceDB, SQLite, Knowledge Graph. |
| **4. Shaper** | `forge/` | `tool_mcp_server` | MCP Servers, CLI Tools, Automation Scripts. |
| **5. Injector** | `pulse/` | `heartbeat_async_cycle` | The Main Loop, Cron Jobs, Schedulers. |
| **6. Disruptor** | `venom/` | `test_chaos_monkey` | Unit Tests, Red Team scripts, Drift Detectors. |
| **7. Immunizer** | `carapace/` | `guard_pydantic_validator` | Pydantic Models, Config, Security Policies. |
| **8. Assimilator** | `digest/` | `ingest_delta_parser` | Ingestion scripts, ETL pipelines. |

## 3. The Registry File (`REGISTRY.yaml`)
We will create a `REGISTRY.yaml` at the root of the Bud to enforce this mapping.
The `genesis.py` script will read this registry to determine where to place generated code.

```yaml
# REGISTRY.yaml (Draft)
organs:
  brain:
    path: brain/
    types: [".md", ".feature"]
  eyes:
    path: eyes/
    types: [".py"]
  memory:
    path: memory/
    types: [".md", ".json", ".lance"]
  forge:
    path: forge/
    types: [".py", ".sh"]
  pulse:
    path: pulse/
    types: [".py"]
  venom:
    path: venom/
    types: [".py"]
  carapace:
    path: carapace/
    types: [".py"]
  digest:
    path: digest/
    types: [".py"]
```

## 4. Migration Plan
1.  **Create Directories**: `mkdir -p eyes forge pulse venom carapace digest`
2.  **Move Files**:
    *   `src/config.py` -> `carapace/config.py`
    *   `src/bridger.py` -> `memory/bridger.py`
    *   `src/assimilator.py` -> `digest/assimilator.py`
    *   `src/research_agent.py` -> `forge/research_agent.py`
    *   `src/swarm.py` -> `pulse/swarm.py` (Or `forge`? Swarm is the execution engine. `pulse` is the heartbeat. Let's put `swarm.py` in `forge` as a tool, and `heartbeat.py` in `pulse`.)

## 5. Next Steps
1.  Approve this Design.
2.  Run `genesis.py` (updated) to create the folders.
3.  Execute the Migration.
