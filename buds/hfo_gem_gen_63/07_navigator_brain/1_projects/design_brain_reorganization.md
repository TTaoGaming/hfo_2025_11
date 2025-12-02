---
holon:
  id: design-brain-reorg-gen63
  type: design
  status: proposed
  author: Swarmlord
  date: 2025-12-01
  context: Cleanroom Consolidation
---

# 🧠 Design: The Crystal Brain (Knowledge Organization)

> **Status**: PROPOSED
> **Goal**: Reorganize `buds/hfo_gem_gen_63/brain` from a flat "jumble" into a SOTA Knowledge Architecture.
> **Philosophy**: "Separation of Concerns" applied to Knowledge.

## 1. The Problem
The current `brain/` directory is a flat list mixing different *types* of cognition:
*   **Raw Input**: AI Chat logs (`ai-chat-*.md`).
*   **Intent**: High-level goals (`intent_*.md`, `manifesto.md`).
*   **Specification**: Testable requirements (`*.feature`).
*   **Exploration**: Design drafts (`design_*.md`).
*   **Decision**: Finalized choices (mixed into designs).

This makes it hard for Agents to know what is **Truth** (Immutable) vs. **Noise** (Ephemeral).

## 2. SOTA Standards Evaluation (The "Big 4")

To solve the "jumble," we evaluated the 4 best industry standards for knowledge organization.

### Option A: Diataxis (The Content Standard)
*   **Philosophy**: Structure by *User Need*.
*   **Quadrants**:
    1.  **Tutorials**: "Teach me." (Learning-oriented)
    2.  **How-To Guides**: "Help me do it." (Problem-oriented)
    3.  **Reference**: "What is it?" (Information-oriented)
    4.  **Explanation**: "Why is it?" (Understanding-oriented)
*   **Best For**: The `library/` or `docs/` folder. Ensuring Agents know the difference between a *Lesson* and a *Spec*.

### Option B: ARC42 (The Architecture Standard)
*   **Philosophy**: Structure by *System View*.
*   **Key Sections**:
    1.  **Context**: System Scope & Context.
    2.  **Building Blocks**: Static Decomposition (The Code).
    3.  **Runtime View**: Dynamic Behavior (The Agents).
    4.  **Decisions**: Architecture decisions.
*   **Best For**: The `designs/` folder. Ensuring we don't just write "notes" but actual *Architecture*.

### Option C: MADR (The Decision Standard)
*   **Philosophy**: Decisions are *Immutable Events*.
*   **Format**: Markdown Architecture Decision Records.
*   **Structure**: Title, Status, Context, Decision, Consequences (Positive/Negative).
*   **Best For**: The `decisions/` folder. Replacing "chat logs" with "signed verdicts."

### Option D: P.A.R.A. (The Lifecycle Standard)
*   **Philosophy**: Structure by *Actionability*.
*   **Categories**:
    1.  **Projects**: Active goals with a deadline (e.g., `Gen 63`).
    2.  **Areas**: Ongoing responsibilities (e.g., `Security`, `DevOps`).
    3.  **Resources**: Topics of interest / Reference (e.g., `SOTA Research`).
    4.  **Archives**: Inactive items (e.g., `Gen 61`).
*   **Best For**: The top-level directory structure.

---

## 3. Design Iteration: The Fractal Options

We are a **Fractal Octree Architecture**. The organization of the Brain should reflect the organization of the Body.
We have mapped **SOTA Industry Standards** (RFCs, ADRs, Specs) to the **8 Metaphysical Pillars**.

### Option A: The Fractal Octree (8-Fold Path)
> **Philosophy**: "As above, so below." The Brain structure mirrors the Agent structure.
> **Pros**: Perfect alignment with HFO architecture. Infinite composability.
> **Cons**: 8 folders can be sparse if not fully populated.

| Pillar | Metaphysics | SOTA Standard | Content Type |
| :--- | :--- | :--- | :--- |
| **1. Telos** | Purpose | **RFCs** (Request for Comments) | Intents, Manifestos, Strategic Goals. |
| **2. Ontos** | Reality | **Research** (Spikes) | Context, Raw Chat Logs, Market Analysis. |
| **3. Logos** | Logic | **Specs** (Specifications) | Gherkin Features (`.feature`), JSON Schemas, APIs. |
| **4. Techne** | Craft | **Designs** (Blueprints) | Engineering Design Docs, Implementation Plans. |
| **5. Chronos** | Time | **Roadmap** (Logs) | Sprint Plans, Changelogs, Daily Journals. |
| **6. Pathos** | Friction | **Incidents** (Post-Mortems) | Failure Logs, Bug Reports, "The Pain". |
| **7. Ethos** | Ethics | **ADRs** (Decisions) | Architecture Decision Records, Governance, Policies. |
| **8. Topos** | Place | **Library** (Knowledge Base) | Reference Docs, Archives, "The Cold Storage". |

**Proposed Directory Structure:**
```text
brain/
├── 1_telos_rfcs/       # The Why (Intents)
├── 2_ontos_research/   # The Input (Context)
├── 3_logos_specs/      # The Truth (Tests)
├── 4_techne_designs/   # The Plan (Blueprints)
├── 5_chronos_roadmap/  # The Pulse (Logs)
├── 6_pathos_incidents/ # The Friction (Failures)
├── 7_ethos_adrs/       # The Law (Decisions)
└── 8_topos_library/    # The Memory (Archive)
```

### Option B: The Elemental Quadrants (4-Fold Path)
> **Philosophy**: **Diataxis** (User Needs). Grouping the 8 pillars into 4 Elements.
> **Pros**: Simpler, standard documentation structure.
> **Cons**: Loses the granular "Octree" resolution.

1.  **Fire (Will)**: Telos + Techne + Chronos -> **Projects** (Active Work).
2.  **Air (Intellect)**: Logos + Ethos -> **Standards** (Specs & ADRs).
3.  **Water (Flow)**: Ontos + Pathos -> **Context** (Research & Logs).
4.  **Earth (Stability)**: Topos -> **Library** (Archive).

### Option C: The Binary (2-Fold Path)
> **Philosophy**: **Hot vs. Cold** (Stigmergy).
> **Pros**: Extremely simple.
> **Cons**: "Hot" becomes a junk drawer very quickly.

1.  **Hot (Active)**: Intents, Designs, Specs, Logs.
2.  **Cold (Passive)**: ADRs, Library, Research, Archives.

## 4. Recommendation

**We recommend Option A (The Fractal Octree).**
*   It enforces the **0 Invention** rule by using standard terms (RFC, ADR, Spec).
*   It maintains the **Obsidian Theme** (8 Pillars).
*   It is **Composable**: If a folder is empty, it remains as a placeholder for that metaphysical aspect, ensuring we don't neglect it (e.g., if `6_pathos_incidents` is empty, are we not testing enough?).

## 5. Migration Plan

### Step 1: Create Directories
Create the 5 folders: `1_intents`, `2_specs`, `3_designs`, `4_decisions`, `5_context`.

### Step 2: Sort & Rename (The Great Filter)
Move existing files into their correct homes.

| File | Destination | Notes |
| :--- | :--- | :--- |
| `manifesto_gen_63.md` | `1_intents/` | The Root Intent. |
| `intent_*.md` | `1_intents/` | Strategic directives. |
| `*.feature` | `2_specs/features/` | Executable tests. |
| `design_*.md` | `3_designs/active/` | Working documents. |
| `ai-chat-*.md` | `5_context/chats/` | Raw context. |
| `tech_stack_gen63.md` | `4_decisions/ADR-001...` | **Convert to ADR**. |

### Step 3: Refactor Links
Update `AGENTS.md` and other pointers to reference the new paths.

## 5. Validation
*   **Agent Check**: Can the `ResearchAgent` distinguish between a *Design* (Proposal) and a *Spec* (Requirement)?
*   **Human Check**: Is the folder structure intuitive?

## 6. Decision Required
Do we proceed with this structure?
