---
holon:
  id: 3f4a4c14-93e3-4154-a513-bdcb99f8d783
  type: codex_entry
  quadrant: how-to
  source_ref: /home/tommytai3/hive_fleet_obsidian_2025_11/buds/hfo_gem_gen_63/src/stigmergy_loop.py
hexagon:
  ontos: hive_fleet_obsidian
  logos: diataxis
---

# How to Run the Stigmergy Loop

The Stigmergy Loop is a simple asyncio-based program that demonstrates a pattern of interaction between a Navigator and a Shaper in an asynchronous environment. Here's a step-by-step guide to running the Stigmergy Loop.

## Prerequisites
Ensure you have the required packages installed and the appropriate environment set up. Specifically, you need the following modules:
- `asyncio`
- `logging`

## Step-by-Step Instructions

1. **Import Necessary Libraries**  
   The loop begins with importing the required libraries:
   ```python
   import asyncio
   import logging
   import sys
   import os
   ```

2. **Setup System Path**  
   Add the root directory to the path to access local modules:
   ```python
   sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
   ```

3. **Import Configuration and Adapters**  
   Import the necessary settings and adapter modules:
   ```python
   from src.config import settings
   from src.adapters.nats_adapter import NatsAdapter
   from src.adapters.fs_adapter import LocalFileSystemAdapter
   ```

4. **Configure Logging**  
   Set up the logging configuration for better visibility of run-time events:
   ```python
   logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
   logger = logging.getLogger("StigmergyLoop")
   ```

5. **Define the Main Loop Function**  
   Create an asynchronous function that manages the loop:
   ```python
   async def run_loop():
   ```

6. **Initialize the Adapters**  
   Within the loop, initialize the NATS Adapter and File System Adapter:
   ```python
   bus = NatsAdapter(settings.NATS_URL)
   fs = LocalFileSystemAdapter(base_path="buds/hfo_gem_gen_63/sandbox")
   await bus.connect()
   ```

7. **Set Up Callbacks for Navigator and Shaper**  
   Create callback functions to handle messages from the NATS bus:
   ```python
   async def shaper_callback(msg: dict):
       # Handle INTENT messages
   async def navigator_callback(msg: dict):
       # Handle REPORT messages
   ```

8. **Subscribe to NATS Topics**  
   Subscribe the callbacks to the appropriate topics:
   ```python
   await bus.subscribe("hfo.gen63.intent", shaper_callback)
   await bus.subscribe("hfo.gen63.report", navigator_callback)
   ```

9. **Trigger the Loop**  
   Publish an initial intent message to start the process:
   ```python
   await bus.publish("hfo.gen63.intent", {
       "type": "INTENT",
       "payload": {
           "path": "hello_stigmergy.txt",
           "content": "The Swarm is One. The Loop is Closed."
       }
   })
   ```

10. **Handle Completion or Timeout**  
    Use a Future object to wait for the loop to complete or timeout after 5 seconds:
   ```python
   await asyncio.wait_for(loop_complete, timeout=5.0)
   ```

11. **Clean Up**  
    Close the NATS bus connection:
   ```python
   await bus.close()
   ```

12. **Run the Loop**  
    Ensure that `run_loop` is called if the script is executed directly:
   ```python
   if __name__ == "__main__":
       asyncio.run(run_loop())
   ```

By following these steps, you can successfully run the Stigmergy Loop, facilitating communication between a Navigator and Shaper via an asynchronous message bus.