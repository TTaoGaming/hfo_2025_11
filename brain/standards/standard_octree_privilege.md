# 🦅 HFO Standard: Octree Privilege System (Holonic Permissions)

> **Status**: Active (Gen 55)
> **Domain**: Security & Governance
> **Pattern**: Powers of 8 (Octree)

## 1. The Core Concept
HFO uses a **Holonic Privilege System** based on the **Octree** fractal pattern. Permissions are not just "User vs Admin" but represent the **Cognitive Scale** of the agent or entity accessing the system.

## 2. The Levels (Powers of 8)

| Level | Name | Scale (Agents) | Description | Access Scope |
| :--- | :--- | :--- | :--- | :--- |
| **Lvl 0** | **Atomic** | 1 ($8^0$) | A single agent or simple tool. | **Public/Local**: Can read/write ephemeral data. No access to strategic core. |
| **Lvl 1** | **Squad** | 8 ($8^1$) | A tactical squad (The 8 Roles). | **Tactical**: Can coordinate within a hexagon. Access to squad memory. |
| **Lvl 2** | **Platoon** | 64 ($8^2$) | A swarm sector (8 Squads). | **Operational**: Can coordinate across sectors. Access to sector memory. |
| **Lvl 3** | **Legion** | 512 ($8^3$) | A full hive deployment. | **Strategic**: Full system access (excluding Core Directives). |
| ... | ... | ... | ... | ... |
| **Lvl 8** | **Overmind** | N/A | **TTao (The User)** | **Omniscient**: Full read/write/delete access to Core Memory (Logos/Ontos). |

## 3. Implementation
*   **LanceDB**: The `hfo_stigmergy` table includes a `privilege_level` (int32) column.
*   **Ingestion**: Data is tagged with a level upon entry.
    *   `ingest_manifesto.py` -> **Lvl 8** (Core Doctrine).
    *   `ingest_lvl0.py` -> **Lvl 0** (Raw Intake).
*   **Retrieval**: Agents query with `min_privilege`.
    *   A Lvl 0 Agent can only see Lvl 0 data (unless explicitly granted "Read Down" access).
    *   A Lvl 8 Entity (You) can see everything.

## 4. The Golden Rule
> **"The Octree protects the Core."**
> Low-level agents (Lvl 0-2) operate on **Stigmergy** (Signals).
> High-level entities (Lvl 8) operate on **Intent** (Directives).
