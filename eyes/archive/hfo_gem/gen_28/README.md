# Generation 28 – Master Index
**Active Generation**: 28
**Branch**: `hfo-2025-11-quickstart-swarm`
**Last Updated**: 2025-11-11
**Status**: Infrastructure operational, quality tuning in progress

---

## 📍 Quick Start

**New to Gen 28?** Start here:
1. [Reality Summary](./REALITY_SUMMARY.md) - What's real vs hallucinated (5 min read)
2. [SSOT Workflow](./SSOT_WORKFLOW.md) - How to work upstream → downstream
3. [Quickstart](./quickstart.md) - Run your first swarm

**Working on improvements?**
- [Current Tasks](../../hfo_todo/2025-11-11-benchmark-reality-check.md)
- [Benchmark Findings](./BENCHMARK_FINDINGS.md) - What's broken + fixes

---

## 🎯 Single Source of Truth (SSOT)

### Strategic Intent (You Edit)
- **Daily Missions**: `../../hfo_todo/2025-11-*.md`
- **Agent Policy**: `../../AGENTS.md`
- **Personal Notes**: `../../hfo_docs/personal/`

### System Model (Authoritative)
- **SSOT**: `ssot/HFO_SSOT.sysml` (SysML v2) - THE source of truth
- **Diagram Generator**: `ssot/export_ssot_diagrams.py`
- **Obsidian Hourglass Model**: `ssot/obsidian_hourglass/`

**How to use**:
```bash
# Edit the SSOT
vim hfo_gem/gen_28/ssot/HFO_SSOT.sysml

# Generate diagrams
python hfo_gem/gen_28/ssot/export_ssot_diagrams.py

# TODO: Auto-generate code from SSOT (next sprint)
```

### Vision Documents (Context)
- [Vision Level Diagrams](./vision_level_diagrams.md) - High-level architecture
- [SSOT Workflow](./SSOT_WORKFLOW.md) - How SSOT drives development
- [Vision Articulation](./VISION_ARTICULATION.md) - Concept → implementation mapping

---

## 🔬 Current Experiments

### Multi-Agent Swarm Orchestration
**Status**: Infrastructure ✅ working, Quality ❌ needs tuning

**Code**:
- Swarm: `../../hfo_swarm/basic_swarm.py` (349 lines)
- Benchmark: `../../tests/benchmarks/run_math_benchmark.py` (297 lines)
- Dependencies: `../../requirements.txt`

**Database**: `hfo_postgres` Docker container
- 100 agent runs logged (4 agents × 25 missions)
- Timeline: 2025-11-11 21:40 → 22:33 (53 min)

**Results**:
- [Benchmark Findings](./BENCHMARK_FINDINGS.md) - 87.5% hallucination rate analysis
- [Reality Summary](./REALITY_SUMMARY.md) - Verification of what's real

**Next Steps**: Fix prompts (format constraints), strengthen validation

---

## 📦 Handoffs & Snapshots

### Recent Handoffs
- [2025-11-11 Handoff](./handoffs/HANDOFF_2025-11-11.md) - Benchmark session, 3 commits

### State Snapshots
- [2025-11-11 Verified State](./snapshots/verified_state_2025-11-11.md)
- [2025-11-11 Reality Check](./snapshots/REALITY_CHECK_2025-11-11.md) - Full investigation

---

## 🗂️ File Organization

### Gen 28 Structure
```
hfo_gem/gen_28/
├── README.md                    ← You are here
├── REALITY_SUMMARY.md           ← Quick verification status
├── SSOT_WORKFLOW.md             ← How to use SSOT
├── VISION_ARTICULATION.md       ← Concepts → implementation
├── BENCHMARK_FINDINGS.md        ← Quality analysis
├── vision_level_diagrams.md     ← Architecture vision
├── gen_28_todo.md               ← Local task tracking
│
├── ssot/                        ← Single Source of Truth
│   ├── HFO_SSOT.sysml          ← **THE** authoritative model
│   ├── export_ssot_diagrams.py
│   └── obsidian_hourglass/
│       └── Obsidian_Hourglass.sysml
│
├── handoffs/                    ← Session documentation
│   └── HANDOFF_2025-11-11.md
│
└── snapshots/                   ← Point-in-time state
    ├── verified_state_2025-11-11.md
    └── REALITY_CHECK_2025-11-11.md
```

### Related Directories
```
hfo_swarm/          - Multi-agent orchestration code
tests/benchmarks/   - Quality validation tests
hfo_todo/          - Daily mission planning
hfo_docs/          - Cross-generation documentation
scripts/dev/       - Development utilities
```

---

## 🛠️ Development Tools

### Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Verify swarm works
python3 -c "from hfo_swarm.basic_swarm import run_swarm; print('✅')"

# Start infrastructure
docker-compose -f docker-compose.dev.yml up -d

# Check database
docker exec hfo_postgres psql -U postgres -d hfo_obsidian -c "\dt"
```

### Useful Scripts
```bash
# Organize Gen 28 artifacts
bash scripts/dev/organize_gen28.sh

# Safe database query
bash scripts/dev/safe_query.sh "SELECT COUNT(*) FROM missions;" hfo_obsidian

# Health check (cached)
cat ~/.cache/hfo_health/status.json
```

---

## 📚 Documentation Index

### Policy & Process
- [AGENTS.md](../../AGENTS.md) - Swarmlord charter, molt shell policy, PREY loop
- [Gen 28 Todo](./gen_28_todo.md) - Local task tracking
- [Daily Todos](../../hfo_todo/) - Mission planning by date

### Technical Deep Dives
- [Vision Articulation](./VISION_ARTICULATION.md) - Maps concepts to implementations
- [SSOT Workflow](./SSOT_WORKFLOW.md) - Upstream editing, downstream generation
- [Benchmark Findings](./BENCHMARK_FINDINGS.md) - Hallucination analysis + fixes

### Tooling & Infrastructure
- [IDE Modernization Report](../../hfo_docs/ide-modernization-report-2025-11-09.md)
- [AI Chat Tech Stack](../../hfo_docs/ai-chat-tech-stack-2025-11-08.md)
- [Swarm Execution Guardrails](../../hfo_docs/tooling/swarm-execution-guardrails.md)

---

## 🎯 Current Priorities (2025-11-11)

1. **Fix swarm prompts** - Add format constraints to reduce hallucinations
2. **Strengthen validator** - Reject verbose/off-topic responses
3. **Improve extraction** - Parse markdown bold, numbers with units
4. **Organize artifacts** - Move root clutter to proper Gen 28 locations
5. **Build SSOT → Code pipeline** - Auto-generate swarm implementation from SysML

See [2025-11-11 Reality Check Todo](../../hfo_todo/2025-11-11-benchmark-reality-check.md) for details.

---

## ✅ Verification

**To verify this documentation reflects reality**:
```bash
# 1. Check you're in Gen 28
cat hfo_gem/active_generation.txt  # Should show: 28

# 2. Verify code exists
wc -l hfo_swarm/basic_swarm.py hfo_gem/gen_28/ssot/export_ssot_diagrams.py

# 3. Check database has data
docker exec hfo_postgres psql -U postgres -d hfo_obsidian \
  -c "SELECT COUNT(*) FROM agent_runs;"

# 4. Confirm SSOT exists
ls -lh hfo_gem/gen_28/ssot/*.sysml

# 5. Review recent work
git log --oneline --since="2025-11-10"
```

---

## 🧭 Navigation

**Going Deeper**:
- System model: [ssot/HFO_SSOT.sysml](./ssot/HFO_SSOT.sysml)
- Swarm code: [hfo_swarm/basic_swarm.py](../../hfo_swarm/basic_swarm.py)
- Latest findings: [BENCHMARK_FINDINGS.md](./BENCHMARK_FINDINGS.md)

**Going Up**:
- All generations: [hfo_gem/](../)
- Project root: [HiveFleetObsidian/](../../)
- Policy: [AGENTS.md](../../AGENTS.md)

---

**Maintainer**: Update this index when Gen 28 structure changes.
**Last Verified**: 2025-11-11 (100 agent runs, 1404 lines code, 12 commits)
