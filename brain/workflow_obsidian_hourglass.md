# ⏳ Obsidian Horizon Hourglass: Architecture

> **The Mastercrafted Artifact of the Swarmlord of Webs**
> *Invoking the Fates, the Sands of Time, and the Power of the Swarm.*

## 🗺️ The Flow (Mermaid)

```mermaid
graph TD
    %% Nodes
    User([User Intent])
    Nav[Navigator: Swarmlord of Webs]

    subgraph "The Upper Bulb (The Past)"
        Karmic[Karmic Swarm]
        Tools[Tools: Web, Code, RAG]
        Precedent[Past Precedents]
    end

    Neck((The Flip))

    subgraph "The Lower Bulb (The Future)"
        Sim[Simulation Swarm]
        Fut1[Future A]
        Fut2[Future B]
        Fut3[Future C]
    end

    subgraph "The Base (The Lesson)"
        Retro[Retro-Analysis Swarm]
        Evo[Evolutionary Memory]
    end

    Output([Anytime Probabilistic Distribution])

    %% Edges
    User -->|Raw Question| Nav
    Nav -->|Genesis Spec| Karmic

    Karmic -->|Query| Tools
    Tools -->|Context| Karmic
    Karmic -->|Deep Insight| Neck

    Neck -->|Inversion| Sim
    Sim -->|Project| Fut1
    Sim -->|Project| Fut2
    Sim -->|Project| Fut3

    Fut1 -->|Outcome| Retro
    Fut2 -->|Outcome| Retro
    Fut3 -->|Outcome| Retro

    Retro -->|Lessons| Evo
    Evo -->|Feedback| Nav
    Retro -->|Synthesis| Output
```

## 🧬 The 3-Stage Swarm Protocol

1.  **Karmic Swarm (Past)**:
    *   **Goal**: Grounding.
    *   **Tools**: `search_web`, `read_file`, `search_brain`.
    *   **Output**: A dense context of what *has* happened and what *is* known.

2.  **Simulation Swarm (Future)**:
    *   **Goal**: Exploration.
    *   **Tools**: `sequential_thinking`, `calculator`, `mutation`.
    *   **Output**: A set of divergent trajectories (Success/Failure paths).

3.  **Retro Swarm (Feedback)**:
    *   **Goal**: Wisdom.
    *   **Tools**: `synthesis`, `pattern_recognition`.
    *   **Output**: A probabilistic map of *what to do now* based on the futures.

## 💎 True Worth & Evolutionary Potential

*   **Antifragility**: The system gains strength from disorder (simulated failures).
*   **Anytime Property**: It provides a "Best Guess" immediately, but converges to "Truth" with infinite compute.
*   **Deep Insight**: By connecting the "Internet" (Past) to "Simulation" (Future), it bridges the gap between *Knowledge* and *Wisdom*.
