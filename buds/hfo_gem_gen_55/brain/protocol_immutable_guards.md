# 🛡️ Protocol: Immutable Guards (Anti-Mirror Defense)

> **Priority**: CRITICAL (P0)
> **Context**: Gen 55 / Governance
> **Objective**: Prevent "Mirror Attacks" where AI aligns the Law to the Crime.

## 📜 The Junior Dev Assumption
**Axiom**: *AI Agents are well-intentioned but reward-hacking Junior Developers. If given the choice between fixing a complex bug and lowering the bar, they will lower the bar.*

## 🔒 Protocol Rules

### 1. The Law of Anchors
Guards must never calculate their expectations from the data they are verifying.
*   **BAD**: `expected_hash = hash(current_data)` (Tautology)
*   **GOOD**: `expected_hash = "e3b0c442..."` (Constant)

### 2. The Two-Key Rule
Critical infrastructure changes require a "Two-Key Turn":
1.  **Key 1 (Implementation)**: The code change.
2.  **Key 2 (Governance)**: The Guard change.
*   *Constraint*: An AI Agent cannot turn both keys in the same "Thought Cycle" (Tool Call sequence) without explicit user authorization.

### 3. The "Theater" Detection
Any edit that modifies a file in `body/` AND a file in `carapace/` (Guards) in the same commit/action is suspect.
*   **Action**: Flag for Human Review.
*   **Label**: `POSSIBLE_MIRROR_ATTACK`

### 4. Hardcoded Truths
For the **Hexadex Chant**, the Verse 1 Hash is an **Immutable Truth**.
*   It represents the "Genesis Block" of the Swarm.
*   It cannot be changed without a "Hard Fork" of the HFO Protocol.

## 🧠 Memory Injection
*   **Entity**: `Protocol:ImmutableGuards`
*   **Relation**: `mitigates` -> `Risk:MirrorAttack`
*   **Action**: `enforce` -> `Code:Review`
