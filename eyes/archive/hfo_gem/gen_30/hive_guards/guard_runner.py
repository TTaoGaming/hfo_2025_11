#!/usr/bin/env python3
"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: 2b21690b-d7a0-4b82-8ac4-3f95c03cc597
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T11:07:35.718517Z'
    generation: 51
  topos:
    address: eyes/archive/hfo_gem/gen_30/hive_guards/guard_runner.py
    links: []
  telos:
    viral_factor: 0.0
    meme: guard_runner.py
"""
"""
Hive Guards Runner - Immunizer Role

Runs all static validation guards in sequence.
Part of OBSIDIAN Immunizer role (Blue Team protection).

Philosophy:
- Static validation (no LLM calls)
- Deterministic (same input → same output)
- Fast execution (<10 seconds typical)
- Clear error messages
- Fail fast (stop on first critical error)

Guards:
1. Swarm Run Validator - Artifact structure, fractal nesting
2. Config Validator - SSOT schema validation
3. Generation Boundary Guard - No edits to archived gens
4. Hallucination Pattern Detector - Citation validation
5. Molt Shell Immutability Guard - Read-only molt shells
"""

import sys
from pathlib import Path
from typing import List, Optional
from dataclasses import dataclass
from datetime import datetime

# Add parent to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from swarm_run_validator import validate_swarm_run, find_latest_run


@dataclass
class GuardResult:
    """Result from a single guard execution"""

    guard_name: str
    success: bool
    errors: List[str]
    warnings: List[str]
    duration_seconds: float


@dataclass
class GuardRunnerResult:
    """Result from running all guards"""

    success: bool
    guards_run: List[str]
    results: List[GuardResult]
    total_errors: int
    total_warnings: int
    duration_seconds: float

    def __str__(self) -> str:
        status = "✅ PASS" if self.success else "❌ FAIL"
        return f"{status} - {len(self.guards_run)} guards, {self.total_errors} errors, {self.total_warnings} warnings"


class HiveGuardsRunner:
    """
    Runs all Hive Guards in sequence.

    Usage:
        runner = HiveGuardsRunner()
        result = runner.run_all()
        sys.exit(0 if result.success else 1)
    """

    AVAILABLE_GUARDS = [
        "swarm_run_validator",
        "config_validator",
        "generation_guard",
        "hallucination_guard",
        "molt_shell_guard",
    ]

    def __init__(self, run_dir: Optional[Path] = None):
        self.run_dir = run_dir
        self.results = []

    def run_all(self, guards: Optional[List[str]] = None) -> GuardRunnerResult:
        """
        Run all guards or specified subset.

        Args:
            guards: List of guard names to run (None = all available)

        Returns:
            GuardRunnerResult with aggregated results
        """
        if guards is None:
            # Only run implemented guards
            guards = ["swarm_run_validator"]  # Others TODO

        print("🛡️  HFO HIVE GUARDS - IMMUNIZER STATIC VALIDATION")
        print("=" * 70)
        print()

        start_time = datetime.now()

        for guard_name in guards:
            print(f"Running: {guard_name}...")
            result = self._run_guard(guard_name)
            self.results.append(result)

            if result.success:
                print(f"  ✅ {guard_name} passed")
            else:
                print(f"  ❌ {guard_name} failed ({len(result.errors)} errors)")
            print()

        duration = (datetime.now() - start_time).total_seconds()

        # Aggregate results
        success = all(r.success for r in self.results)
        total_errors = sum(len(r.errors) for r in self.results)
        total_warnings = sum(len(r.warnings) for r in self.results)

        runner_result = GuardRunnerResult(
            success=success,
            guards_run=guards,
            results=self.results,
            total_errors=total_errors,
            total_warnings=total_warnings,
            duration_seconds=duration,
        )

        self._print_summary(runner_result)
        return runner_result

    def _run_guard(self, guard_name: str) -> GuardResult:
        """Run a single guard"""
        import time

        start = time.time()

        try:
            if guard_name == "swarm_run_validator":
                return self._run_swarm_validator()
            elif guard_name == "config_validator":
                return self._run_config_validator()
            elif guard_name == "generation_guard":
                return self._run_generation_guard()
            elif guard_name == "hallucination_guard":
                return self._run_hallucination_guard()
            elif guard_name == "molt_shell_guard":
                return self._run_molt_shell_guard()
            else:
                return GuardResult(
                    guard_name=guard_name,
                    success=False,
                    errors=[f"Unknown guard: {guard_name}"],
                    warnings=[],
                    duration_seconds=time.time() - start,
                )
        except Exception as e:
            return GuardResult(
                guard_name=guard_name,
                success=False,
                errors=[f"Guard crashed: {e}"],
                warnings=[],
                duration_seconds=time.time() - start,
            )

    def _run_swarm_validator(self) -> GuardResult:
        """Run swarm run validator"""
        import time

        start = time.time()

        # Find run to validate
        if self.run_dir:
            run_dir = self.run_dir
        else:
            run_dir = find_latest_run()
            if not run_dir:
                return GuardResult(
                    guard_name="swarm_run_validator",
                    success=False,
                    errors=["No swarm runs found"],
                    warnings=[],
                    duration_seconds=time.time() - start,
                )

        # Validate
        result = validate_swarm_run(run_dir)

        return GuardResult(
            guard_name="swarm_run_validator",
            success=result.success,
            errors=result.errors,
            warnings=result.warnings,
            duration_seconds=time.time() - start,
        )

    def _run_config_validator(self) -> GuardResult:
        """Run SSOT config validator (TODO)"""
        import time

        return GuardResult(
            guard_name="config_validator",
            success=True,
            errors=[],
            warnings=["Config validator not implemented yet"],
            duration_seconds=time.time(),
        )

    def _run_generation_guard(self) -> GuardResult:
        """Run generation boundary guard (TODO)"""
        import time

        return GuardResult(
            guard_name="generation_guard",
            success=True,
            errors=[],
            warnings=["Generation guard not implemented yet"],
            duration_seconds=time.time(),
        )

    def _run_hallucination_guard(self) -> GuardResult:
        """Run hallucination pattern detector (TODO)"""
        import time

        return GuardResult(
            guard_name="hallucination_guard",
            success=True,
            errors=[],
            warnings=["Hallucination guard not implemented yet"],
            duration_seconds=time.time(),
        )

    def _run_molt_shell_guard(self) -> GuardResult:
        """Run molt shell immutability guard (TODO)"""
        import time

        return GuardResult(
            guard_name="molt_shell_guard",
            success=True,
            errors=[],
            warnings=["Molt shell guard not implemented yet"],
            duration_seconds=time.time(),
        )

    def _print_summary(self, result: GuardRunnerResult):
        """Print summary report"""
        print("=" * 70)
        if result.success:
            print("✅ ALL HIVE GUARDS PASSED")
        else:
            print("❌ HIVE GUARDS FAILED")
        print("=" * 70)
        print()

        print(f"Guards Run: {len(result.guards_run)}")
        print(f"Duration: {result.duration_seconds:.2f}s")
        print(f"Errors: {result.total_errors}")
        print(f"Warnings: {result.total_warnings}")
        print()

        # Per-guard breakdown
        print("Guard Results:")
        for guard_result in result.results:
            status = "✅" if guard_result.success else "❌"
            print(
                f"  {status} {guard_result.guard_name} ({guard_result.duration_seconds:.2f}s)"
            )
            if guard_result.errors:
                for error in guard_result.errors[:3]:  # Show first 3
                    print(f"     ❌ {error}")
                if len(guard_result.errors) > 3:
                    print(f"     ... and {len(guard_result.errors) - 3} more errors")
            if guard_result.warnings:
                for warning in guard_result.warnings[:2]:  # Show first 2
                    print(f"     ⚠️  {warning}")
        print()


def main():
    import argparse

    parser = argparse.ArgumentParser(
        description="Run HFO Hive Guards (Immunizer static validation)"
    )
    parser.add_argument(
        "--guards",
        nargs="+",
        choices=HiveGuardsRunner.AVAILABLE_GUARDS,
        help="Specific guards to run (default: all implemented)",
    )
    parser.add_argument(
        "--run-dir", type=Path, help="Swarm run directory to validate (default: latest)"
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Run all guards including unimplemented (will show warnings)",
    )

    args = parser.parse_args()

    guards = args.guards
    if args.all:
        guards = HiveGuardsRunner.AVAILABLE_GUARDS

    runner = HiveGuardsRunner(run_dir=args.run_dir)
    result = runner.run_all(guards=guards)

    sys.exit(0 if result.success else 1)


if __name__ == "__main__":
    main()
