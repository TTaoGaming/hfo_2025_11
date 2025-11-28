---
type: research
status: active
author: Swarmlord (Gen 51)
date: 2025-11-24
tags: [organization, methodology, para, diataxis, 5w1h]
---

# ⚔️ Methodology Showdown: Diátaxis vs. PARA

> **Executive Summary**:
> *   **Diátaxis** is the industry standard for **Technical Documentation** (Software Engineering). It focuses on the *reader's needs*.
> *   **PARA** is the industry standard for **Knowledge Management** (Productivity/Second Brain). It focuses on the *writer's actionability*.

---

## 1. Diátaxis Framework (The Engineer's Choice)

**Origin**: Created by Daniele Procida (Canonical/Ubuntu). Adopted by Google, Microsoft, Django, Divio.

### 5W1H Analysis

| Dimension | Description |
| :--- | :--- |
| **WHO** | Technical Writers, Software Engineers, Open Source Maintainers. |
| **WHAT** | A systematic framework organizing documentation into 4 quadrants based on **User Intent**. |
| **WHERE** | `docs/`, Developer Portals, Wikis. |
| **WHEN** | When you are building a product, library, or system for *others* (or your future self) to use. |
| **WHY** | To reduce cognitive load. Users usually have one of 4 distinct goals: doing, learning, understanding, or looking up. |
| **HOW** | Organize files into 4 folders: <br>1. **Tutorials** (Learning-oriented) <br>2. **How-to Guides** (Problem-oriented) <br>3. **Reference** (Information-oriented) <br>4. **Explanation** (Understanding-oriented) |

### The 4 Quadrants
1.  **Tutorials**: "Take me by the hand." (e.g., `genesis_protocol.md` - A lesson)
2.  **How-To**: "I have a problem, solve it." (e.g., `how_to_add_organ.md` - A recipe)
3.  **Reference**: "What is this setting?" (e.g., `registry.yaml`, API Specs - A dictionary)
4.  **Explanation**: "Why did we build it this way?" (e.g., `design_octree.md` - A discussion)

### Tradeoffs
*   **✅ Pros**: Extremely scalable. Clear place for everything. Users find answers fast.
*   **❌ Cons**: Fragments a single feature. "Stigmergy" logic is split across 4 folders (The tutorial, the config spec, the design doc, the setup guide).

---

## 2. PARA Method (The Agent's Choice)

**Origin**: Created by Tiago Forte (Building a Second Brain). Adopted by Notion users, Obsidian users, Knowledge Workers.

### 5W1H Analysis

| Dimension | Description |
| :--- | :--- |
| **WHO** | Project Managers, Researchers, "Agents" (Autonomous entities), Knowledge Workers. |
| **WHAT** | A dynamic system organizing information by **Actionability** (Time horizon & Goal). |
| **WHERE** | Personal Knowledge Bases (Obsidian vaults), Project Drives, Agent Memory. |
| **WHEN** | When you are *executing* work and need to separate "Active" tasks from "Static" knowledge. |
| **WHY** | To focus attention. You only want to see what is relevant *right now*. |
| **HOW** | Organize files into 4 folders: <br>1. **Projects** (Active, Short-term, Deadline) <br>2. **Areas** (Ongoing, Long-term, Responsibility) <br>3. **Resources** (Topics, Interests, Reference) <br>4. **Archives** (Inactive, Completed) |

### The 4 Categories
1.  **Projects**: "Finish the Octree Refactor." (Has a deadline/goal).
2.  **Areas**: "Maintain Architecture." (Never ends, requires standard maintenance).
3.  **Resources**: "Stigmergy Research." (Useful info, but no immediate deadline).
4.  **Archives**: "Gen 50 Brain." (Old stuff).

### Tradeoffs
*   **✅ Pros**: High velocity. Keeps the workspace clean. Focuses on *getting things done*.
*   **❌ Cons**: Low stability. Files move constantly (Resource -> Project -> Archive). Hard for a *team* to find things if they don't know the current project status.

---

## ⚖️ The Verdict: Which one for HFO?

The HFO `brain/` folder serves two masters:
1.  **The Swarm (Agents)**: They need to *execute* (PARA).
2.  **The Overmind (You)**: You need to *understand/design* (Diátaxis).

### Comparison Matrix

| Feature | Diátaxis | PARA |
| :--- | :--- | :--- |
| **Primary Goal** | Clarity & Usability | Actionability & Focus |
| **Structure** | Static (Functional) | Dynamic (Temporal) |
| **Best For** | Documentation / Specs | Task Management / Research |
| **File Movement** | Rare (Files stay put) | Frequent (Files flow down) |
| **HFO Fit** | Good for `docs/` | Good for `brain/` (Memory) |

### 🚀 Recommendation: The "Static PARA" (Hybrid)

Since `brain/` is a mix of **Design** (Static) and **Plans** (Active), use a hybrid:

1.  **Use Diátaxis for `docs/`**: If you publish a manual for HFO, use Diátaxis.
2.  **Use Modified PARA for `brain/`**: Since this is the *working memory* of the system.

**Why PARA wins for `brain/`:**
Your `brain/` folder is full of *Designs* (`design_*.md`), *Intents* (`*.feature`), and *Research* (`research_*.md`).
*   **Projects**: `brain/missions/` (Active Swarm Missions)
*   **Areas**: `brain/domains/` (Architecture, Stigmergy, Memory - Ongoing responsibilities)
*   **Resources**: `brain/patterns/` & `brain/standards/` (Reference material)
*   **Archives**: `brain/archive/`

**However**, pure PARA is hard for codebases. **Diátaxis is safer for code repositories.**

**Final Decision**:
If you want **Industry Best for Engineering**, choose **Diátaxis**.
If you want **Industry Best for Agentic Workflow**, choose **PARA**.

Given HFO is an **Engineering Project**, I recommend **Diátaxis** (or the "Domain" variation of it), because your agents need a *stable reference* to read from. If files move around (PARA), agents might hallucinate paths.
