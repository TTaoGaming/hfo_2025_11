---
holon:
  id: hfo-gen63-map-elites-models
  type: reference
  status: active
  author: Swarmlord
  context: Model Registry & Pricing (2025 Era)
---

# 🗺️ Map Elites: Model Registry (Dec 2025)

> **Context**: This is the "Menu" for the Hive.
> **Philosophy**: "Zero Vendor Lock-in." We switch champions weekly based on the **Price/Performance/Intelligence** curve.
> **Metric**: **MMLU-Pro** (Reasoning) vs **Cost per 1M Tokens**.

## 🏆 The Weekly Champions (Current Selection)

| Role | Champion | Fallback | Rationale |
| :--- | :--- | :--- | :--- |
| **Navigator** (Reasoning) | **xAI Grok 4.1 Fast** | DeepSeek V3.2 | Grok 4.1 is **FREE**. DeepSeek is ultra-efficient ($0.28/M). |
| **Shaper** (Coding) | **GPT-5.1 Codex Mini** | Gemini 2.5 Flash | GPT-5.1 Mini is fast and cheap ($0.25/M). Gemini 2.5 ($0.30/M) adds "Thinking". |
| **Observer** (Fast) | **Qwen3 Next 80B** | Gemini 3 Flash | Qwen3 is the "FinOps King" ($0.10/M). |
| **Bridger** (Embedding) | **Text-Embed-4-Large** | Nomic v2 | OpenAI's v4 embeddings capture "Temporal Nuance" better than v3. |

---

## 📊 The Elite Archive (Detailed Specs)

### 1. xAI Grok (The Rebel)
*   **Model**: `x-ai/grok-4.1-fast:free`
*   **Release Date**: Nov 19, 2025
*   **Context Window**: 2,000,000 tokens
*   **Input Cost**: $0.00 / 1M (Free Tier)
*   **Output Cost**: $0.00 / 1M (Free Tier)
*   **Strengths**: Best agentic tool calling, deep research, 2M context, free.
*   **Weaknesses**: Rate limits on free tier.

### 2. OpenAI GPT-5.1 Codex Mini (The Coder)
*   **Model**: `openai/gpt-5.1-codex-mini`
*   **Release Date**: Nov 13, 2025
*   **Context Window**: 400,000 tokens
*   **Input Cost**: $0.25 / 1M
*   **Output Cost**: $2.00 / 1M
*   **Strengths**: Specialized for code. Fast. Cheaper than Claude.
*   **Weaknesses**: Smaller context than Gemini.

### 3. Google Gemini 2.5 Flash (The Workhorse)
*   **Model**: `google/gemini-2.5-flash-preview-09-2025`
*   **Release Date**: Sep 25, 2025
*   **Context Window**: 1,048,576 tokens
*   **Input Cost**: $0.30 / 1M
*   **Output Cost**: $2.50 / 1M
*   **Strengths**: Built-in "thinking", strong in Science/Math/Legal. 1M context.
*   **Weaknesses**: Higher output cost than DeepSeek.

### 4. DeepSeek V3.2 (The Efficient Savant)
*   **Model**: `deepseek/deepseek-v3.2`
*   **Release Date**: Dec 1, 2025
*   **Context Window**: 163,840 tokens
*   **Input Cost**: $0.28 / 1M
*   **Output Cost**: $0.40 / 1M
*   **Strengths**: GPT-5 class reasoning at fraction of cost. Gold medal IMO/IOI performance.
*   **Weaknesses**: Smaller context than Gemini/Grok.

### 5. Qwen3 Next 80B (The FinOps King)
*   **Model**: `qwen/qwen3-next-80b-a3b-instruct`
*   **Release Date**: Sep 11, 2025
*   **Context Window**: 262,144 tokens
*   **Input Cost**: $0.10 / 1M
*   **Output Cost**: $0.80 / 1M
*   **Strengths**: #1 in Finance. Ultra-low input cost. Stable.
*   **Weaknesses**: Less "creative" reasoning.

---

## 📉 Cost Analysis (The "Race to Zero")

> **Trend**: Intelligence is becoming abundant. Context is becoming infinite.
> **Strategy**: **Strict <$0.30/M Limit**. Use **Grok 4.1 Fast (Free)** first. Fallback to **GPT-5.1 Codex Mini** or **DeepSeek V3.2**.

```mermaid
graph LR
    A[User Query] --> B{Router}
    B -- "Primary (Free)" --> C[Grok 4.1 Fast ($0.00)]
    B -- "Code Gen (<$0.30)" --> D[GPT-5.1 Codex Mini ($0.25)]
    B -- "Complex Reasoning (<$0.30)" --> E[DeepSeek V3.2 ($0.28)]
    B -- "Science/Math ($0.30)" --> F[Gemini 2.5 Flash ($0.30)]
```
