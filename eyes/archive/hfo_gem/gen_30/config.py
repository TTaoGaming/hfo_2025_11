#!/usr/bin/env python3
"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: d50a6b4e-5f02-4929-b007-a8f7f2e27362
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T11:07:35.710007Z'
    generation: 51
  topos:
    address: eyes/archive/hfo_gem/gen_30/config.py
    links: []
  telos:
    viral_factor: 0.0
    meme: config.py
"""
"""
Gen 30 Configuration (DEPRECATED - Import from hfo_sdk instead)
================================================================

⚠️ DEPRECATION NOTICE:
This file is being phased out. Import configuration from hfo_sdk instead:

    from hfo_sdk.config import get_config, HFOConfig, DatabaseConfig, LLMConfig

This file now only provides backward compatibility and gen_30-specific legacy code.
All new code should use hfo_sdk.config directly.

Updated: 2025-11-15 (Smart Cleanup - Config Centralization)
"""

import os
from typing import Dict, Optional, List
from dataclasses import dataclass

# ============================================================================
# IMPORT FROM SDK (Single Source of Truth)
# ============================================================================

from hfo_sdk.config import (
    DatabaseConfig,
    LLMConfig,
    ModelRoles,
    ModelTemperatures,
    ConcurrencyConfig,
    ToolConfig,
    ArtifactConfig,
    HFOConfig,
    get_config,
    print_config_summary,
    print_config_env_template
)

# ============================================================================
# GEN 30 LEGACY CODE (Deprecated - Use hfo_sdk.model_families instead)
# ============================================================================

# Keep for backward compatibility only - will be removed in future version

    @classmethod
    def from_env(cls):
        return cls(
            api_base=os.getenv('OPENAI_BASE_URL', 'https://openrouter.ai/api/v1'),
            api_key=os.getenv('OPENAI_API_KEY', ''),
            default_timeout=int(os.getenv('LLM_TIMEOUT', '30'))
        )


# ============================================================================
# MODEL CONFIGURATION
# ============================================================================

@dataclass
class ModelRoles:
    """Model assignments for different orchestrator roles"""
    orchestrator: str  # Low temp, planning/prompt generation
    researcher: str    # High temp, diverse exploration
    validator: str     # Low temp, fact checking
    analyzer: str      # Low temp, synthesis

    @classmethod
    def from_env(cls):
        """Load from environment with Gen 30 defaults"""
        return cls(
            orchestrator=os.getenv('MODEL_ORCHESTRATOR', 'openai/gpt-4o-mini'),
            researcher=os.getenv('MODEL_RESEARCHER', 'openai/gpt-4o-mini'),
            validator=os.getenv('MODEL_VALIDATOR', 'openai/gpt-4o-mini'),
            analyzer=os.getenv('MODEL_ANALYZER', 'openai/gpt-4o-mini')
        )

    @classmethod
    def from_model_zoo(
        cls,
        num_researchers: int = 10,
        diversity: bool = True,
        high_intelligence_orchestrator: bool = True
    ):
        """
        Load models from ModelZoo with FinOps-aware selection.

        Uses dependency injection from model_catalog JSONL:
        - FREE models (first choice)
        - ULTRA_CHEAP models (<$0.10/M input)
        - CHEAP models (<$0.20/M input)
        - HIGH_INTELLIGENCE for orchestrator (Grok 4 Fast)

        Returns single researcher model (for compatibility with existing code).
        Use select_diverse_researchers() for multi-model swarms.
        """
        from .model_zoo import select_swarm_models

        selection = select_swarm_models(
            num_researchers=num_researchers,
            diversity=diversity,
            high_intelligence_orchestrator=high_intelligence_orchestrator
        )

        # For now, return first researcher model (backward compatibility)
        # TODO: Update orchestrators to support per-researcher model lists
        researcher_model = selection['researchers'][0]

        return cls(
            orchestrator=selection['orchestrator'],
            researcher=researcher_model,
            validator=researcher_model,  # Use same affordable model
            analyzer=researcher_model     # Use same affordable model
        )


@dataclass
class ModelTemperatures:
    """Temperature settings per role"""
    orchestrator: float = 0.3  # Focused planning
    researcher: float = 0.7    # Diverse exploration
    validator: float = 0.2     # Consistent analysis
    analyzer: float = 0.5      # Balanced synthesis


@dataclass
class SwarmModelSelection:
    """
    Multi-model swarm configuration with diversity.

    For testing different models' success/fail rates.
    """
    orchestrator: str
    researchers: List[str]  # Can be different models per researcher
    validator: str
    analyzer: str

    @classmethod
    def from_model_zoo(
        cls,
        num_researchers: int = 10,
        diversity: bool = True,
        high_intelligence_orchestrator: bool = True,
        prefer_tier: str = 'ULTRA_CHEAP'
    ):
        """
        Select diverse models for swarm testing.

        Enables A/B testing across tiers:
        - Mix FREE + ULTRA_CHEAP + CHEAP for researchers
        - HIGH_INTELLIGENCE (Grok 4 Fast) for orchestrator
        - Track success/fail rates per model
        """
        from .model_zoo import get_model_zoo

        zoo = get_model_zoo()
        selection = zoo.select_for_swarm(
            num_researchers=num_researchers,
            prefer_tier=prefer_tier,
            diversity=diversity,
            high_intelligence_orchestrator=high_intelligence_orchestrator
        )

        # Use affordable model for validator/analyzer
        affordable = zoo.get_ultra_cheap()[0].id

        return cls(
            orchestrator=selection['orchestrator'],
            researchers=selection['researchers'],
            validator=affordable,
            analyzer=affordable
        )


# ============================================================================
# CONCURRENCY & RESOURCE LIMITS
# ============================================================================

@dataclass
class ConcurrencyConfig:
    """Thread pool and resource limits"""
    max_workers: int                # ThreadPoolExecutor cap
    max_researchers: int            # Upper bound for num_researchers
    overall_timeout_per_researcher: int  # 60s × num_researchers
    per_researcher_timeout: int     # Max execution time per researcher
    per_llm_call_timeout: int       # Max time per LLM invoke
    per_tool_call_timeout: int      # Max time per tool execution
    max_tool_iterations: int        # Max LLM→tool loops per researcher (was hardcoded=5)

    @classmethod
    def from_env(cls):
        """Load with conservative defaults to prevent freezes"""
        return cls(
            max_workers=int(os.getenv('HFO_MAX_WORKERS', '10')),  # Increased from 4 to 10 for L1 swarms
            max_researchers=int(os.getenv('HFO_MAX_RESEARCHERS', '100')),  # Support L2 swarms
            overall_timeout_per_researcher=int(os.getenv('HFO_OVERALL_TIMEOUT_PER_RESEARCHER', '120')),  # 2min per researcher
            per_researcher_timeout=int(os.getenv('HFO_RESEARCHER_TIMEOUT', '180')),  # 3min total per researcher
            per_llm_call_timeout=int(os.getenv('HFO_LLM_CALL_TIMEOUT', '60')),  # 1min per LLM call (was 30s, too short)
            per_tool_call_timeout=int(os.getenv('HFO_TOOL_CALL_TIMEOUT', '30')),  # 30s per tool (was 15s, too short)
            max_tool_iterations=int(os.getenv('HFO_MAX_TOOL_ITERATIONS', '10'))  # NEW: Was hardcoded=5, now 10
        )


# ============================================================================
# TOOL ACCESS & FEATURES
# ============================================================================

@dataclass
class ToolConfig:
    """Research tool configuration"""
    enabled: bool          # Enable read_file, grep_search, etc.
    max_file_size_mb: int  # Max file size to read
    max_output_chars: int  # Truncate tool outputs

    @classmethod
    def from_env(cls):
        return cls(
            enabled=(os.getenv('DISABLE_RESEARCHER_TOOLS', '0') != '1'),
            max_file_size_mb=int(os.getenv('TOOL_MAX_FILE_SIZE_MB', '10')),
            max_output_chars=int(os.getenv('TOOL_MAX_OUTPUT_CHARS', '2000'))
        )


# ============================================================================
# ARTIFACT & STORAGE
# ============================================================================

@dataclass
class ArtifactConfig:
    """Swarm run artifact configuration"""
    base_dir: str          # Root for hfo_swarm_runs/
    save_artifacts: bool   # Enable artifact saving
    compress_old_runs: bool  # Gzip runs older than N days

    @classmethod
    def from_env(cls):
        return cls(
            base_dir=os.getenv('HFO_ARTIFACT_DIR', 'hfo_swarm_runs'),
            save_artifacts=(os.getenv('HFO_SAVE_ARTIFACTS', '1') == '1'),
            compress_old_runs=(os.getenv('HFO_COMPRESS_OLD_RUNS', '0') == '1')
        )


# ============================================================================
# MULTI-MODEL DIVERSITY
# ============================================================================
# Updated: 2025-11-14 - L1 Swarm Consensus (run_204637)
# Source: OpenRouter Top Weekly Models (Nov 2025)
# Validated by 7/10 researchers with focus on cost/context/recency

# Free tier (experimental, $0.00)
FREE_MODELS = [
    'tngtech/deepseek-r1t2-chimera:free',  # 163K context
    'z-ai/glm-4.5-air:free',                # 131K context
]

# Ultra-cheap tier ($0.02-$0.10/M input)
ULTRA_CHEAP_MODELS = [
    'mistralai/mistral-nemo',               # $0.02/M - CHEAPEST, 131K context
    'openai/gpt-oss-20b',                   # $0.03/M - 131K context
    'openai/gpt-oss-120b',                  # $0.04/M - 131K context
    'qwen/qwen3-235b-a22b-2507',            # $0.08/M - 262K context (largest in tier)
    'google/gemma-3-27b-it',                # $0.09/M - 131K context
]

# Moderate tier ($0.10-$0.20/M input)
MODERATE_MODELS = [
    'google/gemini-2.0-flash-001',          # $0.10/M - 1M context (LARGEST)
    'google/gemini-2.5-flash-lite',         # $0.10/M - 1M context (NEWEST - Nov 2025)
    'openai/gpt-4o-mini',                   # $0.15/M - 128K context (production standard)
]

# High intelligence tier ($0.20/M input) - orchestrator/analyzer
HIGH_INTELLIGENCE_MODELS = [
    'x-ai/grok-4-fast',                     # $0.20/M - 2M context, newest reasoning model
    'deepseek/deepseek-chat-v3.1',          # $0.20/M - 163K context
    'x-ai/grok-code-fast-1',                # $0.20/M - 256K context
]

# Legacy tiers (kept for backward compatibility)
PREMIUM_MODELS = [
    'qwen/qwen-3-235b-instruct',
    'xai/grok-2-1212',
    'zhipu/glm-4-6',
    'moonshot/kimi-k2',
]

def get_multi_model_roster(tier: str = 'ultra_cheap') -> list:
    """
    Get model roster for multi-model swarms.

    Updated: 2025-11-14 - L1 Swarm Consensus
    Based on OpenRouter Top Weekly (Nov 2025) + cost/context analysis
    """
    if tier == 'free':
        return FREE_MODELS
    elif tier == 'ultra_cheap':
        return ULTRA_CHEAP_MODELS
    elif tier == 'moderate':
        return MODERATE_MODELS
    elif tier == 'high_intelligence':
        return HIGH_INTELLIGENCE_MODELS
    elif tier == 'premium':
        return PREMIUM_MODELS
    elif tier == 'balanced_10':
        # L1 Swarm Consensus: Optimal 10-model roster for L2/L3 scaling
        # 20% FREE, 50% ULTRA_CHEAP, 30% MODERATE
        return [
            # FREE tier (2 models)
            'tngtech/deepseek-r1t2-chimera:free',
            'z-ai/glm-4.5-air:free',
            # ULTRA_CHEAP tier (5 models)
            'mistralai/mistral-nemo',
            'openai/gpt-oss-20b',
            'openai/gpt-oss-120b',
            'qwen/qwen3-235b-a22b-2507',
            'google/gemma-3-27b-it',
            # MODERATE tier (3 models)
            'google/gemini-2.0-flash-001',
            'google/gemini-2.5-flash-lite',
            'openai/gpt-4o-mini',
        ]
    elif tier == 'diverse':
        # Deprecated - use 'balanced_10' instead
        return get_multi_model_roster('balanced_10')
    else:
        raise ValueError(f"Unknown tier: {tier}. Valid: free, ultra_cheap, moderate, high_intelligence, balanced_10")


# ============================================================================
# GLOBAL SINGLETON CONFIG
# ============================================================================

class HFOConfig:
    """
    Global HFO configuration singleton.

    Usage:
        from hfo_gem.gen_30.config import config

        llm = ChatOpenAI(
            model=config.models.orchestrator,
            temperature=config.temperatures.orchestrator,
            openai_api_base=config.llm.api_base,
            openai_api_key=config.llm.api_key
        )

        with ThreadPoolExecutor(max_workers=config.concurrency.max_workers) as executor:
            ...
    """

    def __init__(self):
        self.database = DatabaseConfig.from_env()
        self.llm = LLMConfig.from_env()
        self.models = ModelRoles.from_env()
        self.temperatures = ModelTemperatures()
        self.concurrency = ConcurrencyConfig.from_env()
        self.tools = ToolConfig.from_env()
        self.artifacts = ArtifactConfig.from_env()

    def get_model_config(self, role: str) -> Dict:
        """Get LLM init kwargs for a specific role"""
        role_temps = {
            'orchestrator': self.temperatures.orchestrator,
            'researcher': self.temperatures.researcher,
            'validator': self.temperatures.validator,
            'analyzer': self.temperatures.analyzer,
        }

        role_models = {
            'orchestrator': self.models.orchestrator,
            'researcher': self.models.researcher,
            'validator': self.models.validator,
            'analyzer': self.models.analyzer,
        }

        return {
            'model': role_models.get(role, self.models.researcher),
            'temperature': role_temps.get(role, 0.7),
            'openai_api_base': self.llm.api_base,
            'openai_api_key': self.llm.api_key,
        }

    def __repr__(self):
        return f"""HFOConfig(
  database={self.database.url},
  llm_base={self.llm.api_base},
  orchestrator={self.models.orchestrator} @ {self.temperatures.orchestrator},
  researcher={self.models.researcher} @ {self.temperatures.researcher},
  max_workers={self.concurrency.max_workers},
  tools_enabled={self.tools.enabled}
)"""


# Global singleton - import this
config = HFOConfig()


# ============================================================================
# CONVENIENCE FUNCTIONS
# ============================================================================

def print_config_summary():
    """Print current configuration for debugging"""
    print("="*70)
    print("  HFO Gen 30 Configuration")
    print("="*70)
    print(f"\nDatabase: {config.database.url}")
    print(f"LLM Base: {config.llm.api_base}")
    print(f"\nModels:")
    print(f"  Orchestrator: {config.models.orchestrator} @ temp={config.temperatures.orchestrator}")
    print(f"  Researcher:   {config.models.researcher} @ temp={config.temperatures.researcher}")
    print(f"  Validator:    {config.models.validator} @ temp={config.temperatures.validator}")
    print(f"  Analyzer:     {config.models.analyzer} @ temp={config.temperatures.analyzer}")
    print(f"\nConcurrency:")
    print(f"  Max Workers:     {config.concurrency.max_workers}")
    print(f"  Max Researchers: {config.concurrency.max_researchers}")
    print(f"  Per-Researcher Timeout: {config.concurrency.per_researcher_timeout}s")
    print(f"  Per-LLM-Call Timeout:   {config.concurrency.per_llm_call_timeout}s")
    print(f"  Per-Tool-Call Timeout:  {config.concurrency.per_tool_call_timeout}s")
    print(f"\nTools:")
    print(f"  Enabled: {config.tools.enabled}")
    print(f"  Max File Size: {config.tools.max_file_size_mb}MB")
    print(f"  Max Output: {config.tools.max_output_chars} chars")
    print(f"\nArtifacts:")
    print(f"  Base Dir: {config.artifacts.base_dir}")
    print(f"  Save: {config.artifacts.save_artifacts}")
    print("="*70)


if __name__ == '__main__':
    # Quick test
    print_config_summary()
