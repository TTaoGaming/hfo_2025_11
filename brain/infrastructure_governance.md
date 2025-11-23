---
title: Holonic File Governance
status: Active (Gen 51)
domain: Infrastructure
owners:
- Immunizer
- Swarmlord
type: Policy

# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: c69a9939-4b2f-4e27-9a5f-bf6ca20f1545
    type: doc
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T06:32:09.788638Z'
  topos:
    address: 1.0.0
    links: []
  telos:
    viral_factor: 0.0
    meme: Holonic File Governance
---


# 📜 Holonic File Governance

## ⚡ BLUF (Bottom Line Up Front)
The **Holocron** (`brain/registry.yaml`) is the absolute law of the Hive. If a file is not registered, it is "Slop" and will be purged. All Brain concepts must follow the **Swarmlord of Webs** format: Gherkin for Intent, and a rich Markdown document (YAML + BLUF + Matrix + 3xMermaid) for Visualization.

## 📊 Governance Matrix

| Component | Requirement | Enforcer | Failure Consequence |
| :--- | :--- | :--- | :--- |
| **Registry** | All files must be listed in `registry.yaml` or `concepts.yaml` | `guard_brain.py` | File is flagged as Slop |
| **Intent** | Every concept needs a `.feature` file | `guard_brain.py` | Concept marked Invalid |
| **Visuals** | Every concept needs a `.md` with 3+ Mermaid diagrams | `guard_brain.py` | Concept marked Invalid |
| **Header** | YAML Frontmatter with Status/Domain | `guard_brain.py` | Metadata extraction fails |

## 🧠 Concept Visualization

### View 1: The Holocron Hierarchy
*This diagram shows the relationship between the Registry and the Organs.*

```mermaid
graph TD
    Registry[registry.yaml] -->|Defines| Organs

    subgraph Organs
        Brain[brain/: Intent]
        Body[body/: Execution]
        Memory[memory/: Knowledge]
    end

    Brain -->|Enforced by| Guard[Hive Guard]
    Body -->|Enforced by| Guard
    Memory -->|Enforced by| Guard
```

### View 2: The Swarmlord of Webs Format
*This diagram illustrates the required structure of a Brain Concept.*

```mermaid
classDiagram
    class BrainConcept {
        +FeatureFile: .feature
        +SummaryFile: .md
    }

    class SummaryFile {
        +YAML_Header
        +BLUF
        +Matrix_Table
        +Diagram_1_Conceptual
        +Diagram_2_Logical
        +Diagram_3_Physical
        +Executive_Summary
    }

    BrainConcept *-- FeatureFile
    BrainConcept *-- SummaryFile
```

### View 3: The Governance Flow
*This sequence diagram shows how the Immunizer enforces the rules.*

```mermaid
sequenceDiagram
    participant Dev as Developer
    participant Git as Git Hook
    participant Guard as Brain Guard
    participant Repo as Repository

    Dev->>Git: Commit Changes
    Git->>Guard: Run Checks
    Guard->>Repo: Check Registry
    Guard->>Repo: Check Format (3x Mermaid)
    alt Valid
        Guard-->>Git: Pass
        Git->>Repo: Commit
    else Invalid
        Guard-->>Git: Fail (Block)
        Git-->>Dev: Error Report
    end
```

## 🦅 Executive Summary
Hive Fleet Obsidian (Gen 51) operates on **Intent-Based Engineering**. This means the "Brain" is not just a folder of notes; it is a compiled database of requirements.

To ensure this database remains high-quality, we enforce **Holonic File Governance**.
1.  **The Registry**: `brain/registry.yaml` and `brain/concepts.yaml` act as the "DNA" of the project. If a file isn't in the DNA, it's a tumor.
2.  **The Format**: We demand high-density information. Text is cheap; Diagrams and Matrices are valuable. The **Swarmlord of Webs** format ensures that every concept is viewed from multiple angles (Conceptual, Logical, Physical) before it is accepted.
3.  **The Guard**: The `guard_brain.py` script is the immune system. It ruthlessly blocks commits that don't meet these standards.
