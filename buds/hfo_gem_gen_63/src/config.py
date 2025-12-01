import os
from pydantic_settings import BaseSettings
from typing import Optional

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
    OPENROUTER_MODEL: str = "openai/gpt-4o"
    
    # Memory
    LANCEDB_PATH: str = "buds/hfo_gem_gen_63/memory/lancedb"
    SQLITE_PATH: str = "buds/hfo_gem_gen_63/memory/hfo.db"
    
    # NATS
    NATS_URL: str = "nats://localhost:4225"
    
    class Config:
        env_file = ".env"
        # env_prefix = "HFO_"  # Removed prefix to match .env file
        extra = "ignore"

settings = Settings()

if __name__ == "__main__":
    print(f"Loaded Settings for HFO Gen {settings.GENERATION} in {settings.ENV} mode.")
