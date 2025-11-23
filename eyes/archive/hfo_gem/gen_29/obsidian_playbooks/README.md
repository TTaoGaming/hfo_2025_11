---
hexagon:
  ontos:
    id: 2db916df-3af2-4d4c-93f1-abb2fb52db1a
    type: md
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T11:07:36.010749Z'
    generation: 51
  topos:
    address: eyes/archive/hfo_gem/gen_29/obsidian_playbooks/README.md
    links: []
  telos:
    viral_factor: 0.0
    meme: README.md
---
# OBSIDIAN Playbooks – Role Documentation

**Created**: 2025-11-11
**Purpose**: Document the 8 OBSIDIAN roles (JADC2-aligned personas for HFO swarm)
**Status**: 🔄 In Progress (1/8 complete)

---

## Overview

OBSIDIAN is an acronym representing 8 specialized roles that span the JADC2 mosaic warfare mission threads:

- **O** - Observer (sensing, telemetry)
- **B** - Bridger (intent translation)
- **S** - Shaper (execution, knowledge sculpting)
- **I₁** - Injector (resource allocation, FINOPS)
- **D** - Disruptor (red team, adversarial testing)
- **I₂** - Immunizer (blue team, quality assurance)
- **A** - Assimilator (knowledge fusion, SSOT updates)
- **N** - Navigator (strategic planning, campaign design)

Each role maps to JADC2 combat-tested doctrine and the PREY loop (Perceive → React → Execute → Yield).

---

## Playbook Structure

Each playbook contains:
1. **Mission Voice** - Role philosophy and strategic anchor
2. **Core Responsibilities** - What this role does
3. **System Prompt Template** - LLM instructions for this persona
4. **Temperature & Model Settings** - Optimal configuration
5. **Tools & Capabilities** - Available resources
6. **PREY Loop Responsibilities** - Role-specific PREY phase tasks
7. **Decision Matrix** - How this role handles different situations
8. **Validation Criteria** - Quality gates for outputs
9. **Example Flows** - Concrete usage scenarios
10. **Failure Modes & Recovery** - Error handling patterns
11. **Integration with Other Roles** - Inter-role communication
12. **Metrics & KPIs** - Success measurement
13. **Evolution Roadmap** - Gen 30+ enhancements

---

## Playbook Status

| Role | File | Status | Owner | Notes |
|------|------|--------|-------|-------|
| **Navigator (N)** | `N_Navigator_Playbook.md` | ✅ Complete | Swarmlord of Webs | Strategic C2, PREYOrchestrator |
| **Bridger (B)** | `B_Bridger_Playbook.md` | 🔄 Pending | - | Intent translation, InterpreterAgent |
| **Shaper (S)** | `S_Shaper_Playbook.md` | 🔄 Pending | - | Research execution, ResearcherAgent |
| **Observer (O)** | `O_Observer_Playbook.md` | 🔄 Pending | - | Telemetry, signal capture |
| **Injector (I₁)** | `I1_Injector_Playbook.md` | 🔄 Pending | - | Cost management, resource allocation |
| **Disruptor (D)** | `D_Disruptor_Playbook.md` | 🔄 Pending | - | Red team, hallucination detection |
| **Immunizer (I₂)** | `I2_Immunizer_Playbook.md` | 🔄 Pending | - | Blue team, quorum consensus |
| **Assimilator (A)** | `A_Assimilator_Playbook.md` | 🔄 Pending | - | Knowledge fusion, SynthesizerAgent |

---

## Role Mapping to Gen 29 Code

| OBSIDIAN Role | Gen 29 Implementation | File | Status |
|---------------|----------------------|------|--------|
| **Navigator (N)** | `PREYOrchestrator` | `hfo_swarm/prey_orchestrator.py` | ✅ Implemented |
| **Bridger (B)** | `InterpreterAgent` | `hfo_swarm/prey_orchestrator.py` | ✅ Implemented |
| **Shaper (S)** | `ResearcherAgent` | `hfo_swarm/prey_orchestrator.py` | ✅ Implemented |
| **Observer (O)** | (pending) | - | ❌ Not implemented |
| **Injector (I₁)** | (pending) | - | ❌ Not implemented |
| **Disruptor (D)** | `ValidatorAgent` (hallucination) | `hfo_swarm/prey_orchestrator.py` | 🔄 Partial (needs split) |
| **Immunizer (I₂)** | `ValidatorAgent` (quorum) | `hfo_swarm/prey_orchestrator.py` | 🔄 Partial (needs split) |
| **Assimilator (A)** | `SynthesizerAgent` | `hfo_swarm/prey_orchestrator.py` | ✅ Implemented |

---

## JADC2 → PREY → OBSIDIAN Alignment Matrix

| JADC2 Phase | PREY Phase | OBSIDIAN Roles | Gen 29 Implementation |
|-------------|------------|----------------|----------------------|
| **Sense** | **Perceive** | Observer (O), Bridger (B) | InterpreterAgent extracts mission structure |
| **Make Sense** | **React** | Navigator (N) | PREYOrchestrator selects workflow, composes team |
| **Act** | **Execute** | Shaper (S), Injector (I₁) | ResearcherAgent × N executes research |
| **Feedback** | **Yield** | Disruptor (D), Immunizer (I₂), Assimilator (A) | ValidatorAgent + SynthesizerAgent produce digest |

**Source**: U.S. DoD (2020). *Joint All-Domain Command and Control (JADC2) Concept*.

---

## Usage Patterns

### Single Role Execution (Solo Mode)
```python
# Bridger translates user intent
mission_structure = bridger_agent.interpret(
    user_input="What are the best practices for Kubernetes?"
)

# Shaper executes research (single worker, no swarm)
research = shaper_agent.research(
    orchestration_prompt=mission_structure["orchestration_prompt"]
)

# Assimilator synthesizes result
digest = assimilator_agent.synthesize(research)
```

### Multi-Role Swarm (Full PREY Loop)
```python
# Navigator orchestrates all roles
result = navigator.execute_mission(
    user_input="What are the best practices for Kubernetes?",
    num_shapers=5,  # 5 ResearcherAgents
    enable_disruptor=True,  # Hallucination detection
    enable_immunizer=True,  # Quorum consensus
    enable_observer=False,  # Telemetry (pending Gen 30)
    enable_injector=False   # Cost tracking (pending Gen 30)
)
```

### Role-Specific Override
```python
# Use custom Shaper for specialized domain
custom_shaper = ShaperAgent(
    system_prompt="You are a Kubernetes CKA-certified expert...",
    temperature=0.9,  # Higher creativity
    model="openai/gpt-4-turbo"  # More capable model
)

result = navigator.execute_mission(
    user_input="...",
    custom_roles={"shaper": custom_shaper}
)
```

---

## Development Roadmap

### Week 1: Core Playbooks (Days 1-7)
- [x] Navigator (N) - ✅ Complete
- [ ] Bridger (B) - Maps to InterpreterAgent
- [ ] Shaper (S) - Maps to ResearcherAgent
- [ ] Assimilator (A) - Maps to SynthesizerAgent

### Week 2: Validation Roles (Days 8-14)
- [ ] Disruptor (D) - Red team, hallucination detection
- [ ] Immunizer (I₂) - Blue team, quorum consensus
- [ ] Split ValidatorAgent into Disruptor + Immunizer

### Week 3: Infrastructure Roles (Days 15-21)
- [ ] Observer (O) - Telemetry collection, signal capture
- [ ] Injector (I₁) - Cost management, resource allocation

### Week 4: Integration & Testing (Days 22-30)
- [ ] JADC2 alignment matrix validation
- [ ] Role integration tests
- [ ] Full PREY loop with all 8 roles
- [ ] Documentation finalization

---

## Quick Reference

### Role Temperature Recommendations
- **Navigator**: 0.4 (strategic balance)
- **Bridger**: 0.3 (precise translation)
- **Shaper**: 0.8 (creative exploration)
- **Observer**: 0.1 (objective measurement)
- **Injector**: 0.2 (quantitative allocation)
- **Disruptor**: 0.5 (adversarial creativity)
- **Immunizer**: 0.1 (objective validation)
- **Assimilator**: 0.5 (structured synthesis)

### Role Model Recommendations
- **Navigator**: `MODEL_PLANNER` (strategic reasoning)
- **Bridger**: `MODEL_PLANNER` (precise extraction)
- **Shaper**: `MODEL_RESEARCHER` (domain expertise)
- **Observer**: `MODEL_VALIDATOR` (objective observation)
- **Injector**: `MODEL_VALIDATOR` (quantitative analysis)
- **Disruptor**: `MODEL_VALIDATOR` (adversarial testing)
- **Immunizer**: `MODEL_VALIDATOR` (quality assurance)
- **Assimilator**: `MODEL_EXECUTOR` (structured synthesis)

---

## References

- **JADC2 Doctrine**: U.S. Department of Defense (2020). *Joint All-Domain Command and Control (JADC2) Concept*.
- **Gen 28 OBSIDIAN Roles**: `hfo_gem/gen_28/vision_level_diagrams.md`
- **Gen 29 Architecture**: `hfo_gem/gen_29/deep_dive.md`
- **Gen 29 Hardening Roadmap**: `hfo_gem/gen_29/GEN_29_HARDENING_ROADMAP.md`
- **PREY Loop Spec**: `PREY_ORCHESTRATOR_SPEC.md`

---

**Next**: Complete Bridger (B) and Shaper (S) playbooks
**Owner**: Swarmlord of Webs (Navigator role)
**Status**: 1/8 playbooks complete (12.5%)
