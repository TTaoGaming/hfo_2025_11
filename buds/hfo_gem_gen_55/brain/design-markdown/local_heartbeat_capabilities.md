# HFO Guide: The Local Heartbeat (Gemma 3 4B)

> **Model**: Gemma 3 4B (via Ollama)
> **Role**: Lvl 0 (Atomic) Heartbeat
> **Status**: Installed

## 1. What Can It Do? (The Brain)
Gemma 3 4B is a **Reasoning Engine**. Think of it as a very smart brain in a jar.
*   **✅ Reasoning**: It can look at a log line and tell you if it's an error or just noise.
*   **✅ Formatting**: It can turn messy text into clean JSON.
*   **✅ Decision Making**: It can decide *which* workflow to trigger based on the time of day.
*   **✅ Summarization**: It can compress a paragraph into a sentence.

## 2. What Can't It Do? (The Body)
Gemma **cannot** interact with the world directly. It is just text-in, text-out.
*   **❌ No Built-in Memory**: It forgets everything the moment the script stops or the context window (8k tokens) fills up. It does not "remember" yesterday unless you feed it yesterday's logs.
*   **❌ No Direct Action**: It cannot "run a workflow" or "write to NATS". It can only output the text: `"ACTION: RUN_WORKFLOW"`.
*   **❌ No Clock**: It doesn't know what time it is unless you tell it in the prompt.

## 3. How We Give It Powers (The Suit)
To make Gemma "run workflows" and "write to Stigmergy", we wrap it in a Python script (`heartbeat.py`). This script is the **Body**.

### The Cycle (The Pulse)
1.  **Input (Senses)**: Python reads the time, checks NATS (Hot Stigmergy), and reads the last few logs.
2.  **Prompt (Thought)**: Python sends this to Gemma: *"It is 12:00 PM. The logs say 'Error'. What should I do?"*
3.  **Output (Decision)**: Gemma replies: *"ACTION: LOG_ERROR payload={'severity': 'high'}"*
4.  **Action (Hands)**: Python parses that string and actually executes the NATS publish command.

## 4. Can It Write to HOT Stigmergy?
**Yes, but indirectly.**
*   **You ask**: "Can Gemma write to NATS?"
*   **Answer**: Gemma generates the *content* and the *intent*. The Python script does the *writing*.

## 5. Can It Orchestrate?
**Yes, via "Micro-Decisions".**
*   You can set up a cron job (or a loop) that wakes Gemma up every minute.
*   Gemma checks the schedule (fed via prompt).
*   Gemma decides: "Time to run the backup."
*   Python executes the backup script.

## 6. The "Heartbeat" Script Plan
We will write `heartbeat.py` to:
1.  **Loop** every 60 seconds.
2.  **Inject Context**: Current Time, System Load, Recent Stigmergy Signals.
3.  **Ask Gemma**: "Status Check. Any orders?"
4.  **Execute**: If Gemma says "WRITE_STIGMERGY", the script writes to NATS.
