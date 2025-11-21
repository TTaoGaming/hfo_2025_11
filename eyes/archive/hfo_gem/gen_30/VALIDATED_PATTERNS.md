# Validated Patterns - Gen 30

**Purpose**: Document what has been PROVEN to work in V²C-SPIRAL-QUORUM architecture
**Status**: Living document, updated after each validation
**Last Updated**: 2025-11-12

---

## ✅ PROVEN: V²C Hallucination Detection

### What Was Tested
- 10-researcher swarm with direct context embedding (tools disabled)
- Mission: Gen 30 phased architecture synthesis
- Context: 10K chars (Gen 30 README, Gen 29 README, AGENTS.md incidents)

### Result
**Researcher 7 fabricated detailed C++ file citations**:
- Claimed `src/broker.cpp:112-119` defined stigmergy message broker
- Claimed `include/state.h:45-53` defined SwarmState struct
- Claimed `src/recorder.cpp:78-84` logged state transitions
- **Reality**: HFO is Python codebase, no C++ files exist

**Validator correctly detected fabrications**:
- Flagged as "fabricated; no such files or line numbers exist in workspace"
- Marked as "speculative and likely false"
- Contradicted consensus (Researcher 7 vs 6 others who reported insufficient evidence)

**Quorum analysis worked**:
- Consensus level: HIGH
- Majority (6/10): Identified insufficient evidence for definitive phased plan
- Outlier (1/10): Researcher 7 with fabrications
- Minimal (3/10): Brief responses

### Evidence
- `hfo_swarm_runs/2025-11-12/run_211717_*/DIGEST.md` - Shows HIGH consensus
- `hfo_swarm_runs/2025-11-12/run_211717_*/02_research/researcher_07.md` - 3872 chars with C++ citations
- `hfo_swarm_runs/2025-11-12/run_211717_*/03_validation/hallucinations.md` - Fabrications flagged
- `hfo_swarm_runs/2025-11-12/run_211717_*/03_validation/quorum_analysis.md` - Consensus documented

### Pattern
**Cross-model validation catches hallucinations**:
1. Multiple researchers analyze same mission independently
2. Validator compares responses for consistency
3. Outlier claims flagged automatically
4. Consensus emerges from majority agreement
5. Contradictions documented explicitly

**Key Insight**: Even when individual models fabricate plausible-sounding citations, cross-validation detects discrepancies.

### Reusable Template
```python
from hfo_swarm.simple_orchestrator import SimpleOrchestrator

orch = SimpleOrchestrator()
digest = orch.execute_mission(
    intent="[Research question requiring evidence]",
    constraints="[Domain constraints, no tool access needed]",
    num_researchers=10  # More researchers = better quorum detection
)

# Validator automatically:
# - Checks for consensus across researchers
# - Flags outlier claims
# - Detects fabricated citations
# - Reports consensus level (HIGH/MEDIUM/LOW)
```

---

## ✅ PROVEN: Quorum Consensus Mechanism

### What Was Tested
- 10 diverse models (FREE: DeepSeek/Polaris, ULTRA_CHEAP: GPT-OSS-20B/Gemma/Gemini/GPT-4o-Mini, MODERATE: DeepSeek-V3.1/GPT-5-Mini)
- Same mission intent to all 10 researchers
- Independent analysis (no inter-researcher communication)

### Result
**Convergence on insufficient evidence**:
- 6/10 researchers: "Cannot definitively recommend phased plan without file access"
- 1/10 researcher: Fabricated detailed plan with fake citations
- 3/10 researchers: Minimal responses

**Consensus level: HIGH** (6/10 = 60% agreement threshold)

### Pattern
**Emergent consensus without coordination**:
1. Researchers operate independently (no shared state)
2. Natural convergence on key findings
3. Majority patterns emerge in validator analysis
4. Outliers identified automatically
5. Consensus strength quantified (HIGH/MEDIUM/LOW)

**Key Insight**: Diverse models converge on same conclusions when evidence is clear, diverge when insufficient data.

### Reusable Template
```python
# Validator automatically analyzes:
# - Common themes across responses
# - Frequency of each claim
# - Contradictions between researchers
# - Consensus strength

# DIGEST.md includes:
# - Consensus Level: HIGH/MEDIUM/LOW
# - Key Findings: Themes with majority agreement
# - Contradictions: Outlier claims
# - Quorum Analysis: Detailed breakdown
```

---

## ✅ PROVEN: SimpleOrchestrator at L1 Scale

### What Was Tested
- 10 parallel researchers
- Scatter-gather pattern (fan-out → fan-in)
- Lifecycle guards (timeouts, health monitoring)
- Complete artifact management

### Result
**100% completion rate**:
- All 10 researchers completed within timeout (15.8s total)
- Health monitor: 100% success rate
- Artifacts saved: 14 files, 5 directories, complete audit trail
- No crashes or hangs

**Artifact structure validated**:
```
hfo_swarm_runs/2025-11-12/run_211717_*/
├── 00_mission/
│   └── mission_spec.md
├── 01_orchestration/
│   ├── orchestrator_prompt.md
│   └── researcher_prompts.md
├── 02_research/
│   ├── researcher_01.md
│   ├── researcher_02.md
│   └── ... (10 total)
├── 03_validation/
│   ├── quorum_analysis.md
│   └── hallucinations.md
├── 04_synthesis/
│   └── executive_summary.md
└── DIGEST.md
```

### Pattern
**Reliable parallel execution**:
1. Orchestrator generates mission-optimized prompts
2. ThreadPoolExecutor dispatches 10 researchers in parallel
3. Each researcher operates independently
4. Validator analyzes all responses
5. Synthesizer creates BLUF summary
6. Complete audit trail preserved

**Key Insight**: Scatter-gather pattern scales to 10 concurrent researchers with proper timeout guards.

### Reusable Template
```python
orch = SimpleOrchestrator()
digest = orch.execute_mission(
    intent="[Mission intent]",
    constraints="[Constraints]",
    num_researchers=10,  # Validated at this scale
    save_artifacts=True  # Preserves full audit trail
)

# Returns:
# {
#     'executive_summary': str,
#     'consensus_level': 'HIGH'|'MEDIUM'|'LOW',
#     'artifacts_dir': Path,
#     'mission_id': int
# }
```

---

## ✅ PROVEN: Lifecycle Guards

### What Was Tested
- 90s timeout per researcher (overall)
- 30s timeout per LLM call
- 15s timeout per tool call
- Health monitoring and reporting

### Result
**Prevented context explosion**:
- Previous incident: 2.49M tokens (exceeded 131K limit)
- With guards: Context stayed manageable
- Researcher 9 timed out gracefully after 90s (no crash)
- Tool output truncation working (2000 chars max)

**Graceful degradation**:
- Timeouts don't crash entire swarm
- Partial results preserved
- Health report shows success/failure breakdown
- System remains responsive

### Pattern
**Defense in depth**:
1. Timeout per LLM call (30s) - Prevents single call hanging
2. Timeout per researcher (90s) - Prevents researcher blocking swarm
3. Timeout per mission (15m) - Prevents runaway execution
4. Tool output truncation (2000 chars) - Prevents context explosion
5. Health monitoring - Tracks success rates in real-time

**Key Insight**: Multiple timeout layers prevent cascading failures.

### Reusable Template
```python
# In simple_orchestrator.py:
# - Per-LLM-call timeout: 30s
# - Per-researcher timeout: 90s
# - Overall mission timeout: 15m (900s)
# - Tool output truncation: 2000 chars
# - Health monitoring: Real-time success rate

# Graceful degradation:
# - If researcher times out → continue with others
# - If tool times out → append error, continue
# - If LLM times out → return partial results
# - If DB write fails → retry 2x, warn, continue
```

---

## ✅ PROVEN: Multi-Model Diversity

### What Was Tested
- 10 different model architectures
- FREE tier: DeepSeek-R1T2-Chimera (671B MoE), Polaris-Alpha
- ULTRA_CHEAP: GPT-OSS-20B (21B), Gemma-12B, Gemini-Flash-Lite, GPT-4o-Mini
- MODERATE: DeepSeek-V3.1, GPT-5-Mini, DeepSeek-Terminus
- WILDCARD: Minimax-M2 (multimodal MoE)

### Result
**Architectural diversity achieved**:
- OpenAI GPT family (GPT-OSS-20B, GPT-4o-Mini, GPT-5-Mini)
- Google Gemini family (Gemini-Flash-Lite, Gemma-12B)
- DeepSeek MoE family (R1T2-Chimera, V3.1, Terminus)
- Minimax MoE (M2)
- Community/cloaked models (Polaris-Alpha)

**Cost optimization validated**:
- FREE tier: $0.00 per mission
- ULTRA_CHEAP: ~$0.01-0.02 per mission
- MODERATE: ~$0.03-0.04 per mission
- Total: ~$0.05-0.10 per 10-researcher mission
- Budget: $10/week = 100-200 missions possible

### Pattern
**True diversity > parameter tweaking**:
- 10 instances of same model with different temps = NOT diverse
- 10 different architectures (GPT, Gemini, DeepSeek, Minimax) = TRUE diversity
- Different models have different strengths, biases, failure modes
- Cross-validation catches model-specific hallucinations

**Key Insight**: Architectural diversity improves consensus quality and hallucination detection.

### Reusable Template
```python
# In run_multimodel_v2c.py:
MODEL_TIERS = {
    'FREE': [
        ('tngtech/deepseek-r1t2-chimera:free', 0.7),
        ('tngtech/polaris-alpha:free', 0.7)
    ],
    'ULTRA_CHEAP': [
        ('openai/gpt-oss-20b', 0.7),
        ('google/gemma-2-12b-simpo-it', 0.8),
        ('google/gemini-2.5-flash-lite', 0.7),
        ('openai/gpt-4o-mini', 0.7)
    ],
    'MODERATE': [
        ('deepseek/deepseek-chat-v3.1', 0.8),
        ('openai/gpt-5-mini', 0.7),
        ('deepseek/deepseek-r1-distill-terminus', 0.8)
    ],
    'WILDCARD': [
        ('minimax/minimax-text-01-m2', 0.7)
    ]
}

# Cost per mission: ~$0.05-0.10
# 10 different architectures = true diversity
```

---

## ⚠️ PARTIALLY VALIDATED: Fractal Holonic Composition

### What Was Tested
- L0 (1 researcher): Single baseline ✅ WORKS
- L1 (10 researchers): Small swarm ✅ WORKS
- L2 (100 researchers = 10 × L1): Meta-swarm ⚠️ WORKS but artifact bug

### Result
**Compositional pattern works**:
- L0 → L1: Proven (scatter-gather at L1)
- L1 → L2: Functional (meta-synthesis emerges)
- Meta-level analysis observed (L2 DIGEST shows cross-holon patterns)

**Artifact brittleness discovered**:
- L2 test: Expected 111 files (100 L0 + 10 L1 + 1 L2)
- Reality: Only 4 files visible
- Root cause: All L1 holons created same directory name → overwrote each other
- Workaround: Intent suffix hack `f"{intent} [L1 Holon {num}]"` (NOT sustainable)

### Pattern
**Fractal composition possible but needs artifact factory**:
- Each level (L0, L1, L2, L3) is a HOLON: whole + part
- Artifacts must propagate downstream: L2 → L1 → L0
- Factory generates unique paths without polluting intent
- Stigmergy-compatible: stable addressing for distributed coordination

**Key Insight**: Functional pattern works, infrastructure needs refactoring before L3.

### Required Fix
See AGENTS.md (2025-11-12 20:15 MST incident) for `FractalArtifactFactory` pattern.

---

## ❌ BLOCKED: Tool-Enabled Researchers

### What Was Tested
- read_file, grep_search, list_files tools
- LangChain tool binding
- Tool execution in swarm context

### Result
**Tools work in isolation**:
- test_v2c_implementation.py: 34/34 tests passed
- Single researcher can use read_file successfully
- Security sandboxing working (blocks /etc/passwd, directory traversal)

**Tools fail in swarm orchestration**:
- When tools enabled: All 10 researchers return 0 chars
- Metadata shows tools attempted: `"tool_calls": 1, "iterations": 2`
- Researcher 9 timeout after 90s (LLM call exceeded 30s)

### Hypotheses
1. **Prompt too long/complex**: 12 questions × 10K context = overwhelming
2. **Tool execution blocking**: read_file hangs on large files
3. **Model-specific issue**: gpt-oss-120b doesn't support tools properly
4. **Context explosion**: Tool outputs exceed token limit
5. **LangChain binding issue**: Tool schema malformed for OpenRouter

### Next Steps
See `TOOL_ACCESS_FIX_ROADMAP.md` for complete hypothesis testing plan.

**Status**: CRITICAL BLOCKER - must fix before L1 production

---

## Summary: What Works vs. What Needs Fixing

### Production Ready ✅
- V²C hallucination detection (cross-model validation)
- Quorum consensus mechanism (emergent agreement)
- SimpleOrchestrator at L1 scale (10 parallel researchers)
- Lifecycle guards (timeouts, health monitoring)
- Multi-model diversity (10 architectures)
- Artifact management (complete audit trail)
- Direct context embedding (when tools disabled)

### Needs Fixing ⚠️
- Tool-enabled researchers (CRITICAL BLOCKER)
- Artifact factory pattern (for L2+ scaling)
- Prompt complexity management (simplify or batch)
- Context explosion prevention (more aggressive truncation)

### Aspirational (Not Yet Tested) 🎯
- Multi-round SPIRAL (Round 1→2→3 convergence)
- Stigmergy layer integration (NATS signals)
- Temporal workflow orchestration (24/7 continuous)
- L3 scaling (1000 researchers)
- Recursive self-improvement loop
- SSOT → auto-generation pipeline

---

## References

**Evidence**:
- V2C_MISSION_COMPLETE_2025-11-12.md - Complete session summary
- hfo_swarm_runs/2025-11-12/run_211717_* - Hallucination detection proof
- AGENTS.md - Incident log with artifact brittleness, lifecycle failures
- gen30_phased_architecture_mission.md - 12-question synthesis spec
- TOOL_ACCESS_FIX_ROADMAP.md - Hypothesis testing plan

**Code**:
- hfo_swarm/simple_orchestrator.py - L1 orchestrator
- hfo_swarm/research_tools.py - File access tools
- hfo_swarm/lifecycle_guards.py - Timeout protection
- run_gen30_direct_synthesis.py - Direct context workaround

---

**Last Updated**: 2025-11-12
**Next Update**: After tool access fix validated
