# HFO Stigmergy System Tests

This folder contains tests for the HFO Stigmergy System (Gen 55).

## `test_stigmergy_system.py`

This script tests the full "Hot -> Cold" Stigmergy loop using NATS JetStream (Hot) and LanceDB (Cold).

### Prerequisites
1.  NATS Server running on `localhost:4225`.
2.  `lancedb` and `nats-py` installed.

### What it does
1.  **Setup**: Initializes NATS Streams (`HFO`) and KV Bucket (`hfo_pillars`), and LanceDB Table (`hfo_stigmergy`).
2.  **Assimilator**: Starts a background process (`scripts/run_assimilator.py`) that listens to NATS and writes to LanceDB.
3.  **Publish**: Publishes test messages to all 8 Stigmergy Pillars (`hfo.ontos`, `hfo.logos`, etc.) and updates NATS KV.
4.  **Verify KV**: Checks if NATS KV contains the latest state for each pillar.
5.  **Verify LanceDB**: Checks if LanceDB contains the historical records for each pillar.

### How to Run
From the workspace root:
```bash
python3 buds/hfo_gem_gen_56/venom/tests/test_stigmergy_system.py
```
