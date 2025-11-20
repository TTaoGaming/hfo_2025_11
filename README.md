# Hive Fleet Obsidian (Gen 50) - November 2025

## Vision: The Phoenix Project
This repository represents the "Phoenix" rebirth of Hive Fleet Obsidian (HFO), designated **Generation 50**. 

**Core Philosophy:**
*   **Declarative First:** All logic is defined first in **Gherkin** (Behavior Driven Development) and **Mermaid** diagrams.
*   **Intent/Implementation Split:** 
    *   **Intent:** Human-defined specs (Gherkin/Mermaid).
    *   **Implementation:** AI-generated code (Python) that satisfies the intent.
*   **Unified Memory:** Leveraging `pgvector` to consolidate all historical data and "AI slop" into a queryable, semantic memory bank.
*   **SOTA Tooling:** Using the best-in-class tools for 2025 (Pytest-BDD, LangChain/LlamaIndex, Postgres+pgvector).

## Structure
*   `intent/`: The source of truth. Contains `.feature` files and `.mmd` diagrams.
*   `src/`: The implementation code.
*   `tests/`: Test runners and step definitions.
*   `ingestion/`: Tools to process and ingest the "Archive" into the Unified Memory Bank.

## Getting Started
1.  Install dependencies: `pip install -r requirements.txt`
2.  Run tests: `pytest`
