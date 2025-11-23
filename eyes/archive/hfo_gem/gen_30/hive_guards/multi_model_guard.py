#!/usr/bin/env python3
"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: a8108a23-9390-4517-a543-c2404d8e425c
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T11:07:35.720826Z'
    generation: 51
  topos:
    address: eyes/archive/hfo_gem/gen_30/hive_guards/multi_model_guard.py
    links: []
  telos:
    viral_factor: 0.0
    meme: multi_model_guard.py
"""
"""
Hive Guard: Multi-Model Diversity Validator
============================================

IMMUNIZER ROLE: Static validation guard (no LLM, deterministic)

Validates that multi-model missions actually use diverse models,
not just pretend via prompt engineering.

Guards Against:
- All researchers using same model (hallucinated diversity)
- Model names in prompts but not actual LLM instances
- Missing model metadata in researcher artifacts
- Groupthink: near-duplicate responses despite diverse model labels

Validation Method:
1. Parse researcher artifact metadata
2. Extract actual model names used
3. Canonicalize into families to detect label variants
4. Compute textual similarity (Jaccard) across responses
5. Verify diversity threshold met (e.g., 70% unique families)
6. Flag violations with file:line precision

Exit Codes:
- 0: PASS (diversity threshold met, no groupthink)
- 1: FAIL (insufficient diversity, missing metadata, or groupthink)
"""

import sys
import json
from pathlib import Path
from typing import Dict, List, Optional
from dataclasses import dataclass
from collections import Counter


@dataclass
class MultiModelViolation:
    """Single diversity violation"""

    severity: str  # "critical" | "warning"
    researcher_num: int
    expected_model: Optional[str]
    actual_model: str
    message: str
    file_path: str

    def to_dict(self):
        return {
            "severity": self.severity,
            "researcher_num": self.researcher_num,
            "expected_model": self.expected_model,
            "actual_model": self.actual_model,
            "message": self.message,
            "file_path": self.file_path,
        }


class MultiModelGuard:
    """Validates multi-model diversity in swarm runs"""

    def __init__(
        self, diversity_threshold: float = 0.7, similarity_threshold: float = 0.75
    ):
        """
        Args:
            diversity_threshold: Minimum ratio of unique model families required (0.0-1.0)
                                e.g., 0.7 means 7+ unique families out of 10 researchers
            similarity_threshold: Max avg pairwise Jaccard similarity before flagging groupthink
        """
        self.diversity_threshold = diversity_threshold
        self.similarity_threshold = similarity_threshold

        # Model family canonicalization map to detect label variants mapping to same underlying model
        self.family_map = {
            "gpt-4o-mini": "gpt-4o-mini",
            "gpt-4o": "gpt-4o",
            "gpt-5-mini": "gpt-5-mini",
            "deepseek": "deepseek",
            "gemini": "gemini",
            "openai/": "openai",
        }
        self.violations: List[MultiModelViolation] = []

    def validate_run(self, run_dir: Path) -> bool:
        """
        Validate multi-model diversity in a swarm run.

        Args:
            run_dir: Path to swarm run directory (e.g., hfo_swarm_runs/2025-11-14/run_083828_*)

        Returns:
            True if validation passes, False otherwise
        """
        self.violations.clear()

        # Find all researcher files
        research_dir = run_dir / "02_research"
        if not research_dir.exists():
            self.violations.append(
                MultiModelViolation(
                    severity="critical",
                    researcher_num=0,
                    expected_model=None,
                    actual_model="N/A",
                    message=f"Research directory not found: {research_dir}",
                    file_path=str(research_dir),
                )
            )
            return False

        # Parse researcher metadata
        researcher_models: Dict[int, str] = {}
        researcher_texts: Dict[int, str] = {}
        researcher_files = sorted(research_dir.glob("researcher_*.md"))

        if not researcher_files:
            self.violations.append(
                MultiModelViolation(
                    severity="critical",
                    researcher_num=0,
                    expected_model=None,
                    actual_model="N/A",
                    message=f"No researcher files found in {research_dir}",
                    file_path=str(research_dir),
                )
            )
            return False

        for researcher_file in researcher_files:
            researcher_num = self._extract_researcher_num(researcher_file.name)
            if researcher_num is None:
                continue

            # Extract model from metadata
            model = self._extract_model(researcher_file)
            if model is None:
                self.violations.append(
                    MultiModelViolation(
                        severity="warning",
                        researcher_num=researcher_num,
                        expected_model=None,
                        actual_model="unknown",
                        message="Missing model metadata in researcher file",
                        file_path=str(researcher_file),
                    )
                )
                continue

            researcher_models[researcher_num] = model
            # Also capture the response body for similarity checks
            try:
                content = researcher_file.read_text()
                # Heuristic: strip header lines (metadata) and keep main body
                body = self._strip_metadata_block(content)
                researcher_texts[researcher_num] = body
            except Exception:
                researcher_texts[researcher_num] = ""

        # Check diversity
        if not researcher_models:
            self.violations.append(
                MultiModelViolation(
                    severity="critical",
                    researcher_num=0,
                    expected_model=None,
                    actual_model="N/A",
                    message="No valid researcher models found",
                    file_path=str(research_dir),
                )
            )
            return False

        total_researchers = len(researcher_models)

        # Check for unverified models (from prompts, not metadata)
        unverified_count = sum(
            1 for model in researcher_models.values() if model.endswith("!")
        )
        if unverified_count > 0:
            self.violations.append(
                MultiModelViolation(
                    severity="critical",
                    researcher_num=0,
                    expected_model="verified metadata",
                    actual_model=f"{unverified_count}/{total_researchers} from prompts",
                    message=f"HALLUCINATION RISK: {unverified_count}/{total_researchers} models extracted from prompts (not verified metadata). Models may be fake.",
                    file_path=str(run_dir),
                )
            )

            # Flag each unverified researcher
            for researcher_num, model in researcher_models.items():
                if model.endswith("!"):
                    researcher_file = (
                        research_dir / f"researcher_{researcher_num:02d}.md"
                    )
                    self.violations.append(
                        MultiModelViolation(
                            severity="warning",
                            researcher_num=researcher_num,
                            expected_model="verified metadata (- Model: xyz)",
                            actual_model=model.rstrip("!"),
                            message="Model name extracted from prompt text, not metadata. Likely hallucinated diversity.",
                            file_path=str(researcher_file),
                        )
                    )

            return False

        # Canonicalize model names into families to avoid fake diversity caused by label variants
        canonical_models = {
            rn: self._canonicalize_model(m) for rn, m in researcher_models.items()
        }
        unique_models = set(canonical_models.values())
        diversity_ratio = len(unique_models) / total_researchers

        # Check if diversity threshold met
        if diversity_ratio < self.diversity_threshold:
            # Report most common canonical family first, fall back to raw label
            family_counts = Counter(canonical_models.values())
            most_common_family, fam_count = family_counts.most_common(1)[0]
            model_counts = Counter(researcher_models.values())
            most_common_model, count = model_counts.most_common(1)[0]

            self.violations.append(
                MultiModelViolation(
                    severity="critical",
                    researcher_num=0,
                    expected_model=None,
                    actual_model=most_common_family,
                    message=(
                        f"HALLUCINATED DIVERSITY: {len(unique_models)}/{total_researchers} unique families ({diversity_ratio:.0%}), "
                        f"threshold {self.diversity_threshold:.0%}. Most common family: {most_common_family} ({fam_count}/{total_researchers}); "
                        f"most common label: {most_common_model} ({count}/{total_researchers})"
                    ),
                    file_path=str(run_dir),
                )
            )

            # Flag researchers using dominant model
            for researcher_num, model in researcher_models.items():
                if model == most_common_model:
                    researcher_file = (
                        research_dir / f"researcher_{researcher_num:02d}.md"
                    )
                    self.violations.append(
                        MultiModelViolation(
                            severity="warning",
                            researcher_num=researcher_num,
                            expected_model="unique model",
                            actual_model=model,
                            message=f"Using dominant model (part of {count}/{total_researchers} cluster)",
                            file_path=str(researcher_file),
                        )
                    )

            return False

        # ADDITIONAL GROUPTHINK CHECK: compute lightweight pairwise similarity across responses
        # If responses are near-duplicate across many researchers, flag as groupthink even if labels look diverse
        if researcher_texts:
            avg_sim = self._average_pairwise_jaccard(list(researcher_texts.values()))
            if avg_sim >= self.similarity_threshold:
                self.violations.append(
                    MultiModelViolation(
                        severity="critical",
                        researcher_num=0,
                        expected_model=None,
                        actual_model=f"avg_jaccard={avg_sim:.2f}",
                        message=(
                            f"GROUPTHINK DETECTED: Average pairwise textual similarity {avg_sim:.2f} >= "
                            f"similarity threshold {self.similarity_threshold:.2f}. Responses are near-duplicates."
                        ),
                        file_path=str(run_dir),
                    )
                )
                return False

        # SUCCESS: Diversity threshold met
        print(
            f"✅ Multi-model diversity: {len(unique_models)}/{total_researchers} unique models ({diversity_ratio:.0%})"
        )
        print(f"   Models: {', '.join(sorted(unique_models))}")
        return True

    def _extract_researcher_num(self, filename: str) -> Optional[int]:
        """Extract researcher number from filename (researcher_01.md -> 1)"""
        import re

        match = re.search(r"researcher_(\d+)\.md", filename)
        return int(match.group(1)) if match else None

    def _extract_model(self, researcher_file: Path) -> Optional[str]:
        """
        Extract actual model used from researcher metadata.

        Priority:
        1. Metadata header: "- Model: xyz" (TRUTH - actual model used)
        2. Prompt text: "using model xyz" (FALLBACK - may be hallucinated)
        """
        try:
            content = researcher_file.read_text()

            # PRIORITY 1: Check metadata header (saved by orchestrator from actual LLM instance)
            import re

            metadata_match = re.search(
                r"^- (?:M|m)odel:\s*(.+)$", content, re.MULTILINE
            )
            if metadata_match:
                return metadata_match.group(1).strip()

            # PRIORITY 2: Fallback to prompt text (WARNING: may be hallucinated)
            prompt_match = re.search(r"using model\s+([a-zA-Z0-9/_.:!-]+)", content)
            if prompt_match:
                # Add warning marker to indicate this came from prompt, not metadata
                return (
                    f"{prompt_match.group(1).strip()}!"  # ! = from prompt (unverified)
                )

            return None
        except Exception as e:
            print(f"⚠️  Error reading {researcher_file}: {e}")
            return None

    def generate_report(self) -> str:
        """Generate validation report"""
        if not self.violations:
            return "✅ PASS: Multi-model diversity validated\n"

        report_lines = [
            "❌ FAIL: Multi-model diversity validation failed\n",
            f"Found {len(self.violations)} violation(s):\n",
        ]

        for i, violation in enumerate(self.violations, 1):
            report_lines.append(
                f"\n{i}. [{violation.severity.upper()}] {violation.message}"
            )
            report_lines.append(f"   File: {violation.file_path}")
            if violation.researcher_num > 0:
                report_lines.append(f"   Researcher: #{violation.researcher_num}")
            if violation.expected_model:
                report_lines.append(f"   Expected: {violation.expected_model}")
            report_lines.append(f"   Actual: {violation.actual_model}")

        return "\n".join(report_lines)


def main():
    """CLI entry point for CI/CD integration"""
    import argparse

    parser = argparse.ArgumentParser(
        description="Validate multi-model diversity in swarm runs"
    )
    parser.add_argument("run_dir", type=Path, help="Path to swarm run directory")
    parser.add_argument(
        "--threshold",
        type=float,
        default=0.7,
        help="Diversity threshold (0.0-1.0, default 0.7)",
    )
    parser.add_argument("--json", action="store_true", help="Output JSON format")

    args = parser.parse_args()

    guard = MultiModelGuard(diversity_threshold=args.threshold)
    passed = guard.validate_run(args.run_dir)

    if args.json:
        result = {
            "passed": passed,
            "violations": [v.to_dict() for v in guard.violations],
        }
        print(json.dumps(result, indent=2))
    else:
        print(guard.generate_report())

    sys.exit(0 if passed else 1)


if __name__ == "__main__":
    main()
