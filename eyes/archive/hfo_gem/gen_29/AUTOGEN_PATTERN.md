---
hexagon:
  ontos:
    id: abf6238a-8221-4dfa-8117-bbdf7f01025d
    type: md
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T11:07:35.979672Z'
    generation: 51
  topos:
    address: eyes/archive/hfo_gem/gen_29/AUTOGEN_PATTERN.md
    links: []
  telos:
    viral_factor: 0.0
    meme: AUTOGEN_PATTERN.md
---

# Generation 29: SSOT Autogeneration Pattern

**Vision**: Define swarm orchestration patterns in SysML v2, auto-generate Python implementation

---

## Current Manual Process (Gen 29)

### Steps
1. User dictates swarm type ("scatter-gather research swarm with PREY loops")
2. Developer hand-codes 4 agent classes (InterpreterAgent, ResearcherAgent, ValidatorAgent, SynthesizerAgent)
3. Developer writes system prompts (ANALYTICAL, CREATIVE, OBJECTIVE, CONCISE philosophies)
4. Developer tunes temperatures (0.3, 0.8, 0.1, 0.5)
5. Developer builds LangGraph workflow (SENSE → ACT → YIELD)
6. Developer creates database schema (3 tables: missions, researchers, analysis)
7. Developer writes artifact manager (5-directory hierarchy)
8. Developer creates CLI entrypoint (`run_swarm.py`)
9. Developer writes tests

### Pain Points
- **760 lines of boilerplate** for single swarm type
- **System prompts buried** in Python strings (hard to version, compare, evolve)
- **Temperature tuning trial-and-error** (no systematic exploration)
- **No standardized pattern** (each new swarm type requires full rewrite)
- **Manual consistency** (agent roles, flow order, state passing)
- **Undocumented design decisions** (why temp=0.3 for interpreter?)

### Example: Agent Definition (Manual)

```python
class InterpreterAgent(BaseAgent):
    """SENSE phase: Extract mission structure."""

    SYSTEM_PROMPTS = {
        "interpret": """
            You are an ANALYTICAL and PRECISE mission interpreter.
            Your role is to extract structured information from user input.

            You do NOT:
            - Speculate about answers
            - Provide research
            - Generate strategies

            You DO:
            - Extract intent clearly
            - Identify constraints
            - Create orchestration prompts for workers
        """
    }

    def __init__(self):
        super().__init__(
            model_name=os.getenv("MODEL_PLANNER", "openai/gpt-oss-120b"),
            temperature=0.3  # Why 0.3? Precision requirement (undocumented)
        )
```

**Problems**:
- System prompt is magic string (no schema, no validation)
- Temperature 0.3 has no documented rationale
- Model selection via env var (no model diversity per role)
- No connection to architectural intent (SENSE phase)

---

## Future SSOT-Driven Process (Gen 30+)

### Vision
Define swarm architecture once in `HFO_SSOT.sysml`, auto-generate all implementation artifacts.

### Steps
1. User defines swarm pattern in SysML v2 (`HFO_SSOT.sysml`)
2. Parser extracts agent definitions, flows, constraints
3. Generator creates Python agent classes
4. Generator creates LangGraph workflow
5. Generator creates database schema SQL
6. Generator creates artifact manager
7. Generator creates CLI entrypoint
8. Generator creates tests
9. **One command**: `python scripts/generate_orchestrator.py --ssot HFO_SSOT.sysml --output hfo_swarm/`

### Benefits
- **Single source of truth**: All architectural decisions in SSOT
- **Versioned evolution**: Track swarm changes via git diffs on SSOT
- **Rapid iteration**: Modify SSOT, regenerate code in seconds
- **Design documentation**: SSOT is self-documenting (why temp=0.3? constraint in SSOT)
- **Pattern library**: Reusable SSOT modules (scatter-gather, map-reduce, tree-search)
- **Multi-model support**: Define model per role (Claude for research, GPT for synthesis)

---

## SSOT Definition Example (SysML v2)

### Complete PREYOrchestrator Definition

```sysml
package SwarmOrchestration {

    import ScalarValues::*;
    import Collections::*;

    // ================================================================
    // PREY Orchestrator Pattern (Scatter-Gather Research Swarm)
    // ================================================================

    part def PREYOrchestrator {
        doc /*
            Scatter-gather research swarm with nested PREY loops.

            Orchestrator PREY: SENSE → ACT → YIELD
            Worker PREY: SENSE → REACT → ACT → YIELD

            Use for: Broad research questions requiring diverse perspectives + consensus analysis
        */

        // ============================================================
        // Agent Roles (Single Responsibility Principle)
        // ============================================================

        part interpreter : InterpreterAgent;
        part researchers[1..*] : ResearcherAgent;
        part validator : ValidatorAgent;
        part synthesizer : SynthesizerAgent;

        // ============================================================
        // PREY Flow Definition
        // ============================================================

        flow sense : interpreter.output -> researchers.input;
        flow act : researchers.output -> validator.input;
        flow yield : validator.output -> synthesizer.input;

        // ============================================================
        // Configuration Parameters
        // ============================================================

        attribute num_workers : Integer = 10;
        attribute consensus_threshold : Real = 0.8;
        attribute execution_timeout : Integer = 300;  // seconds
        attribute enable_hallucination_check : Boolean = true;

        // ============================================================
        // Constraints (Design Requirements)
        // ============================================================

        constraint parallel_execution {
            doc /* Workers must execute in parallel (scatter-gather) */
            // Implementation: ThreadPoolExecutor or Temporal parallel Activities
        }

        constraint quorum_required {
            doc /* Must analyze consensus across workers */
            consensus_threshold >= 0.5
        }

        constraint cognitive_load_management {
            doc /* Output must be scannable in <10 minutes */
            // Implementation: Swarmlord digest format
        }
    }

    // ================================================================
    // Agent Definitions
    // ================================================================

    part def InterpreterAgent {
        doc /*
            SENSE phase: Extract mission structure from user input.

            Role: ANALYTICAL and PRECISE - extracts intent without speculation
            Temperature: Low (0.3) for precision
            Model: General-purpose LLM (no specialized reasoning needed)
        */

        // Model configuration
        attribute model : String = "openai/gpt-oss-120b";
        attribute temperature : Real = 0.3;
        attribute max_tokens : Integer = 2000;

        // System prompt (design philosophy)
        attribute system_prompt : String = """
            You are an ANALYTICAL and PRECISE mission interpreter.
            Your role is to extract structured information from user input.

            You do NOT:
            - Speculate about answers
            - Provide research
            - Generate strategies

            You DO:
            - Extract mission_intent clearly
            - Identify constraints
            - Create orchestration_prompt for workers

            Output format: JSON with {mission_intent, constraints, orchestration_prompt}
        """;

        // Input/Output ports
        port input : UserInput {
            doc /* Natural language mission request */
        }

        port output : MissionStructure {
            doc /* Structured mission data for workers */
            attribute mission_intent : String;
            attribute constraints : String;
            attribute orchestration_prompt : String;
        }

        // Design constraints
        constraint precision {
            doc /* Temperature must be low for consistent extraction */
            temperature < 0.5
        }

        constraint deterministic {
            doc /* Same input should yield similar outputs */
            // Rationale: Orchestration consistency across reruns
        }
    }

    part def ResearcherAgent {
        doc /*
            ACT phase: Execute research with internal PREY loop.

            Role: CREATIVE EXPERT - explores diverse perspectives
            Temperature: High (0.8) for diversity across workers
            Model: General-purpose LLM (future: research-optimized model)

            Internal PREY loop:
            1. SENSE: Read orchestration prompt
            2. REACT: Choose research angle/perspective
            3. ACT: Generate research content
            4. YIELD: Format structured response
        */

        // Model configuration
        attribute model : String = "openai/gpt-oss-120b";
        attribute temperature : Real = 0.8;
        attribute max_tokens : Integer = 1500;

        // System prompt
        attribute system_prompt : String = """
            You are a CREATIVE EXPERT researcher.

            Run internal PREY loop:
            1. SENSE: Read the orchestration prompt carefully
            2. REACT: Decide your research angle/perspective
            3. ACT: Execute research from your chosen angle
            4. YIELD: Format and return findings (300-500 words)

            You provide DIVERSE perspectives - your research angle may differ from other workers.
            Include evidence, examples, and concrete recommendations.
        """;

        // Input/Output ports
        port input : OrchestrationPrompt {
            doc /* Research instructions from interpreter */
        }

        port output : ResearchResponse {
            doc /* 300-500 word research findings */
            attribute content : String;
            attribute worker_id : Integer;
        }

        // Design constraints
        constraint diversity {
            doc /* Temperature must be high for diverse perspectives */
            temperature > 0.5
        }

        constraint substantive_research {
            doc /* Output must be substantive (not trivial) */
            // Rationale: Quorum analysis requires real content
            // Implementation: Check word count > 200
        }

        constraint parallel_execution {
            doc /* Workers must execute independently (no shared state) */
            // Rationale: True scatter-gather requires independence
        }
    }

    part def ValidatorAgent {
        doc /*
            YIELD phase (part 1): Quorum analysis + hallucination detection.

            Role: OBJECTIVE ANALYST - identifies consensus without bias
            Temperature: Very low (0.1) for objectivity
            Model: General-purpose LLM (future: fact-checking model)
        */

        // Model configuration
        attribute model : String = "openai/gpt-oss-120b";
        attribute temperature : Real = 0.1;
        attribute max_tokens : Integer = 3000;

        // System prompts (multiple analysis types)
        attribute system_prompts : Map<String, String> = {
            "quorum": """
                You are an OBJECTIVE analyst identifying consensus themes.

                Do NOT:
                - Invent themes that aren't present
                - Force consensus where there is genuine disagreement

                DO:
                - Identify themes where multiple workers independently agree
                - Count worker agreement per theme (e.g., 4/5 workers)
                - Classify consensus strength (HIGH: 80%+, MEDIUM: 50-79%, LOW: <50%)
            """,

            "hallucination": """
                You are a CRITICAL reviewer identifying fabricated content.

                Common hallucinations:
                - Non-existent software versions (e.g., Istio 1.22 when latest is 1.18)
                - Fake documents/reports (e.g., "CNCF 2025 whitepaper")
                - Invented statistics (e.g., "87% of enterprises...")
                - Non-existent features (e.g., "Kubernetes 1.30 auto-healing")

                For each worker, flag suspicious items with severity (HIGH/MEDIUM/LOW).
            """
        };

        // Input/Output ports
        port input : ResearchResults {
            doc /* Array of research responses from all workers */
            attribute responses[*] : ResearchResponse;
        }

        port output : ValidationReport {
            doc /* Quorum summary + hallucination analysis */
            attribute quorum_summary : String;
            attribute consensus_themes : Integer;  // Count
            attribute hallucinations : String;
        }

        // Design constraints
        constraint objectivity {
            doc /* Temperature must be very low for unbiased analysis */
            temperature < 0.2
        }

        constraint comprehensive_analysis {
            doc /* Must analyze ALL workers (no sampling) */
            // Rationale: Missing worker could contain critical info
        }
    }

    part def SynthesizerAgent {
        doc /*
            YIELD phase (part 2): BLUF extraction + executive summary.

            Role: STRUCTURED COMMUNICATOR - manages cognitive load
            Temperature: Medium (0.5) for structure + clarity
            Model: General-purpose LLM (future: summarization-optimized model)
        */

        // Model configuration
        attribute model : String = "openai/gpt-oss-120b";
        attribute temperature : Real = 0.5;
        attribute max_tokens : Integer = 2500;

        // System prompts
        attribute system_prompts : Map<String, String> = {
            "bluf": """
                You are a STRUCTURED analyst managing cognitive load.

                Extract BLUF (Bottom Line Up Front):
                - consensus_level: HIGH | MEDIUM | LOW
                - key_findings: Array of 3-7 actionable insights
                - contradictions: Array of disagreements between workers
                - confidence_score: 0-100 percentage

                Do NOT return empty arrays. If no contradictions, explain why consensus is strong.
            """,

            "executive": """
                You are a CONCISE communicator focused on business impact.

                Create executive summary (2-3 paragraphs):
                1. What the research found (key themes)
                2. What it means (business/technical implications)
                3. What to do (next actions with confidence level)

                Target audience: Decision-makers who need actionable takeaways.
            """
        };

        // Input/Output ports
        port input : AnalysisData {
            doc /* Quorum summary, hallucination report, research responses */
        }

        port output : Digest {
            doc /* Complete Swarmlord digest */
            attribute bluf : JSON;
            attribute executive_summary : String;
            attribute digest_markdown : String;
        }

        // Design constraints
        constraint balanced_creativity {
            doc /* Temperature balanced for structure + clarity */
            0.3 < temperature < 0.7
        }

        constraint cognitive_load_limit {
            doc /* BLUF must be scannable in 30 seconds */
            // Implementation: Structure as decision matrix
        }

        constraint stakeholder_ready {
            doc /* Executive summary must be non-technical (when possible) */
            // Rationale: Decision-makers may lack deep technical context
        }
    }

    // ================================================================
    // State Definition (LangGraph StateGraph)
    // ================================================================

    part def PREYState {
        doc /* State passed through PREY loop nodes */

        // Input
        attribute user_input : String;
        attribute num_workers : Integer;

        // SENSE outputs
        attribute mission_intent : String;
        attribute constraints : String;
        attribute orchestration_prompt : String;
        attribute mission_id : Integer;

        // ACT outputs
        attribute research_results[*] : String;

        // YIELD outputs
        attribute quorum_summary : String;
        attribute hallucinations : String;
        attribute bluf : JSON;
        attribute executive_summary : String;
        attribute digest : String;

        // Metadata
        attribute start_time : Real;
        attribute end_time : Real;
    }
}
```

---

## Autogeneration Script (Future Implementation)

### Script: `scripts/generate_orchestrator.py`

```python
#!/usr/bin/env python3
"""
Generate orchestrator code from HFO_SSOT.sysml definition.

Usage:
    python scripts/generate_orchestrator.py --ssot HFO_SSOT.sysml --output hfo_swarm/

Generates:
    - prey_orchestrator.py (agent classes + workflow)
    - schema.sql (database schema)
    - run_swarm.py (CLI entrypoint)
    - tests/test_prey_orchestrator.py (unit tests)
"""

import argparse
from pathlib import Path
from typing import Dict, List, Any

# Note: Requires SysML v2 parser (future dependency)
# from sysml_parser import parse_sysml


def parse_ssot(ssot_file: str) -> Dict[str, Any]:
    """
    Parse HFO_SSOT.sysml and extract orchestrator definition.

    Returns:
        {
            "orchestrator": {
                "name": "PREYOrchestrator",
                "agents": [...],
                "flows": [...],
                "config": {...}
            },
            "agents": {
                "InterpreterAgent": {...},
                "ResearcherAgent": {...},
                ...
            },
            "state": {...}
        }
    """
    # TODO: Implement SysML v2 parsing
    # For now, return mock structure
    pass


def generate_agent_class(agent_def: Dict[str, Any]) -> str:
    """
    Generate Python agent class from SSOT definition.

    Example:
        agent_def = {
            "name": "InterpreterAgent",
            "model": "openai/gpt-oss-120b",
            "temperature": 0.3,
            "system_prompt": "You are...",
            "max_tokens": 2000
        }

    Returns Python code:
        class InterpreterAgent(BaseAgent):
            SYSTEM_PROMPTS = {"interpret": "You are..."}

            def __init__(self):
                super().__init__(
                    model_name="openai/gpt-oss-120b",
                    temperature=0.3,
                    max_tokens=2000
                )
    """
    name = agent_def["name"]
    model = agent_def["model"]
    temp = agent_def["temperature"]
    max_tokens = agent_def.get("max_tokens", 2000)

    # Extract system prompts
    if "system_prompts" in agent_def:
        # Multiple prompts (e.g., ValidatorAgent)
        prompts_dict = agent_def["system_prompts"]
        prompts_str = "{\n"
        for key, value in prompts_dict.items():
            prompts_str += f'        "{key}": """{value}""",\n'
        prompts_str += "    }"
    else:
        # Single prompt
        prompt = agent_def["system_prompt"]
        prompts_dict = {name.lower(): prompt}
        prompts_str = f'{{\n        "{name.lower()}": """{prompt}"""\n    }}'

    # Generate class code
    code = f'''
class {name}(BaseAgent):
    """
    {agent_def.get("doc", f"{name} agent")}
    """

    SYSTEM_PROMPTS = {prompts_str}

    def __init__(self):
        super().__init__(
            model_name=os.getenv("MODEL_{name.upper()}", "{model}"),
            temperature={temp},
            max_tokens={max_tokens}
        )
'''

    return code


def generate_langgraph_workflow(orchestrator_def: Dict[str, Any]) -> str:
    """
    Generate LangGraph workflow from SSOT flows.

    Example:
        flows = [
            {"from": "interpreter", "to": "researchers"},
            {"from": "researchers", "to": "validator"},
            {"from": "validator", "to": "synthesizer"}
        ]

    Returns Python code:
        workflow = StateGraph(PREYState)
        workflow.add_node("sense", self._sense_node)
        workflow.add_node("act", self._act_node)
        workflow.add_node("yield_phase", self._yield_node)
        workflow.set_entry_point("sense")
        workflow.add_edge("sense", "act")
        workflow.add_edge("act", "yield_phase")
        workflow.add_edge("yield_phase", END)
    """
    # TODO: Implement flow parsing
    pass


def generate_database_schema(orchestrator_def: Dict[str, Any]) -> str:
    """
    Generate PostgreSQL schema from SSOT state definition.

    Returns SQL:
        CREATE TABLE missions (...);
        CREATE TABLE researchers (...);
        CREATE TABLE analysis (...);
    """
    # TODO: Implement schema generation
    pass


def generate_cli_entrypoint(orchestrator_def: Dict[str, Any]) -> str:
    """
    Generate CLI entrypoint (run_swarm.py).

    Returns Python code:
        if __name__ == "__main__":
            parser = argparse.ArgumentParser()
            parser.add_argument("--mission", required=True)
            ...
            orchestrator = PREYOrchestrator()
            result = orchestrator.execute(args.mission, num_workers=args.workers)
    """
    # TODO: Implement CLI generation
    pass


def generate_tests(agents: List[Dict[str, Any]]) -> str:
    """
    Generate unit tests for each agent.

    Returns Python code:
        def test_interpreter_agent():
            agent = InterpreterAgent()
            result = agent.interpret_mission("Test mission")
            assert "mission_intent" in result
    """
    # TODO: Implement test generation
    pass


def main():
    parser = argparse.ArgumentParser(description="Generate orchestrator from SSOT")
    parser.add_argument("--ssot", required=True, help="Path to HFO_SSOT.sysml")
    parser.add_argument("--output", required=True, help="Output directory")
    args = parser.parse_args()

    # Parse SSOT
    ssot = parse_ssot(args.ssot)

    # Generate components
    agents_code = "\n\n".join([
        generate_agent_class(agent)
        for agent in ssot["agents"].values()
    ])

    workflow_code = generate_langgraph_workflow(ssot["orchestrator"])
    schema_sql = generate_database_schema(ssot["orchestrator"])
    cli_code = generate_cli_entrypoint(ssot["orchestrator"])
    tests_code = generate_tests(list(ssot["agents"].values()))

    # Write files
    output_dir = Path(args.output)
    output_dir.mkdir(exist_ok=True)

    # Combine into orchestrator.py
    orchestrator_code = f'''
"""
Auto-generated from HFO_SSOT.sysml
DO NOT EDIT MANUALLY - regenerate with scripts/generate_orchestrator.py
"""

import os
from typing import Dict, Any, List
from langgraph.graph import StateGraph, END
# ... other imports

{agents_code}

{workflow_code}
'''

    (output_dir / "prey_orchestrator.py").write_text(orchestrator_code)
    (output_dir / "schema.sql").write_text(schema_sql)
    (output_dir / "run_swarm.py").write_text(cli_code)
    (output_dir.parent / "tests" / "test_prey_orchestrator.py").write_text(tests_code)

    print(f"✅ Generated orchestrator in {output_dir}")
    print(f"   - prey_orchestrator.py ({len(orchestrator_code)} bytes)")
    print(f"   - schema.sql ({len(schema_sql)} bytes)")
    print(f"   - run_swarm.py ({len(cli_code)} bytes)")
    print(f"   - tests/test_prey_orchestrator.py ({len(tests_code)} bytes)")


if __name__ == "__main__":
    main()
```

---

## Migration Path: Gen 29 → Gen 30

### Phase 1: SSOT Definition (Gen 30)
1. Create `HFO_SSOT.sysml` with PREYOrchestrator definition (above)
2. Validate SSOT syntax with SysML v2 tools
3. Document design decisions in SSOT (constraint rationales)

### Phase 2: Parser Development (Gen 30)
1. Build SysML v2 parser (`scripts/sysml_parser.py`)
2. Extract agent definitions, flows, state structure
3. Test parser on PREY example

### Phase 3: Generator Development (Gen 30-31)
1. Implement `generate_agent_class()` (simplest: templates + string formatting)
2. Implement `generate_langgraph_workflow()` (map flows to graph edges)
3. Implement `generate_database_schema()` (map state to SQL tables)
4. Implement `generate_cli_entrypoint()` (argparse + orchestrator invocation)
5. Implement `generate_tests()` (basic smoke tests per agent)

### Phase 4: Validation (Gen 31)
1. Regenerate current PREY orchestrator from SSOT
2. Compare generated code to hand-written Gen 29 code
3. Run tests on generated code
4. Validate digest output matches Gen 29

### Phase 5: Evolution (Gen 32+)
1. Define new swarm type in SSOT (e.g., TreeSearchOrchestrator)
2. Regenerate with same script
3. Compare effort: Gen 29 (760 lines manual) vs Gen 32 (50 lines SSOT + autogen)

---

## Benefits of SSOT-Driven Approach

### 1. Design Documentation
**Before (Gen 29)**:
```python
temperature=0.3  # Why? Unknown (lost in git history)
```

**After (Gen 30+)**:
```sysml
attribute temperature : Real = 0.3;

constraint precision {
    doc /* Temperature must be low for consistent extraction */
    temperature < 0.5
}
```

**Impact**: Design rationale preserved forever in SSOT.

### 2. Rapid Iteration
**Before**: Change temperature 0.3 → 0.4 requires:
- Find all places where InterpreterAgent is instantiated
- Update each manually
- Risk inconsistency (some 0.3, some 0.4)

**After**: Change in SSOT, regenerate (1 command)

### 3. Model Diversity
**Before**: One model for all roles
```python
MODEL_RESEARCHER = "openai/gpt-oss-120b"  # Used everywhere
```

**After**: Model per role in SSOT
```sysml
part def ResearcherAgent {
    attribute model : String = "anthropic/claude-3.5-sonnet";  // Creative research
}

part def ValidatorAgent {
    attribute model : String = "openai/gpt-4o";  // Objective validation
}
```

### 4. Pattern Library
**Future**: Reusable SSOT modules

```sysml
import PREYPatterns::ScatterGatherOrchestrator;
import PREYPatterns::MapReduceOrchestrator;
import PREYPatterns::TreeSearchOrchestrator;

part mySwarm : ScatterGatherOrchestrator {
    // Override config
    attribute num_workers = 20;
}
```

### 5. Constraint Validation
**SSOT can enforce design rules**:

```sysml
constraint temperature_diversity {
    doc /* Workers must have higher temperature than interpreter */
    researchers.temperature > interpreter.temperature
}

constraint quorum_feasible {
    doc /* Consensus threshold must allow for disagreement */
    consensus_threshold < 1.0
}
```

**Generator validates** before code generation (catch design errors early).

---

## Example: Generating New Swarm Type (Gen 32+)

### User Request
"Create a map-reduce swarm for long documents: chunk into 10 parts, map (summarize each), reduce (synthesize summaries)."

### SSOT Definition (50 lines)

```sysml
part def MapReduceOrchestrator {
    part chunker : ChunkerAgent;
    part mappers[1..*] : MapperAgent;
    part reducer : ReducerAgent;

    flow chunk : chunker.output -> mappers.input;
    flow map : mappers.output -> reducer.input;

    attribute num_chunks : Integer = 10;
}

part def ChunkerAgent {
    attribute model : String = "openai/gpt-oss-120b";
    attribute temperature : Real = 0.1;  // Deterministic chunking
    attribute system_prompt : String = "Split document into N equal chunks...";
}

part def MapperAgent {
    attribute model : String = "openai/gpt-oss-120b";
    attribute temperature : Real = 0.3;  // Focused summarization
    attribute system_prompt : String = "Summarize this chunk...";
}

part def ReducerAgent {
    attribute model : String = "anthropic/claude-3.5-sonnet";
    attribute temperature : Real = 0.5;  // Creative synthesis
    attribute system_prompt : String = "Synthesize these summaries...";
}
```

### Autogeneration
```bash
python scripts/generate_orchestrator.py \
    --ssot HFO_SSOT.sysml \
    --output hfo_swarm/mapreduce_orchestrator.py
```

**Output**: 600-line implementation (agent classes, workflow, CLI, tests)

**Manual effort**: 50 lines SSOT (vs 760 lines manual coding in Gen 29)

**Time savings**: 90%+

---

## Summary

### Current State (Gen 29)
- ✅ Working PREY orchestrator (760 lines)
- ❌ Design decisions buried in code
- ❌ Temperature rationales undocumented
- ❌ No pattern reuse (each swarm type is full rewrite)

### Target State (Gen 30+)
- ✅ SSOT defines all swarm patterns
- ✅ Design rationale preserved in constraints
- ✅ One-command regeneration
- ✅ Pattern library for reuse
- ✅ Constraint validation catches design errors early

### Next Steps (Gen 30 Roadmap)
1. Create `HFO_SSOT.sysml` with PREY definition
2. Build SysML v2 parser
3. Implement code generator (start with agent classes)
4. Validate by regenerating Gen 29 PREY orchestrator
5. Document pattern library (scatter-gather, map-reduce, tree-search)
