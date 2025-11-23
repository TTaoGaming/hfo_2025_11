# # ==================================================================
# # 🤖 THE HEXAGON (System Generated)
# # ==================================================================
# hexagon:
#   ontos:
#     id: eb3dc8e6-e096-472b-a414-fd6eb490da61
#     type: feature
#     owner: Swarmlord
#   chronos:
#     status: active
#     urgency: 0.5
#     decay: 0.5
#     created: '2025-11-23T10:21:06.990535+00:00'
#   topos:
#     address: memory/episodic/gen_50_archive/hfo_system_architecture.feature
#     links: []
#   telos:
#     viral_factor: 0.0
#     meme: hfo_system_architecture.feature
#

Feature: HFO System Architecture (Organs, Roles, Champions)
    As the Swarmlord
    I want a composable architecture where Champions inhabit Roles to operate Organs
    So that the system is evolutionary, mission-agnostic, and JADC2-aligned

    # ==========================================
    # 🧬 The Anatomy (Organs) - The "Where"
    # ==========================================

    Scenario: The Brain (Strategic Domain)
        Given the "Brain" organ at "brain/"
        Then it serves as the "Seat of Will"
        And it stores "Intent" (Gherkin) and "Architecture" (Mermaid)
        And it emits "signal:directive" when Strategy changes

    Scenario: The Eyes (Sensory Domain)
        Given the "Eyes" organ at "eyes/"
        Then it serves as the "Seat of Perception"
        And it ingests "Raw Data" and "Telemetry"
        And it emits "signal:stimulus" when Data arrives

    Scenario: The Nerves (Coordination Domain)
        Given the "Nerves" organ at "body/nerves/"
        Then it serves as the "Seat of Connection"
        And it routes "Signals" and manages "State"
        And it emits "signal:impulse" to trigger Action

    Scenario: The Hands (Execution Domain)
        Given the "Hands" organ at "body/hands/"
        Then it serves as the "Seat of Action"
        And it houses "Tools" (MCP) and "Effectors"
        And it emits "signal:action" when Tools execute

    Scenario: The Blood (Logistics Domain)
        Given the "Blood" organ at "body/blood/"
        Then it serves as the "Seat of Resources"
        And it circulates "Config", "Keys", and "Models"
        And it emits "signal:nutrient" to fuel the system

    Scenario: The Carapace (Protection Domain)
        Given the "Carapace" organ at "carapace/"
        Then it serves as the "Seat of Governance"
        And it enforces "Standards" and "Boundaries"
        And it emits "signal:barrier" to block violations

    Scenario: The Venom (Adversarial Domain)
        Given the "Venom" organ at "venom/"
        Then it serves as the "Seat of Stress"
        And it houses "Chaos Agents" and "Red Team Tests"
        And it emits "signal:catalyst" to force evolution

    Scenario: The Memory (Intelligence Domain)
        Given the "Memory" organ at "memory/"
        Then it serves as the "Seat of Wisdom"
        And it assimilates "Experience" into "Knowledge Graphs"
        And it emits "signal:spore" for long-term retention

    # ==========================================
    # 🎭 The Physiology (Roles) - The "How"
    # ==========================================

    Scenario: Role Composition (JADC2 Mapping)
        Given a "Champion" (Persona) is assigned to a "Role"
        When the Role is "Navigator"
            Then the Champion acts as "Commander (C2)"
            And primarily operates in the "Brain"
        When the Role is "Observer"
            Then the Champion acts as "Sensor (ISR)"
            And primarily operates in the "Eyes"
        When the Role is "Bridger"
            Then the Champion acts as "Communicator"
            And primarily operates in the "Nerves"
        When the Role is "Shaper"
            Then the Champion acts as "Decider/Effector"
            And primarily operates in the "Hands"
        When the Role is "Injector"
            Then the Champion acts as "Logistics"
            And primarily operates in the "Blood"
        When the Role is "Immunizer"
            Then the Champion acts as "Blue Team"
            And primarily operates in the "Carapace"
        When the Role is "Disruptor"
            Then the Champion acts as "Red Team"
            And primarily operates in the "Venom"
        When the Role is "Assimilator"
            Then the Champion acts as "Intelligence"
            And primarily operates in the "Memory"

    # ==========================================
    # ⚔️ The Soul (Champions) - The "Who"
    # ==========================================

    Scenario: Champion Evolution (Quality Diversity)
        Given a roster of "Champions" (Personas)
        When a Champion is "Bred" or "Evolved"
        Then its "Hyper-Heuristics" and "Prompts" are mutated
        And it can be assigned to different "Roles" based on "Mission Needs"
        And it can operate across multiple "Organs" to achieve its goal
