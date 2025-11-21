Feature: Single Researcher PREY Loop
    As the Swarmlord
    I want a single autonomous agent to execute a PREY loop
    So that it can reliably complete research tasks with self-correction

    # Lineage Note: PREY is not an invention. It is a composition of:
    # - OODA Loop (Observe-Orient-Decide-Act)
    # - MAPE-K (Monitor-Analyze-Plan-Execute-Knowledge)
    # - JADC2 (Sense-Make Sense-Act)

    Scenario: Agent executes a full PREY cycle
        Given a research intent "Analyze the latest trends in AI agent frameworks"
        And the agent is initialized with the "Observer" role

        # P - Perceive
        When the agent enters the "Perceive" phase
        Then it should gather context from "memory"
        And it should use tools to "search_internet" for "AI agent frameworks 2025"
        And it should output a "Context Object" containing raw data

        # R - React
        When the agent enters the "React" phase
        And it analyzes the "Context Object" using "Cynefin Framework"
        Then it should generate a "Plan" with specific steps
        And the plan should include "Case-Based Reasoning" from similar past missions

        # E - Execute
        When the agent enters the "Execute" phase
        Then it should execute the steps in the "Plan"
        And it should use tools to "read_documentation" or "run_code"
        And it should produce an "Execution Result"

        # Y - Yield
        When the agent enters the "Yield" phase
        Then it should perform a "Self-Audit" on the "Execution Result"
        And it should ask "Did I satisfy the intent?"
        And if the answer is "No", it should trigger a "Retry" with updated constraints
        And if the answer is "Yes", it should "Commit" the findings to memory
