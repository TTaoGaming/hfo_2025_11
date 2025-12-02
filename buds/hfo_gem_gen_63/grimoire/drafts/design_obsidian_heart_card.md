---
card:
  id: obsidian-heart-atomic-heartbeat
  source: design_obsidian_heart.md
  type: Concept
---

# 🃏 💓 Obsidian Heart

> **Intuition**: A single atomic agent pulses as the unyielding core of a fractal holarchy, vigilantly sustaining system life while summoning resource-intensive squads only from strength.

## 📜 The Incantation (Intent)
```gherkin
Feature: Obsidian Heart Atomic Heartbeat Protocol

  Scenario: Single-threaded heart performs rhythmic cycle without crashing
    Given the Atomic Heart agent is running strictly single-threaded with gemma3:270m model
    And system RAM is monitored
    When the variable heartbeat interval elapses (60s resting / 10s active)
    Then it perceives system health and NATS signals
    And it reacts by performing light maintenance or summoning Fractal Squad if RAM > 4GB
    And it executes the action without exceeding 1GB total usage
    And it yields a heartbeat signal via NATS subject "hfo.heartbeat"
```

## 🧪 The Catalyst (Code)
```python
# The Essence
import time
import psutil  # For RAM monitoring
import nats  # NATS client

def atomic_heartbeat_loop():
    """
    The Obsidian Heart: Single-threaded, always-on loop.
    Perceive -> React -> Execute -> Yield.
    """
    nc = nats.connect("nats://localhost:4222")  # NATS connection
    model = "gemma3:270m"  # Lightweight model
    
    while True:
        # 1. Perceive
        ram_free_gb = psutil.virtual_memory().available / (1024**3)
        signals = nc.subscribe("hfo.tasks").msgs().__anext__() if any_pending() else []
        
        # 2. React & 3. Execute
        if ram_free_gb > 4 and needs_swarm(signals):
            # Summon Squad (gated spawn)
            import subprocess
            subprocess.Popen(["python", "body/hands/fractal_squad.py"])
        else:
            # Light maintenance (e.g., PREY inference)
            light_prey_inference(model)
        
        # 4. Yield
        nc.publish("hfo.heartbeat", b"pulse")
        
        # Variable sleep: rest or active
        sleep_time = 10 if ram_free_gb > 6 else 60
        time.sleep(sleep_time)
```

## ⚔️ Synergies
*   **NATS Integration**: Publishes heartbeats to `hfo.heartbeat` and subscribes to task signals for squad summoning.
*   **Fractal Squad**: Gates `fractal_squad.py` (8 agents) spawn based on RAM >4GB, enforcing holarchy separation.
*   **Resource Optimization**: Tailored for Chromebook Plus (8GB RAM) with `gemma3:270m`, enabling 24/7 operation under 1GB.
*   **Blast Shield Testing**: Pairs with `sandbox/crash_test/run_safe.sh` Docker limits (2GB RAM) for safe swarm validation.
*   **Holarchy Restoration**: Purges ad-hoc multi-loops from `cleanroom_prey_1111.py`, consecrating it as pure atomic heart.