---
hexagon:
  ontos:
    id: 02bd6f6f-9251-43ef-aa87-69940a32eae8
    type: md
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T11:07:35.959089Z'
    generation: 51
  topos:
    address: eyes/archive/hfo_gem/gen_28/SIMPLIFIED_ORCHESTRATION.md
    links: []
  telos:
    viral_factor: 0.0
    meme: SIMPLIFIED_ORCHESTRATION.md
---
# Simplified Orchestration Variants – Fan-Out Research Pattern
**Date**: 2025-11-11
**Goal**: Simplify from 4-agent pipeline to 1 orchestrator + N researchers
**Pattern**: Copilot-style coordinator that fans out to parallel researchers

---

## 🎯 Your Vision (Simplified)

```
User Query
    ↓
Orchestrator (like Copilot - you interact with this)
    ↓ (fan out)
    ├─→ Researcher 1
    ├─→ Researcher 2
    ├─→ Researcher 3
    ├─→ ... (up to 10 researchers)
    └─→ Researcher N
    ↓ (collect)
Orchestrator
    ↓ (manual analysis)
You examine:
  - Quorum (do 7/10 agree?)
  - Stigmergy (what patterns emerge?)
  - Contradictions (who disagrees?)
    ↓
You synthesize final artifact
```

**Key Insight**: You become the validator/synthesizer, not another AI agent.

---

## 🔄 Current vs Simplified

### Current (Complex - 87.5% hallucination)
```
User → ResearcherAgent → PlannerAgent → ExecutorAgent → ValidatorAgent → Result
       (sequential, 4 layers, hidden pipeline, weak validation)
```

### Simplified (Your Idea)
```
User → Orchestrator → [10 parallel researchers] → You analyze → Final artifact
       (parallel, 1 layer, transparent, human validation)
```

**Benefits**:
- ✅ 10x faster (parallel vs sequential)
- ✅ Full transparency (see all 10 responses)
- ✅ You control synthesis (human intelligence)
- ✅ 70% less code (150 lines vs 350)

---

## 📐 Variant 1: Dead Simple (⭐)

**Time**: 30 minutes | **Lines**: ~50 | **Difficulty**: Easy

```python
class SimpleOrchestrator:
    def fan_out(self, query, n=10):
        return [call_llm(query) for _ in range(n)]
```

**Pros**: Trivial to build, full transparency
**Cons**: No persistence, manual quorum only

---

## 📐 Variant 2: Database-Backed (⭐⭐) **RECOMMENDED**

**Time**: 1-2 hours | **Lines**: ~150 | **Difficulty**: Medium

```python
class DatabaseOrchestrator:
    def fan_out(self, query, n=10):
        mission_id = create_mission(query)
        # Parallel execution
        with ThreadPoolExecutor(max_workers=n) as executor:
            responses = executor.map(lambda i: research(mission_id, i, query), range(n))
        return mission_id, list(responses)

    def analyze_quorum(self, mission_id):
        responses = get_responses(mission_id)
        counts = Counter(extract_answer(r) for r in responses)
        return counts.most_common(5)
```

**Database Schema** (2 tables, 8 columns):
```sql
CREATE TABLE simple_missions (
    id SERIAL PRIMARY KEY,
    query TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE simple_researchers (
    id SERIAL PRIMARY KEY,
    mission_id INT REFERENCES simple_missions(id),
    researcher_num INT,
    response TEXT,
    completed_at TIMESTAMP DEFAULT NOW()
);
```

**Pros**: Persistence, automatic quorum, telemetry
**Cons**: Requires Postgres (you have this)

---

## 📐 Variant 3: Stigmergy Analysis (⭐⭐⭐)

**Time**: 3-4 hours | **Lines**: ~250 | **Difficulty**: Medium-Hard

Adds pattern detection, clustering, contradiction finder:

```python
class StigmergyOrchestrator(DatabaseOrchestrator):
    def analyze_stigmergy(self, mission_id):
        return {
            "quorum": find_consensus(),
            "patterns": cluster_responses(),  # Use embeddings
            "outliers": find_unusual(),
            "contradictions": find_disagreements(),
            "confidence": estimate_confidence()
        }
```

**Pros**: Rich analysis, pattern detection
**Cons**: More complex, needs embeddings

---

## 🚀 How Hard? (Effort Estimate)

| Variant | Time | Lines | Difficulty |
|---------|------|-------|------------|
| 1. Dead Simple | 30 min | 50 | ⭐ Easy |
| **2. Database (Recommended)** | **1-2 hrs** | **150** | **⭐⭐ Medium** |
| 3. Stigmergy | 3-4 hrs | 250 | ⭐⭐⭐ Medium-Hard |

**Answer to "how hard?"**: Not hard. Variant 2 takes 1-2 hours and gives you everything you need.

---

## 💡 Build Plan: Variant 2 (90 minutes)

### Step 1: Schema (10 min)
```bash
# Create scripts/dev/compose/postgres/init/02_simple_swarm.sql
# Add 2 tables (missions, researchers)
# Restart postgres container to apply
```

### Step 2: Orchestrator (30 min)
```python
# Create hfo_swarm/simple_orchestrator.py
# - SimpleOrchestrator class
# - fan_out() method (parallel execution)
# - analyze_quorum() helper
# Total: ~150 lines
```

### Step 3: Test Script (15 min)
```python
# Create tests/simple_swarm_test.py
orch = SimpleOrchestrator()
mission_id, _ = orch.fan_out("What is 23 * 47?", n=10)
quorum = orch.analyze_quorum(mission_id)
print(quorum)  # Expected: [("1081", 8), ...]
```

### Step 4: Run & Review (15 min)
```bash
python tests/simple_swarm_test.py
# You manually review 10 responses
# You decide final answer based on quorum
```

---

## 🎯 Comparison: Current vs Simplified

| Aspect | Current (4-agent) | Simplified (1+N) |
|--------|------------------|------------------|
| **Lines of Code** | 349 | 150 (-57%) |
| **Execution Time** | ~120s (sequential) | ~30s (parallel, 4x faster) |
| **Transparency** | Hidden pipeline | All responses visible |
| **Quality Control** | Weak ValidatorAgent | You analyze quorum |
| **Debugging** | Hard (4 layers) | Easy (flat) |
| **Your Control** | Low (AI decides) | High (you decide) |

---

## ✅ My Recommendation: Build Variant 2 Now

**Why Variant 2?**
- ✅ Not too simple (has persistence)
- ✅ Not too complex (150 lines)
- ✅ Already have infrastructure (Postgres running)
- ✅ Quick to build (1-2 hours)
- ✅ Lets you iterate (responses stored)

**What you get**:
1. Send query to 10 researchers (parallel)
2. Store all responses in database
3. Get automatic quorum count
4. Manually review responses
5. You synthesize final answer

**Ready to build?** Say "yes, build variant 2" and I'll create:
- SQL schema
- SimpleOrchestrator class
- Test script
- Documentation

**Time**: 45 minutes to working code you can test tonight.

---

**Bottom Line**: Your idea is brilliant and MUCH simpler than current approach. Variant 2 takes ~2 hours to build and gives you everything you need. Want me to build it now?
