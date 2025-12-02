---
holon:
  id: design-brain-reorg-v3
  type: design
  status: proposed
  author: Swarmlord
  date: 2025-12-01
  context: Cleanroom Consolidation
---

# 🧠 Design V3: The "Obsidian Flow" (PARA + Lake + Diataxis)

> **Goal**: A hybrid architecture optimizing for Speed (PARA), AI-Readability (Lake), and Learning (Diataxis).
> **Status**: **RECOMMENDED**

## 1. The Architecture

We combine three powerful standards into a single workflow:

1.  **Top Level: P.A.R.A.** (Tiago Forte)
    *   Organizes by *Actionability* (Time Horizon).
    *   Keeps the workspace clean.
2.  **The Medium: Semantic Lake** (Stigmergy)
    *   Files in `Projects` and `Areas` are **Flat**.
    *   We rely on **YAML Headers** (Stigmergy) for linking, not deep folders.
    *   *Rule*: "Don't nest. Tag."
3.  **The Library: Diataxis** (Daniele Procida)
    *   The `Resources` folder is strictly structured by *User Need*.
    *   This is where "Messy Thoughts" become "Crystallized Knowledge".

## 2. The Directory Structure

```text
brain/
├── 1_projects/              # [HOT] Active Goals (The Semantic Lake)
│   │                        # Rule: Flat files. Linked by YAML.
│   ├── intent_gen63.md      # The Goal
│   ├── design_gen63.md      # The Plan
│   └── spec_gen63.feature   # The Test
│
├── 2_areas/                 # [WARM] Ongoing Responsibilities
│   ├── architecture/        # ADRs live here
│   ├── security/
│   └── devops/
│
├── 3_resources/             # [COLD] The Knowledge Base (Diataxis)
│   ├── tutorials/           # "Teach me"
│   ├── guides/              # "How-to"
│   ├── reference/           # "What is it?" (Specs, APIs, Cheatsheets)
│   └── explanation/         # "Why?" (Research, Context, Chat Logs)
│
└── 4_archives/              # [FROZEN] Inactive
    └── gen_61_legacy/
```

## 3. The Workflow (The Water Cycle)

1.  **Rain (Input)**: Raw ideas and chats land in `1_projects` (if active) or `3_resources/explanation` (if just research).
2.  **Flow (Execution)**: We work in `1_projects`. We create Intents, Designs, and Specs as flat files.
3.  **Crystallization (Refraction)**: When a Project is done:
    *   The **Code** goes to `src/`.
    *   The **Knowledge** is refracted into `3_resources/` (e.g., a "How-to" guide).
    *   The **Project Files** move to `4_archives`.

## 4. Migration Map

| Current File | New Location | Rationale |
| :--- | :--- | :--- |
| `manifesto_gen_63.md` | `1_projects/intent_gen63_manifesto.md` | Active Project Intent. |
| `intent_*.md` | `1_projects/` | Active Project Intent. |
| `design_*.md` | `1_projects/` | Active Design. |
| `*.feature` | `1_projects/` | Active Specs (co-located with design). |
| `ai-chat-*.md` | `3_resources/explanation/chats/` | Raw Context. |
| `tech_stack_gen63.md` | `2_areas/architecture/ADR-001...` | Long-term Standard. |
| `AGENTS.md` | `1_projects/` | Currently active coordination. |

## 5. The Stigmergy Header (The Glue)

Every file MUST have this header to survive in the Lake:

```yaml
---
holon:
  id: unique-id-or-slug
  type: [intent, design, spec, adr, chat, guide]
  status: [draft, active, done]
  project: gen-63
  tags: [memory, nats, architecture]
---
```

## 6. Execution Plan

1.  **Create** the PARA folders.
2.  **Create** the Diataxis subfolders in `3_resources`.
3.  **Move** the files.
4.  **Update** `AGENTS.md` to point to the new locations.
