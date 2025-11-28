---
id: design_hybrid_swarm_architecture
type: design
status: draft
author: Swarmlord
timestamp: 2025-11-25
tags: [local-ai, hybrid-swarm, openrouter, chromebook-plus]
---

# HFO Design: Hybrid Swarm Architecture (Chromebook Plus)

> **Context**: Running a swarm on limited hardware (8GB RAM) with unlimited cloud scaling (OpenRouter).
> **Goal**: Maximize local autonomy (Heartbeat) while leveraging cloud power for heavy lifting (Swarm).

## 1. The RAM Reality (Diagnosis)
Your Chromebook Plus has ~6.3GB usable RAM.
*   **Ollama (Gemma 2 2B)**: Consumes ~2.1GB (32% of RAM).
*   **VS Code**: Consumes ~1.5GB+ (Multiple processes).
*   **OS/System**: Consumes ~1.0GB.
*   **Free Headroom**: ~1.5GB.

**Verdict**: You **cannot** run a parallel local swarm of 2B+ models. You will crash.
**Solution**:
1.  **Sequential Local**: Run one agent at a time (Time-Sharing).
2.  **Parallel Tiny**: Run multiple 0.5B models (Qwen 2.5 0.5B).
3.  **Hybrid (Recommended)**: Local Heartbeat + Remote Swarm.

## 2. The Hybrid Architecture (Recommended)

### The Heart (Local - Lvl 0)
*   **Model**: Gemma 2 2B (Already installed).
*   **Role**: The Conductor. It never sleeps. It checks the time, monitors NATS, and decides *what* needs to be done.
*   **Cost**: $0 (Local Energy).

### The Hands (Remote - Lvl 1+)
*   **Model**: OpenRouter (Claude 3.5 Haiku, Gemini Flash, Llama 3.1 70B).
*   **Role**: The Workers. When the Heartbeat says "Research this topic", it spawns 10-50 remote agents.
*   **Cost**: Low (Flash/Haiku are cheap), but infinite scale.

```mermaid
graph TD
    subgraph Chromebook [Local Host]
        H[Heartbeat (Gemma 2 2B)] -->|Polls| T[Time/NATS]
        H -->|Decides| D{Action Needed?}
        D -->|Yes| S[Swarm Controller (Python)]
    end

    subgraph Cloud [OpenRouter]
        S -->|Spawns| W1[Worker 1 (Gemini Flash)]
        S -->|Spawns| W2[Worker 2 (Claude Haiku)]
        S -->|Spawns| W3[Worker 3 (Llama 3.1)]
    end

    W1 -->|Writes| N[NATS (Stigmergy)]
    W2 -->|Writes| N
    W3 -->|Writes| N
    N -->|Reads| H
```

## 3. Local Swarm Options (If you MUST stay local)

If you want to run multiple agents *locally* on this device, you must go **Tiny**.

### Option A: The "Ant Farm" (Qwen 2.5 0.5B)
*   **Model**: `qwen2.5:0.5b`
*   **Size**: ~400MB per instance.
*   **Capacity**: You could run ~3-4 of these in parallel.
*   **Intelligence**: Surprisingly good for simple tasks (classification, simple JSON), but don't ask for philosophy.

### Option B: The "Time-Share" (Sequential)
*   **Model**: Gemma 2 2B.
*   **Method**: Agent 1 runs -> Unloads -> Agent 2 runs -> Unloads.
*   **Pros**: Smarter agents.
*   **Cons**: Slow. Not a "swarm" in real-time, more like a relay race.

## 4. Recommendation
**Stick to the Hybrid Model.**
1.  Keep **Gemma 2 2B** as your always-on Heartbeat.
2.  Use **OpenRouter** for the heavy lifting (Research, Coding, Analysis).
3.  Use **NATS** as the glue between them.

## 5. How to Free RAM?
1.  **Kill Unused Models**: `ollama stop gemma3:4b` (if running).
2.  **VS Code Extensions**: Disable heavy extensions if not needed.
3.  **Browser Tabs**: Chrome eats RAM. Close unused tabs.
4.  **Restart Ollama**: Sometimes it holds onto VRAM. `sudo systemctl restart ollama`.
