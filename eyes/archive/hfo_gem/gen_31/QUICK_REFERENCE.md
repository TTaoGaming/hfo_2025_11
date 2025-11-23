---
hexagon:
  ontos:
    id: 4712eb89-004d-4b14-84a7-5dd0acd1ba74
    type: md
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T11:07:36.024001Z'
    generation: 51
  topos:
    address: eyes/archive/hfo_gem/gen_31/QUICK_REFERENCE.md
    links: []
  telos:
    viral_factor: 0.0
    meme: QUICK_REFERENCE.md
---
# HFO Quick Reference - Generation 31

**Last Updated**: 2025-11-14
**Your Launcher**: `hfo.py` (THE ONE canonical launcher)

---

## 🚀 Quick Start (3 Commands)

```bash
# 1. Interactive mode (recommended)
python3 hfo.py

# 2. Command-line mode
python3 hfo.py "What are SOTA patterns for distributed tracing?"

# 3. Show model roster
python3 hfo.py --models
```

**That's it.** No other launcher needed.

---

## 📊 What You Get

**Input**: Plain language research question
**Output**: Human-readable DIGEST with audit trail
**Cost**: ~$0.05 per mission
**Duration**: ~90 seconds

---

## 🎯 Scatter-Gather Pattern

```
YOU PROVIDE:
├─ Intent: "What are SOTA patterns for X?"
└─ Constraints: "Focus on production, avoid academic theory"

SYSTEM DOES:
├─ SCATTER: 10 diverse AI models research in parallel
├─ GATHER: Quorum consensus + hallucination detection
├─ VALIDATE: Static guards (can't hallucinate)
└─ OUTPUT: DIGEST.md with full audit trail
```

---

## 🤖 10 AI Families (BALANCED_ROSTER_10)

| Family | Model | Cost | Notes |
|--------|-------|------|-------|
| DeepSeek | v3.1 | $0.20/M | 671B MoE, reasoning |
| OpenAI | gpt-4o-mini | $0.15/M | Reliable workhorse |
| Google | gemini-2.5-flash-lite | $0.10/M | 1M context, fast |
| Anthropic | claude-3.5-haiku | $0.25/M | Precise instructions |
| xAI | grok-beta | $0.20/M | Experimental, fresh |
| Minimax | minimax-01 | $0.20/M | Multimodal MoE |
| Cohere | command-r | $0.20/M | RAG-optimized |
| Meta | llama-3.3-70b | $0.20/M | Open weights |
| Mistral | mistral-large-2411 | $0.20/M | European, multilingual |
| Qwen | qwen-2.5-72b | $0.20/M | Alibaba, multilingual |

**Total**: 10 different architectures (not 10 GPT instances)
**Geographic**: USA, China, Europe
**Diversity**: MoE, Transformer, Multimodal, Open/Closed

---

## 📂 Where to Find Results

```bash
# Find today's runs
ls hfo_swarm_runs/$(date +%Y-%m-%d)/

# Read the digest (START HERE)
cat hfo_swarm_runs/2025-11-14/run_*/DIGEST.md

# Check consensus
cat hfo_swarm_runs/2025-11-14/run_*/03_validation/quorum_analysis.md

# Check hallucinations
cat hfo_swarm_runs/2025-11-14/run_*/03_validation/hallucinations.md

# Audit individual researchers
ls hfo_swarm_runs/2025-11-14/run_*/02_research/

# View validation status
cat hfo_swarm_runs/2025-11-14/run_*/05_hive_guards/summary.md
```

---

## ✅ Success Criteria

**HIGH Consensus** = 7+/10 researchers agree (70%)
**MEDIUM Consensus** = 4-6/10 agree (40-60%)
**LOW Consensus** = <4/10 agree (<40%)

**Hive Guards**:
- ✅ PASS = No errors, all checks passed
- ⚠️  WARN = 1-5 warnings, review recommended
- ❌ FAIL = >0 errors, mission integrity compromised

---

## 🛠️ Advanced Usage

### Dry Run (Preview Without Execution)

```bash
python3 hfo.py --dry-run "Research topic"
# Shows plan, model roster, cost estimate
# Does NOT execute mission
```

### Check Model Roster

```bash
python3 hfo.py --models
# Displays BALANCED_ROSTER_10
# Shows pricing, context lengths, capabilities
```

### Custom Constraints

```python
# In interactive mode, provide constraints:
# - "Focus on production use cases, avoid academic theory"
# - "Include real-world examples from FAANG companies"
# - "Cite specific benchmarks and performance data"
# - "Prioritize open-source solutions"
```

---

## 💰 Cost Budgeting

**Per Mission**: ~$0.05
**Per Week** ($10 budget): ~200 missions
**Per Day**: ~28 missions

**Cost Breakdown**:
- Orchestrator: $0.0003
- 10 Researchers: $0.03
- Analyzer: $0.0024
- Validator: $0.0012
- Synthesizer: $0.003
- **Total**: ~$0.04-0.06

---

## ⚡ Performance

**Execution Timeline**:
- Orchestrator prompt: ~5s
- 10 parallel researchers: ~45s
- Quorum analysis: ~10s
- Hallucination check: ~10s
- Executive synthesis: ~15s
- Hive Guards: <5s
- **Total**: ~90 seconds

**Parallelization**:
- 10 researchers run simultaneously (not serial)
- ThreadPoolExecutor with smart timeouts
- Timeout formula: `ceil(researchers/workers) × 60s × 2.0x`

---

## 🔧 Troubleshooting

### "Import Error" or "Module Not Found"

```bash
# Check Python environment
python3 -c "import hfo_swarm.simple_orchestrator; print('✅ OK')"

# If fails, check you're in correct directory
cd /home/tommytai3/HiveFleetObsidian
```

### "API Key Error"

```bash
# Check .env has OPENROUTER_API_KEY
grep OPENROUTER_API_KEY .env

# Get API key from https://openrouter.ai/keys
```

### "Empty Researcher Responses"

- Some FREE tier models don't support tools (known issue)
- GPT-OSS models sometimes return empty (investigating)
- 9/10 successful is acceptable (90% success rate)

### "Mission Too Slow"

- Normal: 90-120s for 10 researchers
- If >5min: Check internet connection, OpenRouter status
- Timeouts auto-scale based on parallelization

---

## 📚 Documentation

**Gen 31 (Current)**:
- `hfo_gem/gen_31/HFO_LAUNCHER_ARCHITECTURE.md` - Complete architecture
- `hfo_gem/gen_31/HFO_SCATTER_GATHER_DIAGRAMS.md` - Visual diagrams
- `hfo_gem/gen_31/GENERATION_INTENT.md` - Vision and roadmap
- `hfo_gem/gen_31/user_dictation/` - User quotes captured

**Gen 30 (Context)**:
- `AGENTS.md` - Historical incidents, lessons learned
- `BALANCED_10_SUCCESS.md` - Multi-model validation results

**Code**:
- `hfo.py` - Launcher (read this for implementation)
- `hfo_sdk/model_families.py` - Model roster definitions
- `hfo_swarm/simple_orchestrator.py` - Scatter-gather logic

---

## 🎯 Common Use Cases

### Research SOTA Patterns

```bash
python3 hfo.py "What are SOTA patterns for distributed tracing in microservices?"
```

### Compare Technologies

```bash
python3 hfo.py "Compare Temporal vs Prefect for workflow orchestration"
```

### Production Best Practices

```bash
python3 hfo.py "How do production systems handle rate limiting and backpressure?"
```

### Architecture Decisions

```bash
python3 hfo.py "What are tradeoffs between monorepo vs polyrepo for microservices?"
```

**Pro Tip**: Add constraints to narrow focus and improve quality

---

## 🚀 Next Steps (Gen 31 Roadmap)

**Phase 1 (Week 1)**: Tool Enhancements
- LLM-powered result summarization
- Graceful degradation for FREE tier models
- Model capability matrix

**Phase 2 (Week 2)**: Stigmergy Integration
- Wire coordinator to consume NATS signals
- Confidence-weighted quorum
- Abort on critical alerts

**Phase 3 (Week 3)**: Fractal Scaling
- L2 test (100 researchers)
- L3 test (1000 researchers)
- Push the limit validation

**Phase 4 (Ongoing)**: Knowledge Transfer
- Systematic user dictation capture
- Cross-generation synthesis
- Documentation automation

---

## 💡 Key Insights

**Why 10 Researchers?**
- Quorum math: 7/10 = 70% consensus (statistically strong)
- Cost-optimized: 10× diversity without 100× cost
- Parallel execution: 10 workers → ~2min (not 20min serial)

**Why Multi-Model?**
- Different architectures → different blind spots
- Geographic diversity → different perspectives
- Reduces groupthink, surfaces competing hypotheses

**Why Static Guards?**
- LLMs can hallucinate validation results
- Static guards = pure Python, can't hallucinate
- Fast (<5s), deterministic, trust validation

**Why Single Launcher?**
- No proliferation of test scripts
- Clear entry point for AI assistants
- Enforces production best practices

---

## 🎓 Philosophy

**Scatter-Gather Pattern**:
- SCATTER: Disperse to diverse models (parallel)
- GATHER: Converge to consensus (quorum + validation)

**V²C Validation**:
- VERIFY: Quorum analysis (consensus detection)
- VALIDATE: Hallucination check (fabrication detection)
- CONSENSUS: Executive synthesis (BLUF + findings)

**Production-Ready Enforcement**:
- 10 researchers (quorum requirement)
- BALANCED_ROSTER_10 (true diversity)
- Full artifacts (audit trail)
- Hive Guards (static validation)

---

## 📞 Quick Commands Cheat Sheet

```bash
# Run mission (interactive)
python3 hfo.py

# Run mission (CLI)
python3 hfo.py "Research topic"

# Show models
python3 hfo.py --models

# Dry run (preview)
python3 hfo.py --dry-run "Topic"

# Find results
ls hfo_swarm_runs/$(date +%Y-%m-%d)/

# Read digest
cat hfo_swarm_runs/2025-11-14/run_*/DIGEST.md

# Check consensus
cat hfo_swarm_runs/2025-11-14/run_*/03_validation/quorum_analysis.md

# Check hallucinations
cat hfo_swarm_runs/2025-11-14/run_*/03_validation/hallucinations.md

# View guards
cat hfo_swarm_runs/2025-11-14/run_*/05_hive_guards/summary.md
```

---

**Status**: ✅ READY TO USE
**Generation**: 31
**Your Launcher**: `hfo.py` (THE ONE)

**Questions?** Read `hfo_gem/gen_31/HFO_LAUNCHER_ARCHITECTURE.md` for details.
