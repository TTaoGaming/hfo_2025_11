---
card:
  id: karmic_web_workflow
  source: workflow_karmic_web.md
  type: Concept
---

# 🃏 Karmic Web Workflow

> **Intuition**: The Karmic Web transmutes the ephemera of agent actions into perdurable stigmergic wisdom, bridging the frenzy of reflex with the sagacity of ancestral memory.

## 📜 The Incantation (Intent)
```gherkin
Feature: Assimilate Ephemeral Signals into Stigmergic Graph

  Scenario: Crystallize Agent Signal into Karmic Web
    Given an agent publishes a validated signal to NATS Hot State
    When the Assimilator consumes and parses the signal
    Then entities are extracted and merged into Node Store
    And relations are extracted and merged into Edge Store
    And semantic embeddings are upserted into Vector Store
    And acknowledgments are propagated back to NATS
```

## 🧪 The Catalyst (Code)
```python
# The Essence
from pydantic import BaseModel
from typing import Dict, Any
import networkx as nx
import pgvector  # Assuming pgvector integration

def assimilate_karmic_signal(signal: Dict[str, Any]) -> bool:
    """
    Core Assimilator: Parse, Extract, Crystallize.
    """
    # Parse & Validate
    event = SignalEvent.model_validate(signal)  # Pydantic
    
    # Extract Entities/Relations (LLM or rule-based)
    entities = extract_entities(event.content)
    relations = extract_relations(event.content, entities)
    
    # Merge into Graph (Postgres + NetworkX)
    graph = nx.MultiDiGraph()  # Load subgraph
    for entity in entities:
        graph.add_node(entity.id, **entity.props)
    for rel in relations:
        graph.add_edge(rel.source, rel.target, **rel.props)
    upsert_graph(graph)  # Custom Postgres upsert
    
    # Embed & Upsert Vector
    embedding = embed_content(event.content)  # e.g., OpenAI
    upsert_vector(event.id, embedding, metadata={
        'entities': [e.id for e in entities],
        'relations': len(relations)
    })
    
    return True  # Ack success
```

## ⚔️ Synergies
*   **NATS Hot State**: Consumes ephemeral signals from agent actions/results for immediate ingestion.
*   **Tri-Brain Architecture**: Mediates Reflex (fast) and Reasoning (slow) brains via persistent graph queries.
*   **Planner Agents**: Provides "Ancestral Wisdom" for long-horizon planning through vector similarity and graph traversal.
*   **Stigmergic GraphRAG**: Leverages Postgres (nodes/edges), NetworkX (traversal), pgvector (semantics) for emergent memory.
*   **State Lifecycle**: Supports transitions from Ephemeral → Crystallized → Reinforced/Decaying → Pruned via citations and GC.