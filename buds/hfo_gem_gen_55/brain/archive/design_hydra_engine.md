# 🐉 The Hydra Engine: Gen 55 Architecture

> **Status**: Draft
> **Context**: Gen 55 (The Gem)
> **Role**: The Physical Execution Engine for the Fractal Swarm.
> **Tags**: #hydra #temporal #phoenix #cleanroom #spec-driven

## ⚡ BLUF (Bottom Line Up Front)
The **Hydra Engine** is the durable, antifragile runtime that powers the HFO Swarm. It is built on **Cleanroom Principles**: the code is a direct projection of the Intent (Specs). If the engine is poisoned or corrupted, we invoke the **Phoenix Protocol**: burn the implementation and rebuild it from the Genesis Specs.

---

## 🏗️ Architecture: The R.A.P.T.O.R. Redux

We retain the Gen 51 R.A.P.T.O.R. stack but strictly enforce the **Intent-First** flow.

### 1. The Brain (Intent)
*   **Format**: Gherkin (`.feature`) + Mermaid (`.mmd`).
*   **Role**: The DNA. Immutable during execution.
*   **Storage**: `brain/intent-literate-gherkin/`.

### 2. The Nervous System (Temporal)
*   **Role**: Orchestration & Durability.
*   **Function**:
    *   Manages the **1-8-64-8-1** Fractal Workflow.
    *   Persists state (Checkpoints) to the database.
    *   Handles retries and timeouts.
*   **Key Pattern**: **"The Workflow is the State"**. If the machine dies, Temporal resumes the workflow on a new machine exactly where it left off.

### 3. The Muscles (Ray)
*   **Role**: Distributed Execution.
*   **Function**:
    *   Spawns the 64 **Shapers** and **Disruptors**.
    *   Executes heavy compute tasks (LLM inference, Tool use).
    *   Isolates failures (Actor supervision).

### 4. The Immune System (Phoenix Protocol)
*   **Role**: Regeneration.
*   **Trigger**:
    *   **Poison Detected**: Immunizers flag a systemic hallucination.
    *   **Drift Detected**: Implementation diverges from Spec.
*   **Action**:
    *   **Burn**: Delete the compromised `body/` code or `memory/` artifact.
    *   **Rebuild**: Re-run `genesis.py` to regenerate the code from the Gherkin Spec.

---

## 🔄 The Cleanroom Cycle

1.  **Define**: Swarmlord writes `hydra_engine.feature`.
2.  **Generate**: Genesis Agent reads `.feature` and generates `hydra_workflow.py`.
3.  **Execute**: Temporal runs `hydra_workflow.py`.
4.  **Verify**: Venom (pytest-bdd) asserts that `hydra_workflow.py` matches `hydra_engine.feature`.
5.  **Phoenix**: If Verification fails, delete `hydra_workflow.py` and GOTO 2.

---

## 🧬 The Phoenix Protocol (Spec)

> "If the body is sick, shed it. The mind remains."

```python
def phoenix_protocol(component_id: str):
    # 1. Identify the Spec
    spec = registry.get_spec_for(component_id)

    # 2. Burn the Body
    implementation_path = registry.get_path_for(component_id)
    os.remove(implementation_path)

    # 3. Rebirth from Genesis
    genesis.generate(spec, output_path=implementation_path)

    # 4. Verify
    result = venom.verify(spec, implementation_path)
    if not result.passed:
        raise SystemExit("Genesis Failed. Check Spec.")
```
