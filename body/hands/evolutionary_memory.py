"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: 20d9b9e7-ca98-49f3-9da7-d700d90f0538
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T10:21:31.375008+00:00'
    generation: 51
  topos:
    address: body/hands/evolutionary_memory.py
    links: []
  telos:
    viral_factor: 0.0
    meme: evolutionary_memory.py
"""

import json
import os
import random
from typing import List
from pydantic import BaseModel

"""
🦅 Hive Fleet Obsidian: Evolutionary Memory
Intent: Manages the DNA (Prompt Genes) of the agents.
Linked to: brain/architecture_hybrid_memory.feature
"""


class PromptGene(BaseModel):
    """A single unit of prompt strategy."""

    strategy_name: str
    instruction: str
    success_rate: float = 0.5
    usage_count: int = 0


class EvolutionaryMemory:
    """
    🧬 The DNA of the Agent.
    Manages evolutionary prompts and strategies.
    """

    def __init__(self, memory_path: str = "memory/evolutionary/prompt_genes.json"):
        self.memory_path = memory_path
        self.genes: List[PromptGene] = []
        self._load_genes()

    def _load_genes(self):
        if os.path.exists(self.memory_path):
            try:
                with open(self.memory_path, "r") as f:
                    data = json.load(f)
                    self.genes = [PromptGene(**g) for g in data]
            except Exception:
                self.genes = []

        # Seed with default genes if empty
        if not self.genes:
            self._seed_defaults()

    def _seed_defaults(self):
        defaults = [
            PromptGene(
                strategy_name="Direct",
                instruction="Solve the problem directly and concisely.",
                success_rate=0.5,
            ),
            PromptGene(
                strategy_name="ChainOfThought",
                instruction="Think step-by-step. Break the problem down into small components.",
                success_rate=0.6,
            ),
            PromptGene(
                strategy_name="Reflexion",
                instruction="Critique your own plan before executing it. Look for flaws.",
                success_rate=0.7,
            ),
            PromptGene(
                strategy_name="Creative",
                instruction="Think outside the box. Propose a novel solution.",
                success_rate=0.4,
            ),
        ]
        self.genes.extend(defaults)
        self._save_genes()

    def _save_genes(self):
        os.makedirs(os.path.dirname(self.memory_path), exist_ok=True)
        with open(self.memory_path, "w") as f:
            json.dump([g.dict() for g in self.genes], f, indent=2)

    def select_strategy(self) -> PromptGene:
        """Selects a strategy based on success rate (Roulette Wheel Selection)."""
        total_fitness = sum(g.success_rate for g in self.genes)
        pick = random.uniform(0, total_fitness)
        current = 0.0
        for gene in self.genes:
            current += gene.success_rate
            if current > pick:
                return gene
        return self.genes[0]

    def update_fitness(self, strategy_name: str, success: bool):
        """Updates the success rate of a strategy."""
        for gene in self.genes:
            if gene.strategy_name == strategy_name:
                gene.usage_count += 1
                # Simple moving average for fitness update
                alpha = 0.1
                reward = 1.0 if success else 0.0
                gene.success_rate = (1 - alpha) * gene.success_rate + alpha * reward
                break
        self._save_genes()

    def mutate(self, new_strategy: str, new_instruction: str):
        """Adds a new mutation to the gene pool."""
        self.genes.append(
            PromptGene(
                strategy_name=new_strategy,
                instruction=new_instruction,
                success_rate=0.5,  # Start neutral
            )
        )
        self._save_genes()
