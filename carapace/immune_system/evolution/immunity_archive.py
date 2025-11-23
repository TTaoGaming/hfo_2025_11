"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: 19061e5f-0b68-4f9d-8382-1263a4bfaae8
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T10:21:31.556093+00:00'
  topos:
    address: carapace/immune_system/evolution/immunity_archive.py
    links: []
  telos:
    viral_factor: 0.0
    meme: immunity_archive.py
"""

import numpy as np
from ribs.archives import GridArchive
from ribs.emitters import GaussianEmitter
from ribs.schedulers import Scheduler


class ImmunityForge:
    """
    The Evolutionary Forge for the Immune System.
    Uses MAP-Elites (via pyribs) to evolve diverse and high-performing defense configurations.
    """

    def __init__(self, seed=42):
        self.seed = seed
        self.rng = np.random.default_rng(seed)
        self.archive = self._create_archive()
        self.emitters = self._create_emitters()
        self.scheduler = Scheduler(self.archive, self.emitters)

    def _create_archive(self):
        """
        Creates a GridArchive.
        Dimensions (Behavior Descriptors):
        1. Strictness (0.0 - 1.0): How aggressive the guards are.
        2. Cost Efficiency (0.0 - 1.0): How cheap the defense is to run.
        """
        return GridArchive(
            solution_dim=5,  # [static_threshold, neural_threshold, max_tokens, circuit_breaker_limit, quarantine_duration]
            dims=[20, 20],  # 20x20 grid
            ranges=[(0.0, 1.0), (0.0, 1.0)],  # Strictness, Cost Efficiency
            seed=self.seed,
        )

    def _create_emitters(self):
        """
        Creates Gaussian Emitters to explore the solution space.
        """
        return [
            GaussianEmitter(
                archive=self.archive,
                sigma=0.1,
                x0=self.rng.random(5),  # Random initial solution
                batch_size=10,
                seed=self.seed,
            )
            for _ in range(3)  # 3 Emitters for parallel exploration
        ]

    def evolve_step(self):
        """
        Runs one generation of evolution.
        1. Ask for new solutions (defense configs).
        2. Evaluate them (simulate attacks).
        3. Tell the archive the results.
        """
        solutions = self.scheduler.ask()

        # Simulation Placeholder: In a real run, we would test these against Venom.
        # Here we simulate objective (performance) and measures (behavior).
        objectives = []
        measures = []

        for sol in solutions:
            # Simulate: Higher strictness = better defense but higher cost
            strictness = np.mean(sol[:2])
            cost_efficiency = 1.0 - (np.mean(sol[2:]) * strictness)

            # Objective: Defense Score (0-100)
            defense_score = (strictness * 0.7 + cost_efficiency * 0.3) * 100

            objectives.append(defense_score)
            measures.append([strictness, cost_efficiency])

        self.scheduler.tell(objectives, measures)

        return {
            "solutions_count": len(solutions),
            "best_score": self.archive.stats.obj_max,
            "archive_size": self.archive.stats.num_elites,
        }

    def get_best_defense(self):
        """Returns the best defense configuration found so far."""
        if self.archive.stats.num_elites == 0:
            return None
        return self.archive.best_elite


if __name__ == "__main__":
    print("🛡️ Initializing Immunity Forge (MAP-Elites)...")
    forge = ImmunityForge()

    print("🧬 Evolving Defense Patterns...")
    for i in range(100):
        stats = forge.evolve_step()
        if i % 10 == 0:
            print(
                f"   Gen {i}: Best Score={stats['best_score']:.2f} | Archive Size={stats['archive_size']}"
            )

    best = forge.get_best_defense()
    # Ribs returns an Elite object, but sometimes it might be a dict depending on version/usage.
    # In recent ribs versions, it's an Elite namedtuple or similar.
    # Let's handle it safely.
    if best is not None:
        # Check if best is a dict (older ribs or specific config) or object
        if isinstance(best, dict):
            print(f"\n🏆 Best Defense Config: {best['solution']}")
            print(f"   Score: {best['objective']:.2f}")
            print(f"   Measures (Strictness, Efficiency): {best['measures']}")
        else:
            print(f"\n🏆 Best Defense Config: {best.solution}")
            print(f"   Score: {best.objective:.2f}")
            print(f"   Measures (Strictness, Efficiency): {best.measures}")
