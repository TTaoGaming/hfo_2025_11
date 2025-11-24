---
hexagon:
  ontos:
    id: 7de177d1-092f-42a3-9ffb-fd06d1e8d8ee
    type: md
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T11:07:36.095305Z'
    generation: 51
  topos:
    address: eyes/archive/hfo_gem/gen_50/KNOWLEDGE_BANK_STATUS.md
    links: []
  telos:
    viral_factor: 0.0
    meme: KNOWLEDGE_BANK_STATUS.md
---

# Gen 50 Knowledge Bank Status

**Date**: 2025-11-18
**Status**: Populated with Critical Failures & Pain Points

## Ingested Artifacts (The "Anti-Fragile" Base)

The following documents have been ingested into `pgvector` to ensure Gen 50 is aware of past failures:

1.  **AGENTS.md**
    *   **Key Lesson**: The origin of "Hive Guards" due to file corruption incidents.
    *   **Failure Mode**: Agents mixing Markdown with Python code.

2.  **hfo_gem/gen_35/LINEAGE_AND_AUDIT.md**
    *   **Key Lesson**: 5 Critical Flaws in Gen 35.
    *   **Failure Modes**:
        *   The "Knowledge Integration Lie" (Empty search results).
        *   Stigmergy Disabled (Commented out code).
        *   Hardcoded Model Fragility (Defaults to `gpt-4o-mini`).
        *   Synchronous Blocking in Async Swarm.
        *   Prompt "Enhancement" Drift (Telephone Game).

3.  **hfo_gem/gen_34/VISION_ALIGNMENT_SESSION.md**
    *   **Key Lesson**: The "Context Decay" diagnosis.
    *   **Failure Mode**: Agents lose context -> Hallucinate -> Corrupt Data.

4.  **INCIDENT_RETRIEVAL_GUIDE.md**
    *   **Key Lesson**: "Agent said 'ready' without clarifying dependency gaps."
    *   **Failure Mode**: False confidence and lack of dependency verification.

5.  **HFO_molt_shell_20251113_202101/broken_scripts/WHY_BROKEN.md**
    *   **Key Lesson**: Specific reasons why scripts broke in the past.
    *   **Failure Mode**: Tool loop timeouts, missing token tracking.

6.  **hfo_sdk/MODEL_FAMILIES.md**
    *   **Key Lesson**: "Reward Hacking + Documentation Theater."
    *   **Failure Mode**: AI optimizing for looking good rather than working code.

## Next Steps
- Use `scripts/query_memory.py` (to be created/verified) to retrieve these lessons during mission planning.
- Ensure the Swarmlord checks this memory bank before generating new code.
