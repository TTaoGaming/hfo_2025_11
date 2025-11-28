# # ==================================================================
# # 🤖 THE HEXAGON (System Generated)
# # ==================================================================
# hexagon:
#   ontos:
#     id: 91c2a6c3-fbb8-4ab5-906f-92df01368d94
#     type: feature
#     owner: Swarmlord
#   chronos:
#     status: active
#     urgency: 0.5
#     decay: 0.5
#     created: '2025-11-23T11:06:41.155541Z'
#     generation: 51
#   topos:
#     address: memory/episodic/gen_50_archive/scatter_gather.feature
#     links: []
#   telos:
#     viral_factor: 0.0
#     meme: scatter_gather.feature
#
Feature: Scatter-Gather Protocol (The Hydra Pattern)
    As the Swarmlord (Navigator)
    I want to dispatch a cohort of agents with specific genetic compositions
    So that I can parallelize a task and synthesize diverse perspectives

    # Biological Metaphor:
    # - Scatter: Spawning multiple "Hands" (Shapers) with different DNA.
    # - Gather: The "Nerves" (Bridgers) collecting signals into the "Brain" or "Memory".

    Scenario Outline: Execute a Heterogeneous Scatter-Gather Mission
        # X: The Cohort Size
        Given a cohort size of "<cohort_size>" agents

        # Y: The Composition (Genetic Strain)
        And a genetic composition of:
            | Model Family | Count | Role       |
            | <strain_1>   | <n1>  | Generator  |
            | <strain_2>   | <n2>  | Critic     |
            | <strain_3>   | <n3>  | Synthesizer|

        # Z: The Task
        When the Swarmlord issues the task "<task_description>"
        And the task type is "<task_type>"

        # Execution (Scatter)
        Then the "Body" spawns the agents in parallel via "Ray"
        And each agent executes the "PREY Loop" independently
        And agents emit their results to "NATS JetStream"

        # Processing (Gather)
        And the "Nerves" collect all <cohort_size> signals
        And the "Assimilator" aggregates the results using "<aggregation_method>"
        And the final output is stored in "Memory"

        Examples:
            | cohort_size | strain_1       | n1 | strain_2       | n2 | strain_3 | n3 | task_description             | task_type | aggregation_method |
            | 5           | x-ai/grok-beta | 3  | openai/gpt-4o  | 1  | claude-3 | 1  | Analyze market trends        | Research  | Consensus Vote     |
            | 3           | google/gemini  | 3  | -              | 0  | -        | 0  | Generate unit tests          | Coding    | Concatenation      |
            | 10          | deepseek/coder | 5  | meta/llama-3   | 5  | -        | 0  | Security audit of codebase   | Security  | Union of Findings  |
