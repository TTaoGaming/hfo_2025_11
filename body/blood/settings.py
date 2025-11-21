import os
import yaml
from typing import List, Dict, Optional
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class ModelConfig(BaseSettings):
    """
    Configuration for the Model Registry.
    Loads from src/config/models.yaml
    """

    models: Dict[str, List[str]] = Field(default_factory=dict)

    @classmethod
    def load_from_yaml(cls, path: str = "body/blood/models.yaml") -> "ModelConfig":
        if not os.path.exists(path):
            return cls()
        with open(path, "r") as f:
            data = yaml.safe_load(f)
        return cls(**data)


class Settings(BaseSettings):
    """
    Global Application Settings.
    Loads from .env file.
    """

    # OpenRouter
    openrouter_api_key: str = Field(..., alias="OPENROUTER_API_KEY")
    openrouter_base_url: str = Field(
        "https://openrouter.ai/api/v1", alias="OPENROUTER_BASE_URL"
    )

    # LangSmith
    langchain_tracing_v2: bool = Field(False, alias="LANGCHAIN_TRACING_V2")
    langchain_endpoint: str = Field(
        "https://api.smith.langchain.com", alias="LANGCHAIN_ENDPOINT"
    )
    langchain_api_key: str = Field(..., alias="LANGCHAIN_API_KEY")
    langchain_project: str = Field(
        "hive-fleet-obsidian-gen50", alias="LANGCHAIN_PROJECT"
    )

    # Infrastructure
    ray_address: str = Field("", alias="RAY_ADDRESS")
    temporal_address: str = Field("localhost:7233", alias="TEMPORAL_ADDRESS")

    # DSPy
    dspy_cache_dir: str = Field(".dspy_cache", alias="DSPY_CACHE_DIR")

    model_config: SettingsConfigDict = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )


# Global Instance
settings: Optional["Settings"] = None
model_registry: Optional["ModelConfig"] = None

try:
    settings = Settings()
    model_registry = ModelConfig.load_from_yaml()
except Exception as e:
    print(
        f"⚠️ Warning: Configuration not fully loaded. Check .env and models.yaml. Error: {e}"
    )
    settings = None
    model_registry = None
