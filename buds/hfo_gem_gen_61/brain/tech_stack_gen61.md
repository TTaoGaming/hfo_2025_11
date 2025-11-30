---
holon:
  id: hfo-tech-stack-gen61
  type: architecture
  status: active
  generation: 61
  author: Swarmlord
  theme: Total Tool Virtualization
---

# 🛠️ HFO Gen 61: The Tech Stack

> **Source**: Swarmlord (Brain Dump 2025-11-30)
> **Philosophy**: **Intent/Implementation Split**.
> **Core**: Hexagonal, Anti-fragile, Byzantine Quorum.

## 1. The Intent Layer (The Brain)
*   **Language**: **Literate Declarative Gherkin** (English).
*   **Visualization**: **Mermaid Diagrams** (Flowchart, Sequence, Class).
*   **Role**: Defines *WHAT* needs to happen. No code logic here.

## 2. The Logic Layer (The Nerves)
*   **Validation**: **Pydantic**. Strict typing and schema validation.
*   **Agent Logic**: **Instructor** (Structured Outputs) + **LangGraph** (Stateful Multi-Actor Applications).
*   **Orchestration**: **Temporal**. Durable execution, retries, and state persistence.

## 3. The Compute Layer (The Muscle)
*   **Distributed Compute**: **Ray**. Scaling the swarm across cores and clusters.
*   **Simulation**: **Ray** (for JADC2 Shaping/Monte Carlo).

## 4. The Memory Layer (The Blood)
*   **Hot Stigmergy**: **NATS JetStream**. Event bus for "The Swarm Web" (Present).
*   **Cold Memory**: **SQLite3** (Iron Ledger) + **LanceDB** (Vector Mirror).
*   **Observability**:
    *   **GraphRAG**: Knowledge Graph retrieval.
    *   **PGVector**: (Alternative/Complement to LanceDB).
    *   **LangSmith**: Tracing LLM calls.
    *   **OpenTelemetry**: System-wide tracing.

## 5. The Architecture
*   **Hexagonal**: Ports and Adapters. Vendor neutral.
*   **Anti-fragile**: The system gains strength from stress (Venom/Disruptors).
*   **Adversarial Byzantine Quorum**: 1 Perceive -> 1 Orchestrate -> 8 Chant -> 1 Reflexion (Heartbeat 1181).
