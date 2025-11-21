# 📥 HFO Gem Ingestion Strategy: 4 Viable Options

> **Status**: Decision Matrix
> **Context**: Moving ancestral wisdom from `eyes/archive` to `memory/semantic`.
> **Goal**: Simple, composable ingestion that prepares for future GraphRAG.

## 🦅 Executive Summary

We need to move "HFO Gems" into the Brain. We have 4 levels of sophistication.
**Recommendation**: Start with **Option 2 (The Taxonomist)**. It provides the highest long-term value by cleaning the data *before* we embed or graph it.

---

## 🧩 The 4 Options

### Option 1: The Symbiote (Static Header Injection)
*   **Mechanism**: A simple Python script.
*   **Logic**:
    1.  Read file.
    2.  Check for YAML header.
    3.  If missing, prepend a *generic* header (e.g., `owner: Swarmlord`, `type: gem`).
    4.  Move to `memory/semantic`.
*   **Pros**: ⚡ Instant, 🆓 Free, 🟢 Simple.
*   **Cons**: 🧠 Dumb. Metadata is generic. Doesn't help search much.
*   **Composability**: Base layer. Can be upgraded by Option 2 later.

### Option 2: The Taxonomist (LLM Semantic Tagging)
*   **Mechanism**: `PreyAgent` (Assimilator) using `Instructor`.
*   **Logic**:
    1.  Read file.
    2.  **LLM Call**: "Summarize this and extract 5 key concepts."
    3.  Generate a *rich* YAML header (`summary`, `concepts`, `domain`).
    4.  Save to `memory/semantic`.
*   **Pros**: 🧠 Smart. Makes files self-describing. Enables high-quality filtering.
*   **Cons**: 💲 Token cost (low with Haiku/Flash), 🐢 Slower (seconds per file).
*   **Composability**: **High**. Perfect input for Vector/Graph layers.

### Option 3: The Vectorizer (Embeddings)
*   **Mechanism**: Python script + `pgvector`.
*   **Logic**:
    1.  Read file.
    2.  Chunk text (e.g., 500 tokens).
    3.  **API Call**: Get Embeddings (OpenAI/Cohere).
    4.  Store vectors in Postgres.
*   **Pros**: 🔍 Enables Semantic Search ("Find gems about evolution").
*   **Cons**: 🏗️ Requires Infrastructure (Docker/DB). Harder to debug than text files.
*   **Composability**: Can run *after* Option 2.

### Option 4: The Weaver (Graph Extraction)
*   **Mechanism**: `PreyAgent` + `NetworkX`.
*   **Logic**:
    1.  Read file.
    2.  **LLM Call**: "Extract entities and relationships (A -> relates_to -> B)."
    3.  Save relationships to `memory/semantic/graph_edges.jsonl`.
*   **Pros**: 🕸️ Starts the Knowledge Graph. Connects the dots.
*   **Cons**: 💲 Expensive. Complex schema definitions needed.
*   **Composability**: Can run *parallel* to Option 3.

---

## 📊 Comparison Matrix

| Feature | **1. Symbiote** | **2. Taxonomist** | **3. Vectorizer** | **4. Weaver** |
| :--- | :--- | :--- | :--- | :--- |
| **Intelligence** | 🌑 None | 🌓 High (Metadata) | 🌕 High (Semantic) | 🌟 Deep (Relational) |
| **Cost** | 🆓 Zero | 💲 Low | 💲 Low | 💲💲 Medium |
| **Speed** | ⚡ Instant | 🐇 Fast | 🐇 Fast | 🐢 Slow |
| **Artifact** | File + Header | File + Rich Header | DB Rows | Graph Edges |
| **Dependency** | Python | LLM API | Postgres + API | LLM API |
| **Verdict** | **Too Basic** | **✅ Best Start** | **Add later** | **Add last** |

## 🚀 Proposed Workflow (The Pipeline)

We can compose these into a pipeline:
1.  **Run Option 2 (Taxonomist)**: Clean and tag all files.
2.  **Run Option 3 (Vectorizer)**: Ingest the clean files into `pgvector` for search.
3.  **Run Option 4 (Weaver)**: (Future) Build the graph from the clean files.

**Immediate Action**: Implement **Option 2** using a `PreyAgent` script.
