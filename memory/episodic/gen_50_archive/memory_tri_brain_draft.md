---
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: bbb09ad6-0e96-4704-8775-547cd6137f72
    type: md
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T10:21:06.999407+00:00'
  topos:
    address: memory/episodic/gen_50_archive/memory_tri_brain_draft.md
    links: []
  telos:
    viral_factor: 0.0
    meme: memory_tri_brain_draft.md
---

# 🧠 HFO Tri-Brain Memory Architecture (Draft)

> **Status**: Draft / Proposed
> **Context**: Hierarchical Holonic Memory System for Gen 50.

## 🦅 Executive Summary

To achieve a "Hive Mind" that is both fast (tactical) and wise (strategic), we implement a **Tri-Brain Architecture**. This mimics biological memory consolidation:
1.  **Surface**: Immediate hygiene and structuring.
2.  **Limbic**: Fast, associative recall (Vector).
3.  **Cortical**: Deep, relational understanding (Graph).

---

## 🧩 The Three Layers

### Layer 1: The Scribe (Surface Layer - Hygiene & Structure)
*   **Role**: The **Pre-Processor**. Ensures no "garbage" enters the system. Turns raw text into structured "Stigmergic Artifacts."
*   **Mechanism**: `LangGraph` Agent (Assimilator).
*   **Tools**:
    *   **`Instructor` + `Pydantic`**: Forces LLM to output valid YAML headers (Metadata, Owner, Concepts).
    *   **`Python`**: Physical file management.
*   **The Loop**: `Read File` → `Extract Concepts` → `Generate Header` → `Save to Library`.

### Layer 2: The Hippocampus (Stream Layer - Fast Recall)
*   **Role**: The **Indexer**. Listens to the Scribe and Swarm, instantly turning actions into searchable vectors. This is "Working Memory."
*   **Mechanism**: Event-Driven Worker (NATS Consumer).
*   **Tools**:
    *   **`NATS JetStream`**: The "Nerve Signal" carrying new memory.
    *   **`Postgres` + `pgvector`**: Storage engine (faster/cheaper than Pinecone).
    *   **`OpenAI/Cohere Embeddings`**: Text-to-Vector conversion.
*   **The Loop**: `Listen to NATS` → `Embed Text` → `Insert into pgvector`.

### Layer 3: The Neocortex (Deep Layer - Wisdom & Reasoning)
*   **Role**: The **Dreamer**. Runs periodically (e.g., nightly) to "consolidate" memories. Connects dots between isolated vectors to form a Knowledge Graph.
*   **Mechanism**: Batch Process (GraphRAG).
*   **Tools**:
    *   **`Microsoft GraphRAG`**: Community detection and cluster summarization.
    *   **`NetworkX`**: Local graph analysis.
    *   **`LLM (GPT-4o/Gemini)`**: Heavy Map-Reduce summarization.
*   **The Loop**: `Scan Library` → `Build Graph` → `Detect Communities` → `Summarize Insights`.

---

## 🏗️ Implementation Matrix

| Layer | Speed | Cost | Depth | When to use? |
| :--- | :--- | :--- | :--- | :--- |
| **1. Scribe** | ⚡ Fast | 💲 Low | 🌊 Shallow | **Immediately**. Clean the data first. |
| **2. Stream** | ⚡ Real-time | 💲 Medium | 🏊 Mid | **During Missions**. Agents need fast lookup. |
| **3. Graph** | 🐢 Slow | 💲💲 High | 🤿 Deep | **Between Missions**. "Sleep" processing. |

---

## 🚀 Execution Plan (Bottom-Up)

1.  **Step 1 (The Scribe)**: Create `Assimilator` agent in `body/digestion/assimilator.py`.
    *   *Goal*: Crawl `eyes/archive`, read gems, rewrite with perfect YAML headers.
2.  **Step 2 (The Stream)**: Setup `pgvector` container and NATS worker.
    *   *Goal*: Listen for "New File" events and index them.
3.  **Step 3 (The Graph)**: Install `graphrag` and configure "Nightly Build".
    *   *Goal*: Run Map-Reduce on `memory/semantic` to find hidden patterns.
