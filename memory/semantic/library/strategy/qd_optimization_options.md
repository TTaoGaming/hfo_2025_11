---
title: 'QD Optimization Stacks: Decision Matrix for Evolutionary Engine'
summary: Compares Quality-Diversity optimization options like R.A.P.T.O.R., OpenELM,
  DSPy, and EvoTorch, recommending a hybrid 'Chimera' stack using pyribs, DSPy, and
  LLM mutations for diverse agent evolution in Hive Fleet Obsidian.
domain: Strategy
concepts:
- Quality-Diversity Optimization
- MAP-Elites
- Chimera Stack
- pyribs
- DSPy
owner: Architect
actionable: true
related_files:
- AGENTS.md
type: crystallized_memory
status: active
last_verified: '2025-11-21'
---

# 🧬 Quality-Diversity (QD) Optimization Stacks

> **Status**: Research / Decision Matrix
> **Context**: Selecting the Evolutionary Engine for Gen 50 (The Evolutionary Forge).

## 🦅 Executive Summary

Quality-Diversity (QD) algorithms (like MAP-Elites) differ from standard optimization (like Gradient Descent) in one key way:
*   **Optimization**: Finds the *single highest peak* (The Best Agent).
*   **Quality-Diversity**: Finds the *highest peak of every mountain* (The Best Agent for every Niche).

For Hive Fleet Obsidian, we need **QD** because we want a diverse swarm (Aggressive, Cautious, Creative, Analytical), not just one "perfect" average agent.

---

## 📊 The QD Stack Matrix

| Feature | **1. R.A.P.T.O.R. (Current)** | **2. The Code-Breaker (OpenELM)** | **3. The Prompt-Smith (DSPy)** | **4. The Neuro-Link (EvoTorch)** |
| :--- | :--- | :--- | :--- | :--- |
| **Core Library** | `pyribs` (Python) | `OpenELM` (CarperAI) | `DSPy` (Stanford) | `EvoTorch` (Bosch) |
| **Compute Backend** | `Ray` (Distributed) | `LangChain` / `Transformers` | `PyTorch` (Logic) | `PyTorch` (Tensor) |
| **Algorithm** | **MAP-Elites** / CMA-MAE | **ELM** (Evolutionary LM) | **MIPRO** / BootstrapFewShot | **PGPE** / SNES / CEM |
| **Search Space** | **Feature Space** (Behavior) | **Code Space** (Diffs) | **Prompt Space** (Signatures) | **Parameter Space** (Weights) |
| **Mutation Op** | Gaussian / Iso Line | LLM-Generated Diffs | LLM-Generated Rewrites | Gradient / Noise |
| **Throughput** | 🟢 **High** (Async Actors) | 🟡 **Medium** (Sequential) | 🟢 **High** (Compiled) | 🔴 **Low** (Local Sim focus) |
| **Viability** | ✅ **Production Ready** | ⚠️ **Maintenance Risk** | ⚠️ **Optimization Only** | ❌ **Hard for Text** |

---

## 🔍 Deep Dive

### 1. R.A.P.T.O.R. (The Baseline)
*   **Stack**: `pyribs` + `Ray` + `Pydantic`.
*   **Philosophy**: "The Infrastructure is the Engine."
*   **How it works**:
    1.  **Map**: Define a grid of behaviors (e.g., `x=verbosity`, `y=aggressiveness`).
    2.  **Elites**: Keep the best agent in each cell.
    3.  **Ray**: Spawns 100 agents in parallel to fill the grid.
*   **Pros**: Perfect for API-based agents. Handles latency well. Explicit control over diversity.
*   **Cons**: Requires manual definition of "Behavior Descriptors" (what makes an agent unique?).

### 2. The Code-Breaker (OpenELM)
*   **Stack**: `OpenELM` + `LangChain`.
*   **Philosophy**: "Code is the Genotype."
*   **How it works**:
    1.  Treats the Agent's Python code as the DNA.
    2.  Uses an LLM (The Mutator) to write "Diffs" or patches to improve the code.
    3.  Evaluates the new code in a sandbox.
*   **Pros**: True "Self-Improving Code." Can invent new architectures, not just tune prompts.
*   **Cons**: The library is older (2023) and may need forking. High risk of generating broken code (syntax errors).

### 3. The Prompt-Smith (DSPy)
*   **Stack**: `DSPy` + `MIPRO` (Multi-prompt Instruction PRoposal Optimizer).
*   **Philosophy**: "Programming, not Prompting."
*   **How it works**:
    1.  Treats the Agent as a "Module" with "Signatures" (Inputs/Outputs).
    2.  Runs a Bayesian-style optimization to find the *perfect* prompt instructions and few-shot examples.
*   **Pros**: State-of-the-Art (SOTA) for maximizing a metric (e.g., "Accuracy"). Extremely stable.
*   **Cons**: **Not QD.** It converges to *one* solution. It eliminates diversity to maximize score.

### 4. The Neuro-Link (EvoTorch)
*   **Stack**: `EvoTorch` + `PyTorch`.
*   **Philosophy**: "Evolution is Math."
*   **How it works**:
    1.  Uses Distribution-Based Evolutionary Strategies (NES/CMA-ES).
    2.  Optimizes continuous parameters (vectors).
*   **Pros**: Mathematically rigorous. Great if we are tuning "Soft Prompts" (embeddings).
*   **Cons**: Very hard to apply to discrete text/code. Overkill for API-based agents.

---

## 🧠 The "Chimera" Recommendation

We should not choose *one*. We should **hybridize** the best parts of 1, 2, and 3.

**The "Chimera" Stack:**
1.  **The Skeleton (R.A.P.T.O.R.)**: Use `pyribs` to maintain the **Diversity Grid** (The Archive).
2.  **The Muscle (DSPy)**: Use `DSPy` modules as the **Genotype**. Instead of evolving raw strings, we evolve structured DSPy signatures.
3.  **The Mutation (OpenELM-style)**: Use an LLM to propose changes to the DSPy modules (Mutation Operator), but store the results in the Pyribs grid.

**Why?**
*   `pyribs` ensures we keep diverse agents.
*   `DSPy` ensures the agents actually work (compiles to valid prompts).
*   `OpenELM` logic (LLM-as-Mutator) drives the creativity.

### 🛠️ Next Step
If you agree, I will update `AGENTS.md` to reflect this **"Chimera Strategy"** (Pyribs + DSPy + LLM-Mutation) and deprecate the pure "Ray + LangGraph" approach for the evolutionary layer.


---
**Grafted by Gardener**: [[gen_50_README|Gen 50 Hub]]
