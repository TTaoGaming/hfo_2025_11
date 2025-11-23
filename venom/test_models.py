"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: fed1789b-ae19-4d82-a1f8-ffa8f77bcf0f
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T10:21:31.253351+00:00'
  topos:
    address: venom/test_models.py
    links: []
  telos:
    viral_factor: 0.0
    meme: test_models.py
"""

from body.models import MissionIntent, AgentState, SwarmState, AgentRole, PreyStep


def test_mission_intent_creation():
    intent = MissionIntent(
        description="Test Mission",
        rationale="Testing the SSOT",
        acceptance_criteria=["Scenario: Success"],
        swarm_size=15,
        disruptor_min=2,
        disruptor_max=5,
    )
    assert intent.description == "Test Mission"
    assert intent.status == "pending"
    assert len(intent.constraints) == 0
    assert intent.swarm_size == 15
    assert intent.disruptor_min == 2
    assert intent.evolution_strategy == "MAP-Elites+DSPy"


def test_agent_state_creation():
    state = AgentState(agent_id="agent-007", role=AgentRole.NAVIGATOR)
    assert state.agent_id == "agent-007"
    assert state.role == AgentRole.NAVIGATOR
    assert state.current_step == PreyStep.IDLE


def test_swarm_state_creation():
    swarm = SwarmState(generation_id=50)
    assert swarm.generation_id == 50
    assert swarm.phase == "Set"
    assert len(swarm.active_agents) == 0
