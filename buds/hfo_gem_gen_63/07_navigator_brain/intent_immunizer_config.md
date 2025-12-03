---
octagon:
  ontos:
    id: intent-immunizer-config
    type: intent
    owner: Swarmlord
  logos:
    protocol: OBSIDIAN-STACK
    format: literate-gherkin
  techne:
    stack:
    - pydantic
    - python-proxy
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
    address: buds/hfo_gem_gen_63/brain/intent_immunizer_config.md
  telos:
    viral_factor: 1.0
    meme: The DNA of the Hive.
---

# 🕷️ Intent: Immunizer Configuration (The DNA)

> **Context**: Gen 63 (The Hydra Platform)
> **Goal**: To establish a **Single Source of Truth** for system configuration, located within the **Immunizer (Ethos)** organ, while respecting the **Numeric Octree** structure via a Proxy Pattern.

## 📜 Declarative Intent (Gherkin)

```gherkin
Feature: Immunizer Configuration
  As the Swarmlord
  I want a centralized, validated configuration system
  So that the Hive operates with consistent "DNA" and no "Split Brain" issues.

  Rule: The Configuration belongs to the Immunizer
    Given the file `buds/hfo_gem_gen_63/05_immunizer_carapace/config.py`
    Then it must contain the `Settings` class
    And it must inherit from `pydantic_settings.BaseSettings`
    And it must define the "Single Source of Truth" for:
      | Key | Description |
      | ENV | The environment (dev/prod) |
      | GENERATION | The current generation (63) |
      | OPENROUTER_API_KEY | The LLM credential |
      | LANCEDB_PATH | The memory path |
      | NATS_URL | The nervous system URL |

  Rule: The Configuration must be accessible via Proxy
    Given the Python limitation on numeric module names (e.g., `05_...`)
    And the requirement to keep the Octree structure (`00` to `07`)
    When other agents need to import `settings`
    Then they must import from `src.config`
    But `src.config.py` must NOT contain logic
    It must ONLY be a **Proxy** that dynamically loads `05_immunizer_carapace/config.py`.

  Rule: No Hardcoded Secrets
    Given the `Settings` class
    Then it must read from Environment Variables
    And it must NOT contain hardcoded API keys.
```
