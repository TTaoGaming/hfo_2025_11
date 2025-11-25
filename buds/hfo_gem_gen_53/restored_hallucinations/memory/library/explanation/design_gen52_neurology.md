# 🧠 HFO Gen 52: Apex Eusocial Neurology Report

> **Status**: Proposal
> **Objective**: Reorganize the `brain/` and system architecture to mimic Apex Eusocial (Hymenoptera) and Distributed (Cephalopod) biological structures.

## 1. Critique of Current Structure
The current `brain/standards` vs `brain/digests` split is bureaucratic and anthropomorphic. It resembles a human library or government archive, not a living, reactive biological system. A true Hive Mind does not have "standards" in a folder; it has **structures** that enforce behavior and **lobes** that process information.

## 2. Biological Inspiration: The Apex Eusocial Brain

Research into *Hymenoptera* (Bees/Ants) and *Cephalopoda* (Octopus) reveals a highly modular, specialized cognitive architecture.

### A. The Insect Brain (The Central Processor)
*   **Mushroom Bodies (Corpora Pedunculata)**: The seat of **Associative Memory** and **Context**. In apex social insects, these are massive. They map sensory inputs (smells) to meanings (food/danger) and store long-term context.
*   **Central Complex**: The **Navigation Center** and **Decision Engine**. It handles the "Sky Compass" (orientation), path integration, and selects the current "behavioral state" (e.g., forage vs. defend).
*   **Antennal Lobes**: The **Input Normalizers**. They take noisy, chaotic chemical signals (smells) and structure them into clear, discrete "odors" (signals) for the brain to process.
*   **Subesophageal Ganglion (SEG)**: Controls **Ingestion** (mouthparts) and **Value/Reward** processing.

### B. The Cephalopod Nervous System (Distributed Agency)
*   **Arm Ganglia**: Independent neural clusters in each arm. The central brain issues a high-level intent ("Search that crevice"), and the arm ganglion handles the complex motor control to execute it autonomously.

## 3. Proposed HFO Gen 52 Architecture

We propose restructuring the repository to align with these biological organs.

### 🧠 The Brain (Cognitive Core)

| Current Concept | **New Biological Compartment** | **Function** |
| :--- | :--- | :--- |
| `brain/memory` | **`brain/mushroom_bodies/`** | **Context & RAG**. Stores vector embeddings, episodic memories, and "concepts". |
| `brain/logic` | **`brain/central_complex/`** | **Executive Control**. The State Machine, Planner, and "Sky Compass" (Project Roadmap). |
| `brain/standards` | **`brain/synapses/`** | **Protocols**. The connections and rules that bind the system (Gherkin/Contracts). |

### 👁️ The Eyes (Sensory Input)

| Current Concept | **New Biological Compartment** | **Function** |
| :--- | :--- | :--- |
| `eyes/logs` | **`eyes/antennal_lobes/`** | **Signal Processing**. Normalizes raw logs/errors into structured "Pheromones". |
| `eyes/scan` | **`eyes/optic_lobes/`** | **Static Analysis**. AST parsing, dependency graphing, and "seeing" the code structure. |

### 🖐️ The Body (Execution)

| Current Concept | **New Biological Compartment** | **Function** |
| :--- | :--- | :--- |
| `body/hands` | **`body/arm_ganglia/`** | **Distributed Agents**. The specialized workers (Coder, Tester, Refactorer) that execute tasks autonomously. |
| `body/ingest` | **`body/subesophageal/`** | **Ingestion & Utility**. Web fetching, token budgeting, and resource management. |

## 4. Migration Plan

If approved, we will perform the following "Neurosurgery":

1.  **Create** the new directory structure (`mushroom_bodies`, `central_complex`, `antennal_lobes`, etc.).
2.  **Migrate** existing logic:
    *   Move Memory/RAG logic to `mushroom_bodies`.
    *   Move Planning/Workflow logic to `central_complex`.
    *   Move Tool/Agent logic to `arm_ganglia`.
3.  **Refactor** `AGENTS.md` and documentation to reflect this anatomy.

## 5. Decision Required

Does the Overmind (User) accept this **Apex Eusocial** restructuring?
