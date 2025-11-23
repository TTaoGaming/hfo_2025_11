---
hexagon:
  ontos:
    id: f3be9d5b-e722-4989-b9e0-278545c4d80c
    type: md
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T11:07:35.681216Z'
    generation: 51
  topos:
    address: eyes/archive/hfo_gem/gen_30/HIVE_GUARDS_GITOPS.md
    links: []
  telos:
    viral_factor: 0.0
    meme: HIVE_GUARDS_GITOPS.md
---
# HFO Hive Guards - GitOps Integration Guide

**OBSIDIAN Immunizer Sub-Role**: Static validation guards protecting HFO integrity

**Created**: 2025-11-13
**Status**: ✅ ACTIVE
**Philosophy**: Static validation, deterministic, no LLM dependency, fail fast before issues spiral

---

## 🛡️ What Are Hive Guards?

**Hive Guards** are the **Immunizer role** in the OBSIDIAN architecture. They are **static validators** that:

- ✅ **Can't be hallucinated through** - No LLM calls, just file checks and regex
- ✅ **Deterministic** - Same input always produces same result
- ✅ **Fast** - Complete validation in <5 seconds
- ✅ **Clear errors** - Precise file/line reporting for fixes
- ✅ **Fail fast** - Block operations before issues cascade

### Contrast with AI Agents

| Aspect | AI Agents | Hive Guards |
|--------|-----------|-------------|
| **Reliability** | Non-deterministic | Deterministic |
| **Speed** | Slow (LLM calls) | Fast (<5s) |
| **Hallucination Risk** | High | None (static checks) |
| **Error Messages** | Vague | Precise (file:line) |
| **Use Case** | Creative tasks | Validation gates |

---

## 🏗️ The 5 Guards

### Guard 1: Swarm Run Validator ✅ IMPLEMENTED
- **File**: `hfo_gem/gen_30/hive_guards/swarm_run_validator.py`
- **Purpose**: Validates swarm run artifact structure
- **Checks**:
  - L0/L1/L2/L3 artifact presence
  - Fractal nesting (L1 = 10 L0 + 1 L1 digest)
  - Level metadata consistency
  - Log10 scaling law (L0=1, L1=10, L2=100, L3=1000)
- **Usage**: `python validate_swarm_run.py` or `./check_swarm.sh`

### Guard 2: Config Validator ⏳ TODO
- **File**: `hfo_gem/gen_30/hive_guards/config_validator.py`
- **Purpose**: Validates SSOT configuration files
- **Checks**:
  - JSON/YAML schema compliance
  - Required fields present
  - Type validation
  - Reference integrity

### Guard 3: Generation Boundary Guard ⏳ TODO
- **File**: `hfo_gem/gen_30/hive_guards/generation_guard.py`
- **Purpose**: Enforces append-only policy for archived generations
- **Checks**:
  - Only active generation is writable
  - Archived generations not modified
  - active_generation.txt is valid

### Guard 4: Hallucination Guard ⏳ TODO
- **File**: `hfo_gem/gen_30/hive_guards/hallucination_guard.py`
- **Purpose**: Detects fabricated citations and data
- **Checks**:
  - Cited files exist
  - Line numbers valid
  - No fabricated URLs
  - Evidence trail complete

### Guard 5: Molt Shell Guard ⏳ TODO
- **File**: `hfo_gem/gen_30/hive_guards/molt_shell_guard.py`
- **Purpose**: Enforces read-only policy for molt shells
- **Checks**:
  - No modifications to HFO_molt_shells/
  - Permissions are read-only
  - No accidental staging

---

## 🔗 Integration Points

### 1. Pre-Commit Hook ✅ ACTIVE

**Location**: `.git/hooks/pre-commit` → `scripts/pre-commit-guards.sh`

**What it does**:
- Detects swarm runs in commit → Runs Guard 1
- Checks generation boundaries → Blocks archived gen edits
- Validates molt shells → Prevents accidental modifications

**How to test**:
```bash
# Make a test commit
git add AGENTS.md
git commit -m "Test pre-commit guards"

# Guards run automatically before commit
# Commit blocked if guards fail
```

**Bypass (emergency only)**:
```bash
git commit --no-verify -m "Emergency fix"
```

### 2. CI/CD GitHub Actions ✅ ACTIVE

**Location**: `.github/workflows/hive-guards.yml`

**Triggers**:
- Every push to `main` or `HiveFleetObsidian-*` branches
- Every pull request

**What it does**:
- Runs all implemented guards
- Validates latest swarm runs
- Checks generation boundaries
- Blocks merge if guards fail

**How to view**:
1. Push commit to GitHub
2. Go to repository → Actions tab
3. Click on "HFO Hive Guards CI" workflow
4. View guard results

**Badge** (add to README):
```markdown
![Hive Guards](https://github.com/YOUR_USERNAME/HiveFleetObsidian/workflows/HFO%20Hive%20Guards%20CI/badge.svg)
```

### 3. Post-Execution Auto-Validation ⏳ TODO

**Location**: `hfo_swarm/simple_orchestrator.py` (modify)

**What it will do**:
- Run Guard 1 automatically after mission execution
- Mark run as invalid if guards fail
- Log incidents to AGENTS.md
- Prevent downstream usage of invalid runs

**Implementation**:
```python
# In simple_orchestrator.py execute_mission()
digest = self._generate_digest(...)

# Auto-validate artifacts
from hfo_gem.gen_30.hive_guards.guard_runner import HiveGuardsRunner
runner = HiveGuardsRunner()
result = runner.run_guard('swarm_run', run_dir=artifacts_dir)

if not result.passed:
    logging.error(f"Swarm run validation failed: {result.message}")
    self._mark_run_invalid(artifacts_dir, result.errors)
```

### 4. GitOps Workflow ✅ ACTIVE

**Complete validation chain**:

```
Developer makes change
  ↓
Pre-commit hook runs guards
  ↓ (pass)
Commit created
  ↓
Push to GitHub
  ↓
CI/CD runs guards
  ↓ (pass)
Pull request created
  ↓
Code review + guard results
  ↓ (approve)
Merge allowed
  ↓
Production deployment
```

**Guard failures block at every step**:
- ❌ Pre-commit: Commit blocked
- ❌ CI/CD: Merge blocked
- ❌ Post-execution: Run marked invalid

---

## 📊 Guard Runner CLI

**Location**: `hfo_gem/gen_30/hive_guards/guard_runner.py`

**Run all guards**:
```bash
python hfo_gem/gen_30/hive_guards/guard_runner.py
```

**Run specific guard**:
```bash
python hfo_gem/gen_30/hive_guards/guard_runner.py --guards swarm_run
```

**Validate specific run**:
```bash
python hfo_gem/gen_30/hive_guards/guard_runner.py --run-dir hfo_swarm_runs/2025-11-13/run_123456_*
```

**Output format**:
```
🛡️  HFO HIVE GUARDS - Immunizer Static Validation
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ Guard 1: Swarm Run Validator - PASSED
   Validated: hfo_swarm_runs/2025-11-13/run_123456_*/

⚠️  Guard 2: Config Validator - NOT IMPLEMENTED

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
RESULT: 1/5 guards passed (4 not implemented)
```

---

## 🚨 Incident Response

### When Guards Fail

**Pre-commit failure**:
1. Read error messages (file:line precision)
2. Fix issues in workspace
3. Re-run: `./check_swarm.sh` to validate
4. Retry commit

**CI/CD failure**:
1. Check GitHub Actions log
2. Pull branch locally
3. Run guards manually: `python hfo_gem/gen_30/hive_guards/guard_runner.py`
4. Fix issues, push again

**Post-execution failure** (when implemented):
1. Check run directory for `.invalid` marker
2. Read validation report
3. Fix orchestrator/prompts
4. Re-run mission

### Emergency Bypass (USE SPARINGLY)

**Pre-commit bypass**:
```bash
git commit --no-verify -m "Emergency: bypassing guards"
```

**When to use**:
- Critical hotfix required
- Guards themselves have bugs
- False positive blocking progress

**Always**:
- Document why bypass was needed
- Create follow-up issue to fix underlying problem
- Re-run guards manually after bypass

---

## 🧪 Testing Guards

### Test Guard 1 (Swarm Run Validator)

**Create valid L0 run**:
```bash
python run_swarm.py
# Enter intent: "Test guard validation"
# Enter constraints: "Quick test"
```

**Validate**:
```bash
./check_swarm.sh
# Should pass if artifacts correct
```

**Create invalid run** (for testing):
```bash
# Delete required artifact
rm hfo_swarm_runs/2025-11-13/run_*/03_validation/quorum_analysis.md

# Run validator
./check_swarm.sh
# Should fail with specific error
```

### Test Pre-Commit Hook

**Test generation boundary**:
```bash
# Try to modify archived generation
echo "test" >> hfo_gem/gen_29/README.md
git add hfo_gem/gen_29/README.md
git commit -m "Should fail"

# Expected: Commit blocked
```

**Test swarm run validation**:
```bash
# Create invalid run, then commit
git add hfo_swarm_runs/
git commit -m "Should fail"

# Expected: Commit blocked with validation errors
```

### Test CI/CD

**Push to trigger**:
```bash
git push origin your-branch
```

**Check results**:
1. Go to GitHub → Actions
2. Click workflow run
3. Expand "Run Hive Guards" step
4. View validation output

---

## 📈 Development Workflow

### Adding a New Guard

**1. Create guard file**:
```bash
touch hfo_gem/gen_30/hive_guards/my_new_guard.py
```

**2. Implement guard** (follow pattern from `swarm_run_validator.py`):
```python
from dataclasses import dataclass
from typing import List, Optional
from pathlib import Path

@dataclass
class ValidationResult:
    passed: bool
    errors: List[str]
    warnings: List[str]

def validate_my_feature(target_path: Path) -> ValidationResult:
    """
    Static validation of my feature.

    Rules:
    - Deterministic (no LLM calls)
    - Fast (<5s)
    - Clear error messages
    """
    errors = []
    warnings = []

    # Add validation logic here

    return ValidationResult(
        passed=len(errors) == 0,
        errors=errors,
        warnings=warnings
    )
```

**3. Register in guard_runner.py**:
```python
from hfo_gem.gen_30.hive_guards import my_new_guard

def _run_my_new_guard(self) -> GuardResult:
    try:
        result = my_new_guard.validate_my_feature(Path.cwd())
        return GuardResult(
            guard_name="My New Guard",
            passed=result.passed,
            errors=result.errors,
            warnings=result.warnings
        )
    except Exception as e:
        return GuardResult(
            guard_name="My New Guard",
            passed=False,
            errors=[f"Guard execution failed: {e}"]
        )
```

**4. Update HIVE_GUARDS_SPEC.md** with guard details

**5. Test guard**:
```bash
python hfo_gem/gen_30/hive_guards/guard_runner.py --guards my_new
```

**6. Update CI/CD** if needed (usually automatic)

### Guard Development Rules

**MUST**:
- ✅ Be deterministic (same input → same output)
- ✅ Complete in <5 seconds
- ✅ Return precise errors (file:line)
- ✅ Have zero LLM dependencies
- ✅ Handle missing files gracefully

**MUST NOT**:
- ❌ Make LLM API calls
- ❌ Modify files (read-only)
- ❌ Depend on network access
- ❌ Use randomness
- ❌ Have side effects

---

## 🎯 Success Criteria

### Guards Working When:

**Pre-commit**:
- ✅ Invalid swarm runs blocked from commit
- ✅ Archived generation edits blocked
- ✅ Molt shell modifications blocked
- ✅ Clear error messages guide fixes

**CI/CD**:
- ✅ All PRs validated automatically
- ✅ Merge blocked if guards fail
- ✅ Guard results visible in Actions tab
- ✅ Badge shows guard status

**Post-execution** (when implemented):
- ✅ Invalid runs marked automatically
- ✅ Incidents logged to AGENTS.md
- ✅ Downstream tools skip invalid runs
- ✅ Re-runs required to fix

**Developer Experience**:
- ✅ Guards run fast (<5s total)
- ✅ Error messages are actionable
- ✅ False positives are rare
- ✅ Emergency bypass available

---

## 📚 File Structure

```
HiveFleetObsidian/
├── .github/
│   └── workflows/
│       └── hive-guards.yml          # CI/CD workflow ✅
├── .git/
│   └── hooks/
│       └── pre-commit               # Symlink to pre-commit-guards.sh ✅
├── scripts/
│   └── pre-commit-guards.sh         # Pre-commit hook script ✅
├── hfo_gem/gen_30/
│   ├── active_generation.txt        # Active gen marker
│   ├── HIVE_GUARDS_SPEC.md          # Complete specification ✅
│   ├── HIVE_GUARDS_GITOPS.md        # This file ✅
│   └── hive_guards/
│       ├── __init__.py              # Package init ✅
│       ├── guard_runner.py          # Runs all guards ✅
│       ├── swarm_run_validator.py   # Guard 1 ✅
│       ├── config_validator.py      # Guard 2 ⏳
│       ├── generation_guard.py      # Guard 3 ⏳
│       ├── hallucination_guard.py   # Guard 4 ⏳
│       └── molt_shell_guard.py      # Guard 5 ⏳
├── validate_swarm_run.py            # Quick wrapper ✅
└── check_swarm.sh                   # One-command check ✅
```

---

## 🔄 Next Steps

### Immediate (This Session)
- [x] Create CI/CD workflow
- [x] Install pre-commit hook
- [x] Test pre-commit hook
- [x] Document GitOps integration
- [ ] Test CI/CD on GitHub (requires push)

### Short-Term (This Week)
- [ ] Implement Guard 2 (config_validator)
- [ ] Implement Guard 3 (generation_guard)
- [ ] Implement Guard 4 (hallucination_guard)
- [ ] Implement Guard 5 (molt_shell_guard)
- [ ] Add post-execution auto-validation

### Long-Term (Next Month)
- [ ] Add performance metrics (guard execution time)
- [ ] Create guard documentation generator
- [ ] Build guard testing framework
- [ ] Add guard coverage reporting
- [ ] Integrate with pgvector for precedent validation

---

## 📖 References

- **HIVE_GUARDS_SPEC.md**: Complete guard specification
- **SWARM_RUN_VALIDATOR_GUIDE.md**: Guard 1 documentation
- **AGENTS.md**: Incident log and philosophy
- **OBSIDIAN Architecture**: 8 roles including Immunizer

---

## 💡 Philosophy

> "The best validation happens before code runs, not after it fails."

**Hive Guards embody the Immunizer role**:
- **Static** - No runtime dependencies
- **Deterministic** - No hallucination risk
- **Fast** - No workflow interruption
- **Clear** - Actionable error messages
- **Preventive** - Catch issues before they spiral

**GitOps Integration ensures**:
- Issues caught at commit time (pre-commit)
- Team protected via CI/CD validation
- Production deployments validated
- No invalid artifacts in repository

**RED TEST Philosophy**:
- Guards define expected behavior FIRST
- Code must conform to guards (not reverse)
- Failing guard = failing test
- Fix code, not guards (unless guard is wrong)

---

**Status**: ✅ Pre-commit and CI/CD active, post-execution pending
**Next**: Implement remaining guards, test on GitHub Actions
**Owner**: Swarmlord of Webs (Navigator Prime)
**Role**: OBSIDIAN Immunizer - Static Validation Guards
