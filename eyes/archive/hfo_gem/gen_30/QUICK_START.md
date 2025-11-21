# Gen 30 V²C-SPIRAL-QUORUM - Quick Start

**Status**: ✅ Launchers ready, protocol formalized
**Date**: 2025-11-12
**Goal**: Simple form → AI swarm researches → Swarmlord digest

---

## 🎯 What You Asked For

> "Can I plug in a natural language prompt like 'do mission M intent with M constraint N number of researchers parallel' so I can fill out a simple form and have the AI start doing X tasks for me and after Y time or as anytime algorithm I ask for a digest in my specified Swarmlord of Webs digest format?"

**Answer**: ✅ YES - Two launchers ready to use RIGHT NOW

---

## ⚡ Option 1: Quick CLI (Power Users)

### Simplest Possible Usage

```bash
python3 launch_mission_quick.py "Your research question here"
```

**Example**:
```bash
python3 launch_mission_quick.py "Best practices for Ray distributed computing in production"
```

**Output**: `hfo_swarm_runs/YYYY-MM-DD/run_HHMMSS_*/DIGEST.md`

---

### With Constraints + Custom Researchers

```bash
python3 launch_mission_quick.py "Audit HFO Gen 1-29 for all OBSIDIAN roles" \
    --constraints "Cite generation numbers, track evolution" \
    --researchers 15
```

**All Arguments**:
- `"Intent"` - Your research question (required)
- `--constraints` - Requirements/guardrails (optional)
- `--researchers` - Number of parallel workers: 3-20 (default: 10)
- `--rounds` - SPIRAL iterations: 1-5 (default: 3) *[pending implementation]*
- `--threshold` - Convergence target: 0.0-1.0 (default: 0.6) *[pending implementation]*

---

## 📝 Option 2: Interactive Form (Beginners)

### Step-by-Step Wizard

```bash
python3 launch_mission.py
```

**What It Asks**:

1. **Mission Intent**: "What should the swarm research?"
   - Example: *Research AI swarm architectures 2024-2025*

2. **Constraints** (optional): "Any requirements?"
   - Example: *Focus on production systems, cite peer-reviewed sources*

3. **Researchers**: "How many parallel workers?"
   - Default: 10
   - Range: 3-20

4. **Max Rounds**: "SPIRAL iterations?"
   - Default: 3 (exploration → refinement → exploitation)
   - Range: 1-5

5. **Convergence**: "Consensus threshold?"
   - HIGH (80%), MEDIUM (60%), LOW (40%)
   - Default: MEDIUM

6. **Confirm**: Shows summary, press Y to launch

---

## 🌐 What Happens During Execution

### Current (Gen 29 Single PREY Loop)

```
User fills form
    ↓
Interpreter extracts intent
    ↓
Scatter 10 researchers (parallel PREY loops)
    ↓
Gather responses
    ↓
Validator checks quorum + hallucinations
    ↓
Synthesizer creates BLUF + matrices + diagrams
    ↓
Save DIGEST.md (Swarmlord format)
```

**Duration**: ~30-60 seconds for 10 researchers

---

### Future (Full V²C-SPIRAL-QUORUM)

```
Round 1: Exploration (temp=0.8)
    → Scatter researchers
    → Check quorum
    → If converged: DONE ✅
    → If not: Continue ↓

Round 2: Refinement (temp=0.5)
    → Inject Round 1 digest as context (bidirectional feedback)
    → Scatter researchers
    → Check quorum
    → If converged: DONE ✅
    → If not: Continue ↓

Round 3: Exploitation (temp=0.3)
    → Inject accumulated context
    → Scatter researchers
    → Generate final digest ✅
```

**Anytime Algorithm**: Press **Ctrl+C** at any point → generates digest from current state

---

## 📂 Output: Swarmlord of Webs Digest

### What You Get

Every mission creates: `hfo_swarm_runs/YYYY-MM-DD/run_HHMMSS_<slug>/`

**Key File**: `DIGEST.md` - Designed for **60-second scan → 5-minute decision → 30-minute action**

### DIGEST.md Structure

1. **BLUF** (30 seconds)
   - Consensus level (HIGH/MEDIUM/LOW)
   - Top 3 findings
   - Quick decision recommendation

2. **Decision Matrices** (3+)
   - Consensus analysis
   - Risk-action prioritization
   - Worker quality assessment

3. **Visual Diagrams** (3+)
   - Workflow (Mermaid flowchart)
   - Consensus distribution (pie chart)
   - Timeline (Gantt)

4. **Executive Summary** (2-3 paragraphs)
   - Stakeholder-friendly
   - Confidence scoring

5. **1-Pager Actionable Steps**
   - Immediate (today)
   - Short-term (this week)
   - Medium-term (this month)

6. **Quality Assurance**
   - Hallucination detection results
   - Quorum confidence metrics

---

## 🚀 Example Missions (Copy-Paste Ready)

### Test Mission (Validate Setup)

```bash
python3 launch_mission_quick.py "Best practices for Ray distributed computing" --researchers 5
```

**Expected**: Simple digest in ~30 seconds

---

### Gen 30 Bootstrap: Concept Audit

```bash
python3 launch_mission_quick.py \
    "Audit ALL HFO concepts across Gen 1-29: Extract acronyms (HIVE, GROWTH, SWARM, PREY, OBSIDIAN), role definitions, loop structures, Hourglass variants, stigmergy patterns" \
    --constraints "Must preserve ALL nuance, cite generation numbers, track evolution" \
    --researchers 15
```

**Expected**: Comprehensive concept registry with provenance

---

### OBSIDIAN Roles Deep Dive

```bash
python3 launch_mission_quick.py \
    "Research OBSIDIAN 8 roles evolution: For each role (Observer, Bridger, Shaper, Injector, Disruptor, Immunizer, Assimilator, Navigator), find which HFO generation introduced it, how definition evolved, battle-tested pattern mappings" \
    --constraints "Cite specific generation files, quote original definitions" \
    --researchers 15
```

**Expected**: Role evolution matrix with battle-tested citations

---

### Four Loops Architecture

```bash
python3 launch_mission_quick.py \
    "Research 4 hierarchical fractal loops in HFO: HIVE (Hunt-Integrate-Verify-Evolve), GROWTH (F3EAD mapping), SWARM (D3A mapping), PREY (OODA/MAPE-K). Find how they nest bidirectionally" \
    --constraints "Must include time horizons, Cynefin mappings, Double Diamond references" \
    --researchers 10
```

**Expected**: Nesting diagram + time horizon table

---

## 📊 Reviewing Results

### Quick Scan (30 seconds)

```bash
# Find today's runs
ls hfo_swarm_runs/$(date +%Y-%m-%d)/

# Read BLUF section only
head -50 hfo_swarm_runs/2025-11-12/run_*/DIGEST.md
```

### Deep Dive (5 minutes)

```bash
# Full digest
cat hfo_swarm_runs/2025-11-12/run_*/DIGEST.md

# Check for hallucinations
cat hfo_swarm_runs/2025-11-12/run_*/03_validation/hallucinations.md

# Quorum strength
cat hfo_swarm_runs/2025-11-12/run_*/03_validation/quorum_analysis.md
```

### Audit Workers (30 minutes)

```bash
# Individual researcher responses
ls hfo_swarm_runs/2025-11-12/run_*/02_research/

# Read specific worker
cat hfo_swarm_runs/2025-11-12/run_*/02_research/worker_03.md
```

---

## 🔧 Variables You Control

### Via Form/CLI

| Variable | Purpose | Range | Default |
|----------|---------|-------|---------|
| **Intent** | Research question | Natural language | Required |
| **Constraints** | Requirements/guardrails | Natural language | None |
| **Researchers** | Parallel workers | 3-20 | 10 |
| **Rounds** | SPIRAL iterations | 1-5 | 3 |
| **Threshold** | Consensus target | 0.0-1.0 | 0.6 (60%) |

### Automatic (V²C-SPIRAL-QUORUM Protocol)

- **Temperature Annealing**: [0.8, 0.5, 0.3] (exploration → exploitation)
- **Bidirectional Feedback**: Previous digest → next round context
- **Convergence Detection**: Auto-stop when quorum reached
- **Hallucination Detection**: DNS lookup, version check, date validation
- **Quorum Strength**: Consensus theme extraction

---

## ✅ What Works NOW

- ✅ Form-based mission launcher (`launch_mission.py`)
- ✅ Quick CLI launcher (`launch_mission_quick.py`)
- ✅ Natural language intent + constraints
- ✅ 3-20 parallel researchers
- ✅ Single PREY loop (Gen 29 orchestrator)
- ✅ Swarmlord digest format (BLUF + matrices + diagrams)
- ✅ Artifact management (all outputs saved)
- ✅ Quorum validation
- ✅ Hallucination detection

---

## 🔄 What's NEXT (Pending Implementation)

- ⏳ Multiple SPIRAL rounds (iterative refinement)
- ⏳ Bidirectional feedback (inject previous digest)
- ⏳ Annealing schedule (temperature decay)
- ⏳ Convergence detection (early stopping)
- ⏳ Anytime digest (Ctrl+C handling)

**Requires**: Extending `PREYOrchestrator.execute()` with V²C-SPIRAL-QUORUM protocol

---

## 🎯 Your First Mission (RIGHT NOW)

### 1. Test the launcher

```bash
python3 launch_mission_quick.py "Best practices for pgvector in production" --researchers 5
```

### 2. Check the output

```bash
cat hfo_swarm_runs/$(date +%Y-%m-%d)/run_*/DIGEST.md | head -50
```

### 3. Launch a real mission

```bash
python3 launch_mission_quick.py \
    "Audit ALL HFO concepts across Gen 1-29" \
    --constraints "Preserve nuance, cite generations, track evolution" \
    --researchers 15
```

### 4. Review and synthesize

- Read `DIGEST.md`
- Extract key findings
- Consolidate into Gen 30 docs

---

**Status**: ✅ Simple form → AI swarm → Swarmlord digest **READY TO USE**
**Next**: Run concept audit missions, extend for full V²C-SPIRAL-QUORUM
**Goal**: Bootstrap Gen 30 SSOT using swarm to research its own evolution

---

**See Also**:
- Full guide: `MISSION_LAUNCHER_GUIDE.md`
- Bootstrap examples: `BOOTSTRAP_EXAMPLE.md`
- V²C-SPIRAL-QUORUM spec: `V2C_SPIRAL_QUORUM_SPEC.md`
