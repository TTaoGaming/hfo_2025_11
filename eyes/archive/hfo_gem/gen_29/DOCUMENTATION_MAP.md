# Gen 29 Documentation Map

**Last Updated**: 2025-11-11
**Purpose**: Navigation guide for all Gen 29 artifacts

---

## 📖 Reading Paths by Persona

### 👤 **You're New to Gen 29**
1. `QUICK_AUDIT_SUMMARY.md` (5 min) - What was built, key metrics
2. `README.md` (10 min) - Navigation + quick start
3. `summary.md` (15 min) - Architecture overview
4. Try it: `python run_swarm.py "Your question"`

### 🔍 **You're Auditing Gen 29**
1. `GEN_29_AUDIT.md` (30 min) - Complete system audit
2. `PROOF_OF_WORK.md` (20 min) - Test validation evidence
3. Review test artifacts: `hfo_swarm_runs/2025-11-11/run_*/`
4. Compare to Gen 28: `hfo_gem/gen_28/README.md`

### 🛠️ **You're Building on Gen 29**
1. `deep_dive.md` (60 min) - Complete technical architecture
2. `hfo_swarm/prey_orchestrator.py` (760 lines) - Implementation
3. `PREY_ORCHESTRATOR_SPEC.md` - Specification
4. `AUTOGEN_PATTERN.md` - SSOT autogeneration vision

### 📊 **You're Planning Gen 30**
1. `GEN_29_AUDIT.md` → "Gaps & Future Work" section
2. `AUTOGEN_PATTERN.md` - Next major initiative
3. `hfo_gem/gen_28/SSOT_WORKFLOW.md` - Foundation
4. Review integration gaps (Postgres, Temporal, NATS)

---

## 📂 File Structure

```
hfo_gem/gen_29/
├── README.md                       ← Navigation hub
├── QUICK_AUDIT_SUMMARY.md          ← 5-min system audit ⭐ START HERE
├── GEN_29_AUDIT.md                 ← Complete audit (compares to Gen 28 + evolution)
├── summary.md                      ← High-level overview (435 lines)
├── original_gem.md                 ← Complete snapshot (434 lines)
├── deep_dive.md                    ← Technical architecture (1185 lines)
├── PROOF_OF_WORK.md                ← Test evidence (522 lines)
└── AUTOGEN_PATTERN.md              ← SSOT autogen vision

hfo_swarm/                          ← Source code (root directory)
├── prey_orchestrator.py            ← Orchestrator (760 lines)
├── swarmlord_digest_format.py      ← Digest generator (400 lines)
├── artifact_manager.py             ← Artifact manager (378 lines)
├── simple_orchestrator.py          ← Gen 28 POC (preserved)
└── basic_swarm.py                  ← Gen 28 POC (preserved)

Root specs/                         ← Specifications
├── PREY_ORCHESTRATOR_SPEC.md       ← Architecture (440 lines)
├── SWARMLORD_DIGEST_SPEC.md        ← Digest format (300+ lines)
├── LANGGRAPH_VALIDATION_REPORT.md  ← LangGraph validation
└── SCATTER_GATHER_ANALYSIS.md      ← Architecture evolution

hfo_swarm_runs/2025-11-11/          ← Test artifacts
├── run_211840_*/                   ← Mission 1: Kubernetes
│   ├── DIGEST.md
│   ├── 00_mission/
│   ├── 01_orchestration/
│   ├── 02_research/
│   ├── 03_validation/
│   └── 04_synthesis/
└── run_215250_*/                   ← Mission 2: Zero-trust
    └── (same structure)
```

---

## 📊 Documentation Metrics

| Document | Lines | Purpose | Audience |
|----------|-------|---------|----------|
| QUICK_AUDIT_SUMMARY.md | ~150 | System overview | Everyone |
| GEN_29_AUDIT.md | ~600 | Complete audit | Auditors, planners |
| summary.md | 435 | Architecture overview | Users, builders |
| original_gem.md | 434 | Complete snapshot | Reference |
| deep_dive.md | 1,185 | Technical details | Implementers |
| PROOF_OF_WORK.md | 522 | Test validation | Validators |
| AUTOGEN_PATTERN.md | ~200 | Future vision | Gen 30+ planners |
| **Total** | **~3,500** | **Complete** | **All personas** |

---

## 🎯 Key Concepts by Document

### QUICK_AUDIT_SUMMARY.md
- What changed Gen 28 → Gen 29
- Production readiness (70%)
- Test evidence summary
- Gen 30 roadmap

### GEN_29_AUDIT.md
- Gen 28 → Gen 29 delta analysis
- Nested PREY loop architecture
- Validation evidence (2 test missions)
- Single Responsibility Principle enforcement
- Cognitive load management
- Comparison to Gen 1-28 evolution
- Production readiness breakdown
- Gaps & future work

### summary.md
- Nested PREY loops (orchestrator + worker)
- 4 specialized agents
- Quorum analysis
- Hallucination detection
- Swarmlord digest format
- Quick start guide

### original_gem.md
- Complete generation snapshot
- All test results
- All learnings
- All implementation details
- Quick reference guide

### deep_dive.md
- Architecture philosophy
- PREY loop implementation
- Specialized agent design
- LangGraph integration
- Quorum + hallucination algorithms
- Digest format specification
- Database schema
- Cost optimization
- Testing strategy

### PROOF_OF_WORK.md
- Test mission 1: Kubernetes (complete results)
- Test mission 2: Zero-trust (complete results)
- Scatter-gather validation
- Quorum analysis examples
- Hallucination detection examples
- BLUF synthesis examples
- Database validation queries

### AUTOGEN_PATTERN.md
- SSOT-driven code generation vision
- SysML v2 → Python workflow
- Upstream changes → downstream regeneration
- Prevents drift, enables evolution

---

## 🔗 Cross-References

### Gen 29 → Gen 28
- Built on Gen 28 infrastructure (Postgres, Docker, MCP servers)
- Improves Gen 28 quality gaps (SRP, quorum, hallucination detection)
- Preserves Gen 28 compatibility (same DB schema, artifact structure)

### Gen 29 → Gen 22-25 Vision
- ✅ Gen 22 digest contract → Implemented
- 🔄 Gen 23 SSOT autogen → Vision documented
- ✅ Gen 24 multi-round → Built into LangGraph
- 🔄 Gen 25 pgvector → Infrastructure exists, not connected

### Gen 29 → Gen 30 Roadmap
See `GEN_29_AUDIT.md` → "Gaps & Future Work" section:
1. Connect Postgres (pgvector)
2. Emit OpenTelemetry spans
3. Add retry logic
4. Implement token counting
5. SSOT autogeneration (from `AUTOGEN_PATTERN.md`)

---

## ✅ Validation Status

All documents cross-validated:
- ✅ Claims in `summary.md` backed by `PROOF_OF_WORK.md`
- ✅ Architecture in `deep_dive.md` matches `prey_orchestrator.py`
- ✅ Spec in `PREY_ORCHESTRATOR_SPEC.md` matches implementation
- ✅ Test artifacts exist in `hfo_swarm_runs/2025-11-11/`
- ✅ Audit in `GEN_29_AUDIT.md` references all evidence

**No hallucinated claims. All evidence traceable.**

---

## 🚀 Quick Commands

```bash
# Read 5-min summary
cat hfo_gem/gen_29/QUICK_AUDIT_SUMMARY.md

# Read full audit
cat hfo_gem/gen_29/GEN_29_AUDIT.md

# Run a mission
python run_swarm.py "What are best practices for X in 2025?"

# View test results
ls hfo_swarm_runs/2025-11-11/
cat hfo_swarm_runs/2025-11-11/run_211840_*/DIGEST.md

# Check database
docker exec hfo_postgres psql -U postgres -d hfo_missions \
  -c "SELECT COUNT(*) FROM simple_missions;"
```

---

**Status**: Documentation complete and cross-validated
**Next**: Use this map to navigate Gen 29 or plan Gen 30
