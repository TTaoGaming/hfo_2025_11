---
hexagon:
  ontos:
    id: c820e777-e3ec-448a-8015-64a97b385e2b
    type: md
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T11:07:35.701729Z'
    generation: 51
  topos:
    address: eyes/archive/hfo_gem/gen_30/TOOL_ACCESS_FIX_ROADMAP.md
    links: []
  telos:
    viral_factor: 0.0
    meme: TOOL_ACCESS_FIX_ROADMAP.md
---

# Tool Access Fix Roadmap

**Status**: CRITICAL BLOCKER
**Priority**: Phase 0 (Foundation) - Must fix before L1 production
**Created**: 2025-11-12
**Last Updated**: 2025-11-12

---

## Problem Statement

**Symptom**: When `DISABLE_RESEARCHER_TOOLS='0'`, researchers return 0-character responses despite metadata showing `"tool_calls": 1, "iterations": 2`.

**Impact**: Blocks full V²C-SPIRAL-QUORUM capability - researchers cannot:
- Read actual files for evidence-based validation
- Cross-validate citations against ground truth
- Run iterative PREY loops with file access
- Execute multi-round refinement with real data

**Evidence**:
- `hfo_swarm_runs/2025-11-12/run_211319_*/02_research/` - All 10 researchers returned 0-1728 chars (mostly 0)
- Metadata shows tools were attempted: `"tool_calls": 1, "iterations": 2`
- Researcher 9 timeout after 90s (LLM call exceeded 30s at iteration 2)
- Direct context workaround (tools disabled) produced partial results

---

## Hypotheses (In Priority Order)

### Hypothesis 1: Prompt Too Long/Complex
**Cause**: 12 questions × detailed context = massive prompt → model overwhelmed → refuses to generate

**Evidence**:
- gen30_phased_architecture_mission.md has 11,089 chars
- Additional context: 10K chars (Gen 30 README 3000, Gen 29 README 2000, AGENTS.md 5000)
- Total context: ~21K chars before tool outputs
- When context reduced to 5 questions (run_gen30_direct_synthesis.py), 4/10 researchers responded

**Test**:
1. Create minimal intent: "Read hfo_gem/gen_30/README.md lines 1-50 and summarize V²C vision in 100 words"
2. Run with 3 researchers, tools enabled
3. Expected: All 3 researchers use read_file and return substantive responses
4. If fails: Hypothesis disproven, move to Hypothesis 2

**Fix** (if proven):
- Batch questions: 3 separate missions × 4 questions each
- Simplify constraints: Remove lengthy context, rely on tool access
- Progressive elaboration: Round 1 (simple) → Round 2 (refined) → Round 3 (synthesized)

---

### Hypothesis 2: Tool Execution Blocking/Hanging
**Cause**: read_file/grep_search hangs on large files or filesystem issues → timeout → empty response

**Evidence**:
- Lifecycle guards show 15s timeout on tool calls
- Some Gen 30 files are large (AGENTS.md = 67K chars)
- No logging currently tracks tool execution duration

**Test**:
1. Add debug logging to research_tools.py: timestamp before/after each tool call
2. Run minimal test with 1 researcher
3. Monitor logs for: "Tool read_file started", "Tool read_file completed in X.Xs"
4. Expected: Tool completes in <1s for small files
5. If hangs: Hypothesis proven

**Fix** (if proven):
- Add timeout per tool invocation (not just per LLM call)
- Implement streaming/chunked file reading for large files
- Cache tool results to avoid repeated filesystem access
- Implement circuit breaker: if tool hangs 3x, disable and continue

---

### Hypothesis 3: Model-Specific Tool Handling Issue
**Cause**: openai/gpt-oss-120b doesn't properly handle LangChain tool calling → returns empty

**Evidence**:
- Different models have different tool support (FREE tier models failed with 404 "No endpoints found that support tool use")
- gpt-oss-120b is cheap ($0.03/M) but may have limited tool support
- No testing with known-good model like gpt-4o-mini

**Test**:
1. Modify simple_orchestrator.py to use gpt-4o-mini temporarily
2. Run same minimal test (3 researchers, read_file task)
3. Expected: gpt-4o-mini successfully uses tools and returns responses
4. If succeeds: Hypothesis proven

**Fix** (if proven):
- Use gpt-4o-mini or gpt-3.5-turbo for tool-enabled researchers (cost: $0.15/M vs $0.03/M)
- Document model compatibility matrix: FREE (no tools) → ULTRA_CHEAP (limited tools) → MODERATE (full tools)
- Implement graceful degradation: try with tools, if empty response → retry with direct context

---

### Hypothesis 4: Context Explosion from Tool Outputs
**Cause**: Tool results appended to message history → context grows → exceeds limit → empty response

**Evidence**:
- 2025-11-12 16:35 MST incident: Context explosion to 2.49M tokens (exceeded 131K limit)
- Tool output truncation implemented (2000 chars max) but may be insufficient
- Gen 30 README.md = 18,737 chars, AGENTS.md = 67,000 chars

**Test**:
1. Add logging to track message history size after each tool call
2. Run minimal test, monitor context growth
3. Expected: Context stays under 10K tokens
4. If exceeds: Hypothesis proven

**Fix** (if proven):
- Aggressive truncation: 500 chars per tool output (not 2000)
- Summarization layer: LLM summarizes tool results before appending to history
- Sliding window: Keep only last 3 messages in history, summarize older context
- Tool result caching: Don't re-read same file multiple times

---

### Hypothesis 5: LangChain Tool Binding Issue
**Cause**: researcher_llm.bind_tools(RESEARCH_TOOLS) not properly configured for OpenRouter models

**Evidence**:
- Tool binding works in isolation (test_v2c_implementation.py passed 34/34 tests)
- But fails in swarm orchestration context
- May be incompatibility with OpenRouter API vs OpenAI API

**Test**:
1. Create standalone test: bind_tools → invoke with explicit tool call request
2. Monitor OpenRouter API request/response
3. Expected: Tool call schema properly formatted
4. If malformed: Hypothesis proven

**Fix** (if proven):
- Use OpenAI API directly for tool-enabled researchers (not OpenRouter)
- Implement custom tool calling wrapper for OpenRouter models
- Document which models support native tool calling vs need custom handling

---

## Incremental Testing Strategy

### Phase 0: Minimal Validation (1 hour)
**Goal**: Prove single researcher can use read_file successfully

1. Create `test_minimal_tool_access.py`:
```python
from hfo_swarm.simple_orchestrator import SimpleOrchestrator
import os

os.environ['DISABLE_RESEARCHER_TOOLS'] = '0'
orch = SimpleOrchestrator()

result = orch.execute_mission(
    intent="Read hfo_gem/gen_30/README.md lines 1-50 and summarize the V²C vision in 100 words",
    constraints="Use read_file tool to access the actual file. Cite line numbers.",
    num_researchers=1,
    save_artifacts=True
)

print(f"Response length: {len(result['executive_summary'])}")
print(f"Response: {result['executive_summary']}")
```

2. Run: `python test_minimal_tool_access.py`
3. Success criteria: Response >500 chars, contains line number citations
4. If fails: Check `hfo_swarm_runs/*/02_research/researcher_01.md` for error messages

---

### Phase 1: Incremental Scaling (2 hours)
**Goal**: Validate 3→5→10 researchers with tools

1. Test 3 researchers (same intent as Phase 0)
2. Test 5 researchers (add grep_search: "Find all mentions of 'PREY' in hfo_gem/gen_30/")
3. Test 10 researchers (add list_files: "List all .md files in hfo_gem/gen_30/")
4. Success criteria: >80% response rate, substantive content, tool usage logged

---

### Phase 2: Complexity Increase (3 hours)
**Goal**: Handle multi-file analysis and cross-validation

1. Intent: "Compare Gen 29 vs Gen 30 README files, identify key differences"
2. Expected tools: read_file (2 files), grep_search (cross-check claims)
3. Success criteria: Researchers cite both files, validator cross-checks citations
4. If fails: Reduce scope (compare 2 sections, not whole files)

---

### Phase 3: Full Mission Test (4 hours)
**Goal**: Run phased architecture consensus with tools enabled

1. Use gen30_phased_architecture_mission.md but simplified to 6 questions (not 12)
2. 10 researchers, 3 rounds (SPIRAL iterative refinement)
3. Success criteria: HIGH consensus, no hallucinations, full file access
4. If fails: Document specific failure point, iterate

---

## Success Criteria

**Minimum Viable Fix**:
- ✅ Single researcher can use read_file on small file (<5K chars)
- ✅ 3 researchers can use read_file in parallel
- ✅ Tool outputs appear in message history
- ✅ Responses are substantive (>500 chars each)

**Production Ready**:
- ✅ 10 researchers can use all 3 tools (read_file, grep_search, list_files)
- ✅ >80% response rate with tools enabled
- ✅ No timeouts on standard files (<50K chars)
- ✅ Context stays under 50K tokens per researcher
- ✅ Validator can cross-check citations against tool results

**Full Capability**:
- ✅ Iterative PREY loops: researcher uses tool → analyzes result → uses another tool → refines
- ✅ Multi-round SPIRAL: Round 1 results feed into Round 2 prompt with tool access
- ✅ Cross-validation: Researcher A's claims checked by Researcher B reading same file
- ✅ 24/7 continuous improvement: Temporal workflows trigger swarms with tool access

---

## Timeline

**Week 1** (Foundation):
- Day 1-2: Hypothesis testing (1-5)
- Day 3-4: Implement fix for proven hypothesis
- Day 5: Phase 0-1 testing (minimal → incremental)

**Week 2** (Validation):
- Day 1-2: Phase 2 testing (complexity increase)
- Day 3-4: Phase 3 testing (full mission)
- Day 5: Documentation and handoff

**Estimated Total**: 10 days (2 calendar weeks)

---

## Next Actions

**Immediate** (Today):
1. ✅ Create this roadmap
2. ⏳ Create test_minimal_tool_access.py
3. ⏳ Run Phase 0 test (1 researcher, simple read_file)
4. ⏳ Review logs, identify which hypothesis to test first

**This Week**:
1. ⏳ Test Hypothesis 1 (prompt complexity)
2. ⏳ Test Hypothesis 2 (tool blocking)
3. ⏳ Implement fix for proven hypothesis
4. ⏳ Validate fix with Phase 1 testing

**Next Week**:
1. ⏳ Phase 2-3 testing (complexity + full mission)
2. ⏳ Update V²C spec with validated tool access pattern
3. ⏳ Run phased architecture consensus mission with tools enabled
4. ⏳ Commit production-ready tool-enabled orchestrator

---

## References

- **Incident**: AGENTS.md (2025-11-12 16:35 MST - Lifecycle Management Failure)
- **Evidence**: hfo_swarm_runs/2025-11-12/run_211319_* (tool-enabled, 0-char responses)
- **Workaround**: run_gen30_direct_synthesis.py (tools disabled, partial success)
- **Success**: V2C_MISSION_COMPLETE_2025-11-12.md (hallucination detection validated)
- **Tools**: hfo_swarm/research_tools.py (read_file, grep_search, list_files)
- **Orchestrator**: hfo_swarm/simple_orchestrator.py (tool binding logic)

---

## User Vision

> "once we unlock tools the researchers should be able to do much more especially iterative loops and real file read access"

**Unlocking tools enables**:
- Evidence-based validation (cite actual files, not fabricate)
- Iterative PREY loops (Sense file → Make Sense → Execute grep → Feedback results → Repeat)
- Cross-validation (Researcher A reads file → Researcher B verifies → Consensus)
- Multi-round refinement (Round 1: explore files → Round 2: deep dive → Round 3: synthesize)
- 24/7 continuous improvement (Temporal workflows orchestrate swarms with file access)

**This is the key to full V²C-SPIRAL-QUORUM capability.**

---

**Status**: Roadmap complete, ready to begin hypothesis testing
**Owner**: Swarmlord of Webs (Gen 30 bootstrap team)
**Last Update**: 2025-11-12
