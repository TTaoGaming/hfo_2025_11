# HFO Hive Guards - Immunizer Role Static Validators

**Role**: Immunizer (OBSIDIAN Architecture)
**Sub-Role**: Hive Static Guards
**Type**: Static validation and verification (hallucination-resistant)
**Status**: Active

---

## Philosophy

**Hive Guards are STATIC** - they don't learn, adapt, or change behavior based on LLM input. They are **deterministic validators** that check invariants.

**Why Static Guards?**
- ❌ LLMs can hallucinate → Guards use regex, file existence checks, JSON schema
- ❌ LLMs can be prompt-injected → Guards hardcoded in Python
- ❌ LLMs can drift → Guards are versioned in Git
- ✅ Guards are **predictable, auditable, reproducible**

**Immunizer Role** (OBSIDIAN):
- Protects swarm from contamination
- Detects hallucination early (before it spreads)
- Enforces invariants (log10 scaling, fractal nesting, level metadata)
- Fails fast (pre-commit, CI/CD, post-execution)

---

## Hive Guards Roster

### Guard 1: Swarm Run Validator
**File**: `hfo_gem/gen_30/swarm_run_validator.py`
**Checks**: Artifact structure, level metadata, fractal nesting
**When**: Post-execution, pre-commit, CI/CD

### Guard 2: SSOT Config Validator (TODO)
**File**: `hfo_gem/gen_30/config_validator.py`
**Checks**: Config schema, required fields, type consistency
**When**: Pre-commit, CI/CD

### Guard 3: Gen Boundary Guard (TODO)
**File**: `hfo_gem/gen_30/generation_guard.py`
**Checks**: No edits to archived generations, active gen only
**When**: Pre-commit

### Guard 4: Hallucination Pattern Detector (TODO)
**File**: `hfo_gem/gen_30/hallucination_guard.py`
**Checks**: Fabricated citations, contradiction patterns, confidence violations
**When**: Post-swarm-execution

### Guard 5: Molt Shell Immutability Guard (TODO)
**File**: `hfo_gem/gen_30/molt_shell_guard.py`
**Checks**: Read-only molt shells, no edits to archived snapshots
**When**: Pre-commit

---

## Integration Points

### 1. Pre-Commit Hook
**File**: `.git/hooks/pre-commit`
**Action**: Run all guards before allowing commit
**Failure**: Block commit, show errors

### 2. CI/CD Pipeline
**File**: `.github/workflows/hive-guards.yml`
**Action**: Run all guards on push, PR
**Failure**: Block merge, notify team

### 3. Post-Execution Validation
**File**: Auto-run after `SimpleOrchestrator.execute_mission()`
**Action**: Validate artifacts immediately
**Failure**: Log incident, mark run as invalid

### 4. GitOps Integration
**File**: Auto-validate before `git push`
**Action**: Check all swarm runs are valid
**Failure**: Block push, show validation report

---

## Guard Execution Order

```
┌─────────────────────────────────────────────────┐
│ HIVE STATIC GUARDS (Immunizer Sub-Role)        │
└─────────────────────────────────────────────────┘

PRE-COMMIT (before git commit):
  1. Generation Boundary Guard → No edits to archived gens
  2. Molt Shell Immutability Guard → No edits to archived shells
  3. SSOT Config Validator → Config schema valid
  4. [Allow commit if all pass]

POST-EXECUTION (after swarm mission):
  1. Swarm Run Validator → Artifact structure valid
  2. Hallucination Pattern Detector → No fabricated citations
  3. [Mark run valid/invalid]

CI/CD (on push/PR):
  1. All pre-commit guards
  2. All post-execution guards (on latest runs)
  3. [Block merge if any fail]

GITOPS (before git push):
  1. Swarm Run Validator (all runs in commit)
  2. [Block push if invalid runs detected]
```

---

## Guard Development Rules

### 1. No LLM Dependency
Guards MUST NOT call LLMs or depend on LLM output for validation logic.

**✅ ALLOWED**:
- File existence checks (`Path.exists()`)
- Regex pattern matching (`re.match()`)
- JSON schema validation (`jsonschema.validate()`)
- Line counts, character counts
- Hardcoded thresholds (min 100 chars, etc.)

**❌ FORBIDDEN**:
- Calling OpenAI/OpenRouter APIs
- Using LangChain/LangGraph for validation
- Asking LLM "is this valid?"
- Semantic analysis requiring embeddings

### 2. Deterministic Output
Same input → Same output. No randomness.

**✅ ALLOWED**:
- `assert len(response) >= 100`
- `assert metadata['level'] == 'L1'`
- `assert digest_path.exists()`

**❌ FORBIDDEN**:
- `if random.random() > 0.5: ...`
- `if llm.ask("is this good?"): ...`
- Temperature > 0 for any check

### 3. Fast Execution
Guards should complete in <5 seconds for typical runs.

**Why**: Pre-commit hooks must be fast or developers disable them.

**Optimization**:
- Check file existence before reading full content
- Use regex on metadata sections only (not full file)
- Parallelize independent checks

### 4. Clear Error Messages
Errors must tell developer EXACTLY what to fix.

**❌ BAD**:
```
Error: Validation failed
```

**✅ GOOD**:
```
❌ L1 fractal violation: expected 10 L0 artifacts, got 8
   Missing: researcher_09.md, researcher_10.md
   Fix: Ensure all 10 researchers complete execution
```

### 5. Exit Codes
- `0` = All guards passed
- `1` = One or more guards failed
- `2` = Guard itself has an error (bug in guard code)

---

## File Structure

```
hfo_gem/gen_30/
├── hive_guards/
│   ├── __init__.py
│   ├── swarm_run_validator.py          (Guard 1 - DONE)
│   ├── config_validator.py             (Guard 2 - TODO)
│   ├── generation_guard.py             (Guard 3 - TODO)
│   ├── hallucination_guard.py          (Guard 4 - TODO)
│   ├── molt_shell_guard.py             (Guard 5 - TODO)
│   └── guard_runner.py                 (Run all guards)
│
├── HIVE_GUARDS_SPEC.md                 (This file)
└── swarm_run_validator.py              (Moved to hive_guards/)

scripts/
├── pre-commit-guards.sh                (Pre-commit hook)
└── ci-guards.sh                        (CI/CD validation)

.git/hooks/
└── pre-commit → ../../scripts/pre-commit-guards.sh

.github/workflows/
└── hive-guards.yml                     (CI/CD pipeline)
```

---

## Integration Examples

### Pre-Commit Hook
```bash
#!/bin/bash
# scripts/pre-commit-guards.sh

echo "🛡️  HFO Hive Guards - Pre-Commit Validation"
echo ""

# Guard 3: Generation Boundary
python hfo_gem/gen_30/hive_guards/generation_guard.py || exit 1

# Guard 5: Molt Shell Immutability
python hfo_gem/gen_30/hive_guards/molt_shell_guard.py || exit 1

# Guard 2: SSOT Config
python hfo_gem/gen_30/hive_guards/config_validator.py || exit 1

echo "✅ All pre-commit guards passed"
```

### CI/CD GitHub Actions
```yaml
name: Hive Guards CI

on: [push, pull_request]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2

      - name: Setup Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.10'

      - name: Run Hive Guards
        run: |
          python hfo_gem/gen_30/hive_guards/guard_runner.py --all

      - name: Validate Latest Swarm Runs
        run: |
          python validate_swarm_run.py || exit 1
```

### Post-Execution Auto-Validation
```python
# hfo_swarm/simple_orchestrator.py

def execute_mission(self, ...):
    # ... execute swarm ...

    # Auto-run Hive Guards
    from hfo_gem.gen_30.hive_guards.guard_runner import run_guards

    result = run_guards(
        run_dir=artifacts.run_dir,
        guards=['swarm_run_validator', 'hallucination_guard']
    )

    if not result.success:
        logger.warning(f"Hive Guards failed: {result.errors}")
        # Mark run as invalid in metadata
        artifacts.mark_invalid(result.errors)

    return digest
```

---

## Incident Response

### When Guards Fail

**Pre-Commit**:
1. Guard blocks commit
2. Developer sees error message
3. Developer fixes issue
4. Developer re-runs `git commit`
5. Guards re-validate
6. Commit allowed if pass

**CI/CD**:
1. Guard fails in GitHub Actions
2. PR blocked from merge
3. Team notified in Slack/Discord
4. Developer fixes issue
5. Push new commit
6. CI re-runs guards

**Post-Execution**:
1. Guard detects invalid swarm run
2. Run marked as invalid in metadata
3. Incident logged to AGENTS.md
4. Human reviews before using results
5. Orchestrator fixed
6. Re-run mission
7. Guards validate again

---

## Success Criteria

**Guard is READY when**:
- ✅ Deterministic (same input → same output)
- ✅ Fast (<5 seconds typical case)
- ✅ Clear error messages
- ✅ No LLM dependency
- ✅ Exit code 0/1/2
- ✅ Integrated into pre-commit hook
- ✅ Integrated into CI/CD
- ✅ Documented in HIVE_GUARDS_SPEC.md

**System is PROTECTED when**:
- ✅ All 5 guards implemented
- ✅ Pre-commit hook active
- ✅ CI/CD pipeline active
- ✅ Post-execution validation active
- ✅ 100% guard pass rate on main branch

---

## Current Status

### Implemented ✅
- **Guard 1**: Swarm Run Validator (450 lines)
- **Infrastructure**: Quick check script (`./check_swarm.sh`)
- **Documentation**: SWARM_RUN_VALIDATOR_GUIDE.md

### TODO ⏳
- **Guard 2**: SSOT Config Validator
- **Guard 3**: Generation Boundary Guard
- **Guard 4**: Hallucination Pattern Detector
- **Guard 5**: Molt Shell Immutability Guard
- **Integration**: Pre-commit hook setup
- **Integration**: CI/CD GitHub Actions
- **Integration**: Post-execution auto-validation

---

## Next Steps

1. **Reorganize** Guard 1 into `hfo_gem/gen_30/hive_guards/`
2. **Create** `guard_runner.py` to run all guards
3. **Implement** pre-commit hook
4. **Implement** CI/CD pipeline
5. **Implement** remaining guards (2-5)
6. **Test** full integration end-to-end
7. **Document** in Gen 30 README

---

## Philosophy

**Hive Guards are the IMMUNE SYSTEM of HFO.**

They don't reason, they don't learn, they don't adapt. They **enforce invariants** ruthlessly and **fail fast** when violations detected.

They are the **last line of defense** against:
- Hallucination spiral (fabricated content spreading)
- Artifact corruption (empty files, missing metadata)
- Generation drift (editing archived gens)
- SSOT violations (scattered config, contradictions)

**Static guards >> Dynamic validation** for immune system.

**Immunizer Role** = Hive Guards + Hallucination Detector + Quorum Validator

---

**Status**: Specification complete, Guard 1 implemented, integration pending
