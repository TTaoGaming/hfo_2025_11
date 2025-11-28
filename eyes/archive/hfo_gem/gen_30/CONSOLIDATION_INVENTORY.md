---
hexagon:
  ontos:
    id: dbbf6ae1-4e0d-4062-96b5-cdd1a15bbf71
    type: md
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T11:07:35.677238Z'
    generation: 51
  topos:
    address: eyes/archive/hfo_gem/gen_30/CONSOLIDATION_INVENTORY.md
    links: []
  telos:
    viral_factor: 0.0
    meme: CONSOLIDATION_INVENTORY.md
---

# HFO Gen 30 Consolidation Inventory
**Date**: 2025-11-13
**Goal**: Stable L0/L1/L2 execution with zero config sprawl

---

## 🎯 SDK SOLUTION IMPLEMENTED

**NEW: HFO SDK** - Clean, stable interface that hides all complexity.

```python
from hfo_sdk import swarm

# L0: Single researcher
result = swarm.research("What is stigmergy?")

# L1: 10 researchers with consensus
result = swarm.consensus("Should we use Rust or Python?")

# L2: 100 researchers (meta-swarm)
result = swarm.meta_research("Analyze Gen 30 architecture")
```

**Why this solves sprawl**:
- Users don't need to know about 8 orchestrator variants
- SDK provides stable API that won't break when we refactor internals
- Simple API (3 functions) for 80% of use cases
- Advanced API available for power users
- Consolidation can happen behind SDK without breaking user code

**SDK Structure** (NEW files created):
- `hfo_sdk/__init__.py` - Public API exports
- `hfo_sdk/simple.py` - Simple API (research, consensus, meta_research)
- `hfo_sdk/advanced.py` - Advanced API (Swarm, Mission, Config)
- `hfo_sdk/models.py` - Model tier utilities
- `hfo_sdk/README.md` - Comprehensive documentation
- `examples/sdk_simple.py` - Simple API examples
- `examples/sdk_advanced.py` - Advanced API examples
- `test_sdk.py` - Quick validation test

---

## 🚨 CRITICAL FINDING: Massive Code Sprawl

**Problem**: You've achieved L3 (1000 researchers, 100 concurrent) but system is **brittle** due to:
- 8+ orchestrator variants (some overlapping, some stale)
- 44+ test files (many duplicating same patterns)
- 22+ launcher scripts (inconsistent interfaces)
- 60+ markdown docs scattered at repo root
- Zero registry of what's CANONICAL vs EXPERIMENTAL vs STALE

---

## 📦 ORCHESTRATORS (8 variants found)

### ✅ CANONICAL (Keep & Consolidate)

1. **`hfo_swarm/gen30_orchestrator.py`** (1106 lines)
   - **Status**: PRIMARY - Has L0/L1/L2/L3 methods
   - **Capabilities**: Fractal holonic, multi-model support, lifecycle guards
   - **Issues**:
     - Still uses scattered `os.getenv()` calls (not using SSOT config yet)
     - Artifact creation has intent collision bug (L2 holons overwrite each other)
     - No integration with stigmergy_coordinator.py
   - **Verdict**: **MIGRATE TO SSOT CONFIG**, fix artifact factory pattern

2. **`hfo_swarm/simple_orchestrator.py`** (837 lines)
   - **Status**: CANONICAL for simple missions
   - **Capabilities**: Single-level (no fractal), V²C validation, tool-enabled researchers
   - **Migration Status**: ✅ ALREADY USES SSOT CONFIG (just migrated)
   - **Verdict**: **KEEP AS-IS** - exemplar for simple L0 missions

3. **`hfo_swarm/stigmergy_coordinator.py`** (568 lines)
   - **Status**: DESIGNED but NOT INTEGRATED
   - **Capabilities**: NATS JetStream signals, heartbeat/confidence/citation tracking
   - **Verdict**: **INTEGRATE** into gen30_orchestrator.py for L2+ coordination

### ⚠️ SPECIAL PURPOSE (Document & Keep Separate)

4. **`hfo_swarm/gen30_bootstrap_orchestrator.py`**
   - **Purpose**: Audits Gen 1-29 files to extract evolution history
   - **Verdict**: **KEEP SEPARATE** - bootstrap-only, not for general missions

5. **`run_multimodel_v2c.py::MultiModelOrchestrator`** (444 lines)
   - **Purpose**: Extends SimpleOrchestrator for 10-model diversity
   - **Verdict**: **MERGE PATTERN** into gen30_orchestrator.py (model roster should be built-in)

### ❌ STALE / EXPERIMENTAL (Archive or Delete)

6. **`hfo_swarm/simple_orchestrator.STALE.py`**
   - Verdict: **DELETE** (obsolete, replaced by current simple_orchestrator.py)

7. **`hfo_swarm/scatter_gather_orchestrator.STALE.py`**
   - Verdict: **DELETE** (pattern absorbed into SimpleOrchestrator)

8. **`hfo_swarm/prey_orchestrator.py`** (763 lines)
   - **Status**: Gen 29 artifact, PREY loops implemented
   - **Verdict**: **ARCHIVE** to `hfo_gem/gen_29/` - superceded by gen30_orchestrator

9. **`hfo_swarm/nested_prey_orchestrator.py`** (corrupted header, 1779 lines)
   - **Status**: CORRUPTED (markdown embedded in Python header)
   - **Verdict**: **QUARANTINE** → `hfo_swarm/CORRUPTED/` or delete

### 🧪 TEST-ONLY ORCHESTRATORS (Move to tests/)

10. **`test_fractal_holonic_true.py::FractalHolonicOrchestrator`**
11. **`test_l3_stigmergy_research.py::L3StigmergyOrchestrator`**
    - Verdict: **KEEP IN tests/** - experimental validation patterns

---

## 🧪 TEST FILES (44 found, massive duplication)

### ✅ CANONICAL L0/L1/L2/L3 Tests (Keep)

1. **`test_gen30_orchestrator.py`** - Gen30 L0/L1/L2 validation
2. **`test_l0_no_tools.py`** - L0 without file access (domain knowledge only)
3. **`test_l1_multimodel.py`** - L1 with 10 different models
4. **`test_minimal_tool_access.py`** - Minimal researcher + tools smoke test
5. **`test_lifecycle_guards.py`** - Timeout/health/retry validation

### ⚠️ EXPERIMENTAL (Document Purpose or Archive)

6. `test_l3_stigmergy_research.py` - L3 (1000) with stigmergy
7. `test_fractal_holonic_true.py` - True fractal composition
8. `test_fractal_holonic_swarm.py` - Fractal test variant
9. `test_fractal_simple.py` - Simple fractal test
10. `test_massive_swarm.py` - Large-scale test
11. `test_progressive_fractal.py` - Progressive scaling
12. `test_progressive_no_tools.py` - Progressive without tools
13. `test_multimodel_quick.py` - Quick multi-model test
14. `test_single_researcher_quick.py` - Quick single test

**Problem**: 8+ fractal/progressive tests doing similar things with different patterns

### ❌ DUPLICATES / STALE (Archive)

15. `test_artifact_corruption.py` - Specific incident test
16. `test_artifact_validation.py` - Validation test
17. `test_simple_pricing.py` - One-off pricing test
18. `test_v2c_implementation.py` - V2C validation (merge into test_gen30_orchestrator)

### ✅ ORGANIZED TESTS (tests/ directory - Keep)

- `tests/test_knowledge_graph.py` ✅
- `tests/test_verification.py` ✅
- `tests/test_simple_orchestrator.py` ✅
- `tests/test_disperse_converge.py` ✅
- `tests/benchmarks/run_math_benchmark.py` ✅

---

## 🚀 LAUNCHER SCRIPTS (22 found, inconsistent interfaces)

### ✅ CANONICAL USER-FACING (Keep)

1. **`run_swarm.py`** - Interactive CLI for simple missions
   - Verdict: **MIGRATE TO SSOT CONFIG**

2. **`launch_mission.py`** / **`launch_mission_quick.py`**
   - Verdict: **CONSOLIDATE** into single `launch_mission.py` with --quick flag

### ⚠️ SPECIALIZED (Document & Keep)

3. `launch_gen30_bootstrap.py` - Bootstrap-only
4. `launch_gen30_phased_synthesis.py` - Phased rollout planner
5. `run_multimodel_v2c.py` - 10-model V²C launcher
6. `run_v2c_champion_validation.py` - Champion validation
7. `run_stigmergy_analysis.py` - Stigmergy analysis

### ❌ ONE-OFF / EXPERIMENTAL (Archive)

8. `run_gen30_direct_synthesis.py` - One-off direct synthesis
9. `run_v2c_working.py` - Override to force gpt-4o-mini (workaround script)
10. `run_model_zoo_pricing_mission.py` - Pricing research (one-off)
11. `run_model_zoo_research.py` - Model zoo research (one-off)
12. `run_meta_research.py` - Meta-research (experimental)
13. `run_meta_prey_analysis.py` - PREY analysis (experimental)

### 📜 SHELL SCRIPTS (7 found)

14. `launch_fractal_swarm.sh`
15. `launch_l3_stigmergy.sh`
16. `launch_massive_swarm.sh`
17. `launch_multimodel.sh`
18. `launch_v2c.sh`
19. `run_gen30_tests.sh`
20. `run_progressive_test.sh`

**Verdict**: **CONSOLIDATE** into `scripts/launch/` with clear naming

---

## 📄 DOCUMENTATION SPRAWL (60+ markdown files at repo root)

### 🚨 CRITICAL ISSUE: No Clear SSOT for Docs

**Root Cause**: Session-based documentation without consolidation
**Impact**: User can't find canonical info, multiple contradictory docs

### ✅ CANONICAL REFERENCE (Keep at Root)

1. `README.md` (if exists - didn't see it!)
2. `AGENTS.md` (2931 lines, incident log - needs migration to knowledge graph)

### ⏳ SESSION ARTIFACTS (Consolidate → hfo_gem/gen_30/sessions/)

- `V2C_MISSION_COMPLETE_2025-11-12.md`
- `HANDOFF_2025-11-12-2300.md`
- `HANDOFF_MULTIMODEL_2025-11-12.md`
- `FINAL_HANDOFF_2025-11-12.md`
- `GITOPS_COMPLETE_2025-11-12.md`
- `GIT_COMMIT_COMPLETE.md`
- `GIT_OPERATIONS_PLAN.md`
- `GIT_PUSH_STATUS.md`
- `GEN_30_SESSION_SUMMARY.md`
- `HFO_CURRENT_STATE_2025-11-12.md`
- ... (20+ more)

### 📚 PERMANENT REFERENCE (Move → hfo_gem/gen_30/docs/)

- `FRACTAL_HOLONIC_SUMMARY.md`
- `LIFECYCLE_GUARDS_QUICK_REF.md`
- `V2C_EXECUTION_GUIDE.md`
- `SWARM_QUICKSTART.md`
- `LAUNCHER_CHEAT_SHEET.md`
- `MISSION_LAUNCHER_GUIDE.md`

### 🧪 TEST RESULTS (Move → hfo_swarm_runs/docs/)

- `TEST_RESULTS_MULTIMODEL_2025-11-12.md`
- `TEST_RESULTS_V2C_2025-11-12.md`
- `TEST_RESULTS_PRICING_MISSION.md`
- `SMOKE_TEST_RESULTS_2025-11-12.md`
- `KNOWLEDGE_GRAPH_TEST_RESULTS.md`

### 📊 INCIDENT/ANALYSIS (Move → hfo_gem/gen_30/incidents/)

- `L0_BREAKTHROUGH.md`
- `L2_ARTIFACT_STRUCTURE_ANALYSIS.md`
- `L2_FRACTAL_SUCCESS.md`
- `HALLUCINATION_REDUCTION_PLAN.md`
- `ARCHITECTURE_AUDIT_2025-11-12.md`
- `MASSIVE_SWARM_ANALYSIS.md`

---

## 🏗️ INFRASTRUCTURE STATUS

### ✅ WORKING

1. **`hfo_swarm/lifecycle_guards.py`** (347 lines) - Timeout/health/retry
2. **`hfo_swarm/research_tools.py`** (282 lines) - File/grep/list tools
3. **`hfo_swarm/artifact_manager.py`** (378 lines) - Timestamped run artifacts
4. **`hfo_gem/gen_30/config.py`** (337 lines) - ✅ NEW SSOT CONFIG

### ⚠️ PARTIAL

5. **`hfo_swarm/stigmergy_coordinator.py`** (568 lines) - Designed, not integrated
6. **Knowledge graph** (schema exists, DB not running, migration not done)

### ❌ STALE

7. **`model_allowlist.py`** - Replaced by `hfo_gem/gen_30/config.py` model rosters

---

## 🎯 ROOT CAUSE ANALYSIS: Why Brittleness?

### 1. **No Registry of Canonical vs Experimental**
- User doesn't know which orchestrator to use for what
- Tests overlap but no clear "this is the reference implementation"
- Scripts have inconsistent interfaces (some take CLI args, some hardcoded)

### 2. **Scattered Configuration**
- ✅ FIXED: Created `hfo_gem/gen_30/config.py` SSOT
- ⏳ MIGRATION NEEDED: gen30_orchestrator.py still has 30+ `os.getenv()` calls

### 3. **Artifact Factory Pattern Missing**
- `SwarmRunArtifacts.__init__()` hardcodes timestamped directory creation
- L2 holons with same intent → same directory name → collision
- No factory pattern for "create unique artifact tree for holon N at level L"

### 4. **No Clear Entry Points**
- Want L0? Use which file?
- Want L1? Use which file?
- Want L2? Use which file?
- Want multi-model? Use which file?

### 5. **Documentation Sprawl**
- 60+ markdown files at root, no index
- Session artifacts mixed with permanent reference
- Quick refs scattered, no single source

---

## ✅ CONSOLIDATION PLAN (Phased)

### PHASE 0: Inventory & Cleanup (THIS DOCUMENT)
- ✅ Catalog all orchestrators, tests, launchers, docs
- ✅ Identify CANONICAL vs EXPERIMENTAL vs STALE
- ✅ Root cause analysis of brittleness

### PHASE 1: Stabilize L0/L1/L2 Core (Priority 1)

**Goal**: ONE canonical path for L0, L1, L2 that always works

#### 1.1 Consolidate Orchestrators
```
CANONICAL HIERARCHY:
- SimpleOrchestrator (L0 only, simple missions) ✅ DONE
- Gen30Orchestrator (L0/L1/L2/L3, fractal missions) ⏳ MIGRATE TO SSOT
  - Absorb MultiModelOrchestrator pattern (10-model roster built-in)
  - Integrate stigmergy_coordinator for L2+
  - Fix artifact factory pattern (unique dirs per holon)
```

#### 1.2 SSOT Config Migration
```
✅ hfo_gem/gen_30/config.py created (SSOT)
✅ simple_orchestrator.py migrated
⏳ gen30_orchestrator.py migration
⏳ test files migration
⏳ launcher scripts migration
```

#### 1.3 Artifact Factory Pattern
```
PROBLEM: L2 holons create same directory (intent collision)
SOLUTION: Abstract factory pattern
- HolonAddress(level, path) → unique addressing
- FractalArtifactFactory → generates unique artifact trees
- Propagates level metadata downstream
FILE: hfo_swarm/fractal_artifact_factory.py (designed, not implemented)
```

#### 1.4 Entry Point Registry
```
CREATE: hfo_gem/gen_30/ENTRY_POINTS.md

L0 (1 researcher):
  - Simple: python run_swarm.py
  - Programmatic: from hfo_swarm.simple_orchestrator import SimpleOrchestrator

L1 (10 researchers, quorum):
  - python -m hfo_swarm.gen30_orchestrator --level=1 --intent="..."
  - from hfo_swarm.gen30_orchestrator import Gen30Orchestrator; orch.execute_l1(...)

L2 (100 researchers, 10 holons):
  - python -m hfo_swarm.gen30_orchestrator --level=2 --intent="..."
  - orch.execute_l2(intent, num_l1_holons=10)

L3 (1000 researchers, 10 L2 holons):
  - python -m hfo_swarm.gen30_orchestrator --level=3 --intent="..."
  - orch.execute_l3(intent, num_l2_holons=10)

Multi-Model (10 different architectures):
  - from hfo_gem.gen_30.config import get_multi_model_roster
  - orch = Gen30Orchestrator(researcher_models=get_multi_model_roster('diverse'))
```

### PHASE 2: Test Suite Consolidation

#### 2.1 Canonical Test Pyramid
```
tests/unit/
  - test_lifecycle_guards.py (timeouts, health, retry)
  - test_research_tools.py (file/grep/list)
  - test_artifact_manager.py (directory structure)

tests/integration/
  - test_l0_simple.py (single researcher, no tools)
  - test_l0_tools.py (single researcher, file access)
  - test_l1_quorum.py (10 researchers, consensus)
  - test_l2_fractal.py (100 researchers, 10 holons)
  - test_multimodel.py (10 different architectures)

tests/smoke/
  - test_quick_l0.py (30s smoke test)
  - test_quick_l1.py (2min smoke test)
```

#### 2.2 Archive Experimental Tests
```
Move to: tests/experimental/
- test_l3_stigmergy_research.py
- test_fractal_holonic_true.py
- test_massive_swarm.py
- test_progressive_*.py
```

### PHASE 3: Documentation Reorganization

#### 3.1 Directory Structure
```
hfo_gem/gen_30/
  ├── README.md (Gen 30 overview)
  ├── config.py (SSOT configuration)
  ├── ENTRY_POINTS.md (canonical usage patterns)
  ├── docs/
  │   ├── FRACTAL_HOLONIC_GUIDE.md
  │   ├── V2C_PROTOCOL.md
  │   ├── LIFECYCLE_GUARDS.md
  │   └── QUICK_START.md
  ├── sessions/ (dated session logs)
  │   └── 2025-11-12/
  │       ├── handoff.md
  │       ├── gitops.md
  │       └── test_results.md
  ├── incidents/ (root cause analyses)
  │   ├── 2025-11-12-artifact-collision.md
  │   ├── 2025-11-12-hallucination.md
  │   └── 2025-11-11-freeze-death-spiral.md
  └── schema/
      └── knowledge_graph.sql
```

#### 3.2 Deprecation Plan
```
DELETE from root:
- *.STALE.py files
- Session handoff docs older than 7 days
- One-off test result files

MOVE to appropriate dirs:
- Quick refs → hfo_gem/gen_30/docs/
- Session logs → hfo_gem/gen_30/sessions/YYYY-MM-DD/
- Incident analyses → hfo_gem/gen_30/incidents/
```

### PHASE 4: Launcher Consolidation

#### 4.1 Unified CLI
```
CREATE: hfo_cli.py (single entry point)

python hfo_cli.py mission --level=0 "Research X"
python hfo_cli.py mission --level=1 --models=diverse "Research X"
python hfo_cli.py mission --level=2 --holons=10 "Research X"
python hfo_cli.py bootstrap  # Gen 1-29 audit
python hfo_cli.py validate   # Run test suite
```

#### 4.2 Scripts Organization
```
scripts/
  ├── launch/
  │   ├── l0_simple.sh
  │   ├── l1_quorum.sh
  │   ├── l2_fractal.sh
  │   └── multimodel.sh
  ├── dev/
  │   ├── check_tooling.sh
  │   └── run_tests.sh
  └── ops/
      ├── backup_runs.sh
      └── compress_old_runs.sh
```

---

## 📊 METRICS: Current vs Target State

| Metric | Current | Target | Gap |
|--------|---------|--------|-----|
| Orchestrator variants | 8-10 | 2 | -75% |
| Test files (root) | 20+ | 0 | Move to tests/ |
| Test files (tests/) | 4 | 10 | Consolidate patterns |
| Launcher scripts | 22 | 1 CLI + 4 helpers | -80% |
| Root markdown files | 60+ | 5 max | -90% |
| Config touch points | 100+ `os.getenv()` | 1 SSOT import | ✅ 50% done |
| Entry point clarity | ❌ Confused | ✅ Clear registry | Need ENTRY_POINTS.md |
| L0 stability | ⚠️ Works sometimes | ✅ Always works | Fix artifact factory |
| L1 stability | ⚠️ Works sometimes | ✅ Always works | SSOT migration |
| L2 stability | ❌ Artifact collision | ✅ Always works | Factory pattern |

---

## 🚦 RECOMMENDED EXECUTION ORDER

### IMMEDIATE (This Week)
1. ✅ Create this inventory (DONE)
2. ⏳ Implement artifact factory pattern (FractalArtifactFactory)
3. ⏳ Migrate gen30_orchestrator.py to SSOT config
4. ⏳ Create ENTRY_POINTS.md registry
5. ⏳ Run L0/L1/L2 smoke tests to establish baseline

### SHORT-TERM (Next Week)
6. ⏳ Consolidate test suite (canonical pyramid)
7. ⏳ Archive experimental tests
8. ⏳ Move docs to hfo_gem/gen_30/ structure
9. ⏳ Delete stale orchestrators/tests
10. ⏳ Create unified hfo_cli.py

### MEDIUM-TERM (Within Month)
11. ⏳ Integrate stigmergy_coordinator into Gen30Orchestrator
12. ⏳ Implement knowledge graph migration from AGENTS.md
13. ⏳ Full L3 (1000) validation with new factory pattern
14. ⏳ Performance benchmarking suite

---

## 🎯 SUCCESS CRITERIA

**L0 Stability**:
- ✅ Single researcher always completes (99% success rate)
- ✅ Tool access works reliably
- ✅ Artifacts always created correctly
- ✅ Config loaded from SSOT only

**L1 Stability**:
- ✅ 10 researchers always complete (95% success rate)
- ✅ Quorum consensus detected
- ✅ Hallucination detection works
- ✅ DIGEST.md always generated

**L2 Stability**:
- ✅ 100 researchers (10 holons) always complete (90% success rate)
- ✅ Each holon has unique artifact directory
- ✅ 10 L1 digests + 1 L2 meta-digest generated
- ✅ No artifact collisions
- ✅ Graceful degradation if some holons timeout

**Configuration**:
- ✅ Zero `os.getenv()` calls outside hfo_gem/gen_30/config.py
- ✅ All timeouts configurable via SSOT
- ✅ All models configurable via SSOT
- ✅ Single import for all orchestrators

**User Experience**:
- ✅ Clear entry points documented
- ✅ One command to run L0/L1/L2
- ✅ Predictable artifact structure
- ✅ <5 files at repo root

---

## 📝 NEXT ACTIONS (In Order)

1. **Review this inventory with user** - Confirm priorities
2. **Implement FractalArtifactFactory** - Fix L2 artifact collision
3. **Migrate gen30_orchestrator.py to SSOT** - Eliminate config sprawl
4. **Create ENTRY_POINTS.md** - Document canonical usage
5. **Run baseline tests** - Establish L0/L1/L2 success rates
6. **Execute Phase 1** - Stabilize core before scaling

---

**Status**: 📋 INVENTORY COMPLETE - Ready for consolidation execution
