---
holon:
  id: 35d4d8d1-d4c2-4a80-a88b-4ff4e4a0c18e
  type: codex_entry
  quadrant: how-to
  source_ref: /home/tommytai3/hive_fleet_obsidian_2025_11/buds/hfo_gem_gen_63/src/verify_nats.py
hexagon:
  ontos: Hive Fleet Obsidian
  logos: diataxis
---

# How to Verify NATS Connection and JetStream Functionality

This guide provides step-by-step instructions for verifying a NATS connection and the functionality of JetStream within the context of the `verify_nats.py` script.

## Explanation

**Why**: Verifying the NATS connection and JetStream functionality is essential for ensuring that your application can communicate effectively over NATS, which is a messaging system designed for performance and scalability.

**What**: This script connects to a NATS server, subscribes to a specific subject, publishes a message to it, and then verifies that the message can be received correctly.

## Step-by-Step Instructions

1. **Import Necessary Modules**: The script starts by importing required libraries. Ensure you have the necessary libraries installed, such as `nats` and `asyncio`.
   ```python
   import asyncio
   import nats
   from nats.errors import ConnectionClosedError, TimeoutError, NoServersError
   import sys
   import os
   ```

2. **Add Root to Path**: Modify the system path to include the configuration settings by adding a specific directory.
   ```python
   sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
   ```

3. **Load Configuration**: Import settings from the config module to retrieve the NATS URL.
   ```python
   from src.config import settings
   ```

4. **Define the Asynchronous Function**: Create an asynchronous function named `verify_nats`. This function encompasses all the connection verification logic.
   ```python
   async def verify_nats():
   ```

5. **Connect to NATS Server**: Use the NATS URL from settings to establish a connection.
   ```python
   nc = await nats.connect(settings.NATS_URL)
   ```

6. **Create JetStream Context**: After connecting, create a JetStream context to perform streaming operations.
   ```python
   js = nc.jetstream()
   ```

7. **Subscribe to a Subject**: Subscribe to the `hfo.gen63.heartbeat` subject to listen for messages.
   ```python
   sub = await nc.subscribe("hfo.gen63.heartbeat")
   ```

8. **Publish a Message**: Send a test message to the same subject to ensure publishing is operational.
   ```python
   payload = b"Gen 63 Pulse"
   await nc.publish("hfo.gen63.heartbeat", payload)
   ```

9. **Receive the Message**: Attempt to receive a message and validate that it matches the published payload.
   ```python
   msg = await sub.next_msg(timeout=2)
   ```

10. **Close the Connection**: Finally, close the connection to the NATS server.
   ```python
   await nc.close()
   ```

## Handling Errors

The script includes error handling for various scenarios: 
- If there are no available NATS servers, it captures the `NoServersError`.
- General exceptions are also caught to handle any unforeseen errors during the process. 