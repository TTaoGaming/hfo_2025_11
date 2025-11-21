# Hive Guards Architecture - Gen 32

**Status**: FORMALIZED - 2025-11-16
**Role**: IMMUNIZER (OBSIDIAN 8 Roles - Blue Team Protection)
**Philosophy**: Defense in Depth - Multiple Guard Layers at Different Lifecycle Stages

---

## Motivation

**CRITICAL INCIDENT**: Third recurrence of file corruption (2025-11-16)
- AI assistant mixed markdown into Python code during SOTA upgrade
- hfo.py + hfo_sdk/__init__.py corrupted with SyntaxError
- No automated validation caught corruption until user execution
- 85 minutes to diagnose and restore from molt shell backups

**ROOT CAUSE**: Single-layer validation insufficient
- Only runtime execution caught corruption
- No pre-commit checks
- No active monitoring during file edits
- No scheduled health checks

**SOLUTION**: Four Classes of Hive Guards (Defense in Depth)

---

## Design Philosophy

### Core Principle
**All Hive Guards are subset of IMMUNIZER role** (OBSIDIAN 8 roles)

IMMUNIZER = Blue Team protection against:
- Hallucinations (fabricated facts)
- Context drift (mission objective rewriting)
- Code corruption (syntax errors, circular imports)
- System degradation (dependency drift, SOTA deltas)
- Resource exhaustion (memory leaks, process bloat)
- Byzantine failures (consensus collapse, quorum loss)

### Defense in Depth
Multiple guard layers operating at different lifecycle stages:
1. **Static Guards**: Fast deterministic checks (pre-commit, CI/CD)
2. **Active Guards**: LLM-powered runtime monitoring (during missions)
3. **Pre-Commit Guards**: Git hooks blocking bad commits
4. **Scheduled Guards**: Automated periodic health checks

Each layer catches different failure modes. Overlap is intentional (redundancy).

---

## Class 1: Static Guards (No LLM)

**Type**: Fast deterministic validation (<5 seconds)
**Execution**: Pre-commit hooks + CI/CD workflows
**Cannot hallucinate**: Pure Python logic, no LLM dependency

### Examples
1. **Syntax Validation**
   - `python3 -m py_compile *.py`
   - Catch SyntaxError before commit
   - Prevents file corruption incidents

2. **Import Smoke Tests**
   - `python3 -c "from hfo_sdk import byzantine_consensus"`
   - Verify critical imports work
   - Catch circular import loops

3. **Markdown Detection**
   - `grep -l "^```" *.py`
   - Flag code blocks in Python files
   - Prevents documentation-in-code corruption

4. **Artifact Structure Validation**
   - Check DIGEST.md exists
   - Verify researcher_*.md files (10 expected for L1)
   - Validate quorum_analysis.md + hallucinations.md

5. **File Size Anomalies**
   - Flag files >10KB growth in single commit
   - Detect accidental paste/merge operations

### Implementation
```python
# scripts/safeguards/static_guards.py

def run_static_guards():
    """Run all static guards (fast, deterministic)."""

    # Guard 1: Syntax validation
    for file in Path('.').glob('**/*.py'):
        subprocess.run(['python3', '-m', 'py_compile', file], check=True)

    # Guard 2: Import smoke tests
    subprocess.run(['python3', '-c', 'from hfo_sdk import byzantine_consensus'], check=True)

    # Guard 3: Markdown detection
    result = subprocess.run(['grep', '-l', '^```', '*.py'], capture_output=True)
    if result.returncode == 0:
        raise ValueError(f"Markdown found in Python files: {result.stdout}")

    # Guard 4: Artifact structure (if swarm run)
    # ...
```

### Status
- ✅ Syntax validation: `scripts/safeguards/pre-commit.sh` created
- ✅ Import smoke tests: Implemented
- ✅ Markdown detection: Implemented
- ⏳ Artifact validation: TODO (Guard 1 from gen_30/hive_guards)
- ⏳ File size checks: TODO

---

## Class 2: Active Guards (LLM-Powered)

**Type**: Real-time monitoring during swarm execution
**Execution**: Runtime (during missions)
**Role**: IMMUNIZER Blue Team - detect and prevent cascading failures

### Examples
1. **Hallucination Detection**
   - Cross-validate researcher citations
   - Check if cited files exist
   - Verify line numbers are accurate
   - Flag fabricated quotes

2. **Quorum Validation**
   - Detect consensus levels (HIGH/MEDIUM/LOW)
   - Flag when quorum fails (<7/10 for L1)
   - Alert on unanimous agreement (potential groupthink)

3. **Citation Verification**
   - Parse citations: `file.py:42-67`
   - Verify file exists in workspace
   - Check line ranges are valid
   - Flag citations to non-existent content

4. **Context Drift Detection**
   - Compare researcher responses to mission intent
   - Flag if researchers analyze different topics
   - Detect mission objective rewriting by orchestrator

5. **Tool Loop Monitoring**
   - Track tool call iterations per researcher
   - Alert on >5 iterations (potential loop)
   - Force finalization after MAX_ITERATIONS

6. **Memory Corruption Detection**
   - Validate precedent retrieval doesn't rewrite intent
   - Check orchestrator prompt matches user request
   - Flag if memory injects unrelated content

### Implementation
```python
# hfo_swarm/active_guards.py

class ActiveGuards:
    """LLM-powered runtime monitoring (IMMUNIZER role)."""

    def __init__(self, orchestrator):
        self.orch = orchestrator
        self.validator_llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)

    def check_hallucinations(self, researcher_responses: List[str]) -> List[str]:
        """Detect fabricated citations via LLM cross-validation."""

        # Extract all citations from responses
        citations = self._extract_citations(researcher_responses)

        # Verify each citation exists
        hallucinations = []
        for cite in citations:
            if not self._citation_exists(cite):
                hallucinations.append(cite)

        return hallucinations

    def check_quorum(self, responses: List[str]) -> str:
        """Detect consensus level via LLM analysis."""

        prompt = f"""Analyze these {len(responses)} researcher responses.
        Identify common themes and disagreements.
        Return consensus level: HIGH (7+/10 agree), MEDIUM (4-6/10), LOW (<4/10)"""

        # ... LLM call to analyze quorum

    def check_context_drift(self, intent: str, responses: List[str]) -> bool:
        """Detect if researchers analyzed different topic than requested."""

        # Compare intent to actual topics discussed
        # Flag if mismatch
```

### Status
- ✅ Hallucination detection: Implemented in `simple_orchestrator.py` (Validator role)
- ✅ Quorum validation: Implemented in `simple_orchestrator.py` (Analyzer role)
- ⚠️ Citation verification: Partial (no line number checks)
- ❌ Context drift: NOT IMPLEMENTED (critical gap - memory can rewrite intent)
- ❌ Tool loop monitoring: NOT IMPLEMENTED (researchers can loop infinitely)
- ❌ Memory corruption: NOT IMPLEMENTED (precedents can hijack mission)

---

## Class 3: Pre-Commit Guards (Blocking)

**Type**: Git commit hooks (Static + Light LLM)
**Execution**: On every `git commit` attempt
**Blocking**: Prevents commit if guards FAIL

### Examples
1. **File Corruption Detection**
   - Run all Static Guards (Class 1)
   - Block commit if syntax errors
   - Require manual override for exceptions

2. **Circular Import Checks**
   - Parse import statements in modified .py files
   - Build dependency graph
   - Flag circular dependencies

3. **API Surface Validation**
   - Check `__all__` exports in modified __init__.py
   - Verify exported functions exist
   - Flag deprecated functions still exported

4. **Documentation Sync**
   - If README.md modified, check if code updated
   - If SSOT changed, flag if Python not regenerated
   - Prevent doc-code drift

5. **Test Coverage**
   - If .py file modified, check if test exists
   - Flag new functions without tests
   - Require coverage >80% (configurable)

### Implementation
```bash
#!/bin/bash
# .git/hooks/pre-commit (symlink to scripts/safeguards/pre-commit.sh)

set -e

echo "🛡️ Hive Guards - Pre-Commit Validation"

# Run all static guards
python3 scripts/safeguards/static_guards.py || exit 1

# Check for circular imports
python3 scripts/safeguards/check_circular_imports.py || exit 1

# Validate API surface
python3 scripts/safeguards/validate_api_surface.py || exit 1

echo "✅ All pre-commit guards passed"
```

### Status
- ⏳ File corruption: `scripts/safeguards/pre-commit.sh` created (not installed)
- ❌ Circular imports: NOT IMPLEMENTED
- ❌ API surface: NOT IMPLEMENTED
- ❌ Documentation sync: NOT IMPLEMENTED
- ❌ Test coverage: NOT IMPLEMENTED

---

## Class 4: Scheduled Guards (Automated)

**Type**: Time-based health checks (hourly/daily/weekly)
**Execution**: Cron jobs or systemd timers
**Alerting**: Notify on degradation trends

### Examples
1. **Dependency Drift Detection** (Daily)
   - Check for upstream package updates
   - Flag breaking changes in dependencies
   - Alert on security vulnerabilities (pip audit)

2. **SOTA Delta Analysis** (Weekly)
   - Compare HFO patterns vs latest research
   - Flag new SOTA techniques (LangGraph, Temporal)
   - Suggest architecture updates

3. **Memory Leak Detection** (Hourly)
   - Monitor process memory usage
   - Flag growth trends (>10% per hour)
   - Alert on near-OOM conditions

4. **Model Roster Health** (Daily)
   - Test all models in weekly roster
   - Flag 404 errors (broken models)
   - Update blacklist automatically

5. **Artifact Trail Integrity** (Weekly)
   - Scan all hfo_swarm_runs/ directories
   - Flag incomplete runs (missing DIGEST.md)
   - Archive old runs (>30 days)

6. **Database Health** (Hourly)
   - Check pgvector connection
   - Validate table sizes (prevent bloat)
   - Test embedding generation latency

### Implementation
```bash
# /etc/systemd/user/hfo-scheduled-guards.timer

[Unit]
Description=HFO Scheduled Guards (Hourly)

[Timer]
OnCalendar=hourly
Persistent=true

[Install]
WantedBy=timers.target
```

```python
# scripts/safeguards/scheduled_guards.py

def run_hourly_guards():
    """Hourly health checks."""
    check_memory_usage()
    check_database_health()
    check_process_count()

def run_daily_guards():
    """Daily health checks."""
    check_dependency_updates()
    check_model_roster_health()
    audit_pip_security()

def run_weekly_guards():
    """Weekly health checks."""
    analyze_sota_deltas()
    audit_artifact_trail()
    generate_health_report()
```

### Status
- ⏳ Systemd timer: `scripts/dev/hfo-watchdog.timer` exists (30s interval - too frequent)
- ❌ Dependency drift: NOT IMPLEMENTED
- ❌ SOTA delta: NOT IMPLEMENTED
- ❌ Memory leak: Partial (watchdog checks process count)
- ❌ Model roster health: NOT IMPLEMENTED
- ❌ Artifact audit: NOT IMPLEMENTED
- ❌ Database health: NOT IMPLEMENTED

---

## Guard Hierarchy

```
IMMUNIZER (OBSIDIAN Role - Blue Team Protection)
│
├── Class 1: Static Guards (Fast, No LLM)
│   ├── Syntax validation
│   ├── Import smoke tests
│   ├── Markdown detection
│   ├── Artifact structure checks
│   └── File size anomalies
│
├── Class 2: Active Guards (LLM-Powered Runtime)
│   ├── Hallucination detection
│   ├── Quorum validation
│   ├── Citation verification
│   ├── Context drift detection
│   ├── Tool loop monitoring
│   └── Memory corruption detection
│
├── Class 3: Pre-Commit Guards (Blocking Git Hooks)
│   ├── All Static Guards (Class 1)
│   ├── Circular import checks
│   ├── API surface validation
│   ├── Documentation sync
│   └── Test coverage enforcement
│
└── Class 4: Scheduled Guards (Time-Based Automation)
    ├── Hourly: Memory leaks, DB health, process count
    ├── Daily: Dependency drift, model health, security audit
    └── Weekly: SOTA deltas, artifact audit, health reports
```

---

## Implementation Roadmap

### Phase 1: Pre-Commit Guards (IMMEDIATE - Prevent Recurrence)
**Priority**: CRITICAL (blocking file corruption incidents)

1. ✅ Create `scripts/safeguards/pre-commit.sh` with static guards
2. ⏳ Install as git hook: `ln -sf ../../scripts/safeguards/pre-commit.sh .git/hooks/pre-commit`
3. ⏳ Test with intentional syntax error (should block commit)
4. ⏳ Add circular import detection
5. ⏳ Add API surface validation
6. ⏳ Document manual override procedure (for emergencies)

**ETA**: 1-2 hours
**Blocker**: None (all tools available)

### Phase 2: Active Guards Enhancement (SHORT-TERM)
**Priority**: HIGH (improve runtime protection)

1. ⏳ Implement context drift detection (LLM validates intent vs responses)
2. ⏳ Add tool loop monitoring (MAX_ITERATIONS enforcement)
3. ⏳ Enhance citation verification (check line numbers, not just file existence)
4. ⏳ Add memory corruption detection (precedents shouldn't rewrite intent)
5. ⏳ Create ActiveGuards class with consolidated LLM validation

**ETA**: 1 week
**Blocker**: Requires LangChain 1.0.x upgrade (✅ COMPLETE)

### Phase 3: Scheduled Guards Framework (MEDIUM-TERM)
**Priority**: MEDIUM (automated health monitoring)

1. ⏳ Adjust watchdog timer interval (30s → hourly for memory/DB checks)
2. ⏳ Add daily dependency drift checks (`pip list --outdated`)
3. ⏳ Add daily model roster health (test all 10 models, update blacklist)
4. ⏳ Add weekly SOTA delta analysis (swarm researches new patterns)
5. ⏳ Add weekly artifact audit (scan hfo_swarm_runs/, archive old runs)
6. ⏳ Create health report dashboard (HTML summary of all checks)

**ETA**: 2-3 weeks
**Blocker**: Requires systemd timer tuning, dashboard UI

### Phase 4: Guard Coverage Expansion (ONGOING)
**Priority**: LOW (expand based on incident patterns)

- Add guards for new failure modes as discovered
- Analyze incident logs for patterns
- Use Byzantine consensus to design new guards
- Document guard rationale in AGENTS.md

---

## Guard Design Principles

### 1. Fail Fast
Guards should detect issues EARLY in lifecycle:
- Static guards at commit time (before code enters main branch)
- Active guards during execution (before cascading failures)
- Scheduled guards between executions (catch slow degradation)

### 2. No False Negatives
**Better to over-alert than miss critical issues.**
- Static guards: Zero tolerance (block all syntax errors)
- Active guards: High sensitivity (flag potential hallucinations)
- Scheduled guards: Trend detection (alert on degradation patterns)

### 3. Minimal False Positives
**But don't cry wolf - users will disable noisy guards.**
- Use multiple signals before alerting
- Provide clear diagnostics (file:line, not vague errors)
- Allow manual overrides with justification

### 4. Self-Healing Where Possible
**Guards should fix problems, not just report them.**
- Static guards: Auto-format code where unambiguous
- Active guards: Auto-filter broken models (blacklist)
- Scheduled guards: Auto-archive old runs, prune memory

### 5. Defense in Depth
**Multiple layers catch different failure modes.**
- Don't rely on single guard class
- Overlap is intentional (redundancy prevents blind spots)
- Each layer has different trust model (static=deterministic, active=LLM, scheduled=trends)

### 6. No LLM Dependency for Critical Guards
**Static guards cannot hallucinate - pure Python logic.**
- Syntax validation: `py_compile` (no LLM)
- Import tests: `python -c "import ..."` (no LLM)
- File checks: `os.path.exists()` (no LLM)
- Active guards MAY use LLM (hallucination detection requires reasoning)

---

## Incident Prevention Matrix

| Incident Type | Class 1 (Static) | Class 2 (Active) | Class 3 (Pre-Commit) | Class 4 (Scheduled) |
|---------------|------------------|------------------|----------------------|---------------------|
| File corruption (markdown-in-code) | ✅ Markdown detection | ❌ | ✅ Syntax validation | ❌ |
| Circular imports | ❌ | ❌ | ⏳ Dependency graph | ⏳ Import smoke test |
| Hallucinations | ❌ | ✅ Citation check | ❌ | ❌ |
| Context drift | ❌ | ⏳ Intent validation | ❌ | ❌ |
| Tool loops | ❌ | ⏳ Iteration monitor | ❌ | ❌ |
| Memory corruption | ❌ | ⏳ Precedent audit | ❌ | ⏳ Memory integrity |
| Dependency drift | ❌ | ❌ | ❌ | ⏳ pip outdated |
| Model roster decay | ❌ | ✅ Self-healing blacklist | ❌ | ⏳ Health test |
| Artifact bloat | ❌ | ❌ | ❌ | ⏳ Auto-archive |
| Resource exhaustion | ❌ | ❌ | ❌ | ⏳ Process monitor |

**Legend**: ✅ Implemented, ⏳ Planned, ❌ Not applicable

---

## Testing Strategy

### Guard Validation
Each guard class must have:
1. **Unit tests**: Guard logic in isolation
2. **Integration tests**: Guard + actual codebase
3. **Regression tests**: Known incidents should be caught

### Test Matrix
```python
# tests/test_static_guards.py

def test_syntax_guard_catches_corruption():
    """Guard should block commit with syntax error."""
    # Create file with syntax error
    # Run static guards
    # Assert: FAIL

def test_markdown_guard_catches_code_blocks():
    """Guard should flag ``` in .py files."""
    # Create .py with markdown
    # Run static guards
    # Assert: FAIL

# tests/test_active_guards.py

def test_hallucination_guard_flags_fake_citation():
    """Guard should detect non-existent file citations."""
    # Researcher cites fake_file.py:42
    # Run active guard
    # Assert: Hallucination flagged

# tests/test_precommit_guards.py

def test_precommit_blocks_corrupted_file():
    """Git hook should prevent commit with syntax error."""
    # Stage file with syntax error
    # Run pre-commit hook
    # Assert: Commit blocked
```

---

## Metrics & Observability

### Guard Health Metrics
Track per guard class:
- **Execution time**: How long do guards take?
- **Detection rate**: How many issues caught?
- **False positive rate**: How often do guards cry wolf?
- **Override frequency**: How often are guards bypassed?

### System Health Metrics
Track overall system:
- **Incident recurrence**: Are we catching known issues?
- **Time to detection**: How fast do guards catch problems?
- **Time to resolution**: How long to fix flagged issues?
- **Guard coverage**: What % of codebase has guard protection?

### Dashboard
```
HFO Hive Guards Health Dashboard
═══════════════════════════════════════
Static Guards (Class 1)
  ✅ Syntax validation: 100% coverage, 0.5s avg
  ✅ Import tests: 15 imports checked, 1.2s avg
  ✅ Markdown detection: 247 .py files scanned

Active Guards (Class 2)
  ✅ Hallucination detection: 8/10 missions, 0 false positives
  ⚠️  Context drift: NOT IMPLEMENTED
  ⚠️  Tool loops: NOT IMPLEMENTED

Pre-Commit Guards (Class 3)
  ⚠️  Not installed (manual execution only)

Scheduled Guards (Class 4)
  ⏳ Timer interval: 30s (too frequent, should be hourly)
  ❌ Dependency drift: NOT IMPLEMENTED
  ❌ SOTA delta: NOT IMPLEMENTED

Incidents Prevented (Last 7 Days)
  - 0 file corruptions (guards not installed yet)
  - 3 hallucinations caught
  - 2 quorum failures flagged
```

---

## Future Enhancements

### Self-Improving Guards (Gen 33+)
- **Byzantine guard design**: 10 researchers propose new guards based on incident patterns
- **Evolutionary algorithms**: Mutate guard logic, keep high-detection variants
- **Meta-guards**: Guards that monitor other guards (prevent guard drift)

### LLM-Assisted Debugging (Active Guards)
- **Root cause analysis**: When guard fails, LLM explains why
- **Fix suggestions**: Guard proposes code changes to resolve issue
- **Auto-fix mode**: Guard applies fixes if high confidence (user approval required)

### Distributed Guards (L2+ Swarms)
- **Guard sharding**: Different guards run on different nodes
- **Quorum validation**: 3+ guards must agree before flagging issue
- **Byzantine fault tolerance**: Guards tolerate 1-2 failures

---

## Conclusion

**Hive Guards = IMMUNIZER Role Formalized**

Four classes of guards provide defense in depth:
1. **Static**: Fast deterministic checks (pre-commit, CI/CD)
2. **Active**: LLM-powered runtime monitoring (Blue Team)
3. **Pre-Commit**: Blocking git hooks (prevent bad commits)
4. **Scheduled**: Automated periodic health (catch slow drift)

**Immediate Priority**: Implement Pre-Commit Guards (Class 3) to prevent file corruption recurrence.

**Next Steps**:
1. Install pre-commit hook: `ln -sf ../../scripts/safeguards/pre-commit.sh .git/hooks/pre-commit`
2. Test with intentional corruption
3. Enhance Active Guards (context drift, tool loops)
4. Tune Scheduled Guards (30s → hourly)

**Status**: Architecture formalized, Phase 1 ready for implementation.

---

**Author**: HiveFleetObsidian Gen 32 Swarmlord
**Date**: 2025-11-16
**Logged to Memory**: ✅ pgvector (mission_id=79, 80)
**References**: FILE_RESTORATION_COMPLETE.md, AGENTS.md (2025-11-16 incident)
