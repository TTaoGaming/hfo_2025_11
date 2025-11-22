---
holon:
  id: 550e8400-e29b-41d4-a716-446655440001
  type: architecture
  layer: static
  status: draft
  author: Swarmlord
  timestamp: 2025-11-22T12:00:00Z
---
# 🌀 Holonic Stigmergy Architecture

> **Status**: Draft
> **Type**: Architecture
> **Domain**: Biology/Infrastructure

## 1. The Core Concept
The HFO Stigmergy System is **Holonic** (recursive/nested) and **Self-Referential**. It manifests in three states of matter, sharing a unified DNA (Schema).

### The Three States
1.  **Static Stigmergy (Solid)**: YAML Headers in Files. (Source of Truth)
2.  **Hot Stigmergy (Gas)**: NATS JetStream Messages. (Real-time Signaling)
3.  **Cold Stigmergy (Liquid)**: GraphRAG/Postgres Entries. (Long-term Memory)

## 2. The Unified Holon Schema
Every artifact, signal, or memory unit is a **Holon**. It must contain the standard **Holon Header**.

### 2.1 The Header (YAML/JSON)
```yaml
holon:
  id: <UUID>                  # Unique Identifier (v4)
  type: <String>              # e.g., "intent", "concept", "task", "artifact"
  version: <String>           # Schema version (e.g., "1.0")

  # Holonic Structure
  parent_id: <UUID|null>      # The container Holon (e.g., Mission -> Task)
  refs: [<UUID>]              # Lateral references (Dependencies/Related)

  # State
  layer: <Enum>               # "static", "hot", "cold"
  status: <Enum>              # "active", "archived", "draft"

  # Provenance
  author: <String>            # Agent ID or User
  timestamp: <ISO8601>        # Creation time
  hash: <SHA256>              # Content hash for integrity
```

## 3. Implementation Across Layers

### 3.1 Static (Files)
**Format**: YAML Frontmatter in Markdown/Code files.
**Location**: `brain/`, `body/`, `memory/`.

```markdown
---
holon:
  id: 550e8400-e29b-41d4-a716-446655440000
  type: concept
  layer: static
  status: active
  author: Swarmlord
  timestamp: 2025-11-22T12:00:00Z
---
# Content Here...
```

### 3.2 Hot (NATS)
**Format**: JSON Payload in JetStream Subject `hfo.<type>.<id>`.
**Location**: NATS Stream `HIVE_MIND`.

```json
{
  "holon": {
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "type": "signal",
    "layer": "hot",
    "parent_id": "...",
    "timestamp": "..."
  },
  "payload": {
    "message": "Task completed",
    "result": "..."
  }
}
```

### 3.3 Cold (Memory/DB)
**Format**: Relational Row + JSONB + Vector.
**Location**: Postgres `holons` table.

| Column | Type | Description |
| :--- | :--- | :--- |
| `id` | UUID | Primary Key |
| `header` | JSONB | The full Holon Header |
| `body` | TEXT | The content (Markdown/Code) |
| `embedding` | VECTOR | Semantic embedding of body |
| `links` | JSONB | Adjacency list (derived from refs) |

## 4. The Cycle of Matter
1.  **Sublimation (Static -> Hot)**: An agent reads a file and broadcasts its intent.
2.  **Deposition (Hot -> Static)**: An agent receives a signal and writes a file (Artifact).
3.  **Condensation (Hot -> Cold)**: The Assimilator consumes signals and stores them in DB.
4.  **Freezing (Static -> Cold)**: The Assimilator ingests files into the DB.
