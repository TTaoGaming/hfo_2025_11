---
holon:
  id: design-brain-reorg-v2
  type: design
  status: proposed
  author: Swarmlord
  date: 2025-12-01
  context: Cleanroom Consolidation
---

# 🧠 Design V2: The Brain Architecture Comparison

> **Goal**: Select the optimal organization for `buds/hfo_gem_gen_63/brain/`.
> **Constraints**: Must be SOTA, Composable, and support the Swarm.

## 📊 The Comparison Matrix

| Feature | **1. Fractal Octree** (Obsidian) | **2. P.A.R.A.** (Fast Track) | **3. Semantic Lake** (AI Native) | **4. Diataxis** (Doc Standard) |
| :--- | :--- | :--- | :--- | :--- |
| **Philosophy** | "As Above, So Below" | "Actionability" | "Graph Theory" | "User Needs" |
| **Structure** | 8 Folders (Pillars) | 4 Folders | Flat + Metadata | 4 Folders |
| **Human Readability** | ⭐⭐⭐ (Thematic) | ⭐⭐⭐⭐⭐ (Intuitive) | ⭐ (Chaos) | ⭐⭐⭐⭐ (Educational) |
| **AI Readability** | ⭐⭐⭐⭐ (Structured) | ⭐⭐⭐ (Generic) | ⭐⭐⭐⭐⭐ (Native) | ⭐⭐⭐ (Contextual) |
| **Impl. Speed** | Medium | **Fastest** | Slow (Requires Tooling) | Medium |
| **Maintenance** | High (Strict Slots) | Low (Flexible) | Automated | Medium |

---

## 🏛️ Option 1: The Fractal Octree (The Obsidian Standard)
> **Best For**: Alignment with HFO Architecture & "0 Invention" via SOTA mapping.

We map the 8 Metaphysical Pillars to 8 Industry Standard Artifact types.

*   **Structure**:
    1.  `1_telos_rfcs/` (Intents / Manifestos)
    2.  `2_ontos_research/` (Context / Spikes)
    3.  `3_logos_specs/` (Gherkin / Schemas)
    4.  `4_techne_designs/` (Blueprints / Plans)
    5.  `5_chronos_roadmap/` (Sprints / Logs)
    6.  `6_pathos_incidents/` (Post-Mortems / Bugs)
    7.  `7_ethos_adrs/` (Decisions / Policies)
    8.  `8_topos_library/` (Reference / Archive)

*   **Pros**: Perfect architectural symmetry. Empty folders reveal "blind spots" (e.g., no Incidents = poor observation).
*   **Cons**: Can feel "heavy" for small iterations.

---

## ⚡ Option 2: P.A.R.A. (The Fast Track)
> **Best For**: Speed of Implementation & Human Organization.

Tiago Forte's "Building a Second Brain" standard. Organized by *Actionability*.

*   **Structure**:
    1.  `1_projects/` (Active Goals with Deadlines: `Gen 63 Consolidation`)
    2.  `2_areas/` (Ongoing Responsibilities: `Security`, `Architecture`)
    3.  `3_resources/` (Topics of Interest: `SOTA Research`, `Chat Logs`)
    4.  `4_archives/` (Inactive Items: `Gen 61 Designs`)

*   **Pros**: Extremely fast to set up. Very clear where things go.
*   **Cons**: "Resources" becomes a junk drawer. Doesn't distinguish between a "Spec" (Truth) and a "Note" (Noise).

---

## 🤖 Option 3: The Semantic Lake (AI Swarm Friendly)
> **Best For**: Automated Agents & Vector Search.

Agents don't care about folders; they care about **Tags** and **Links**. We flatten the hierarchy and rely on strict Frontmatter (YAML).

*   **Structure**:
    *   `pool/` (All files live here, flat)
    *   `schemas/` (Validation logic)

*   **The Glue (YAML Headers)**:
    ```yaml
    type: [intent | spec | design | adr]
    status: [draft | active | deprecated]
    tags: [gen63, memory, nats]
    relates_to: [id-of-other-doc]
    ```

*   **Pros**: Zero friction for writing. Perfect for Vector DB ingestion.
*   **Cons**: Nightmare for humans to browse via file explorer. Requires a "Librarian Agent" to maintain order.

---

## 📚 Option 4: Diataxis (The Documentation Standard)
> **Best For**: Knowledge Transfer & Onboarding.

Daniele Procida's framework. Organized by the *User's Mental State*.

*   **Structure**:
    1.  `tutorials/` (Learning-oriented: "Lesson 1")
    2.  `guides/` (Task-oriented: "How to Deploy")
    3.  `reference/` (Information-oriented: "API Spec")
    4.  `explanation/` (Understanding-oriented: "Why NATS?")

*   **Pros**: Excellent for creating a "Manual".
*   **Cons**: Bad for "Work in Progress". Where does a draft design go? (Usually "Explanation", but it's messy).

---

## 🏆 Recommendation

**Hybrid Approach: The "Octree-PARA"**

We use **Option 1 (Octree)** as the *Folder Structure* because it enforces the System Architecture, but we simplify the *Content* using **Option 2 (PARA)** principles inside.

**Why?**
1.  **AI Friendly**: The numbered folders (`1_...`, `2_...`) act as a priority queue for the Context Window.
2.  **Fast**: We just move files. No complex tagging required yet.
3.  **SOTA**: We use standard terms (RFC, ADR, Spec).

**Proposed Action**:
Adopt **Option 1**. It is the only one that respects the "Fractal" nature of the Hive Fleet while using standard industry terminology.
