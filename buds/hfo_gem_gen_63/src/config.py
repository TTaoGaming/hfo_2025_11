"""
---
holon:
  id: hfo-c719c163
  type: implementation
  file: config.py
  status: active
---
"""
import os
import yaml
from pydantic_settings import BaseSettings
from typing import Optional, Dict, Any

def load_registry() -> Dict[str, Any]:
    """Load the Weekly Champions Registry."""
    try:
        with open("buds/hfo_gem_gen_63/REGISTRY.yaml", "r") as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        return {}

registry_data = load_registry()

class Settings(BaseSettings):
    """
    HFO Gen 63 Configuration.
    Reads from environment variables or .env file.
    """
    # Identity
    ENV: str = "dev"
    GENERATION: str = "63"
    
    # LLM Provider (OpenRouter)
    OPENROUTER_API_KEY: Optional[str] = None
    
    # Dynamic Model Selection (Weekly Champions)
    # Defaults to Registry, falls back to safe defaults if registry missing
    MODEL_REASONING: str = registry_data.get("champions", {}).get("reasoning", {}).get("primary", "openai/gpt-4o")
    MODEL_CODING: str = registry_data.get("champions", {}).get("coding", {}).get("primary", "anthropic/claude-3-5-sonnet")
    MODEL_EMBEDDING: str = registry_data.get("champions", {}).get("embedding", {}).get("primary", "openai/text-embedding-3-small")
    
    # Memory
    LANCEDB_PATH: str = "buds/hfo_gem_gen_63/06_assimilator_memory/lancedb"
    SQLITE_PATH: str = "buds/hfo_gem_gen_63/06_assimilator_memory/hfo.db"
    
    # NATS
    NATS_URL: str = "nats://localhost:4225"
    
    class Config:
        env_file = ".env"
        # env_prefix = "HFO_"  # Removed prefix to match .env file
        extra = "ignore"

settings = Settings()

if __name__ == "__main__":
    print(f"Loaded Settings for HFO Gen {settings.GENERATION} in {settings.ENV} mode.")
    print(f"Champion (Reasoning): {settings.MODEL_REASONING}")

