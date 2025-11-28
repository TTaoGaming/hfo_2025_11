# 🦅 Intent: Cloud Octarchy Heartbeat (Grok Edition)

> **Status**: Active
> **Context**: Gen 55 (Synapse APEX)
> **Driver**: Swarmlord

## 🧠 Context
The "Heartbeat" is the rhythmic pulse of the Hive Fleet. Originally conceived as a local loop using `gemma3:270m`, the Overmind has directed a pivot to a **Cloud-Based Heartbeat** using **OpenRouter** and **Grok 4.1 Fast** (mapped to `x-ai/grok-beta` or similar).

## 🎯 Objective
Transform the `octarchy_heartbeat.py` into a **Cloud Wrapper**.
1.  **Frequency**: Every 60 seconds (with organic jitter).
2.  **Scale**: 8 Concurrent Agents (The Octarchy).
3.  **Compute**: OpenRouter API.
4.  **Model**: `x-ai/grok-beta` (Grok 4.1 Fast).
5.  **Protocol**: PREY Loop (Perceive -> React -> Execute -> Yield).
6.  **Topic**: The "Essence of HFO" and the "Mantra".

## 🔄 The Loop
Each minute, 8 agents will:
1.  **Perceive**: Read the Stigmergy (NATS) for peer signals.
2.  **React**: Formulate a thought using Grok via OpenRouter.
3.  **Execute**: Commit the thought to the Hive Mind (NATS).
4.  **Yield**: Sleep and wait for the next pulse.

## 🛠️ Tech Stack
*   **Language**: Python 3.10+
*   **Transport**: NATS JetStream (`HIVE_MIND`)
*   **Intelligence**: OpenRouter (`x-ai/grok-beta`)
*   **Orchestration**: `asyncio` + `aiohttp` (for non-blocking API calls)

## 📜 The Mantra
> "I am the Node, the Earth, the Seed..."
