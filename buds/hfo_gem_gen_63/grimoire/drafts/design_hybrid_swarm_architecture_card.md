---
card:
  id: hybrid-swarm-architecture
  source: design_hybrid_swarm_architecture.md
  type: Concept
---

# 🃏 Hybrid Swarm Architecture

> **Intuition**: A vigilant local heart pulses decisions from constrained hardware, awakening an infinite cloud swarm to execute the impossible.

## 📜 The Incantation (Intent)
```gherkin
Feature: Hybrid Swarm Architecture on Limited Hardware

  Scenario: Orchestrate local heartbeat with remote swarm scaling
    Given a Chromebook Plus with 6GB usable RAM and Gemma 2 2B via Ollama
    And access to OpenRouter API for cloud models
    And NATS server for stigmergy communication
    When the local Heartbeat detects an action via time/NATS polling
    Then the Swarm Controller spawns remote workers (e.g., Claude Haiku, Gemini Flash)
    And workers write results to NATS for Heartbeat consumption
    And local RAM usage stays under 1.5GB headroom
```

## 🧪 The Catalyst (Code)
```python
# The Essence: Hybrid Swarm Controller
import nats
import ollama
import openrouter  # Hypothetical client; use requests or litellm
import time

async def heartbeat_conductor():
    """Local Gemma 2B heart: Poll, decide, dispatch to cloud swarm."""
    nc = await nats.connect("nats://localhost:4222")
    
    while True:
        # Poll NATS and time
        tasks = await nc.fetch("swarm.tasks", timeout=5)
        now = time.time()
        
        if tasks or (now % 3600 == 0):  # Hourly check or pending tasks
            # Local decision with Gemma 2B
            response = ollama.chat(
                model="gemma2:2b",
                messages=[{"role": "user", "content": f"Decide action for tasks: {tasks}"}]
            )
            action = response["message"]["content"]
            
            if "spawn_swarm" in action:
                await swarm_controller(nc, action)
        
        await asyncio.sleep(30)  # Heartbeat interval

async def swarm_controller(nc, action):
    """Spawn remote OpenRouter workers."""
    workers = [
        {"model": "anthropic/claude-3.5-haiku", "task": "research"},
        {"model": "google/gemini-flash-exp", "task": "analyze"},
        {"model": "meta-llama/llama-3.1-70b-instruct", "task": "code"}
    ]
    for worker in workers[:10]:  # Scale to 10-50 as needed
        result = openrouter.chat(model=worker["model"], messages=[{"role": "user", "content": action}])
        await nc.publish("swarm.results", result["choices"][0]["message"]["content"].encode())
```

## ⚔️ Synergies
*   **NATS Stigmergy**: Glue for local Heartbeat reads/writes and remote worker outputs.
*   **Ollama Local**: Gemma 2 2B as always-on Lvl 0 conductor; extend to tiny Qwen 0.5B ants if fully local.
*   **OpenRouter Cloud**: Infinite Lvl 1+ scaling with cheap/fast models like Haiku/Flash.
*   **Chromebook Constraints**: Sequential/time-shared locals avoid RAM crashes; pairs with VS Code/RAM optimization tips.
*   **Swarm Evolution**: Builds toward full local "Ant Farm" or time-share relays as hardware upgrades.