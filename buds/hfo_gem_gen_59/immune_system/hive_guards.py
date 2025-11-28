import logging
from typing import Dict, Any, List
from pydantic import ValidationError
from ..blood.schema import Level0Artifact, Level1Artifact, PreySequence, PillarAnalysis

# Setup Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("HiveGuard")

class HiveGuard:
    """
    The Immune System of HFO Gen 59.
    Enforces strict structural integrity for Level 0 and Level 1 Artifacts.
    """

    @staticmethod
    def inspect_level0(data: Dict[str, Any]) -> bool:
        """
        Validates a Level 0 Artifact.
        Must have:
        1. PREY Loop Evidence
        2. 8 Stigmergy Pillars
        """
        try:
            artifact = Level0Artifact(**data)
            
            # Schema validation passes, now check logic if needed
            # (Pydantic handles the 8 pillars existence and PREY loop existence)
            
            logger.info(f"✅ Level 0 Artifact {artifact.source_hash[:8]}... is VALID.")
            return True
            
        except ValidationError as e:
            logger.error(f"🛑 Level 0 Artifact REJECTED: {e}")
            return False

    @staticmethod
    def inspect_level1(data: Dict[str, Any]) -> bool:
        """
        Validates a Level 1 Artifact.
        Must have:
        1. Links to exactly 8 Level 0 Artifacts
        """
        try:
            artifact = Level1Artifact(**data)
            
            # Check if constituent_hashes has exactly 8 items (Pydantic handles this too via min_length/max_length)
            if len(artifact.constituent_hashes) != 8:
                logger.error(f"🛑 Level 1 Artifact REJECTED: Expected 8 constituents, got {len(artifact.constituent_hashes)}")
                return False
                
            logger.info(f"✅ Level 1 Artifact {artifact.source_hash[:8]}... is VALID.")
            return True
            
        except ValidationError as e:
            logger.error(f"🛑 Level 1 Artifact REJECTED: {e}")
            return False

    @staticmethod
    def run_static_diagnostics():
        """
        Runs a self-test to confirm the Guard is operational.
        """
        logger.info("🛡️ Initiating Hive Guard Static Diagnostics...")
        
        # 1. Test Valid Level 0
        valid_l0 = {
            "source_hash": "hash123",
            "agent_id": 1,
            "model_used": "test-model",
            "prey": {
                "perceive": "I see data",
                "react": "I will analyze",
                "execute": "Analyzing...",
                "yield": "Analysis complete"
            },
            "ontos": {"summary": "s", "key_findings": ["f"], "confidence": 0.9},
            "logos": {"summary": "s", "key_findings": ["f"], "confidence": 0.9},
            "telos": {"summary": "s", "key_findings": ["f"], "confidence": 0.9},
            "chronos": {"summary": "s", "key_findings": ["f"], "confidence": 0.9},
            "pathos": {"summary": "s", "key_findings": ["f"], "confidence": 0.9},
            "ethos": {"summary": "s", "key_findings": ["f"], "confidence": 0.9},
            "topos": {"summary": "s", "key_findings": ["f"], "confidence": 0.9},
            "nomos": {"summary": "s", "key_findings": ["f"], "confidence": 0.9}
        }
        if not HiveGuard.inspect_level0(valid_l0):
            logger.error("❌ Diagnostic Failed: Valid Level 0 rejected.")
            return False

        # 2. Test Invalid Level 0 (Missing Pillar)
        invalid_l0 = valid_l0.copy()
        del invalid_l0["ontos"]
        if HiveGuard.inspect_level0(invalid_l0):
            logger.error("❌ Diagnostic Failed: Invalid Level 0 accepted.")
            return False

        # 3. Test Valid Level 1
        valid_l1 = {
            "source_hash": "hash456",
            "constituent_hashes": ["h1", "h2", "h3", "h4", "h5", "h6", "h7", "h8"],
            "consensus_score": 0.95,
            "synthesis": "The truth is out there.",
            "model_used": "grok-beta"
        }
        if not HiveGuard.inspect_level1(valid_l1):
            logger.error("❌ Diagnostic Failed: Valid Level 1 rejected.")
            return False

        # 4. Test Invalid Level 1 (Wrong Count)
        invalid_l1 = valid_l1.copy()
        invalid_l1["constituent_hashes"] = ["h1"] # Only 1
        if HiveGuard.inspect_level1(invalid_l1):
            logger.error("❌ Diagnostic Failed: Invalid Level 1 accepted.")
            return False

        logger.info("✅ Hive Guard Static Diagnostics PASSED. System is Operational.")
        return True
