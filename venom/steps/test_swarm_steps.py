import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from body.models import MissionIntent, SwarmState, AgentState, AgentRole, SwarmPhase

# Load scenarios from the feature file
scenarios('../../intent/swarm_workflow.feature')

# Fixtures
@pytest.fixture
def swarm_context():
    return {
        "intent": None,
        "swarm_state": None,
        "agents": [],
        "constraints": [],
        "signals": [],
        "traces": [],
        "results": [],
        "disruptor_detected": False,
        "archive_updated": False
    }

# Given Steps
@given(parsers.parse('a mission intent "{description}"'))
def mission_intent(swarm_context, description):
    swarm_context["intent"] = MissionIntent(
        description=description,
        rationale="Test Rationale"
    )

@given(parsers.parse('a swarm size of {count:d} agents'))
def swarm_size(swarm_context, count):
    swarm_context["swarm_state"] = SwarmState(generation_id=1)
    # Update the Intent SSOT
    if swarm_context["intent"]:
        swarm_context["intent"].swarm_size = count

@given(parsers.parse('selects "{group}" for coordination'))
def select_coordination_group(swarm_context, group):
    if swarm_context["intent"]:
        swarm_context["intent"].coordination_model_group = group
        assert swarm_context["intent"].coordination_model_group == "Cheap Navigators"

@given(parsers.parse('selects "{group}" for execution'))
def select_execution_group(swarm_context, group):
    if swarm_context["intent"]:
        swarm_context["intent"].execution_model_group = group
        assert swarm_context["intent"].execution_model_group == "Cheap QD Swarm"

@given(parsers.parse('excludes "{model}" from swarm operations'))
def exclude_model(swarm_context, model):
    if swarm_context["intent"]:
        swarm_context["intent"].excluded_models.append(model)
        assert model in swarm_context["intent"].excluded_models

# When Steps (Set)
@when(parsers.parse('the Swarmlord "Sets" the mission parameters'))
def set_mission(swarm_context):
    swarm_context["swarm_state"].phase = SwarmPhase.SET
    # Verify SSOT is set
    assert swarm_context["intent"] is not None

@when(parsers.parse('defines the "Search Space" for evolution'))
def define_search_space(swarm_context):
    # Mocking search space definition
    swarm_context["search_space"] = {"param_a": [0, 1]}
    # Ensure strategy is recorded in SSOT
    if swarm_context["intent"]:
        assert "DSPy" in swarm_context["intent"].evolution_strategy

@when(parsers.parse('establishes "Constraints" ({constraints})'))
def establish_constraints(swarm_context, constraints):
    constraint_list = [c.strip() for c in constraints.split(',')]
    swarm_context["constraints"] = constraint_list

# When Steps (Watch)
@when(parsers.parse('the system "Watches" for stigmergy signals via "{mechanism}"'))
def watch_signals(swarm_context, mechanism):
    swarm_context["swarm_state"].phase = SwarmPhase.WATCH
    swarm_context["signals"].append(mechanism)

@when(parsers.parse('initializes "{tool}" traces for observability'))
def init_traces(swarm_context, tool):
    swarm_context["traces"].append(tool)

# When Steps (Act)
@when(parsers.parse('the swarm "Acts" using a "{pattern}" pattern'))
def act_pattern(swarm_context, pattern):
    swarm_context["swarm_state"].phase = SwarmPhase.ACT
    swarm_context["pattern"] = pattern

@when(parsers.parse('spawns {count:d} agents (including {disruptor_range} "Disruptors") to execute the "{loop}"'))
def spawn_agents_with_disruptors(swarm_context, count, disruptor_range, loop):
    # Parse disruptor range "1-3"
    min_d, max_d = map(int, disruptor_range.split('-'))
    
    # Update SSOT
    if swarm_context["intent"]:
        swarm_context["intent"].disruptor_min = min_d
        swarm_context["intent"].disruptor_max = max_d
    
    num_disruptors = min_d # For test simplicity, pick min
    
    for i in range(count):
        role = AgentRole.DISRUPTOR if i < num_disruptors else AgentRole.SHAPER
        agent = AgentState(agent_id=f"agent-{i}", role=role)
        swarm_context["agents"].append(agent)

@when(parsers.parse('agents communicate via "{mechanism}"'))
def agent_comm(swarm_context, mechanism):
    # Mock communication channel
    pass

# When Steps (Review)
@when(parsers.parse('the system "Reviews" the results via "{mechanism}"'))
def review_results(swarm_context, mechanism):
    swarm_context["swarm_state"].phase = SwarmPhase.REVIEW

@when(parsers.parse('"{role}" agents (Blue Team) attempt to detect the disruptors'))
def immunizer_detect(swarm_context, role):
    # Mock detection logic - check if any disruptors exist
    disruptors = [a for a in swarm_context["agents"] if a.role == AgentRole.DISRUPTOR]
    if disruptors:
        swarm_context["disruptor_detected"] = True

@when(parsers.parse('the consensus confidence is capped at {percent:d}% ({reason})'))
def cap_confidence(swarm_context, percent, reason):
    swarm_context["swarm_state"].consensus_confidence = min(0.95, percent / 100.0)

# When Steps (Mutate)
@when(parsers.parse('the system "Mutates" the "{framework}" prompts and swarm parameters using "{method}"'))
def mutate_system(swarm_context, framework, method):
    swarm_context["swarm_state"].phase = SwarmPhase.MUTATE
    swarm_context["mutation_framework"] = framework
    
    # Update State SSOT
    swarm_context["swarm_state"].current_dspy_prompt = "optimized_signature_v2"
    swarm_context["swarm_state"].mutation_history.append(f"Applied {method} via {framework}")

@when(parsers.parse('updates the "{archive}" archive'))
def update_archive(swarm_context, archive):
    swarm_context["archive_updated"] = True

@when(parsers.parse('evolves the entire swarm strategy for the next cycle'))
def evolve_strategy(swarm_context):
    # Mock evolution
    pass
