# 🧪 HFO Phoenix Smoke Tests

This repository is configured with a **Dev Container** that spins up the full Gen 50 stack.

## 🚀 How to Run Tests

1.  **Enter the Container:**
    *   Press `Ctrl+Shift+P` (or `Cmd+Shift+P`).
    *   Select **"Dev Containers: Reopen in Container"**.
    *   Wait for the build to complete.

2.  **Run the Smoke Test Script:**
    ```bash
    python src/smoke_test.py
    ```

3.  **Run via Pytest:**
    ```bash
    pytest tests/test_infrastructure.py
    ```

## 🔍 What is Tested?

| Component | Check |
| :--- | :--- |
| **Postgres** | Connects to `db:5432`, verifies credentials, checks for `pgvector` extension. |
| **NATS** | Connects to `nats:4222`, creates a JetStream, publishes/consumes a message. |
| **Temporal** | Connects to `temporal:7233`, verifies namespace access. |
| **Libraries** | Verifies `langchain`, `pydantic`, and other core deps are installed. |
