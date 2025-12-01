---
holon:
  id: hfo-design-architecture-enforcement
  type: design
  status: draft
  generation: 63
  author: Swarmlord
  theme: Intent-First Architecture
---

# 📐 Design: HFO Gen 63 Architecture & The "Intent-First" Gatekeeper

> **The Golden Rule**: "No Code shall be written that has not first been Dreamed."
> **Objective**: Enforce a strict separation of Intent (Brain) and Implementation (Body) to prevent "Sprawl" and "Drift".

## 1. The Philosophy: Intent-First Development
In previous generations, we wrote code to solve immediate problems. This led to "Sprawl"—a collection of disconnected tools.
In Gen 63, we invert this.
1.  **Intent is Primary**: The `.md` or `.feature` file is the "Soul".
2.  **Code is Secondary**: The `.py` file is merely the "Body" that executes the Soul's will.
3.  **Drift is Death**: If the Code does something the Intent didn't specify, it is a bug (or a mutation that must be rejected).

## 2. The Architecture: Fractal Octree (The 8 Pillars)
The structure of the application is not arbitrary. It follows the **Fractal Octree**. Every file must live in one of these 8 Organs.

| Pillar | Organ | Role | Artifacts (Intent) | Implementation (Code) |
| :--- | :--- | :--- | :--- | :--- |
| **1. Navigator** | `brain/` | **Decides** | Manifestos, Gherkin Features, Strategy Docs | *None (Pure Intent)* |
| **2. Observer** | `eyes/` | **Sees** | Sensor Definitions, Data Schemas | NATS Listeners, Polling Scripts |
| **3. Bridger** | `memory/` | **Remembers** | Knowledge Graph Schema, Ontology | LanceDB, SQLite, Vector Stores |
| **4. Shaper** | `forge/` | **Acts** | Tool Definitions (MCP), API Specs | MCP Servers, CLI Tools |
| **5. Injector** | `pulse/` | **Beats** | Schedule Definitions, Cron Specs | Event Loops, Schedulers |
| **6. Disruptor** | `venom/` | **Tests** | Test Plans, Chaos Scenarios | Unit Tests, Red Team Scripts |
| **7. Immunizer** | `carapace/` | **Protects** | Security Policies, Config Schemas | Pydantic Models, Env Validators |
| **8. Assimilator** | `digest/` | **Absorbs** | ETL Pipelines, Data Maps | Ingestion Scripts |

## 3. The Enforcement Mechanism: The "Gatekeeper"
How do we ensure no code is written without intent? We cannot rely on discipline alone. We need a **Gatekeeper**.

### 3.1 The Stigmergic Link
Every code file (`.py`) must contain a YAML Frontmatter header that links back to its Intent.

**Example `forge/my_tool.py`:**
```python
"""
---
holon:
  id: hfo-tool-my-tool
  type: tool
  layer: forge
  intent: buds/hfo_gem_gen_63/brain/feature_my_tool.feature  <-- THE LINK
---
"""
```

### 3.2 The Gatekeeper Script (`venom/gatekeeper.py`)
We will design a script that runs on `pre-commit` or `genesis`:
1.  **Scan**: It scans all `.py` files in the Bud.
2.  **Verify**: It reads the `intent` field in the header.
3.  **Check**: It verifies that the linked Intent file exists in `brain/`.
4.  **Reject**: If the link is missing or broken, the build fails.

### 3.3 The "Genesis" Workflow
We do not manually create files. We use a `genesis` tool.
1.  **User**: Writes `brain/feature_x.md`.
2.  **User**: Runs `python genesis.py scaffold brain/feature_x.md`.
3.  **System**: Reads the Intent, determines the necessary Organs, and generates the `.py` stubs *with the correct headers pre-filled*.

## 4. The Registry (`REGISTRY.yaml`)
To make the Gatekeeper work, we need a single source of truth for the directory structure.
This file defines *where* things go, so the Gatekeeper knows that a file in `eyes/` is a Sensor and must have a Sensor Intent.

```yaml
# REGISTRY.yaml Concept
organs:
  eyes:
    required_intent_type: "sensor_definition"
    allowed_extensions: [".py"]
  forge:
    required_intent_type: "tool_definition"
    allowed_extensions: [".py"]
```

## 5. Summary of Rules
1.  **Brain First**: You cannot create a file outside of `brain/` manually.
2.  **Genesis Scaffolds**: You must use `genesis.py` to create the Body from the Brain.
3.  **Gatekeeper Guards**: The CI/CD pipeline will reject any Body without a Soul.
