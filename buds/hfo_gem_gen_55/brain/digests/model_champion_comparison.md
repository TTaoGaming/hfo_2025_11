# HFO Digest: Local Model Championship (Nov 2025)

> **Context**: Selecting the Lvl 0 Heartbeat for a Chromebook Plus (8GB RAM).
> **Constraint**: Must leave RAM for OS + VS Code. Ideally < 2.5GB VRAM usage.

## 1. The Current Champion: Llama 3.2 3B
*   **Vibe**: "The Special Forces Scout"
*   **Why it wins**: Meta specifically trained this for "Edge AI" (phones/laptops). It has excellent instruction following for its size.
*   **Strengths**:
    *   **Tool Use**: Very good at outputting structured JSON (crucial for the Heartbeat).
    *   **Size**: ~2.0GB. Fits comfortably.
    *   **Speed**: Fast enough.
*   **Weaknesses**: Can be a bit generic in personality.

### 2. The Contenders (2B - 4B Parameters)

| Model | Params | Est. RAM (Q4) | Strengths | Weaknesses | Best For |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Llama 3.2** | 3B | ~2.0 GB | Balanced, Tool Use, "Edge" Optimized | Generic personality | **Daily Driver** |
| **Qwen 2.5** | 3B | ~2.2 GB | **Coding**, Math, Logic, JSON | "Dry" / Robotic tone | **Coding Assistant** |
| **Gemma 2** | 2B | ~1.6 GB | **Fastest**, Lightest | "2B Dumb" (Hallucinations) | **Background / Safety** |
| **Phi-3.5 Mini**| 3.8B | ~2.4 GB | Deep Reasoning, 128k Context | **Heavy**, Slow | **Deep Research** |
| **Gemma 3** | 4B | ~3.3 GB | Multimodal (Vision) | **Too Heavy** for 8GB RAM | **Multimedia** |

### 3. The Verdict for Chromebook Plus (8GB)

1.  **The Safe Bet (Current Champion):** `llama3.2:3b`
    *   It sits right at the 2GB mark, leaving ~2-3GB for VS Code and Chrome.
    *   It has excellent tool calling capabilities for our agentic needs.

2.  **The "Unstick" Option:** `gemma2:2b`
    *   If your system is hanging, **switch to this**.
    *   It saves ~400MB-600MB of RAM compared to Llama/Qwen.
    *   *Trade-off:* It is less smart at complex instructions.

3.  **The Coding Specialist:** `qwen2.5:3b`
    *   If you are doing pure coding tasks and Llama is failing.
    *   *Warning:* It uses slightly more RAM than Llama.

### 4. Diagnostic Status (2025-11-25)
*   **System Status:** ⚠️ **Redlining**
*   **Memory:** 5.5GB / 6.3GB Used (87%).
*   **Culprit:** `ollama runner` (~2.4GB) + VS Code (~1.5GB).
*   **Recommendation:** If the system hangs, downgrade to **Gemma 2 2B** or close browser tabs.

## 3. The Speedster: Gemma 2 2B
*   **Vibe**: "The Hummingbird"
*   **Why consider it**: It's tiny (1.6GB).
*   **Strengths**:
    *   **Safety**: It will almost never crash your system.
    *   **Speed**: Blazing fast.
*   **Weaknesses**: It's "2B dumb". It might miss subtle context or hallucinate on complex instructions.
*   **Verdict**: **Use only if RAM is tight**.

## 4. The Professor: Phi-3.5 Mini (3.8B)
*   **Vibe**: "The Library Owl"
*   **Why consider it**: It was trained on "textbook quality" data. It reasons like a 7B model.
*   **Strengths**:
    *   **IQ**: The smartest model in this weight class.
    *   **Context**: 128k context window (can read huge logs).
*   **Weaknesses**:
    *   **Heavy**: ~2.4GB. It pushes the limit of your 8GB RAM when context fills up.
    *   **Slow**: Slower than Llama/Gemma.
*   **Verdict**: **High Risk / High Reward**. Use for "Deep Thinking" pulses, not rapid ones.

## 5. The Heavyweight: Gemma 3 4B
*   **Status**: **Disqualified**
*   **Reason**: At ~3.3GB, it choked the system during our test. It leaves no room for the OS or VS Code.

---

## Recommendation for Next Week
If **Llama 3.2 3B** is working well, keep it.
If you want to experiment, try **Qwen 2.5 3B**. It might be sharper at following the strict JSON format of the heartbeat protocol.
