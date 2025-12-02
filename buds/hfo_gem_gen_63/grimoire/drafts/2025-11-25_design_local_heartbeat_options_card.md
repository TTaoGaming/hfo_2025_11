---
card:
  id: design_local_heartbeat_2025_11_25
  source: 2025-11-25_design_local_heartbeat_options.md
  type: Spell
---

# 🃏 Obsidian Heart: Local Heartbeat LLM

> **Intuition**: The Obsidian Heart is the unyielding, minimalistic pulse of edge AI vigilance, a perpetually awake guardian that detects anomalies on constrained hardware while preserving swarm rhythm.

## 📜 The Incantation (Intent)
```gherkin
Feature: Deploy Local Heartbeat LLM for 24/7 Anomaly Detection

  Scenario: Monitor system logs on Chromebook Plus
    Given Ollama server running Gemma 3 4B model on Chromebook Plus
    And recent system logs or NATS messages are available
    When the heartbeat service polls logs every 60 seconds
    And submits logs to the LLM with prompt: "You are the Heartbeat. Output 'NOMINAL' if clear. Output 'SIGNAL: <reason>' if anomalous."
    Then the LLM responds with "NOMINAL" for normal state and logs "Thump-Thump"
    And routes "SIGNAL: <reason>" to alert Swarm Level 1
```

## 🧪 The Catalyst (Code)
```python
# The Essence
import requests
import time
import subprocess

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "gemma3:4b"

def heartbeat_check(logs: str) -> str:
    """Poll Ollama for anomaly detection in logs."""
    prompt = f"""You are the Heartbeat. Output 'NOMINAL' if logs are clear.
Output 'SIGNAL: <reason>' if interesting. Logs: {logs}"""
    
    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    }
    
    try:
        resp = requests.post(OLLAMA_URL, json=payload, timeout=30)
        resp.raise_for_status()
        result = resp.json()["response"].strip()
        return result
    except Exception as e:
        return f"SIGNAL: Heartbeat error - {str(e)}"

# Usage in systemd service loop
def main_loop():
    while True:
        # Fetch logs (e.g., tail system logs or NATS)
        logs = subprocess.getoutput("tail -n 50 /var/log/syslog || echo 'No logs'")
        status = heartbeat_check(logs)
        print(f"Heartbeat: {status}")
        if "SIGNAL:" in status:
            # Alert Swarm Lvl 1 (e.g., via NATS pub)
            pass
        time.sleep(60)

if __name__ == "__main__":
    main_loop()
```

## ⚔️ Synergies
*   **Systemd Integration**: Runs as a persistent `hfo-heartbeat` service for 24/7 availability on Chromebook Plus.
*   **Swarm Escalation**: Anomalies trigger alerts to higher Octree levels (Lvl 1 Swarm) via NATS or logs.
*   **Ollama Ecosystem**: Leverages Ollama for seamless model serving; extensible to Phi-3.5, Llama 3.2, or Qwen 3 alternatives.
*   **Edge Hardware**: Optimized for Chromebook Plus (8GB+ RAM), leaving headroom for OS and multi-tasking.
*   **Prompt Chaining**: Feeds into tool-calling agents for deeper analysis in full HFO architecture.