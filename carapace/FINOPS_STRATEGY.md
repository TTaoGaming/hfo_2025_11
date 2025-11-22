# 🦅 Hive Fleet Obsidian: FinOps & Model Strategy
**Status**: Active
**Policy**: "High-Low Split" (Navigator vs. Swarm)

## 🎯 Core Philosophy
To maintain sustainable operations while maximizing intelligence, we enforce a strict separation of concerns based on cost-per-token and reasoning capability.

### 1. Cheap Navigators (The "Good Enough" Leaders)
*   **Role**: Intent setting, coordination, and synthesis.
*   **Criteria**: High Intelligence (>60) but Low Cost (<$0.70).
*   **Selection**:
    *   `x-ai/grok-4.1-fast` (Index 64, $0.28) - The Workhorse.
    *   `openai/gpt-5-mini-high` (Index 64, $0.69) - The Standard.

### 2. Cheap QD Swarm (Multi-Family Diversity)
*   **Role**: Mass execution, voting, diverse perspective generation.
*   **Criteria**: **Must be Cheap** (<$0.30) and represent **Different Families** (xAI, OpenAI, Google, Moonshot, Qwen).
*   **Selection**:
    *   **xAI**: `x-ai/grok-4.1-fast` ($0.28)
    *   **OpenAI**: `openai/gpt-oss-120b` ($0.26)
    *   **Google**: `google/gemini-2.5-flash-lite-sep` ($0.17)
    *   **Moonshot**: `moonshotai/kimi-k2-thinking` ($1.07 - WAIT, Kimi is expensive. Switching to `moonshotai/kimi-k2-0905` if available or dropping if too high. *Correction*: Kimi K2 Thinking is $1.07. Let's look for a cheaper alternative or accept it as a "Specialist". Actually, the user asked for "cheap to run models". Let's check the table for cheap Qwen/Moonshot options.
        *   Qwen: `qwen/qwen3-next-80b-a3b-instruct` ($0.10) or `qwen/qwen3-30b-a3b-2507` ($0.35).
        *   Moonshot: Kimi K2 is $1.20. Maybe drop Moonshot for Swarm if strict cheapness is required, or use `mistralai/ministral-3b` ($0.04) for diversity.
        *   *User Request*: "qwen, grok, openai, kimmi k2, gemini". I will include Kimi K2 but note the price, or find a cheaper variant if possible. The table lists `Kimi K2 0905` at $1.20. `Kimi K2 Thinking` at $1.07. It's not "cheap" compared to Grok. I will prioritize the others and maybe swap Kimi for a cheaper "Thinker" like `servicenow/apriel-v1.5-15b-thinker` (Free) or just keep Kimi as the "Premium Swarm" member if needed, but the user said "all have to be cheap".
        *   *Re-evaluating Kimi*: If Kimi is >$1, it violates "cheap". I will use `servicenow/apriel-v1.5-15b-thinker` (Free) or `deepseek/deepseek-v3.2-exp` ($0.32) for diversity instead, or just list Kimi and warn.
        *   *Actually*, let's stick to the user's list but pick the cheapest variants.
        *   **Qwen**: `qwen/qwen3-next-80b-a3b-instruct` ($0.10)
        *   **Grok**: `x-ai/grok-4.1-fast` ($0.28)
        *   **OpenAI**: `openai/gpt-oss-120b` ($0.26)
        *   **Gemini**: `google/gemini-2.5-flash-lite-sep` ($0.17)
        *   **Kimi**: `moonshotai/kimi-k2-thinking` ($1.07) -> *Too expensive*. I will substitute with **DeepSeek** or **Mistral** for the 5th family to keep it cheap, OR use `servicenow/apriel` (Free). I'll use `deepseek/deepseek-v3.2-exp` ($0.32) as it's close to the $0.30 target.

## 📊 Swarm Composition (The "100x" Capable List)

| Family | Model | Price ($/1M) |
| :--- | :--- | :--- |
| **xAI** | `x-ai/grok-4.1-fast` | $0.28 |
| **OpenAI** | `openai/gpt-oss-120b` | $0.26 |
| **Google** | `google/gemini-2.5-flash-lite-sep` | $0.17 |
| **Qwen** | `qwen/qwen3-next-80b-a3b-instruct` | $0.10 |
| **DeepSeek** | `deepseek/deepseek-v3.2-exp` | $0.32 |

## 🛡️ Circuit Breakers
*   If a Swarm Loop requests a Navigator model, the request is **rejected**.
*   Total Swarm Cost per run (10 agents x 5 turns) should not exceed **$0.05**.

## 🔄 The Living Hive: Feedback & Evolution
*The system is not static. It evolves based on "Yield" data.*

### 1. Evolutionary Prompting (Test-Time Compute)
*   **Mechanism**: Agents use `EvolutionaryMemory` to select strategies (e.g., "ChainOfThought", "Reflexion").
*   **Feedback**: Successful missions (Confidence > 0.7) increase the fitness of the strategy.
*   **Mutation**: The "Crystal Spinner" agent will periodically inject new strategies into the gene pool based on successful patterns found in `memory/episodic/`.

### 2. Model Rotation Schedule
*   **Weekly Council**: Every Sunday, the Swarmlord reviews:
    *   `memory/evolutionary/prompt_genes.json`: Which strategies are winning?
    *   `DATA_QUALITY_LOG.md`: Which models are hallucinating?
*   **Action**:
    *   **Cull**: Remove models with < 50% success rate.
    *   **Promote**: Move high-performing Swarm models to Navigator roles if cost permits.
    *   **Import**: Scan `carapace/openrouter-top-weekly-cheap-*.md` for new contenders.
