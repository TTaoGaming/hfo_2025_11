---
type: research
status: active
author: Swarmlord (Gen 53)
date: 2025-11-24
tags: [kcs, knowledge-management, industry-standard, sota]
---

# 🏆 Industry Exemplar: Knowledge-Centered Service (KCS) v6

> **Context**: You asked for "KCS v6". This stands for **Knowledge-Centered Service**, the SOTA methodology maintained by the *Consortium for Service Innovation*.
> **Adoption**: Used by HP, Dell, Salesforce, and major enterprise support organizations.

## 1. What is KCS v6?
KCS is not just a folder structure; it is a **Methodology** for how knowledge is created and maintained.
**Core Philosophy**: "Knowledge is the by-product of interaction."
Don't write docs *after* the work. Write docs *during* the work.

## 2. The KCS Double Loop
KCS v6 defines two reinforcing loops. This fits perfectly with our "Biological" HFO theme.

### 🔄 Loop A: The Solve Loop (The "Prey" Loop)
*Actionable, transactional, fast.*
1.  **Capture**: Capture the problem/intent in the user's context. (e.g., "Agent failed to connect to NATS").
2.  **Structure**: Format it for reuse (Issue, Environment, Resolution).
3.  **Reuse**: Search the brain. If it exists, link it. (Don't reinvent).
4.  **Improve**: If the existing doc is wrong, fix it *in the moment*.

### ♾️ Loop B: The Evolve Loop (The "Swarm" Loop)
*Strategic, reflective, slow.*
1.  **Content Health**: Reviewing drafts, archiving old stuff (The "Gardener" role).
2.  **Process Integration**: Integrating knowledge into the workflow (The "Swarmlord" role).
3.  **Performance Assessment**: Is the knowledge actually useful? (Stigmergy signals).
4.  **Leadership**: Defining the strategy.

---

## 3. KCS Article Structure vs. Diátaxis
KCS prescribes a specific format for "Knowledge Articles" (KAs).

| KCS Field | HFO Equivalent |
| :--- | :--- |
| **Issue / Problem** | "User Intent" or "Error Log" |
| **Environment** | "Context" (Gen 53, Linux, Python 3.10) |
| **Resolution / Fix** | "The Code" or "The Guide" |
| **Cause** | "Root Cause Analysis" (Explanation) |

**Synthesis**:
*   **Diátaxis** tells us *where* to put files (Tutorials vs Guides).
*   **KCS v6** tells us *how* to write them (Capture -> Structure -> Reuse).

---

## 4. Implementing KCS v6 in HFO (The "Knowledge State")
KCS v6 uses a specific **Content State** lifecycle, which aligns with our KVS v6 idea.

1.  **Work in Progress (WIP)**: "I'm working on this now." (Active Memory)
2.  **Draft**: "I think this is right, but unverified."
3.  **Approved**: "Verified by a Subject Matter Expert (SME)." (Long-Term Memory)
4.  **Published**: "Visible to the Customer." (Public Docs)
5.  **Archived**: "Old."

### The "Flag It or Fix It" Rule
In KCS, if an agent sees a wrong doc:
*   **Fix It**: If they are confident (License to Modify).
*   **Flag It**: If they are unsure (Comment/Tag for Review).

---

## 5. Recommendation: The "KCS-Diátaxis" Fusion

We can adopt KCS v6 **Processes** within the Diátaxis **Structure**.

### The Workflow
1.  **Agent encounters a problem.**
2.  **Search**: Check `brain/guides/` and `brain/reference/`.
3.  **Found?**:
    *   **Yes**: Use it. If it works, add a "Confidence Vote" (Stigmergy). If it fails, **Fix It**.
    *   **No**: **Capture** the solution in `brain/active_memory/` (WIP).
4.  **Evolve**:
    *   Once the WIP solution is verified, **Structure** it into a Diátaxis Guide.
    *   Move to `brain/long_term_memory/guides/`.

### Tradeoffs
*   **Pros**: Self-healing knowledge base. Reduces "Documentation Debt".
*   **Cons**: Requires discipline. Agents must search *before* creating.

**Verdict**: KCS v6 is the **Operational System** for our Brain. Diátaxis is the **File System**. They work together.
