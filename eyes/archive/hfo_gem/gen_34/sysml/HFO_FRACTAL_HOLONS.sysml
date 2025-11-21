package HFO_Fractal_System {

    private import ScalarValues::*;

    doc /*
    Hive Fleet Obsidian: Fractal Holonic Architecture
    Defined in SysML v2

    This package defines the structural hierarchy of HFO, from the atomic agent (L0)
    to the apex swarm (L3), demonstrating how capabilities emerge at scale.
    */

    // ============================================================
    // 1. CAPABILITY DEFINITIONS
    // ============================================================

    package Capabilities {
        // L0 Capabilities
        part def PREY_Loop;
        part def Tool_Use;
        part def Local_Memory;

        // L1 Capabilities
        part def Byzantine_Consensus;
        part def V2C_Validation;
        part def Hallucination_Detection;

        // L2 Capabilities
        part def Stigmergy_Coordination {
            attribute protocol : String = "NATS JetStream";
            // attribute signal_types : String[*] = ["Heartbeat", "Confidence", "Citation"];
        }
        part def Temporal_Orchestration;

        // L3 Capabilities
        part def Obsidian_Hourglass_Planning;
        part def Global_Optimization;
    }

    // ============================================================
    // 2. HOLON DEFINITIONS (MOSAIC TILES)
    // ============================================================

    private import Capabilities::*;

    // --- The Abstract Mosaic Tile ---
    // Inspired by JADC2 Mosaic Warfare: Composable, Disaggregated, Flexible.
    abstract part def Mosaic_Tile {
        // Every tile connects to the Stigmergy Mesh
        port stigmergy_port;

        // Every tile has an Immune System (Fractal Immunity)
        part immune_system : Hallucination_Detection;

        // Behavior: Self-Assignment
        // Tiles listen to the mesh and assign themselves roles.
    }

    // --- L0: The Atomic Holon (1 Agent) ---
    part def L0_Atomic_Holon :> Mosaic_Tile {
        attribute scale : Integer = 1;
        attribute cost_per_mission : Real = 0.00001;

        // Core Components
        part prey_loop : PREY_Loop;
        part tools : Tool_Use;
        part memory : Local_Memory;

        // Ports
        port input_intent;
        port output_result;
    }

    // --- L1: The Quorum Holon (10 Agents) ---
    part def L1_Quorum_Holon :> Mosaic_Tile {
        attribute scale : Integer = 10;
        attribute cost_per_mission : Real = 0.0001;
        attribute quorum_threshold : Real = 0.7; // 7/10

        // Composition: 10 Atomic Holons acting as a Mesh
        part researchers : L0_Atomic_Holon[10];

        // Emergent Capabilities
        part consensus : Byzantine_Consensus;
        part validation : V2C_Validation;

        // Internal Connections: MESH TOPOLOGY
        // Researchers coordinate via Stigmergy, not just central command
        connect researchers.stigmergy_port to stigmergy_port;
    }

    // --- L2: The Meta Holon (100 Agents) ---
    part def L2_Meta_Holon :> Mosaic_Tile {
        attribute scale : Integer = 100;
        attribute cost_per_mission : Real = 0.001;

        // Composition: 10 Quorum Holons acting as a Mesh
        part swarms : L1_Quorum_Holon[10];

        // Emergent Capabilities
        part stigmergy_hub : Stigmergy_Coordination;
        part orchestrator : Temporal_Orchestration;

        // The Mesh scales: L1s coordinate via the L2 Stigmergy Hub
        connect swarms.stigmergy_port to stigmergy_hub;
    }

    // --- L3: The Apex Holon (1000 Agents) ---
    part def L3_Apex_Holon {
        attribute scale : Integer = 1000;
        attribute cost_per_mission : Real = 0.01;

        // Composition: 10 Meta Holons
        part meta_swarms : L2_Meta_Holon[10];

        // Emergent Capabilities
        part hourglass : Obsidian_Hourglass_Planning;
        part optimizer : Global_Optimization;

        doc /*
        At L3, the system is capable of strategic long-horizon planning
        using the Obsidian Hourglass to manage constraints and precedents
        across the entire fleet.
        */
    }

    // ============================================================
    // 3. SYSTEM CONFIGURATION
    // ============================================================

    part def HFO_System {
        // The system can be instantiated at any level depending on the mission
        part active_holon : L3_Apex_Holon; // Defaulting to full scale for definition
    }
}
