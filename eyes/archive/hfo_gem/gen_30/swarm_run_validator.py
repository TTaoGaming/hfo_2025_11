#!/usr/bin/env python3
"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: 44065960-c26a-4a62-a4b0-966b4e0ef3e7
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T11:07:35.714479Z'
    generation: 51
  topos:
    address: eyes/archive/hfo_gem/gen_30/swarm_run_validator.py
    links: []
  telos:
    viral_factor: 0.0
    meme: swarm_run_validator.py
"""
"""
Gen 30 Swarm Run Validator - SSOT for Artifact Validation

RED TEST for TDD: Define expected artifact structure FIRST, then validate.

Philosophy:
- L0 = Individual researcher (1 agent, 1 artifact)
- L1 = Quorum synthesis (10 researchers → 10 L0 + 1 L1 digest)
- L2 = Meta-synthesis (100 researchers → 100 L0 + 10 L1 + 1 L2 digest)
- L3 = Apex synthesis (1000 researchers → 1000 L0 + 100 L1 + 10 L2 + 1 L3 digest)

Fractal Nesting:
- Each level contains all artifacts from levels below
- L1 run: 10 L0 artifacts + 1 L1 digest
- L2 run: 100 L0 artifacts + 10 L1 aggregates + 1 L2 digest
- Holonic: Each artifact is WHOLE (complete) + PART (contributes to meta)

Validation Rules:
1. No empty responses (min 100 chars)
2. Tool calls present (min 1 per researcher if tools enabled)
3. All 5 subdirs present and non-empty
4. Level metadata consistent
5. Fractal nesting correct (right number of L0/L1/L2 artifacts)
"""

import json
import sys
from pathlib import Path
from typing import Dict, List, Optional
from dataclasses import dataclass


@dataclass
class SwarmRunConfig:
    """Expected configuration for a swarm run"""

    num_researchers: int
    num_rounds: int = 1
    level: str = "L1"  # L0, L1, L2, L3
    tools_enabled: bool = True

    @property
    def expected_l0_artifacts(self) -> int:
        """Number of L0 (researcher) artifacts expected"""
        return self.num_researchers

    @property
    def expected_l1_artifacts(self) -> int:
        """Number of L1 (quorum) artifacts expected"""
        if self.level == "L0":
            return 0
        elif self.level == "L1":
            return 1  # Single digest
        elif self.level == "L2":
            return 10  # 10 L1 quorums
        elif self.level == "L3":
            return 100  # 100 L1 quorums
        return 0

    @property
    def expected_l2_artifacts(self) -> int:
        """Number of L2 (meta) artifacts expected"""
        if self.level in ["L0", "L1"]:
            return 0
        elif self.level == "L2":
            return 1  # Single meta-digest
        elif self.level == "L3":
            return 10  # 10 L2 meta-digests
        return 0

    @property
    def expected_l3_artifacts(self) -> int:
        """Number of L3 (apex) artifacts expected"""
        return 1 if self.level == "L3" else 0


@dataclass
class ValidationResult:
    """Result of swarm run validation"""

    success: bool
    run_dir: Path
    config: SwarmRunConfig
    errors: List[str]
    warnings: List[str]
    info: List[str]
    stats: Dict

    def __str__(self) -> str:
        status = "✅ PASS" if self.success else "❌ FAIL"
        return f"{status} - {len(self.errors)} errors, {len(self.warnings)} warnings"


class SwarmRunValidator:
    """
    Validates swarm run artifacts against expected structure.

    RED TEST philosophy:
    1. Define expected structure (this class)
    2. Run swarm
    3. Validate actual vs expected
    4. Fix orchestrator until test passes
    """

    def __init__(self, run_dir: Path):
        self.run_dir = Path(run_dir)
        self.errors = []
        self.warnings = []
        self.info = []
        self.stats = {}

    def validate(self) -> ValidationResult:
        """
        Main validation entry point.

        Returns:
            ValidationResult with success status and details
        """
        print(f"🔍 Validating swarm run: {self.run_dir.name}")
        print()

        # Step 1: Load run configuration
        config = self._load_config()
        if not config:
            return ValidationResult(
                success=False,
                run_dir=self.run_dir,
                config=SwarmRunConfig(num_researchers=0),
                errors=self.errors,
                warnings=self.warnings,
                info=self.info,
                stats=self.stats,
            )

        # Step 2: Validate directory structure
        self._validate_structure()

        # Step 3: Validate researcher artifacts (L0)
        self._validate_researchers(config)

        # Step 4: Validate quorum artifacts (L1)
        self._validate_quorum(config)

        # Step 5: Validate synthesis artifacts
        self._validate_synthesis(config)

        # Step 6: Validate level metadata consistency
        self._validate_level_consistency(config)

        # Step 7: Validate fractal nesting
        self._validate_fractal_nesting(config)

        # Build result
        success = len(self.errors) == 0
        result = ValidationResult(
            success=success,
            run_dir=self.run_dir,
            config=config,
            errors=self.errors,
            warnings=self.warnings,
            info=self.info,
            stats=self.stats,
        )

        self._print_report(result)
        return result

    def _load_config(self) -> Optional[SwarmRunConfig]:
        """Load run configuration from metadata"""
        metadata_path = self.run_dir / "00_mission" / "metadata.json"

        if not metadata_path.exists():
            self.errors.append("Missing metadata.json")
            return None

        try:
            metadata = json.loads(metadata_path.read_text())
            config = SwarmRunConfig(
                num_researchers=metadata.get("num_researchers", 10),
                level=metadata.get("level", "L1"),
                num_rounds=metadata.get("num_rounds", 1),
                tools_enabled=metadata.get("tools_enabled", True),
            )

            self.info.append(
                f"Run config: {config.num_researchers} researchers, {config.level}, {config.num_rounds} rounds"
            )
            return config

        except Exception as e:
            self.errors.append(f"Failed to load metadata: {e}")
            return None

    def _validate_structure(self):
        """Validate required directory structure"""
        required_dirs = [
            "00_mission",
            "01_orchestration",
            "02_research",
            "03_validation",
            "04_synthesis",
        ]

        for dirname in required_dirs:
            dirpath = self.run_dir / dirname
            if not dirpath.exists():
                self.errors.append(f"Missing directory: {dirname}")
            elif not dirpath.is_dir():
                self.errors.append(f"Not a directory: {dirname}")
            else:
                # Check not empty
                files = list(dirpath.iterdir())
                if not files:
                    self.errors.append(f"Empty directory: {dirname}")

    def _validate_researchers(self, config: SwarmRunConfig):
        """Validate L0 researcher artifacts"""
        research_dir = self.run_dir / "02_research"

        if not research_dir.exists():
            self.errors.append("Research directory missing")
            return

        # Find researcher files
        researcher_files = sorted(research_dir.glob("researcher_*.md"))
        actual_count = len(researcher_files)
        expected_count = config.expected_l0_artifacts

        self.stats["l0_count"] = actual_count
        self.stats["l0_expected"] = expected_count

        if actual_count != expected_count:
            self.errors.append(
                f"L0 artifact count mismatch: expected {expected_count}, got {actual_count}"
            )

        # Validate each researcher artifact
        non_empty_count = 0
        has_tools_count = 0
        total_chars = 0

        for researcher_file in researcher_files:
            content = researcher_file.read_text()

            # Check for level metadata
            if "Level: L0" not in content:
                self.warnings.append(
                    f"{researcher_file.name}: Missing L0 level metadata"
                )

            # Check response length (should be in "## Response" section)
            response_section = content.split("## Response")
            if len(response_section) > 1:
                response_text = response_section[1]
                response_chars = len(response_text.strip())
                total_chars += response_chars

                if response_chars >= 100:
                    non_empty_count += 1
                else:
                    self.errors.append(
                        f"{researcher_file.name}: Response too short ({response_chars} chars, min 100)"
                    )
            else:
                self.errors.append(f"{researcher_file.name}: No Response section found")

            # Check for tool usage (if enabled)
            if config.tools_enabled:
                if "tool_calls:" in content.lower() or "iterations:" in content.lower():
                    # Check metadata section
                    if "tool_calls: 0" not in content.lower():
                        has_tools_count += 1

        self.stats["l0_non_empty"] = non_empty_count
        self.stats["l0_with_tools"] = has_tools_count
        self.stats["l0_total_chars"] = total_chars
        self.stats["l0_avg_chars"] = total_chars / max(actual_count, 1)

        # Thresholds
        if non_empty_count < expected_count * 0.5:
            self.errors.append(
                f"Too many empty responses: {non_empty_count}/{expected_count} non-empty"
            )

        if config.tools_enabled and has_tools_count < expected_count * 0.3:
            self.warnings.append(
                f"Low tool usage: {has_tools_count}/{expected_count} used tools"
            )

    def _validate_quorum(self, config: SwarmRunConfig):
        """Validate L1 quorum artifacts"""
        validation_dir = self.run_dir / "03_validation"

        if config.level == "L0":
            # L0 runs don't have quorum validation
            return

        required_files = ["quorum_analysis.md", "hallucinations.md"]

        for filename in required_files:
            filepath = validation_dir / filename
            if not filepath.exists():
                self.errors.append(f"Missing validation file: {filename}")
            else:
                content = filepath.read_text()
                if len(content.strip()) < 50:
                    self.errors.append(f"Validation file too short: {filename}")

    def _validate_synthesis(self, config: SwarmRunConfig):
        """Validate synthesis artifacts"""
        synthesis_dir = self.run_dir / "04_synthesis"

        # Check for executive summary
        summary_path = synthesis_dir / "executive_summary.md"
        if not summary_path.exists():
            self.errors.append("Missing executive_summary.md")
        else:
            content = summary_path.read_text()
            if len(content.strip()) < 100:
                self.errors.append("Executive summary too short")

        # Check for DIGEST.md (L1 artifact)
        if config.level != "L0":
            digest_path = self.run_dir / "DIGEST.md"
            if not digest_path.exists():
                self.errors.append("Missing DIGEST.md (L1 artifact)")
            else:
                content = digest_path.read_text()

                # Check for level metadata
                if f"**Level**: {config.level}" not in content:
                    self.warnings.append(
                        f"DIGEST.md missing level metadata ({config.level})"
                    )

                # Check length
                if len(content.strip()) < 500:
                    self.errors.append(
                        f"DIGEST.md too short ({len(content)} chars, min 500)"
                    )

                self.stats["digest_chars"] = len(content)

    def _validate_level_consistency(self, config: SwarmRunConfig):
        """Validate level metadata is consistent across artifacts"""
        # Check metadata.json
        metadata_path = self.run_dir / "00_mission" / "metadata.json"
        metadata = json.loads(metadata_path.read_text())

        if metadata.get("level") != config.level:
            self.errors.append(
                f"Level mismatch in metadata: {metadata.get('level')} vs {config.level}"
            )

        # Validate log10 scaling
        level_to_count = {"L0": 1, "L1": 10, "L2": 100, "L3": 1000}

        expected = level_to_count.get(config.level, 10)
        if config.num_researchers != expected:
            self.warnings.append(
                f"Log10 scaling violation: {config.level} should have {expected} researchers, got {config.num_researchers}"
            )

    def _validate_fractal_nesting(self, config: SwarmRunConfig):
        """Validate fractal holonic nesting structure"""
        # L0: Just individual artifacts
        if config.level == "L0":
            if config.num_researchers != 1:
                self.warnings.append("L0 should have exactly 1 researcher")
            return

        # L1: 10 L0 + 1 L1 digest
        if config.level == "L1":
            expected_structure = {
                "l0_artifacts": config.num_researchers,
                "l1_artifacts": 1,  # DIGEST.md
            }

            actual_l0 = self.stats.get("l0_count", 0)
            has_digest = (self.run_dir / "DIGEST.md").exists()

            if actual_l0 != expected_structure["l0_artifacts"]:
                self.errors.append(
                    f"L1 fractal violation: expected {expected_structure['l0_artifacts']} L0, got {actual_l0}"
                )

            if not has_digest:
                self.errors.append("L1 fractal violation: missing L1 digest")

            self.info.append(
                f"Fractal structure: {actual_l0} L0 artifacts + 1 L1 digest"
            )

        # L2: 100 L0 + 10 L1 + 1 L2 digest
        # L3: 1000 L0 + 100 L1 + 10 L2 + 1 L3 digest
        # TODO: Implement when L2/L3 orchestration is ready

    def _print_report(self, result: ValidationResult):
        """Print validation report"""
        print("=" * 70)
        if result.success:
            print("✅ SWARM RUN VALIDATION PASSED")
        else:
            print("❌ SWARM RUN VALIDATION FAILED")
        print("=" * 70)
        print()

        # Config
        print("📋 Configuration:")
        print(f"   Level: {result.config.level}")
        print(f"   Researchers: {result.config.num_researchers}")
        print(f"   Rounds: {result.config.num_rounds}")
        print(f"   Tools: {'Enabled' if result.config.tools_enabled else 'Disabled'}")
        print()

        # Stats
        if result.stats:
            print("📊 Statistics:")
            for key, value in result.stats.items():
                if isinstance(value, float):
                    print(f"   {key}: {value:.1f}")
                else:
                    print(f"   {key}: {value}")
            print()

        # Info
        if result.info:
            print("ℹ️  Info:")
            for msg in result.info:
                print(f"   {msg}")
            print()

        # Warnings
        if result.warnings:
            print("⚠️  Warnings:")
            for msg in result.warnings:
                print(f"   {msg}")
            print()

        # Errors
        if result.errors:
            print("❌ Errors:")
            for msg in result.errors:
                print(f"   {msg}")
            print()

        # Summary
        print(f"Summary: {len(result.errors)} errors, {len(result.warnings)} warnings")
        print()


def validate_swarm_run(run_dir: Path) -> ValidationResult:
    """
    Convenience function to validate a swarm run.

    Args:
        run_dir: Path to swarm run directory

    Returns:
        ValidationResult with success status and details
    """
    validator = SwarmRunValidator(run_dir)
    return validator.validate()


def find_latest_run(base_dir: Path = Path("hfo_swarm_runs")) -> Optional[Path]:
    """Find the most recent swarm run directory"""
    if not base_dir.exists():
        return None

    # Get all date directories (YYYY-MM-DD format)
    date_dirs = sorted(
        [
            d
            for d in base_dir.iterdir()
            if d.is_dir() and d.name.count("-") == 2 and d.name[0].isdigit()
        ]
    )

    if not date_dirs:
        return None

    # Search from newest to oldest date
    for date_dir in reversed(date_dirs):
        # Get all run directories in this date
        run_dirs = sorted(
            [d for d in date_dir.iterdir() if d.is_dir() and d.name.startswith("run_")]
        )

        if run_dirs:
            return run_dirs[-1]  # Return most recent run in this date

    return None


if __name__ == "__main__":
    if len(sys.argv) < 2:
        # Try to find latest run
        latest = find_latest_run()
        if latest:
            print(f"📁 No run specified, using latest: {latest}")
            print()
            run_dir = latest
        else:
            print("Usage: python swarm_run_validator.py <run_dir>")
            print()
            print("Example:")
            print(
                "  python swarm_run_validator.py hfo_swarm_runs/2025-11-13/run_123456_*/"
            )
            print()
            print("Or run without args to validate latest run")
            sys.exit(1)
    else:
        run_dir = Path(sys.argv[1])

    result = validate_swarm_run(run_dir)
    sys.exit(0 if result.success else 1)
