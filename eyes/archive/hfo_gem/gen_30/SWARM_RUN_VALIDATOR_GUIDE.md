# Swarm Run Validator - Quick Reference

## Location

**SSOT**: `hfo_gem/gen_30/swarm_run_validator.py` (canonical source)
**Wrapper**: `validate_swarm_run.py` (root convenience wrapper)

## Usage

### Validate Latest Run
```bash
python validate_swarm_run.py
```

### Validate Specific Run
```bash
python validate_swarm_run.py hfo_swarm_runs/2025-11-13/run_123456_*/
```

### From Gen 30 SSOT
```bash
python hfo_gem/gen_30/swarm_run_validator.py <run_dir>
```

## What It Checks

### Level 0 (L0) - Individual Researcher
- ✅ 1 researcher artifact
- ✅ Non-empty response (min 100 chars)
- ✅ Tool calls present (if tools enabled)
- ✅ Level metadata: "Level: L0"

### Level 1 (L1) - Quorum Synthesis
- ✅ 10 L0 researcher artifacts
- ✅ 1 L1 digest artifact (DIGEST.md)
- ✅ quorum_analysis.md
- ✅ hallucinations.md
- ✅ executive_summary.md
- ✅ Level metadata: "Level: L1"
- ✅ Fractal nesting: 10 L0 + 1 L1

### Level 2 (L2) - Meta-Synthesis
- ✅ 100 L0 researcher artifacts
- ✅ 10 L1 quorum artifacts
- ✅ 1 L2 meta-digest artifact
- ✅ Level metadata: "Level: L2"
- ✅ Fractal nesting: 100 L0 + 10 L1 + 1 L2

### Level 3 (L3) - Apex Synthesis
- ✅ 1000 L0 researcher artifacts
- ✅ 100 L1 quorum artifacts
- ✅ 10 L2 meta-digest artifacts
- ✅ 1 L3 apex-digest artifact
- ✅ Level metadata: "Level: L3"
- ✅ Fractal nesting: 1000 L0 + 100 L1 + 10 L2 + 1 L3

## Validation Rules

### RED TEST Philosophy (TDD)
1. **Define expected structure FIRST** (this validator)
2. **Run swarm**
3. **Validate actual vs expected**
4. **Fix orchestrator until test passes**

### Log10 Scaling Law
- L0 = 1 researcher
- L1 = 10 researchers
- L2 = 100 researchers
- L3 = 1000 researchers

### Minimum Content Requirements
- Researcher response: ≥100 chars
- Tool calls: ≥1 per researcher (if enabled)
- Validation files: ≥50 chars
- Executive summary: ≥100 chars
- DIGEST.md: ≥500 chars

### Fractal Holonic Structure
- Each level contains all artifacts from levels below
- L1: 10 L0 + 1 L1 digest
- L2: 100 L0 + 10 L1 + 1 L2 digest
- L3: 1000 L0 + 100 L1 + 10 L2 + 1 L3 digest

## Output Format

### Success
```
✅ SWARM RUN VALIDATION PASSED

📋 Configuration:
   Level: L1
   Researchers: 10
   Rounds: 1
   Tools: Enabled

📊 Statistics:
   l0_count: 10
   l0_non_empty: 10
   l0_with_tools: 10
   l0_avg_chars: 1523.4

ℹ️  Info:
   Fractal structure: 10 L0 artifacts + 1 L1 digest

Summary: 0 errors, 0 warnings
```

### Failure
```
❌ SWARM RUN VALIDATION FAILED

❌ Errors:
   researcher_01.md: Response too short (0 chars, min 100)
   Missing DIGEST.md (L1 artifact)
   L1 fractal violation: missing L1 digest

Summary: 18 errors, 0 warnings
```

## Exit Codes

- `0` = Validation passed
- `1` = Validation failed

## Integration

### In Scripts
```python
from pathlib import Path
import sys
sys.path.insert(0, "hfo_gem/gen_30")
from swarm_run_validator import validate_swarm_run

result = validate_swarm_run(Path("hfo_swarm_runs/2025-11-13/run_*/"))
if result.success:
    print("✅ Swarm run valid")
else:
    print(f"❌ {len(result.errors)} errors")
```

### In CI/CD
```bash
# Run swarm mission
python run_knowledge_mission_auto.py

# Validate output
python validate_swarm_run.py || exit 1
```

## Current Status (2025-11-13)

Latest run: `hfo_swarm_runs/2025-11-13/run_122807_knowledge_store_ingestion_validation_mission_v_c/`

**Validation Result**: ❌ FAILED

**Errors**:
- 10/10 researchers returned 0 characters (empty responses)
- Missing validation artifacts (quorum, hallucinations)
- Missing synthesis artifacts (summary, digest)
- L1 fractal violation (no L1 digest)

**Root Cause**: Researchers not completing execution (likely LLM timeout or model unavailable)

**Next Steps**:
1. Debug empty researcher responses
2. Check LLM API availability
3. Add timeout guards to researcher execution
4. Re-run mission with fixed orchestrator
5. Re-validate until test passes

## Philosophy

This validator embodies **RED TEST for TDD**:

- We define what SHOULD happen (this validator)
- We run the system
- We check what ACTUALLY happened
- We iterate until actual == expected

The validator is the **specification** - the orchestrator must conform to it, not the other way around.

## See Also

- `hfo_gem/gen_30/swarm_run_validator.py` - Full validator source (SSOT)
- `AGENTS.md` - Incident logs showing past validation failures
- `hfo_swarm/simple_orchestrator.py` - Orchestrator that needs to pass validation
- `artifact_watchdog.py` - Older artifact validator (deprecated, use swarm_run_validator.py)
