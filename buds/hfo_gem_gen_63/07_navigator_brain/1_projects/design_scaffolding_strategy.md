---
holon:
  id: design-scaffolding-strategy
  type: design
  status: active
  author: Swarmlord
  date: 2025-12-01
  context: HFO Second Brain
---

# 🏗️ Design: Scaffolding Strategy & Migration (The Strangler Fig)

> **Context**: We have 1 year of code and hundreds of GBs of data (Legacy). We are building the "Iron Garden" (Gen 63).
> **Problem**: How do we enforce strict architecture (Positive/Negative Checks) without "boiling the ocean" or losing access to the massive legacy memory?

## ⚖️ Analysis: Positive vs. Negative Checks

To manage a large, evolving system, we need both types of feedback loops.

### ✅ Positive Checks (The Builder's Level)
*   **Definition**: Verifying that a component *complies* with the Spec.
*   **Mechanism**: "Does X exist? Is X valid?"
*   **Examples**:
    *   **Genesis**: "Did `genesis.py` create the file?" (Yes/No)
    *   **Schema**: "Does `HolonHeader` parse correctly?" (Pydantic)
    *   **Tests**: "Does `test_knowledge_structure.py` pass?"
*   **Role**: **Ensures Quality of NEW Growth**.
*   **Implementation**: Built into the **MCP Tools** and **Genesis Script**.

### ❌ Negative Checks (The Guard's Shield)
*   **Definition**: Detecting *violations* or *anomalies* in the environment.
*   **Mechanism**: "Is there anything here that *shouldn't* be?"
*   **Examples**:
    *   **Drift Detection**: "Are there files in `brain/` without headers?"
    *   **Linter**: "Are there Python files with circular imports?"
    *   **Security**: "Are there secrets in the committed code?"
*   **Role**: **Contains the Legacy Debt**.
*   **Implementation**: **Pre-commit Hooks** and **Nightly Cron Jobs**.

---

## 🚀 The Strategy: "Strangler Fig" Migration

We cannot migrate 100GB of data instantly. We must build the new system *around* the old one and consume it slowly.

### Phase 1: The Iron Perimeter (Stop the Bleeding)
*   **Goal**: Ensure **ZERO** new technical debt is added.
*   **Action**:
    1.  **Activate the Guard**: `guard_knowledge_structure.py` runs on all *new* commits.
    2.  **Whitelist Legacy**: Configure the Guard to *ignore* `legacy/` or specific old directories.
    3.  **Strict Mode for Gen 63**: Any file added to `buds/hfo_gem_gen_63/` MUST pass Positive Checks.

### Phase 2: The Fractal Seed (Start the Growth)
*   **Goal**: Make doing the "Right Thing" easier than the "Wrong Thing".
*   **Action**:
    1.  **Build `genesis.py`**: A CLI/Script to generate compliant Holons.
    2.  **Build MCP Interface**: Agents use `create_intent` which calls `genesis.py`.
    3.  **Result**: New features grow perfectly formed.

### Phase 3: The Pointer Bridge (Link the Memory)
*   **Goal**: Access the 100GB of data without moving it.
*   **Action**:
    1.  **Do NOT Copy**: Moving 100GB is expensive and breaks paths.
    2.  **Create Pointers**: Create lightweight Markdown files in `brain/3_resources/reference/` that *point* to the heavy data.
    3.  **Example**:
        ```yaml
        ---
        holon:
          type: reference
          target: /mnt/data/heavy_dataset_2024.parquet
        ---
        # Reference to Legacy Data
        This Holon points to the 2024 dataset.
        ```
    4.  **Lazy Ingestion**: Only ingest the *metadata* of the heavy data into LanceDB, not the content itself.

---

## 🛠️ Implementation Plan (Scaffolding)

### Step 1: The Genesis Script (Positive Check)
We need a tool that generates the "Perfect Holon".

```python
# forge/genesis.py
def create_holon(title, type, octant):
    # 1. Validate Inputs (Positive Check)
    # 2. Generate Path (e.g., brain/1_projects/{title}.md)
    # 3. Generate Header (YAML)
    # 4. Write File
    # 5. Register in Registry.yaml
```

### Step 2: The Guard Configuration (Negative Check)
Update the Guard to handle the "Legacy Whitelist".

```python
# carapace/guard.py
IGNORE_PATHS = ["legacy/", "archive/", "data/"]
def validate(file_path):
    if any(p in file_path for p in IGNORE_PATHS):
        return True # Skip Legacy
    # ... Run Strict Checks ...
```

### Step 3: The Pointer Generator
A script to scan your 100GB drive and generate "Pointer Holons" in the new Brain.

---

## 🏁 Recommendation: Start with Genesis
The best way to start is to **build the `genesis.py` script**.
*   **Why?**: It solves the immediate problem (Agents creating bad files).
*   **Positive Reinforcement**: It gives you and the agents a "Button" to push to make progress correctly.
*   **Negative Checks** can be added later to clean up the mess, but **Genesis** prevents the mess from growing.
