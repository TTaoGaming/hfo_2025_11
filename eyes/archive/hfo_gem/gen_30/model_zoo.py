#!/usr/bin/env python3
"""
Gen 30 Model Zoo
================

Loads and manages model catalog from JSONL with tier-based selection.

Philosophy:
- Models loaded from JSONL (single source of truth)
- Tier-based selection (FREE > ULTRA_CHEAP > CHEAP > HIGH_INTELLIGENCE)
- No hardcoded model lists
- FinOps-aware cost tracking
"""

import json
import random
from pathlib import Path
from typing import List, Dict, Optional
from dataclasses import dataclass


@dataclass
class ModelSpec:
    """Single model specification"""

    name: str
    id: str
    cost_input_per_1m: float
    cost_output_per_1m: float
    context_tokens: int
    tier: str
    reasoning: str
    weekly_rank: int
    extracted_date: str

    @property
    def is_free(self) -> bool:
        return self.tier == "FREE"

    @property
    def is_ultra_cheap(self) -> bool:
        return self.tier == "ULTRA_CHEAP"

    @property
    def is_cheap(self) -> bool:
        return self.tier == "CHEAP"

    @property
    def is_high_intelligence(self) -> bool:
        return self.tier == "HIGH_INTELLIGENCE"

    @property
    def estimated_cost_per_mission(self) -> float:
        """Estimate cost for typical swarm mission (10k input, 2k output)"""
        input_cost = (self.cost_input_per_1m / 1_000_000) * 10_000
        output_cost = (self.cost_output_per_1m / 1_000_000) * 2_000
        return input_cost + output_cost

    def __repr__(self):
        return (
            f"Model({self.id}, tier={self.tier}, input=${self.cost_input_per_1m:.3f}/M)"
        )


class ModelZoo:
    """Model catalog loader and selector"""

    def __init__(self, catalog_path: Optional[Path] = None):
        """Load model catalog from JSONL"""
        if catalog_path is None:
            # Default to latest catalog in gen_30
            gen30_dir = Path(__file__).parent
            catalog_files = sorted(
                gen30_dir.glob("model_catalog_*.jsonl"), reverse=True
            )
            if not catalog_files:
                raise FileNotFoundError(f"No model catalogs found in {gen30_dir}")
            catalog_path = catalog_files[0]

        self.catalog_path = Path(catalog_path)
        self.models: List[ModelSpec] = []
        self._load_catalog()

    def _load_catalog(self):
        """Parse JSONL catalog"""
        with open(self.catalog_path) as f:
            for line in f:
                if line.strip():
                    data = json.loads(line)
                    self.models.append(ModelSpec(**data))

    def get_by_id(self, model_id: str) -> Optional[ModelSpec]:
        """Get model by exact ID"""
        for model in self.models:
            if model.id == model_id:
                return model
        return None

    def get_by_tier(self, tier: str) -> List[ModelSpec]:
        """Get all models in tier"""
        return [m for m in self.models if m.tier == tier]

    def get_free(self) -> List[ModelSpec]:
        """Get all free models"""
        return self.get_by_tier("FREE")

    def get_ultra_cheap(self) -> List[ModelSpec]:
        """Get ultra cheap models (<$0.10/M input)"""
        return self.get_by_tier("ULTRA_CHEAP")

    def get_cheap(self) -> List[ModelSpec]:
        """Get cheap models (<$0.20/M input)"""
        return self.get_by_tier("CHEAP")

    def get_high_intelligence(self) -> List[ModelSpec]:
        """Get high intelligence models (e.g., Grok 4 Fast)"""
        return self.get_by_tier("HIGH_INTELLIGENCE")

    def get_affordable(self) -> List[ModelSpec]:
        """Get all affordable models (FREE + ULTRA_CHEAP + CHEAP)"""
        return self.get_free() + self.get_ultra_cheap() + self.get_cheap()

    def select_for_swarm(
        self,
        num_researchers: int = 10,
        prefer_tier: str = "ULTRA_CHEAP",
        diversity: bool = True,
        high_intelligence_orchestrator: bool = True,
    ) -> Dict[str, List[str]]:
        """
        Select models for swarm execution with FinOps awareness.

        Args:
            num_researchers: Number of researcher models to select
            prefer_tier: Preferred tier (FREE, ULTRA_CHEAP, CHEAP)
            diversity: Use multiple models vs single model
            high_intelligence_orchestrator: Use Grok 4 Fast for orchestrator

        Returns:
            Dict with 'orchestrator' and 'researchers' model IDs
        """
        # Orchestrator selection
        if high_intelligence_orchestrator:
            hi_models = self.get_high_intelligence()
            orchestrator = hi_models[0].id if hi_models else self.get_cheap()[0].id
        else:
            orchestrator = self.get_ultra_cheap()[0].id

        # Researcher selection
        if diversity:
            # Mix across tiers for diversity
            pool = self.get_affordable()
            # Sort by tier preference: FREE > ULTRA_CHEAP > CHEAP
            tier_priority = {"FREE": 0, "ULTRA_CHEAP": 1, "CHEAP": 2}
            pool.sort(key=lambda m: (tier_priority.get(m.tier, 999), m.weekly_rank))

            # Select top N models
            selected = pool[:num_researchers]
            researchers = [m.id for m in selected]

            # If not enough models, repeat some
            while len(researchers) < num_researchers:
                researchers.append(random.choice([m.id for m in pool]))
        else:
            # Use single preferred model
            preferred = self.get_by_tier(prefer_tier)
            if not preferred:
                preferred = self.get_ultra_cheap()
            model_id = preferred[0].id
            researchers = [model_id] * num_researchers

        return {"orchestrator": orchestrator, "researchers": researchers}

    def estimate_swarm_cost(
        self,
        model_ids: List[str],
        avg_input_tokens: int = 10_000,
        avg_output_tokens: int = 2_000,
    ) -> float:
        """Estimate total cost for swarm mission"""
        total = 0.0
        for model_id in model_ids:
            model = self.get_by_id(model_id)
            if model:
                input_cost = (model.cost_input_per_1m / 1_000_000) * avg_input_tokens
                output_cost = (model.cost_output_per_1m / 1_000_000) * avg_output_tokens
                total += input_cost + output_cost
        return total

    def print_summary(self):
        """Print catalog summary"""
        print(f"Model Zoo: {self.catalog_path.name}")
        print(f"Total models: {len(self.models)}")
        print("\nBy tier:")
        for tier in ["FREE", "ULTRA_CHEAP", "CHEAP", "HIGH_INTELLIGENCE"]:
            models = self.get_by_tier(tier)
            if models:
                print(f"  {tier}: {len(models)} models")
                for m in models[:3]:  # Show top 3
                    print(f"    - {m.id} (${m.cost_input_per_1m:.3f}/M input)")

        print("\nCost estimates (10k input, 2k output):")
        for tier in ["FREE", "ULTRA_CHEAP", "CHEAP"]:
            models = self.get_by_tier(tier)
            if models:
                costs = [m.estimated_cost_per_mission for m in models]
                avg_cost = sum(costs) / len(costs)
                print(f"  {tier}: ${avg_cost:.5f} avg per researcher")


# ============================================================================
# GLOBAL INSTANCE (singleton pattern)
# ============================================================================

_model_zoo: Optional[ModelZoo] = None


def get_model_zoo() -> ModelZoo:
    """Get global ModelZoo instance (lazy loaded)"""
    global _model_zoo
    if _model_zoo is None:
        _model_zoo = ModelZoo()
    return _model_zoo


# ============================================================================
# CONVENIENCE FUNCTIONS
# ============================================================================


def select_swarm_models(
    num_researchers: int = 10,
    diversity: bool = True,
    high_intelligence_orchestrator: bool = True,
) -> Dict[str, List[str]]:
    """Select models for swarm execution (uses global zoo)"""
    zoo = get_model_zoo()
    return zoo.select_for_swarm(
        num_researchers=num_researchers,
        diversity=diversity,
        high_intelligence_orchestrator=high_intelligence_orchestrator,
    )


def estimate_mission_cost(model_ids: List[str]) -> float:
    """Estimate cost for mission (uses global zoo)"""
    zoo = get_model_zoo()
    return zoo.estimate_swarm_cost(model_ids)


if __name__ == "__main__":
    # Demo usage
    zoo = ModelZoo()
    zoo.print_summary()

    print("\n" + "=" * 60)
    print("SWARM SELECTION DEMO")
    print("=" * 60)

    selection = zoo.select_for_swarm(num_researchers=10, diversity=True)
    print(f"\nOrchestrator: {selection['orchestrator']}")
    print(f"Researchers ({len(selection['researchers'])}):")
    for i, model_id in enumerate(selection["researchers"], 1):
        model = zoo.get_by_id(model_id)
        print(
            f"  R{i:02d}: {model_id} ({model.tier}, ${model.cost_input_per_1m:.3f}/M)"
        )

    total_cost = zoo.estimate_swarm_cost(
        [selection["orchestrator"]] + selection["researchers"]
    )
    print(f"\nEstimated mission cost: ${total_cost:.5f}")
