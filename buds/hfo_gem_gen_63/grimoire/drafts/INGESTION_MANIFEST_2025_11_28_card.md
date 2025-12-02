---
card:
  id: ingestion-manifest-2025-11-28
  source: INGESTION_MANIFEST_2025_11_28.md
  type: Spell
---

# 🃏 Operation Cold Forge

> **Intuition**: Forging chaotic repository fragments into an immutable LanceDB citadel of vectorized memory, tempered by iron rules of capped certainty and structured pillars to withstand sybil deception.

## 📜 The Incantation (Intent)
```gherkin
Feature: Consolidate repository into LanceDB Cold Memory via Crawler Swarm

  Scenario: Ingest files with 8 Pillars metadata extraction under strict constraints
    Given a repository scope with recursive includes "**/*" and excludes [".git/", ".venv/", "__pycache__/", "*.pyc", "*.png", "*.jpg", "*.ico", "node_modules/", "buds/hfo_gem_gen_57/memory/lancedb/"]
      And swarm config using "x-ai/grok-beta" model via OpenRouter at temperature 0.0, concurrency 10, retries 3
    When crawler swarm processes each file:
      | Extract full content and 8 Pillars metadata (Ontos, Logos, Techne, Chronos, Pathos, Ethos, Topos, Telos) using "Unknown"/"None" for missing dimensions |
      | Generate 384-dim vector with all-MiniLM-L6-v2 |
      | Cap confidence at MAX 0.8, add tag "HFO lvl0", set UTC ingestion timestamp |
    Then store records in "buds/hfo_gem_gen_57/memory/lancedb" with schema:
      | id (uuid-v4), content, vector, source_path, timestamp, confidence, tags, metadata (8 Pillars) |
```

## 🧪 The Catalyst (Code)
```python
# The Essence
import os
import uuid
import lancedb
from sentence_transformers import SentenceTransformer
from typing import Dict, Any
import yaml  # For config loading

def cold_forge_ingestion(repo_root: str, db_path: str, swarm_config: Dict[str, Any]):
    """
    Orchestrates Crawler Swarm to ingest repo into LanceDB with 8 Pillars and constraints.
    """
    model = SentenceTransformer('all-MiniLM-L6-v2')
    db = lancedb.connect(db_path)
    
    # Hypothetical swarm dispatcher (integrate with actual swarm lib)
    def crawl_and_extract(file_path: str) -> Dict[str, Any]:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Simulate Grok-beta extraction (via OpenRouter API call)
        pillars = extract_pillars_via_swarm(content, file_path, swarm_config)  # Cap confidence <=0.8
        pillars = {p: pillars.get(p, {"unknown": True}) for p in ["ontos", "logos", "techne", "chronos", "pathos", "ethos", "topos", "telos"]}
        
        vector = model.encode(content).tolist()
        record = {
            "id": str(uuid.uuid4()),
            "content": content,
            "vector": vector,
            "source_path": file_path,
            "timestamp": time.time(),
            "confidence": min(pillars.get("confidence", 0.8), 0.8),
            "tags": ["HFO lvl0"],
            "metadata": pillars
        }
        return record
    
    # Parallel crawl (concurrency=10)
    files = [os.path.join(root, f) for root, _, fs in os.walk(repo_root) for f in fs
             if should_include(f)]  # Apply excludes
    records = [crawl_and_extract(f) for f in files[:]]  # Parallelize in prod
    
    table = db.create_table("cold_memory", data=records, mode="create")
    return table

def should_include(path: str) -> bool:
    excludes = {".git", ".venv", "__pycache__", ".pyc", ".png", ".jpg", ".ico", "node_modules", "lancedb"}
    return not any(ex in path for ex in excludes)

# Usage
config = yaml.safe_load(open("swarm_config.yaml"))  # Model: grok-beta, temp=0.0, etc.
cold_forge_ingestion(repo_root="buds/hfo_gem_gen_57", db_path="buds/hfo_gem_gen_57/memory/lancedb", swarm_config=config)
```

## ⚔️ Synergies
*   **LanceDB Integration**: Core vector store for HFO cold memory, enabling RAG and retrieval for gem generation.
*   **8 Pillars Schema**: Standardizes metadata across Ontos (identity) to Telos (purpose), fueling structured querying.
*   **Crawler Swarm**: Leverages Grok-beta for fact extraction, with concurrency and retries for scalable ingestion.
*   **Iron Rules**: Confidence cap (0.8) and "HFO lvl0" tagging prepare data for verification pipelines, linking to Sybil defense.
*   **Operation Cold Forge**: Seeds `hfo_gem_gen_57` memory layer, synergizing with dynamic hot memory for full-spectrum recall.