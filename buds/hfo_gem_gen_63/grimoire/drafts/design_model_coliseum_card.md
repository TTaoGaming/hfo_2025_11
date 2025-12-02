---
card:
  id: model-coliseum
  source: design_model_coliseum.md
  type: Tool
---

# 🃏 Model Coliseum 🏟️

> **Intuition**: In the arena of ruthless concurrency, only models that wed intelligence to efficiency emerge as swarm champions.

## 📜 The Incantation (Intent)
```gherkin
Feature: Swarm Model Evaluation Protocol

  Scenario: Identify Optimal SLM for Local Swarm via Stigmergy Gauntlet
    Given a roster of SLM contenders with VRAM estimates and hypotheses
      And a 2GB RAM Docker constraint
      And concurrency levels of 1, 4, 8 agents
      And 5 Stigmergy Eval tasks enforcing JSON/Pydantic compliance
    When executing the gauntlet harness "sandbox/crash_test/run_safe.sh"
      And measuring pass rate, tokens/sec throughput, and container survival
    Then score models on Swarm Compliance metrics
      And assign tiers (C: Cell, S: Squad, H: Heart) in AGENTS.md
      And crown the champion balancing IQ and >8 concurrency
```

## 🧪 The Catalyst (Code)
```python
# The Essence
import subprocess
import json
from typing import Dict, List
import ollama

def run_model_gauntlet(model: str, concurrency: int, tasks: List[Dict]) -> Dict:
    """
    Execute Stigmergy Eval gauntlet for a model at given concurrency.
    Returns metrics: {'pass_rate': float, 'throughput': float, 'survived': bool}
    """
    # Pull model if needed
    subprocess.run(['ollama', 'pull', model], check=True)
    
    results = {'passes': 0, 'total_tokens': 0, 'start_time': None, 'end_time': None, 'crashed': False}
    
    try:
        start = subprocess.run(['date', '+%s'], capture_output=True, text=True).stdout.strip()
        results['start_time'] = float(start)
        
        for task in tasks:
            # Simulate concurrent agents (parallel ollama calls)
            responses = []
            for _ in range(concurrency):
                resp = ollama.chat(model=model, messages=[{'role': 'user', 'content': task['prompt']}])
                responses.append(resp['message']['content'])
            
            # Validate JSON/Pydantic schema compliance
            valid = all(validate_json_schema(r, task['schema']) for r in responses)
            if valid:
                results['passes'] += 1
            
            results['total_tokens'] += sum(len(r) for r in responses)  # Proxy for tokens
        
        end = subprocess.run(['date', '+%s'], capture_output=True, text=True).stdout.strip()
        results['end_time'] = float(end)
        
    except subprocess.CalledProcessError:
        results['crashed'] = True
    
    duration = results['end_time'] - results['start_time']
    results['pass_rate'] = (results['passes'] / len(tasks)) * 100
    results['throughput'] = results['total_tokens'] / duration if duration > 0 else 0
    return results

def validate_json_schema(response: str, schema: Dict) -> bool:
    """Placeholder: Use Pydantic for strict HFO Stigmergy validation."""
    try:
        data = json.loads(response)
        # PydanticModel(**data)  # Real impl
        return True
    except:
        return False
```

## ⚔️ Synergies
*   **HFO Stigmergy Protocol**: Enforces JSON/Pydantic outputs across all 5 gauntlet tasks (Parser, Decider, etc.).
*   **Ollama Integration**: Local model pulling/running via CLI/API for Chromebook-optimized SLMs like Gemma3/Llama4.
*   **Sandbox Harness**: Leverages `sandbox/crash_test/run_safe.sh` and 2GB Docker for crash-proof eval.
*   **AGENTS.md Scoreboard**: Auto-updates tiers (C/S/H) post-gauntlet for dynamic swarm role assignment.
*   **Tiered Swarm Architecture**: Feeds winners into Cell/Squad/Heart layers for >8 concurrent agents.