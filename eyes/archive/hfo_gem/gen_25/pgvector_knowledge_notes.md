---
hexagon:
  ontos:
    id: 4bae5b28-54d5-442d-ac46-b0d45c0f32ba
    type: md
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T11:07:35.910864Z'
    generation: 51
  topos:
    address: eyes/archive/hfo_gem/gen_25/pgvector_knowledge_notes.md
    links: []
  telos:
    viral_factor: 0.0
    meme: pgvector_knowledge_notes.md
---
# PGVector Knowledge Notes (Gen25)

BLUF: Curated high-signal reference snippets for the Knowledge layer (PostgreSQL + pgvector) to speed agent retrieval and grounding. Each snippet is <= 30 lines, attribution included, and designed for hybrid vector + text search.

## Purpose
- Provide stable anchors (schema, ingestion flow, scoring formula, healthcheck contract) for agents and workflows.
- Reduce duplication inside `AGENTS.md` by centralizing implementation details here.
- Enable rapid repo-aware consult answers that cite canonical sections.

## Schema Overview
PostgreSQL + pgvector extension. Core table (example name: `hfo_chunks`):
```
CREATE TABLE IF NOT EXISTS hfo_chunks (
  id BIGSERIAL PRIMARY KEY,
  source_path TEXT NOT NULL,
  chunk_id INT NOT NULL,
  content TEXT NOT NULL,
  embedding VECTOR(256) NOT NULL,
  provenance JSONB NOT NULL,
  meta JSONB NOT NULL,
  updated_at TIMESTAMPTZ DEFAULT NOW()
);
CREATE INDEX IF NOT EXISTS idx_chunks_path_chunk ON hfo_chunks(source_path, chunk_id);
CREATE INDEX IF NOT EXISTS idx_chunks_embedding ON hfo_chunks USING ivfflat (embedding vector_l2_ops) WITH (lists=100);
```

## Provenance Fields (meta.provenance)
- source: original file path
- source_hash: sha256 of full file
- chunk_span: line range in source
- git_commit: short SHA at ingest time
- model_version: embedding pipeline version (tfidf_svd_v1)
- generation_id: ingest run identifier
- status: active|retired

## Incremental Ingest Flow
1. Scan glob → compute file hashes vs `file_hashes.json`.
2. Classify: added / changed / removed.
3. Chunk changed & added files (target ~600 chars, boundary on sentence).
4. Fit or load TF-IDF + SVD model (256 dims). Normalize vectors.
5. Upsert rows (INSERT ON CONFLICT or DELETE+INSERT) for added/changed.
6. Mark removed paths `status=retired` via meta JSON.
7. Emit spans: counts {added, changed, removed}, timing {embed_ms, upsert_ms}.

## Hybrid Retrieval Formula
Let α = 0.65 (default), bm25_flag on:
```
vector_score = 1 - norm_l2_distance
text_score   = normalized_ts_rank
bm25_score   = normalized_bm25
hybrid = α*vector_score + (1-α)*0.5*(text_score + bm25_score)
```
If BM25 disabled: `hybrid = α*vector_score + (1-α)*text_score`.

## Healthcheck Contract
Output JSON fields:
```
status: PASS|FAIL
extensions: [ { name: "vector" }, ... ]
row_count: integer
vector_column_dims: 256
```
Receipt example evidence_refs: ["extensions:vector", "row_count:<N>"]

## Activity/Workflow Idempotency (Planned)
- Idempotency key: (source_path, source_hash, generation_id).
- Re-ingest same key → no-op or replace identical row.
- generation_id surfaces in spans and receipts for traceability.

## Planned Temporal Activities (preview)
- ingest_delta(root, glob, generation_id, allow_remove=True)
- healthcheck_vector_db()
- query_hybrid(q, k, alpha, bm25_flag)

## Query Result Shape (client.py)
```
{
  "source_path": str,
  "chunk_id": int,
  "content": str,
  "vector_score": float,
  "text_score": float,
  "bm25_score": float|None,
  "hybrid": float,
  "provenance": {...},
  "meta": {...}
}
```

## Common Operational Commands
(Use virtualenv Python where applicable)
```
python scripts/knowledge/ingest_repo.py --root hfo_gem/gen_25 --glob "**/*.{md,markdown,txt,yml,yaml,py,json}" --generation-id auto
python scripts/knowledge/healthcheck_cli.py
python scripts/knowledge/query_cli.py --q "hybrid retrieval" --path-prefix hfo_gem/gen_25/
```

## Safety & Guardrails
- ≤200 lines per write for docs (this file ~150 lines cap target <200).
- No placeholders (avoid TODO / ...).
- Receipts appended for ingest & healthcheck runs.

## References
- Source code: `scripts/knowledge/*.py`
- SSOT docs: `AGENTS.md` (Gen25 section)
- Model artifacts: `knowledge_index/models/`

## Changelog
- 2025-11-07: Initial curated notes created.
