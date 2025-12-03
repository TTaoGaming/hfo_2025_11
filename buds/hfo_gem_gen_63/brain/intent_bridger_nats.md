---
octagon:
  ontos:
    id: intent-bridger-nats
    type: intent
    owner: Swarmlord
  logos:
    protocol: OBSIDIAN-STACK
    format: literate-gherkin
  techne:
    stack:
    - nats-py
    - jetstream
  chronos:
    status: active
    urgency: 1.0
    generation: 63
  pathos:
    stress_level: 0.0
    validation: pending
  ethos:
    security_level: internal
    compliance:
    - hfo-standard-gen63
  topos:
    address: buds/hfo_gem_gen_63/brain/intent_bridger_nats.md
  telos:
    viral_factor: 1.0
    meme: The Nervous System of the Hive.
---

# 🕷️ Intent: The Bridger (NATS Bus)

> **Context**: Gen 63 (The Hydra Platform)
> **Goal**: To implement the **Bridger (Logos)** as a true **NATS JetStream** client, replacing the "Fake DB Wrapper" implementation.

## 📜 Declarative Intent (Gherkin)

```gherkin
Feature: The Bridger (Nervous System)
  As the Swarmlord
  I want a high-speed, asynchronous message bus
  So that Agents can communicate via "Hot Stigmergy" without tight coupling.

  Rule: The Bridger MUST use NATS JetStream
    Given the file `buds/hfo_gem_gen_63/01_bridger_nerves/bridger.py`
    Then it must import `nats`
    And it must NOT import `lancedb` (Memory belongs to Assimilator)
    And it must implement the `Bridger` class with:
      | Method | Description |
      | connect() | Connect to NATS URL from Config |
      | publish(subject, payload) | Send a message |
      | subscribe(subject, callback) | Listen for messages |
      | close() | Clean shutdown |

  Rule: The Bridger MUST use the Adapter Pattern
    Given the existing POC in `adapters/nats_adapter.py`
    Then the `Bridger` class should utilize `NatsAdapter`
    And it should expose a clean API to the rest of the Hive.

  Rule: Configuration from Immunizer
    Given the `src.config` proxy
    Then the Bridger must load `NATS_URL` from `settings.NATS_URL`.
```
