# 🐉 The Hydra Protocol: Architecture & Implementation

> **Strategy**: Regenerative Bulkheads ("Let it Crash")
> **Status**: Selected for Gen 50 Implementation
> **Gherkin**: `brain/antifragile_strategy.feature`

## 🧠 Core Concept
The **Hydra Protocol** treats every agent as a disposable, regenerative cell. We do not fix broken agents; we kill them and replace them. This ensures that compromise is contained and transient.

## 🏗️ Implementation with R.A.P.T.O.R.

### 1. The Cell (Ray Actor)
*   **Technology**: `ray.remote` Actors.
*   **Isolation**: Each agent runs in its own process space.
*   **State**: Ephemeral. Persistent state lives in Postgres/NATS, not the Actor.

### 2. The Suicide Switch (Carapace Interceptor)
*   **Mechanism**: A Python Decorator or Mixin (`@hydra_guarded`).
*   **Trigger**:
    *   `StaticGuard` failure (Runtime code injection).
    *   `NeuralGuard` failure (Hallucination/Refusal).
    *   `Regulator` failure (Resource exhaustion).
*   **Action**:
    1.  Emit `hfo.signal.dying_gasp` to NATS.
    2.  Call `sys.exit(1)` or `ray.actor.exit_actor()`.

### 3. The Regenerator (Injector Role)
*   **Component**: A specialized "Supervisor" agent or the `hydra_swarm.py` main loop.
*   **Loop**:
    1.  **Listen**: Subscribe to `hfo.signal.dying_gasp`.
    2.  **Analyze**: Why did it die? (Attack vs. Bug).
    3.  **Spawn**: Call `Agent.remote()` to create a replacement.
    4.  **Patch**: If it was an attack, inject updated "Immunity DNA" (Config) into the new agent.

## 🔄 The Lifecycle
1.  **Spawn**: Agent born with `mission_id` and `immunity_config`.
2.  **Serve**: Agent processes tasks.
3.  **Breach**: Agent detects anomaly (e.g., unauthorized file access).
4.  **Die**: Agent kills itself.
5.  **Rebirth**: Supervisor spawns a fresh copy.

## 🛡️ Why this is Antifragile
*   **Attack Surface**: Constantly resetting. An attacker loses their foothold every time the agent dies.
*   **Evolution**: The "Rebirth" phase allows us to inject *better* defenses derived from the `ImmunityForge`.
