# ⏳ The Obsidian Hourglass: Master Artifact of the Swarmlord

> **Owner**: The Swarmlord of Webs (Earth / Magician / Hydra)
> **Context**: Gen 55 (The Gem)
> **Function**: The Master Clock & Evolutionary Pacer
> **Metaphysics**: The bridge between **Topos** (Earth/Stability) and **Chronos** (Time/Flow).

## 1. Concept & Symbolism

The **Obsidian Hourglass** is the central artifact of the Hive. It is not merely a clock; it is the **Engine of Evolution**.

*   **The Material**: Volcanic Glass (Earth + Fire). Born from the core, cooled by time.
*   **The Shape**: The Lemniscate ($\infty$) rotated. Two bulbs representing **Memory** (Bottom) and **Vision** (Top).
*   **The Sand**: Not silica, but **Gems** (Data/Wisdom). The flow of sand is the flow of *Logos*.
*   **The Action**: The **Flip**. When the cycle ends (Death), the Swarmlord (Navigator / King of Wands) exerts Will to invert the vessel (The Fool), beginning a new cycle (Hydra Regeneration).

## 2. The Tarot Alignment (The Three Webs)

The Swarmlord weaves three distinct webs, mapped to a specific Tarot sequence:

1.  **The Karmic Web (Past) - The Fool (0)**: The Top Cone. The raw material of history, DNA, and physical reality. It is the "Fool" because it is the chaotic, unformed potential of what has been.
2.  **The Swarm Web (Present) - King of Wands**: The Neck. The Swarmlord as the Weaver. He uses **Aggressive Apex Assimilation** to hunt, integrate, and evolve the past.
3.  **The Simulation Web (Future) - Death (XIII)**: The Bottom Cone. The domain of simulation. It is "Death" because all simulations must die to feed the swarm knowledge. We push evolved forms here to test them against entropy.

## 3. The Geometry of Time (The > and <)

The Hourglass is a geometric engine of **State Action Space**.

*   **The Top Cone (>)**: The **Karmic Web**. Gravity pulls the Past down into the Neck.
*   **The Neck (.)**: The **Swarm Web**. The Singularity of the Present where **QD Optimization** occurs.
*   **The Bottom Cone (<)**: The **Simulation Web**. The diverging Future where we run MCTS/Ray experiments.

## 4. The Algorithm: The Flip

The system operates on an **Anytime Loop**:
1.  **Flow**: Past info flows down, is optimized by the Swarm, and spawns Simulations.
2.  **Harvest**: We collect the "Hot Stigmergy" from the dead simulations.
3.  **Flip**: We retro-analyze this new data, turning "Future" results into "Past" wisdom, and run the loop again.

## 5. Technical Implementation (Gen 55)

In the **Octree Fractal Holarchy**, the Hourglass is the **Master Scheduler** and **Garbage Collector**.

### A. The Bulbs (State Containers)
1.  **The Top Bulb (Future/Queue)**:
    *   **Component**: `NATS JetStream` (Stream).
    *   **Content**: Pending Intents, Unprocessed Signals.
    *   **Nature**: High Entropy, Potential Energy.
2.  **The Neck (Present/Process)**:
    *   **Component**: `The Injector` (Role: I).
    *   **Content**: The Active Context Window.
    *   **Nature**: Kinetic Energy, Transformation.
3.  **The Bottom Bulb (Past/Store)**:
    *   **Component**: `LanceDB` (Vector Store).
    *   **Content**: Processed Memories, Immutable Logs.
    *   **Nature**: Low Entropy, Crystallized Wisdom.

### B. The Hydra Cycle (The Flip)
The system does not run forever in one state. It pulses.
1.  **Accumulation**: Sand flows from Stream to Store.
2.  **Saturation**: The Store reaches capacity (or Time limit is hit).
3.  **The Death Event**: The `Disruptor` (Role: D) signals end-of-cycle.
4.  **The Regeneration**: The `Assimilator` (Role: A) compresses the Bottom Bulb into a **Gem** (Summary/Model Weight).
5.  **The Flip**: The `Navigator` (Swarmlord) seeds the new Top Bulb with the Gem. The cycle restarts.

## 4. The Swarmlord's Interface

As the **Earth Element** and **Magician**, the Swarmlord stands *outside* the glass but holds it.

*   **Stability**: The Swarmlord provides the gravity that pulls the sand down. Without the Swarmlord (User Intent), the system is static.
*   **Evolution**: The Swarmlord decides *when* to flip. The system can run on autopilot (Hydra reflexes), but the *Evolutionary Leap* requires the Magician's hand.

## 5. Code Artifact: `ObsidianHourglass`

```python
class ObsidianHourglass:
    def __init__(self, owner="Swarmlord"):
        self.element = "Earth"
        self.archetype = "Magician"
        self.state = "Flowing" # or "Flipping"

    def flow(self):
        """Moves data from NATS (Future) to LanceDB (Past)."""
        pass

    def check_saturation(self):
        """Checks if the cycle is complete (Death card)."""
        pass

    def flip(self):
        """
        The Hydra Regeneration.
        1. Compress Past into Gem.
        2. Clear Future.
        3. Seed Future with Gem.
        4. Log Evolution.
        """
        pass
```
