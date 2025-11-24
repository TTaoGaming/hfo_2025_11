---
hexagon:
  ontos:
    id: 8c78e968-63d0-4466-af48-e28f8b676303
    type: md
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T11:07:35.692060Z'
    generation: 51
  topos:
    address: eyes/archive/hfo_gem/gen_30/MODEL_ZOO_QUICK_REF.md
    links: []
  telos:
    viral_factor: 0.0
    meme: MODEL_ZOO_QUICK_REF.md
---

# Model Zoo Quick Reference
## Gen 30 SSOT Model Catalog (2025-11-13)

### What This Is
- 106 OpenRouter models extracted from weekly popularity rankings
- Categorized by cost tiers for FinOps control
- JSONL catalog at `hfo_gem/gen_30/model_catalog_2025-11-13.jsonl`
- Dependency injection via `model_zoo.py` (no hardcoded model lists)

### Tier Breakdown
```
FREE:         37 models ($0.00/M input)
ULTRA_CHEAP:  37 models (<$0.10/M input)
CHEAP:        31 models (<$0.20/M input)
HIGH_INTEL:    1 model  (Grok 4 Fast, $0.20/M)
```

### Usage Patterns

#### 1. Load Model Zoo (SSOT)
```python
from hfo_gem.gen_30.model_zoo import get_model_zoo

zoo = get_model_zoo()
zoo.print_summary()
```

#### 2. Select Swarm Models (Auto)
```python
from hfo_gem.gen_30.config import SwarmModelSelection

# Automatic selection with diversity
selection = SwarmModelSelection.from_model_zoo(
    num_researchers=10,
    diversity=True,  # Mix FREE + ULTRA_CHEAP + CHEAP
    high_intelligence_orchestrator=True,  # Grok 4 Fast
    prefer_tier='ULTRA_CHEAP'
)

print(selection.orchestrator)  # x-ai/grok-4-fast
print(selection.researchers)   # List of 10 diverse models
```

#### 3. Manual Selection by Tier
```python
zoo = get_model_zoo()

# Get all free models
free_models = zoo.get_free()

# Get ultra cheap models
ultra_cheap = zoo.get_ultra_cheap()

# Get specific model
grok = zoo.get_by_id('x-ai/grok-4-fast')
print(f"Context: {grok.context_tokens}, Cost: ${grok.cost_input_per_1m}/M")
```

#### 4. Estimate Costs
```python
from hfo_gem.gen_30.model_zoo import estimate_mission_cost

model_ids = ['x-ai/grok-4-fast'] + ['tngtech/deepseek-r1t2-chimera:free'] * 10
cost = estimate_mission_cost(model_ids)
print(f"Mission cost: ${cost:.5f}")
```

#### 5. Test Model Diversity
```bash
# Run diversity test with multiple models
python test_model_zoo_diversity.py --diversity --num-researchers 10

# Run with single ultra-cheap model
python test_model_zoo_diversity.py --num-researchers 10
```

### Cost Estimates (10k input, 2k output tokens)

| Tier | Avg Cost/Researcher | 10-Researcher Mission |
|------|--------------------:|----------------------:|
| FREE | $59.16 | $591.60 |
| ULTRA_CHEAP | $15.94 | $159.40 |
| CHEAP | $77.41 | $774.10 |

**Note**: FREE models have $0 input but non-zero output costs, hence non-zero averages.

### FinOps Strategy

**Default Configuration** (recommended):
- Orchestrator: `x-ai/grok-4-fast` (HIGH_INTELLIGENCE, $0.20/M)
- Researchers: Mix of FREE + ULTRA_CHEAP (diversity testing)
- Validator: First ULTRA_CHEAP model (consistent, affordable)
- Analyzer: First ULTRA_CHEAP model (consistent, affordable)

**Budget Modes**:
1. **FREE Only**: $0 input cost (37 models available)
2. **ULTRA_CHEAP**: <$0.10/M input (37 models)
3. **CHEAP**: <$0.20/M input (31 models)
4. **Mixed**: Diversity across all tiers for A/B testing

### High Reasoning Defaults

All models marked with `"reasoning": "high"` unless specific limitations exist.

**Models with Known Limitations**:
- `openai/gpt-oss-120b` - ❌ DO NOT USE (empty response.content with tools)
- See model compatibility matrix in SDK

**Recommended Models**:
- ✅ `x-ai/grok-4-fast` - High intelligence orchestrator
- ✅ `tngtech/deepseek-r1t2-chimera:free` - FREE tier, good quality
- ✅ `google/gemini-2.5-flash-lite` - ULTRA_CHEAP, excellent context
- ✅ `openai/gpt-4o-mini` - CHEAP, validated working
- ✅ `deepseek/deepseek-chat-v3.1` - CHEAP, strong reasoning

### Files Created

```
hfo_gem/gen_30/
├── model_catalog_2025-11-13.jsonl  ← SSOT (106 models)
├── model_zoo.py                     ← Loader + selector
├── config.py                        ← Updated with SwarmModelSelection
└── MODEL_ZOO_QUICK_REF.md          ← This file

test_model_zoo_diversity.py          ← Test script
```

### Next Steps

1. **Run diversity test**: Validate multiple models work
2. **Track success rates**: Per-model evaluation
3. **Update orchestrator**: Support per-researcher model lists (TODO)
4. **Add to SDK**: Document model compatibility matrix
5. **A/B testing**: Compare FREE vs ULTRA_CHEAP vs CHEAP tiers

### Example: Custom Model Mix

```python
from hfo_gem.gen_30.model_zoo import get_model_zoo

zoo = get_model_zoo()

# Custom mix: 5 FREE + 5 ULTRA_CHEAP
free_models = [m.id for m in zoo.get_free()[:5]]
ultra_cheap = [m.id for m in zoo.get_ultra_cheap()[:5]]
researchers = free_models + ultra_cheap

# Use with orchestrator
from hfo_swarm.simple_orchestrator import SimpleOrchestrator

orch = SimpleOrchestrator(
    orchestrator_model='x-ai/grok-4-fast',
    researcher_model=researchers[0],  # Backward compat
    # TODO: Pass full researchers list when orchestrator supports it
)
```

### Configuration Philosophy

**ZERO HARDCODING**: All models loaded from JSONL catalog.

**DEPENDENCY INJECTION**: Gen 30 config reads from model zoo, not environment variables.

**FINOPS AWARE**: Tier-based selection enforces budget constraints.

**HIGH REASONING**: Default to high reasoning unless model-specific limits exist.

**DIVERSITY FIRST**: Mix models across tiers for robustness testing.

---

**Status**: ✅ Model catalog extracted (106 models)
**Date**: 2025-11-13
**Source**: OpenRouter weekly top models
**Integration**: Gen 30 SSOT config + model zoo
