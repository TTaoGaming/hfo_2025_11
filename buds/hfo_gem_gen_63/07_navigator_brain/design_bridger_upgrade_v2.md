---
holon:
  id: hfo-gen63-design-bridger-v2
  type: design
  status: draft
  author: Swarmlord
  intent_id: obsidian-stack-v1
  context: Bridger Upgrade (SSO + MCP)
---

# 🕷️ Design: Bridger V2 (The Social Spider Oracle)

> **Context**: The current Bridger (`bridger.py`) is a "Dumb Pipe" using local embeddings and simple cosine search.
> **Problem**: It returns "Text Matches", not "Answers". It lacks the "Social Spider" intelligence to triangulate truth.
> **Solution**: Upgrade to **Bridger V2**, an MCP Server that implements **Social Spider Optimization (SSO)** via LLM reasoning.

## 1. The Metaphor: The Web & The Spider
We are not building a "Search Engine". We are building a **Vibration Sensor**.

*   **The Web**: The Vector Database (LanceDB). It holds the "Frozen Stigmergy" of the Hive.
*   **The Vibration**: The User's Query. It is a disturbance in the semantic manifold.
*   **The Attenuation**: The decay of relevance over distance (Cosine Similarity).
*   **The Spider**: The LLM (The **Weekly Champion**). It sits on the web, feels the vibration, and decides if it is "Prey" (Signal) or "Wind" (Noise).

## 2. The Algorithm: Social Spider Optimization (SSO)
We adapt the biological SSO algorithm for Semantic Search.

### Phase 1: The Pluck (Vibration)
*   **Input**: User Query ($Q$).
*   **Action**: Embed $Q$ using `settings.MODEL_EMBEDDING` (e.g., `text-embedding-3-small`).
*   **Physics**: The query "plucks" the LanceDB web.

### Phase 2: The Echo (Attenuation)
*   **Action**: Retrieve Top-$K$ (e.g., 20) results from LanceDB.
*   **Metric**: Cosine Similarity ($S$).
*   **Filter**: Apply a "Vibration Threshold" (e.g., $S > 0.7$). Only strong signals pass.

### Phase 3: The Resonance (Triangulation)
*   **Actor**: The Spider (LLM).
*   **Action**: The Spider "tastes" the Top-$K$ fragments using `settings.MODEL_REASONING`.
*   **Logic**:
    *   *Is this fragment relevant to $Q$?* (Binary Classification).
    *   *Does this fragment contradict another?* (Conflict Detection).
    *   *Is there a missing piece?* (Gap Analysis).
*   **Output**: A "Resonant Set" of validated facts.

### Phase 4: The Silk (Synthesis)
*   **Action**: The Spider weaves the Resonant Set into a coherent Answer.
*   **Format**: Markdown with Citations (Stigmergic Links).

## 3. The Architecture: MCP Server
The Bridger V2 will be implemented as a **Model Context Protocol (MCP)** Server.

### Interface
```json
{
  "name": "bridger-oracle",
  "tools": [
    {
      "name": "consult_oracle",
      "description": "Consult the Ancient Wisdom (LanceDB) via Social Spider Triangulation.",
      "inputSchema": {
        "type": "object",
        "properties": {
          "query": { "type": "string", "description": "The question to ask." },
          "depth": { "type": "string", "enum": ["shallow", "deep"], "default": "shallow" }
        },
        "required": ["query"]
      }
    }
  ]
}
```

### Tech Stack
*   **Runtime**: Python 3.11+
*   **Protocol**: `mcp` (Python SDK)
*   **Memory**: `lancedb`
*   **Embeddings**: `settings.MODEL_EMBEDDING` (Dynamic)
*   **Reasoning**: `settings.MODEL_REASONING` (Dynamic)

## 4. Implementation Plan
1.  **Scaffold**: Create `src/servers/bridger_mcp.py`.
2.  **Migrate**: Port LanceDB logic from `bridger.py`.
3.  **Upgrade**: Replace hardcoded models with `settings.MODEL_*`.
4.  **Implement SSO**: Add the "Resonance" step (LLM verification of search results).
5.  **Test**: Verify against the "Truth" (Gen 63 Memory).

## 5. The "Truth" (Source of Truth)
*   **Primary**: `buds/hfo_gem_gen_63/memory/lancedb` (The Unified Memory).
*   **Fallback**: `buds/hfo_gem_gen_61/memory/hfo_gen_61_lancedb` (The Ancestral Memory).
