# 🛡️ HFO HIVE GUARDS - Quick Reference

**OBSIDIAN Immunizer Role** | Static Validation | Fail Fast

---

## One-Line Commands

```bash
# Validate latest swarm run
./check_swarm.sh

# Validate specific run
python validate_swarm_run.py hfo_swarm_runs/2025-11-13/run_123456_*

# Run all guards
python hfo_gem/gen_30/hive_guards/guard_runner.py

# Run specific guard
python hfo_gem/gen_30/hive_guards/guard_runner.py --guards swarm_run

# Test pre-commit hook
git add . && git commit -m "Test guards"

# Bypass pre-commit (emergency only)
git commit --no-verify -m "Emergency bypass"
```

---

## The 5 Guards

| # | Guard | Status | What It Checks |
|---|-------|--------|----------------|
| 1 | Swarm Run | ✅ | L0-L3 artifacts, fractal nesting, log10 scaling |
| 2 | Config | ⏳ | SSOT schema, JSON/YAML validation |
| 3 | Generation | ⏳ | Active gen only, no archived edits |
| 4 | Hallucination | ⏳ | Citation validity, no fabricated data |
| 5 | Molt Shell | ⏳ | Read-only enforcement |

---

## Integration Points

✅ **Pre-Commit Hook**
- Location: `.git/hooks/pre-commit`
- Runs: Automatically on `git commit`
- Blocks: Invalid swarm runs, archived gen edits

✅ **CI/CD (GitHub Actions)**
- Location: `.github/workflows/hive-guards.yml`
- Runs: On push/PR
- Blocks: Merge if guards fail

⏳ **Post-Execution** (TODO)
- Location: `simple_orchestrator.py`
- Runs: After mission execution
- Marks: Invalid runs automatically

---

## Expected Artifact Structure

### L0 (1 Researcher)
```
run_HHMMSS_intent_slug/
├── metadata.json              # level: 0
├── 01_orchestration/
│   └── mission_brief.md
├── 02_research/
│   └── researcher_01.md
├── 03_validation/
│   ├── quorum_analysis.md
│   └── hallucinations.md
└── 04_synthesis/
    ├── executive_summary.md
    └── DIGEST.md
```

### L1 (10 Researchers)
```
run_HHMMSS_intent_slug_l1/
├── metadata.json              # level: 1
├── 01_orchestration/
├── 02_research/
│   ├── researcher_01.md       # × 10
│   └── ...
├── 03_validation/
├── 04_synthesis/
└── DIGEST.md                  # L1 digest
```

### L2 (100 Researchers = 10 L1)
```
run_HHMMSS_intent_slug_l2/
├── metadata.json              # level: 2
├── 01_orchestration/
├── 02_research/               # 100 L0 artifacts
├── 03_validation/
├── 04_synthesis/
├── l1_runs/                   # 10 L1 subdirectories
│   ├── run_*_l1_holon_01/
│   └── ...
└── DIGEST.md                  # L2 meta-digest
```

---

## Guard Philosophy

**Static Validation**:
- ✅ No LLM calls (can't hallucinate)
- ✅ Deterministic (same input = same output)
- ✅ Fast (<5 seconds total)
- ✅ Clear errors (file:line precision)

**Fail Fast**:
- ❌ Block commit if invalid
- ❌ Block merge if invalid
- ❌ Mark run invalid if failed
- ❌ Prevent cascade failures

**RED TEST Philosophy**:
- Guards define expected behavior FIRST
- Code must conform to guards
- Failing guard = failing test
- Fix code, not guards

---

## Common Errors

### Error: "Missing required artifact"
```
❌ Missing: 03_validation/quorum_analysis.md
   Expected at: hfo_swarm_runs/.../03_validation/quorum_analysis.md
```
**Fix**: Check orchestrator validation step, ensure quorum analysis runs

### Error: "L1 fractal nesting violation"
```
❌ L1 run missing L1 digest
   Expected: DIGEST.md with level: 1
```
**Fix**: Check synthesizer creates L1 digest, not just L0 digests

### Error: "Generation boundary violation"
```
❌ Archived generation modified: hfo_gem/gen_29/README.md
   Only gen_30 should be modified
```
**Fix**: Revert changes to archived gen, edit only active gen

### Error: "Level metadata mismatch"
```
❌ metadata.json level mismatch
   Declared: 1, Expected: 0 (based on artifact count)
```
**Fix**: Check orchestrator sets correct level in metadata.json

---

## Emergency Procedures

### Pre-commit blocked incorrectly
```bash
# Bypass guard (document why!)
git commit --no-verify -m "Bypass: guards have bug"

# File issue for guard fix
# Re-run guards manually later
```

### CI/CD failing on GitHub
```bash
# Pull branch locally
git pull origin your-branch

# Run guards manually
python hfo_gem/gen_30/hive_guards/guard_runner.py

# Fix issues
# Push again
git push origin your-branch
```

### Guard has false positive
```bash
# Document issue in AGENTS.md
# Create issue for guard improvement
# Use --no-verify bypass if urgent
# Fix guard ASAP
```

---

## File Locations

```
📁 Hive Guards Infrastructure
├── 📄 HIVE_GUARDS_SPEC.md              # Complete specification
├── 📄 HIVE_GUARDS_GITOPS.md            # GitOps integration guide
├── 📄 HIVE_GUARDS_QUICK_REF.md         # This file
├── 📁 hive_guards/
│   ├── 📄 guard_runner.py              # Runs all guards
│   ├── 📄 swarm_run_validator.py       # Guard 1 ✅
│   ├── 📄 config_validator.py          # Guard 2 ⏳
│   ├── 📄 generation_guard.py          # Guard 3 ⏳
│   ├── 📄 hallucination_guard.py       # Guard 4 ⏳
│   └── 📄 molt_shell_guard.py          # Guard 5 ⏳
├── 📄 ../../scripts/pre-commit-guards.sh  # Pre-commit hook
├── 📄 ../../.github/workflows/hive-guards.yml  # CI/CD
├── 📄 ../../validate_swarm_run.py      # Quick wrapper
└── 📄 ../../check_swarm.sh             # One-command check
```

---

## Development Workflow

### Test guard locally
```bash
# Create test run (or use existing)
python run_swarm.py

# Validate
./check_swarm.sh

# Should pass or show specific errors
```

### Add new guard
```bash
# 1. Create guard file
touch hfo_gem/gen_30/hive_guards/my_guard.py

# 2. Implement (follow swarm_run_validator.py pattern)
# 3. Register in guard_runner.py
# 4. Update HIVE_GUARDS_SPEC.md
# 5. Test
python hfo_gem/gen_30/hive_guards/guard_runner.py --guards my
```

### Update guard
```bash
# 1. Modify guard file
# 2. Test manually
python validate_swarm_run.py

# 3. Run pre-commit (tests integration)
git add . && git commit -m "Update guard"

# 4. Push to test CI/CD
git push origin your-branch
```

---

## Success Indicators

✅ **Pre-commit working**:
- Invalid commits blocked automatically
- Clear error messages shown
- Valid commits pass through

✅ **CI/CD working**:
- Guards run on every push/PR
- Results visible in Actions tab
- Merge blocked if guards fail

✅ **Guards effective**:
- Catch issues before they spread
- <5 second execution time
- <1% false positive rate
- Clear actionable errors

✅ **Developer experience**:
- Guards help, not hinder
- Errors guide fixes
- Emergency bypass available
- Documentation clear

---

## Quick Troubleshooting

| Symptom | Likely Cause | Fix |
|---------|--------------|-----|
| Commit blocked | Invalid artifacts | Run `./check_swarm.sh` to see errors |
| CI/CD failing | Same as pre-commit | Pull branch, run guards locally |
| False positive | Guard bug | File issue, use `--no-verify` bypass |
| Guard slow | Too many checks | Profile guard, optimize |
| No error message | Guard crashed | Check guard_runner.py for exceptions |

---

## Key Metrics

**Guard Performance**:
- Target: <5 seconds total
- Current: ~2 seconds (Guard 1 only)
- Budget: 1 second per guard

**Guard Coverage**:
- Implemented: 1/5 guards (20%)
- Next: Config validator, Generation guard
- Goal: 5/5 guards by end of week

**False Positive Rate**:
- Target: <1%
- Current: 0% (no false positives yet)
- Action: Monitor and tune thresholds

---

## References

📖 **HIVE_GUARDS_SPEC.md** - Complete specification
📖 **HIVE_GUARDS_GITOPS.md** - GitOps integration
📖 **SWARM_RUN_VALIDATOR_GUIDE.md** - Guard 1 details
📖 **AGENTS.md** - Incident log and philosophy

---

**Role**: OBSIDIAN Immunizer
**Purpose**: Static validation guards
**Philosophy**: Fail fast, clear errors, no hallucinations
**Status**: ✅ Pre-commit + CI/CD active, 1/5 guards implemented
