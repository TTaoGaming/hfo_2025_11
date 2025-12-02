---
card:
  id: cb118335-bb1f-464d-8138-e3e5b40bfb84
  source: biology_organ_loops.md
  type: Concept
---

# 🃏 Physiology Loops

> **Intuition**: The Hive's vitality arises from asynchronous organ rhythms layered by speed, where swift reflexes safeguard ponderous cognition, embodying stratified parallelism over monolithic synchronization.

## 📜 The Incantation (Intent)
```gherkin
Feature: Asynchronous Physiology Loops

  Scenario: Process Incoming Stimulus Across Frequencies
    Given an environmental stimulus arrives at the Hive
    When the Reflex Loop evaluates at 100Hz
    Then if immediate danger detected
      Execute survival action via Ganglia/Mandibles
    Else relay to Cognitive Loop at 0.1Hz for analysis
      And Immune Loop monitors at 0.01Hz for maintenance
    And Evolution Loop adapts over days if patterns emerge
```

## 🧪 The Catalyst (Code)
```python
# The Essence: Simulate asynchronous organ loops with threading
import threading
import time
from typing import Callable

class PhysiologyLoops:
    def __init__(self):
        self.running = True
        self.loops = {
            "reflex": {"freq": 0.01, "target": self._reflex_fn},  # 100Hz
            "cognitive": {"freq": 10.0, "target": self._cognitive_fn},  # 0.1Hz
            "immune": {"freq": 100.0, "target": self._immune_fn},  # 0.01Hz
            "evolution": {"freq": 86400.0, "target": self._evolution_fn}  # Daily
        }
    
    def _reflex_fn(self):
        print("Reflex: Evasion check - FAST!")
    
    def _cognitive_fn(self):
        print("Cognitive: Planning analysis - SLOW.")
    
    def _immune_fn(self):
        print("Immune: Cleanup scan - BACKGROUND.")
    
    def _evolution_fn(self):
        print("Evolution: Genetic adaptation - LONGTERM.")
    
    def run(self):
        threads = []
        for name, config in self.loops.items():
            t = threading.Thread(target=self._loop_runner, args=(config["target"], config["freq"], name))
            t.daemon = True
            threads.append(t)
            t.start()
        
        try:
            while self.running:
                time.sleep(1)
        except KeyboardInterrupt:
            self.running = False
    
    def _loop_runner(self, fn: Callable, freq: float, name: str):
        while self.running:
            fn()
            time.sleep(freq)

# Usage
hive = PhysiologyLoops()
hive.run()
```

## ⚔️ Synergies
* **Sensory Integration**: Hooks into ganglia for stimulus input, enabling reflex short-circuiting.
* **Motor Output**: Reflex/Cognitive actions drive mandible/carapace effectors for world interaction.
* **Hive Architecture**: Scales to broader brain rhythms, preventing "slow brain" bottlenecks in parallel processing.
* **Evolutionary Layer**: Feeds long-term data to genetics module for adaptive tuning of loop frequencies.
* **Mermaid Visuals**: Complements sequence/gantt diagrams for debugging asynchronous flows in simulations.