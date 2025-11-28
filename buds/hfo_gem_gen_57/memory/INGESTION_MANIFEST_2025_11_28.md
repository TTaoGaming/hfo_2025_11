---
holon:
  id: ingestion-manifest-2025-11-28
  type: manifest
  layer: static
  status: pending
  author: Swarmlord
  timestamp: 2025-11-28 12:00:00+00:00
hexagon:
  ontos:
    id: operation-cold-forge
    type: plan
    owner: Swarmlord
  chronos:
    status: pending
    urgency: 1.0
    decay: 0.0
    created: '2025-11-28T12:00:00Z'
  topos:
    address: buds/hfo_gem_gen_57/memory/INGESTION_MANIFEST_2025_11_28.md
  telos:
    viral_factor: 0.0
    meme: The Cold Forge
---

# 📜 Operation Cold Forge: Ingestion Manifest (SSOT)

> **Date**: November 28, 2025
> **Objective**: Consolidate the entire repository into a unified LanceDB Cold Memory.
> **Target**: `buds/hfo_gem_gen_57/memory/lancedb`

## ⚙️ Swarm Configuration

We will use a **Crawler Swarm** to read files, extract metadata, and ingest them into the database.

*   **Model**: `x-ai/grok-beta` (Grok 4.1 Fast)
    *   *Reasoning*: High speed, large context, low cost.
    *   *Note*: Explicitly requested by Overmind. Do not substitute.
*   **Provider**: OpenRouter
*   **Temperature**: `0.0` (Strict Fact Extraction)
*   **Concurrency**: 10 Agents (Parallel Processing)
*   **Retries**: 3 (Exponential Backoff)

## 🛡️ Ingestion Constraints (The Iron Rules)

1.  **Confidence Cap**: **MAX 0.8**.
    *   *Rule*: No matter how certain the model is, the recorded confidence score MUST NOT exceed 0.8.
    *   *Reason*: Recent Sybil attacks require us to treat all new data as "Probable" but not "Absolute".
2.  **Tagging**:
    *   *Rule*: Every record must include the tag `"HFO lvl0"`.
    *   *Reason*: Denotes raw, unverified ingestion.
3.  **Timestamping**:
    *   *Rule*: All records must have a UTC timestamp of ingestion.

## 🏛️ The 8 Pillars Schema (Metadata)

The Swarm must extract the following 8 dimensions from every file. If a dimension is missing, use "Unknown" or "None".

| Pillar | Dimension | Description | Example |
| :--- | :--- | :--- | :--- |
| **Ontos** | Identity | What is this? (Type, ID, Owner) | `{"type": "code", "language": "python"}` |
| **Logos** | Logic | How does it work? (Protocol, Algorithm) | `{"protocol": "stigmergy", "pattern": "pubsub"}` |
| **Techne** | Tools | What does it use? (Stack, Dependencies) | `{"stack": ["nats", "pydantic"]}` |
| **Chronos** | Time | When/Status? (Created, Urgency, Decay) | `{"status": "active", "generation": 57}` |
| **Pathos** | Health | Condition? (Stress, Validation, Quality) | `{"validation": "verified", "coverage": 0.9}` |
| **Ethos** | Rules | Security? (Permissions, Compliance) | `{"security": "internal", "license": "MIT"}` |
| **Topos** | Location | Where is it? (Path, Links) | `{"path": "src/main.py", "links": []}` |
| **Telos** | Purpose | Why does it exist? (Goal, Viral Factor) | `{"goal": "memory_consolidation"}` |

## 💾 Database Schema (LanceDB)

The final record structure for `hfo_gem_gen_57/memory/lancedb`:

```json
{
  "id": "uuid-v4",
  "content": "Full text content of the file...",
  "vector": [0.123, ...], // 384-dim (all-MiniLM-L6-v2)
  "source_path": "buds/hfo_gem_gen_57/AGENTS.md",
  "timestamp": 1732795200.0,
  "confidence": 0.8,
  "tags": ["HFO lvl0", "documentation"],
  "metadata": {
    "ontos": {...},
    "logos": {...},
    "techne": {...},
    "chronos": {...},
    "pathos": {...},
    "ethos": {...},
    "topos": {...},
    "telos": {...}
  }
}
```

## 📂 Scope (The Crawl List)

*   **Include**: `**/*` (Recursive)
*   **Exclude**:
    *   `.git/`
    *   `.venv/`
    *   `__pycache__/`
    *   `*.pyc`
    *   `*.png`, `*.jpg`, `*.ico` (Binary assets)
    *   `node_modules/`
    *   `buds/hfo_gem_gen_57/memory/lancedb/` (Self-reference)
