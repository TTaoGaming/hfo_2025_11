---
title: 'Hive Fleet Obsidian: File Structure Governance (Hybrid Protocol)'
summary: Implements a 'Trust but Verify' hybrid system for Hive file management using
  a central Holocron registry, stigmergic headers on every file, and multi-layer Immunizer
  agents to enforce structure and quarantine aislosop.
domain: Infrastructure
concepts:
- Holocron
- Stigmergic Headers
- Immunizers
- File Governance
- Hybrid Protocol
owner: Swarmlord
actionable: false
related_files:
- brain/registry.yaml
- venom/quarantine/
type: crystallized_memory
status: active
last_verified: '2025-11-21'

# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: ae11ff0b-02f1-4dd9-acef-a5038c0a3a1f
    type: md
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T10:21:10.007878+00:00'
  topos:
    address: memory/semantic/library/infrastructure/file_structure_governance.md
    links: []
  telos:
    viral_factor: 0.0
    meme: file_structure_governance.md

---

# 🏛️ Hive Fleet Obsidian: File Structure Governance (Hybrid Protocol)

> **Status**: Active (Gen 50 Phoenix Protocol)
> **Context**: Combines "The Holocron" (Central Registry) with "The Pheromone" (Stigmergic Headers) to eliminate "aislop" and enable emergent organization.

## 🦅 Executive Summary

This architecture implements a **"Trust but Verify"** system for file management within the Hive.
1.  **The Spine (Static)**: A central `brain/registry.yaml` defines the *allowed* shape of the Hive.
2.  **The Signal (Dynamic)**: Every file carries a **Stigmergic Header** (YAML frontmatter) defining its intent and owner.
3.  **The Immune System**: Three layers of "Immunizer" agents enforce these rules.

---

## 🧩 The Three Pillars

### 1. The Holocron (Registry Spine)
*   **Location**: `brain/registry.yaml`
*   **Purpose**: The Single Source of Truth (SSOT) for directory structure.
*   **Rule**: If a directory isn't in the Holocron, it doesn't exist. Agents cannot create new root-level folders without updating the Holocron first.

### 2. The Pheromone (Stigmergic Headers)
*   **Location**: Top of every file (Markdown, Python, etc.).
*   **Purpose**: Self-describing metadata for emergent organization and GraphRAG indexing.
*   **Format (Python)**:
    ```python
    """
    ---
    type: agent_logic
    domain: core
    owner: Swarmlord
    status: active
    last_verified: 2025-11-21
    ---
    """
    ```
*   **Format (Markdown)**:
    ```yaml
    ---
    type: intent_def
    domain: brain
    owner: Navigator
    status: active
    ---
    ```

### 3. The Immunizers (Guardians)
*   **🛡️ Pre-Commit Guard (Static)**: Runs on `git commit`. Rejects files missing headers.
*   **🛡️ Active Hive Guard (Runtime)**: Scans the drive. Moves "aislop" to `venom/quarantine/`.
*   **🛡️ Gatekeeper (Agent Tool)**: The `create_file` tool checks the Registry.

---

## 📊 Visualizations

### Diagram 1: The Governance Architecture
*How the components interact to maintain order.*

```mermaid
graph TD
    subgraph "The Law (Intent)"
        Holocron[("📜 Holocron\n(intent/registry.yaml)")]
    end

    subgraph "The Wild (Implementation)"
        FileA["📄 File A\n(Has Header)"]
        FileB["📄 File B\n(No Header)"]
        FileC["📄 File C\n(Wrong Folder)"]
    end

    subgraph "The Immune System"
        Gatekeeper{"🛡️ Gatekeeper\n(Tool Level)"}
        ActiveGuard(("🛡️ Active Guard\n(Daemon)"))
        StaticGuard["🛡️ Static Guard\n(Git Hook)"]
    end

    %% Creation Flow
    Agent[("🤖 Agent")] -->|Attempts Write| Gatekeeper
    Gatekeeper -->|Check| Holocron
    Gatekeeper -->|Allowed| FileA
    Gatekeeper -->|Blocked| Agent

    %% Cleaning Flow
    ActiveGuard -->|Scans| FileA
    ActiveGuard -->|Scans| FileB
    ActiveGuard -->|Scans| FileC

    FileA -->|Valid| Safe[("✅ Validated")]
    FileB -->|Invalid| Quarantine[("☣️ Quarantine")]
    FileC -->|Invalid| Quarantine

    %% Commit Flow
    User((User)) -->|Commit| StaticGuard
    StaticGuard -->|Check Headers| FileA
    StaticGuard -->|Reject| FileB
```

### Diagram 2: The Lifecycle of a File
*From Agent intent to permanent storage.*

```mermaid
sequenceDiagram
    participant Agent
    participant Tool as 🛠️ FileTool
    participant Registry as 📜 Registry
    participant FS as 📂 FileSystem
    participant Guard as 🛡️ ActiveGuard

    Note over Agent, Registry: Phase 1: Creation (Prevention)
    Agent->>Tool: create_file("src/new_logic.py")
    Tool->>Registry: Validate Path Allowed?
    alt Path Invalid
        Registry-->>Tool: ❌ Denied (Not in Holocron)
        Tool-->>Agent: Error: Path forbidden.
    else Path Valid
        Registry-->>Tool: ✅ Approved
        Tool->>FS: Write File
    end

    Note over FS, Guard: Phase 2: Maintenance (Cure)
    loop Every 5 Minutes
        Guard->>FS: Scan Files
        FS-->>Guard: File List
        Guard->>Guard: Check Stigmergic Headers
        alt Header Missing
            Guard->>FS: Move to /quarantine/no_header/
        else Wrong Domain
            Guard->>FS: Move to /quarantine/drift/
        end
    end
```

### Diagram 3: The Stigmergic Header Spec
*The DNA of a file.*

```mermaid
classDiagram
    class StigmergyHeader {
        +String type
        +String domain
        +String owner
        +String status
        +List tags
    }

    class FileTypes {
        <<Enumeration>>
        agent_logic
        memory_node
        intent_def
        config
        test
    }

    class Domains {
        <<Enumeration>>
        core
        ingestion
        memory
        research
    }

    StigmergyHeader --> FileTypes : validates against
    StigmergyHeader --> Domains : validates against
```


---
**Grafted by Gardener**: [[gen_50_README|Gen 50 Hub]]
