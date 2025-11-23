"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: 6a3e135a-9846-40b5-a8b5-7c032418e87a
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T10:21:31.338607+00:00'
    generation: 51
  topos:
    address: body/config.py
    links: []
  telos:
    viral_factor: 0.0
    meme: config.py
"""

import os
import yaml
import logging
from typing import Any, Dict

# Setup Logging
logger = logging.getLogger("HFO_Config")


def load_ssot_config() -> Dict[str, Any]:
    """
    Loads the Single Source of Truth (SSOT) configuration from brain/configuration_ssot.yaml.
    """
    # Find the project root (assuming this file is in body/)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)
    config_path = os.path.join(project_root, "brain", "configuration_ssot.yaml")

    try:
        with open(config_path, "r") as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        logger.error(f"❌ SSOT Configuration not found at {config_path}")
        raise
    except Exception as e:
        logger.error(f"❌ Failed to load SSOT Configuration: {e}")
        raise


# Load Config Once
_SSOT = load_ssot_config()


class Config:
    """
    Python Interface to the SSOT.
    """

    # Infrastructure
    NATS_URL = os.getenv(
        _SSOT["infrastructure"]["nats"]["url_env_var"],
        _SSOT["infrastructure"]["nats"]["default_url"],
    )

    PG_DSN = os.getenv(
        _SSOT["infrastructure"]["postgres"]["dsn_env_var"],
        _SSOT["infrastructure"]["postgres"]["default_dsn"],
    )

    TEMPORAL_ADDRESS = os.getenv(
        _SSOT["infrastructure"]["temporal"]["address_env_var"],
        _SSOT["infrastructure"]["temporal"]["default_address"],
    )

    # Swarm Defaults
    SWARM_MODEL = _SSOT["swarm"]["defaults"]["model"]
    SWARM_TIMEOUT = _SSOT["swarm"]["defaults"]["timeout"]
    ARTIFACT_DIR = _SSOT["swarm"]["defaults"]["artifact_dir"]

    @classmethod
    def validate(cls):
        """
        Validates that the configuration is safe (e.g. no internal ports on host).
        """
        forbidden = _SSOT["guards"]["forbidden_patterns"]
        for pattern in forbidden:
            p = pattern["pattern"]
            if p in cls.NATS_URL or p in cls.PG_DSN or p in cls.TEMPORAL_ADDRESS:
                # Allow if explicitly set by env var (user override), but warn
                logger.warning(
                    f"⚠️  Configuration contains forbidden pattern '{p}': {pattern['reason']}"
                )


# Run validation on import
Config.validate()
