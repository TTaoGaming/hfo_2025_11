# 🏟️ The Model Coliseum: Local Swarm Evaluation Protocol

> **Status**: Design (Gen 55)
> **Context**: Chromebook Plus (8GB RAM) Optimization
> **Goal**: Identify the optimal "Swarm Model" that balances **Intelligence** (Instruction Following) with **Efficiency** (Concurrency > 8).

## 1. The Contenders (November 2025)

We are evaluating the following "Small Language Models" (SLMs) for local swarm usage:

| Model | Size | VRAM (Est) | Type | Hypothesis |
| :--- | :--- | :--- | :--- | :--- |
| **Gemma 3 270m** | 0.27B | ~300MB | Base/Instruct | **Champion**. Proven 16+ agents. Low IQ, high speed. |
| **Gemma 3 1b** | 1.1B | ~800MB | Instruct | **Challenger**. Likely smarter, but can we run 8? |
| **Llama 4 1b** | 1.2B | ~900MB | Instruct | **Challenger**. Meta's latest. Optimized for edge. |
| **DeepSeek-R1-Distill-Qwen-1.5B** | 1.5B | ~1.1GB | Reasoning | **Wildcard**. High IQ (CoT), but heavy. Maybe 4 agents? |
| **Phi-4 Mini** | 1.8B | ~1.3GB | Reasoning | **Heavyweight**. Microsoft's reasoning powerhouse. |

## 2. The "Stigmergy Eval" (The Gauntlet)

Standard benchmarks (MMLU) don't matter. We need **Swarm Compliance**.
The model must follow the **HFO Stigmergy Protocol** (JSON Output, Pydantic Schema).

### The Test Set (5 Tasks)
1.  **The Parser**: "Extract these 3 facts from this log into JSON." (Strict Schema)
2.  **The Decider**: "Given this Cynefin state (Chaos), what is the heartbeat interval?" (Logic)
3.  **The Summarizer**: "Condense this 50-line log into a 1-line 'BLUF'." (Compression)
4.  **The Router**: "Which topic (Ontos, Telos, Chronos) does this message belong to?" (Classification)
5.  **The Poet**: "Write a Haiku about Rust." (Creativity/Sanity Check)

## 3. The Arena (Blast Shield)

We will use the `sandbox/crash_test/run_safe.sh` harness to run the gauntlet.

*   **Constraint**: 2GB RAM Limit (Docker).
*   **Concurrency**: 1, 4, 8 Agents.
*   **Metric**:
    *   **Pass Rate**: % of valid JSON outputs.
    *   **Throughput**: Tokens/sec per agent.
    *   **Survival**: Did the container crash?

## 4. The Execution Plan

1.  **Pull Models**: `ollama pull gemma3:1b`, `ollama pull llama4:1b`, etc.
2.  **Run Gauntlet**: Execute `sandbox/crash_test/evaluate_models.py` (to be created).
3.  **Scoreboard**: Update `AGENTS.md` with the winner.

## 5. The "Swarm Tier" Strategy

Based on results, we will assign models to roles:

*   **Tier C (Cell)**: `gemma3:270m`. Runs in the thousands. Simple tasks.
*   **Tier S (Squad)**: `gemma3:1b` / `llama4:1b`. Runs in the dozens. Logic tasks.
*   **Tier H (Heart)**: `deepseek-r1-distill`. Runs singly (1-1-1-1). Complex reasoning.
