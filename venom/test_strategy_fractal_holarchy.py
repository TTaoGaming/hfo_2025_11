from body.hands.prey_agent import PreyAgent
from body.models.state import AgentRole


def test_l0_holon_structure():
    """
    Verify that an L0 Agent (Atomic Holon) contains the required components:
    - Brain (Navigator/Planner) -> Implemented via LLM/PreyStep.REACT
    - Body (Workers/Tools) -> Implemented via ToolSet/PreyStep.EXECUTE
    - Memory (Assimilator) -> Implemented via Stigmergy/PreyStep.YIELD
    """
    agent = PreyAgent("test-holon", AgentRole.OBSERVER)

    # 1. Verify Brain (LLM Client)
    assert agent.client is not None, "Holon missing Brain (LLM Client)"

    # 2. Verify Body (Tools)
    assert hasattr(agent, "tools"), "Holon missing Body (Tools)"

    # 3. Verify Memory (Stigmergy)
    assert hasattr(agent, "stigmergy"), "Holon missing Memory (Stigmergy)"

    # 4. Verify Recursive Potential (Can it spawn others?)
    # Currently L0 cannot spawn, but L1 can.
    # This test just verifies the base components.


def test_temporal_dilation_config():
    """
    Verify that we can configure different time horizons.
    """
    # This is a static check for now as we don't have the L1 controller yet.
    # We check if the AgentState has a 'current_mission' which implies a broader context.
    from body.models.state import AgentState

    assert (
        "current_mission" in AgentState.model_fields
    ), "AgentState missing 'current_mission' for context broadening"
