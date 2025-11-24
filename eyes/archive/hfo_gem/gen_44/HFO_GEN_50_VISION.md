---
hexagon:
  ontos:
    id: ea8b64d6-147f-4f69-b569-3e790cf31132
    type: md
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T11:07:36.078885Z'
    generation: 51
  topos:
    address: eyes/archive/hfo_gem/gen_44/HFO_GEN_50_VISION.md
    links: []
  telos:
    viral_factor: 0.0
    meme: HFO_GEN_50_VISION.md
---

# Hive Fleet Obsidian: Generation 50 Vision

## 1. What is HFO Gen 50?

It is an Automated Game Factory.

The Old Way (Gen 40): You act like a programmer. You write code. You test it. You fix it. You make 1 game a week.

The New Way (Gen 50): You act like a General. You give an order: "Make me 100 games controlled by blinking." The Factory spins up 1,000 invisible workers. They write the code, they play-test the games, they throw away the bad ones, and they deliver the good ones to you.

## 2. The Tech Stack (The "T.R.A.M." Stack)

We threw away the "Corporate IT" tools (Docker, SysML) because they are too slow and heavy. We are using the SOTA (State of the Art) Speed Stack.

Here are the 4 pieces you need:

**T - Temporal (The Manager)**
*   What it is: A "Save Game" system for your code.
*   Why you need it: If you order 1,000 games and your computer crashes on game #99, Temporal remembers exactly where you were. When you restart, it resumes at game #99. It makes the system Durable.

**R - Ray (The Hive)**
*   What it is: A tool that turns your single computer into a "Cluster."
*   Why you need it: You can't run 1,000 agents in a normal script; your computer will freeze. Ray creates 1,000 tiny "Actors" (workers) that run in parallel across every CPU core you have. It handles the Scale.

**A - Agno (The Workers)**
*   What it is: The fastest AI Agent framework available right now.
*   Why you need it: Old frameworks (LangChain) are bloated. Agno agents start in microseconds. They are lightweight and designed to use tools perfectly. This gives you Speed.

**M - MCP (The Universal Plug)**
*   What it is: The "USB-C" for AI tools.
*   Why you need it: Instead of writing custom code to let your agent save files or search the web, you just "plug in" the FileSystem MCP or Brave Search MCP. It connects your agents to the world instantly. This gives you Connectivity.

## 3. How It Works (The Day in the Life)

Here is exactly what happens when you run Gen 50:

1.  **The Order**: You type: "Build a library of 'Endless Runner' games controlled by head tilting."
2.  **The Scatter**: Temporal tells Ray to wake up. Ray spins up 50 Agno Agents (The Builders).
3.  **The Build**: The Builders use MCP to write code for 50 different versions of the game.
4.  **The Gauntlet**: Ray spins up 50 Disruptor Agents (The Red Team). They open invisible web browsers and play the games at 100x speed.
5.  **The Evolution**:
    *   Game A crashes? Deleted.
    *   Game B is boring? Deleted.
    *   Game C works and is fun? Saved.
6.  **The Result**: You go get coffee. You come back 10 minutes later. You have 12 playable games in your folder.

## 4. Why this is "Anti-Fragile"

*   **Fragile**: If a script hits an error, it stops.
*   **Robust**: If a script hits an error, it doesn't crash.
*   **Anti-Fragile**: If a game crashes, the system learns. The Disruptor records why it crashed, and the next Builder avoids that mistake. The system gets smarter the more it fails.

## 5. Summary

HFO Gen 50 is a Factory.

*   **Inputs**: Your Intent (Gesture Games).
*   **Machinery**: Ray (Scale) + Temporal (Reliability).
*   **Workers**: Agno Agents (Smart & Fast).
*   **Outputs**: A War Chest of software.

You stop writing code. You start managing the Factory.

## 6. The Missing Pieces (Evolutionary Engine)

You mentioned "openevolve." In the SOTA academic world, the specific library you want is **pyribs**.

**Missing Piece 1: The Evolution Engine (pyribs)**
*   **The Problem**: Your "Builder" agents just make random games. The swarm converges on the easy stuff.
*   **The SOTA Solution**: MAP-Elites (via the pyribs library).
*   **What is it?** It’s a Grid.
    *   X-Axis: Difficulty (Easy → Hard).
    *   Y-Axis: Mechanic (Blinking → Tilting).
*   **Why you need it**: It forces the Swarm to explore. It guarantees your War Chest has variety, not just quantity.

**Missing Piece 2: The Eyes (Vision Language Models)**
*   **The Problem**: A "Disruptor" can tell if the code crashes, but it cannot tell if the game is fun or ugly.
*   **The SOTA Solution**: VLM (GPT-4o / Claude 3.5 Sonnet via MCP).
*   **The Workflow**: Playwright takes a screenshot -> VLM scores "Aesthetic Fitness".

**Missing Piece 3: The Library (Hugging Face Hub via MCP)**
*   **The Problem**: Where do you put the 10,000 games?
*   **The SOTA Solution**: Hugging Face (HF) Dataset.
*   **Why you need it**: It allows you to browse your War Chest online.

## 7. The Complete "Gen 50" Picture

| Step | The "T.R.A.M." Stack | The New Pieces (Evolution) |
| :--- | :--- | :--- |
| 1. Command | Temporal wakes up. | Checks pyribs Grid: "We need more Hard games." |
| 2. Scatter | Ray spins up Builders. | Builders use Agno to generate code. |
| 3. Test | Ray spins up Disruptors. | Disruptors use Playwright to play & screenshot. |
| 4. Judge | (Missing before) | VLM (Vision) looks at screenshots. Scores "Fun." |
| 5. Sort | (Missing before) | pyribs places game on Grid. "New High Score!" |
| 6. Save | MCP saves file. | Pushes to Hugging Face Dataset. |
