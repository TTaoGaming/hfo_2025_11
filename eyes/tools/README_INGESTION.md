# HFO Unified Ingestion System

This system ingests the entire Hive Fleet Obsidian workspace into a PostgreSQL vector database (`pgvector`).

## Architecture

1.  **Database**: PostgreSQL with `pgvector` extension.
    *   `ingestion_queue`: Tracks the status of every file (PENDING, PROCESSING, COMPLETED, FAILED, SKIPPED).
    *   `knowledge_bank`: Stores the actual content and embeddings.

2.  **Scripts**:
    *   `inventory_scanner.py`: Scans the filesystem and populates the `ingestion_queue`. (Producer)
    *   `queue_worker.py`: Processes files from the queue, generates embeddings, and saves to `knowledge_bank`. (Consumer)
    *   `monitor_dashboard.py`: Real-time dashboard to view ingestion progress.
    *   `force_reset_queue.py`: **DANGER** - Wipes the queue and resets the schema. Use only if you need to restart from scratch.

## How to Run

1.  **Start the Worker**:
    This script does the heavy lifting. It will run until all files are processed.
    ```bash
    python3 queue_worker.py
    ```

2.  **Monitor Progress**:
    Open a new terminal and run this to see a live dashboard.
    ```bash
    python3 monitor_dashboard.py
    ```

## Troubleshooting

*   **Worker crashes**: Just restart `python3 queue_worker.py`. It will pick up where it left off (idempotent).
*   **Stuck "PROCESSING" items**: If the worker crashes mid-file, some items might remain in 'PROCESSING' state. The worker has logic to reset these on startup (or you can manually update them in SQL).
*   **Database Connection Errors**: Ensure the PostgreSQL service is running and credentials in the scripts match your setup.

## Specs
*   **Confidence Cap**: 90% (0.9) for epistemic uncertainty.
*   **HFO Levels**:
    *   `lvl0`: Raw data/logs.
    *   `lvl1`: Consensus/Synthesized knowledge.
