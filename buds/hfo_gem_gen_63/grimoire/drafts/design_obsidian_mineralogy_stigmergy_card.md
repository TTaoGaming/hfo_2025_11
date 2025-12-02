---
card:
  id: 550e8400-e29b-41d4-a716-446655440311
  source: design_obsidian_mineralogy_stigmergy.md
  type: Concept
---

# 🃏 💎 OBSIDIAN Mineralogy & Stigmergy

> **Intuition**: Rapid quenching of viscous, high-silica signals into sharp, amorphous obsidian artifacts—frozen events that agents knap into precise, lethal tools—captures the raw truth of speed over crystallization's bureaucratic decay.

## 📜 The Incantation (Intent)
```gherkin
Feature: OBSIDIAN Stigmergy
  Scenario: Quench high-velocity lava into knappable obsidian for agent utility
    Given a viscous stream of signals from NATS JetStream as "Felsic Lava"
    When the Genesis Protocol performs rapid quenching into Markdown/YAML files
    Then an immutable amorphous solid "Obsidian Glass" artifact is produced
    And agents knap context-specific flakes from the Knowledge Graph core
    And devitrification into grainy rhyolite is prevented by timely refinement
```

## 🧪 The Catalyst (Code)
```python
# The Essence: Quench NATS lava into obsidian file, then knap a flake
import asyncio
from nats.js import JetStreamContext  # Hypothetical NATS interface

async def obsidian_stigmergy(js: JetStreamContext, stream_subject: str, core_path: str, query: str):
    # Phase 1: Rapid Quenching (Capture Lava -> Glass)
    async def quench_lava():
        payload = await js.subscribe(stream_subject).msg.wait()
        obsidian_file = f"{core_path}/obsidian_{asyncio.get_event_loop().time()}.md"
        with open(obsidian_file, 'w') as f:
            f.write(f"---\nsource: {payload.data}\n---\n# Frozen Event\n{payload.data}")
        return obsidian_file

    # Phase 2: Knapping (Core -> Flake for Agent Tool)
    def knap_flake(file_path: str, query: str) -> str:
        with open(file_path, 'r') as f:
            content = f.read()
        # Simulate retrieval: sharp slice matching query
        flake = [line for line in content.split('\n') if query.lower() in line.lower()][0:5]
        return "\n".join(flake)  # Context window flake

    glass = await quench_lava()
    return knap_flake(glass, query)
```

## ⚔️ Synergies
*   **NATS JetStream**: Supplies the "Felsic Lava" of raw, high-bandwidth signals for quenching.
*   **Genesis Protocol**: Executes the rapid quenching transition from stream to immutable file.
*   **Knowledge Graph**: Serves as the dense "Obsidian Core" from which agents knap task-specific flakes.
*   **Agent Tools**: Leverage knapped flakes as sharp context windows for execution, avoiding devitrification rot.
*   **Obsidian Unified Master (refines)**: Builds on thermodynamic stigmergy with geologically accurate mineralogy metaphor.
*   **Hexagon Ontos/Topos**: Integrates with file addressing and linking for viral meme propagation ("Not Crystal, but Glass").