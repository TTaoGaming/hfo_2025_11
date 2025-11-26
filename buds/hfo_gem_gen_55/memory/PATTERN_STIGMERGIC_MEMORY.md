# 🧠 HFO Stigmergic Memory Pattern (The Refinery)

> **Status**: Draft
> **Context**: Gen 55 (The Gem)
> **Philosophy**: "Information moves from High Entropy (Hot) to Low Entropy (Refined)."

## 1. The Thermodynamic Cycle (Hot -> Cold -> Refined)

Memory in HFO is not a static bucket; it is a **flow**. Information enters as "Hot" signals, cools into "Cold" artifacts, and is then "Refined" into "Gem" quality wisdom.

### Phase 0: HOT (The Stream)
*   **Medium**: NATS JetStream (`nerves/bus`)
*   **State**: Ephemeral, High Velocity, High Entropy.
*   **Content**: Agent logs, tool outputs, raw observations, heartbeats.
*   **Retention**: Short (Minutes/Hours).
*   **Action**: **Assimilator** listens and captures relevant signals.

### Phase 1: COLD (The Sediment)
*   **Medium**: File System (`sensors/archives/`)
*   **State**: Durable, Static, Unstructured.
*   **Content**: Raw files, HTML dumps, JSON logs, zip archives of previous generations.
*   **Retention**: Permanent (Archival).
*   **Action**: **Indexer** scans and registers these artifacts in the Manifest.

### Phase 2: REFINED (The Gem)
*   **Medium**: DuckDB (`memory/memory-duckdb/hfo_core.duckdb`)
*   **State**: Structured, Queryable, Typed.
*   **Content**:
    *   **`artifacts`**: Metadata about Cold files (Path, Hash, Size).
    *   **`generations`**: Registry of Gen 1-55 (The History).
    *   **`knowledge`**: Extracted facts, summaries, and vectors.
*   **Refinement Levels (N)**:
    *   **N=0**: Raw Ingestion (Just the file record).
    *   **N=1**: Metadata Extraction (Tags, Dates, Authors).
    *   **N=2**: Summarization (LLM Summary).
    *   **N=3**: Vectorization (Embeddings for Semantic Search).
    *   **N=4**: Integration (Graph Links to other concepts).
    *   **N=5**: Crystallization (Human-verified "Truth" in `docs-diataxis`).

---

## 2. The Data Structure (DuckDB Schema)

The `hfo_core.duckdb` will enforce this pattern.

### Table: `generations`
| Column | Type | Description |
| :--- | :--- | :--- |
| `id` | INT | Generation Number (1-55) |
| `codename` | TEXT | e.g., "Swarmlord", "Gemini", "Obsidian" |
| `status` | TEXT | "Lost", "Archived", "Refined" |
| `summary` | TEXT | High-level description (Refined N=2) |

### Table: `artifacts`
| Column | Type | Description |
| :--- | :--- | :--- |
| `id` | UUID | Unique ID |
| `gen_id` | INT | FK to `generations` |
| `path` | TEXT | Relative path in `sensors/archives` |
| `type` | TEXT | "code", "markdown", "log", "image" |
| `refinement_level` | INT | Current N-level (0-5) |
| `content_hash` | TEXT | For deduplication |

### Table: `knowledge_vectors`
| Column | Type | Description |
| :--- | :--- | :--- |
| `artifact_id` | UUID | FK to `artifacts` |
| `chunk_id` | INT | Sequence number |
| `text_content` | TEXT | The actual text chunk |
| `embedding` | FLOAT[] | 1536d Vector (via `vss`) |

---

## 3. The Ingestion Protocol

1.  **Manifest Creation**: We define `ingestion_manifest.yaml` to list all targets.
2.  **Cold Storage**: We move/copy target files into `sensors/archives/`.
3.  **Registration**: The **Assimilator** reads the manifest and inserts rows into `artifacts` (N=0).
4.  **Refinement Loop**:
    *   **Swarm A (Tagger)**: Selects N=0 items, extracts tags -> Updates to N=1.
    *   **Swarm B (Summarizer)**: Selects N=1 items, generates summary -> Updates to N=2.
    *   **Swarm C (Embedder)**: Selects N=2 items, generates vectors -> Updates to N=3.
