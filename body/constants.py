"""
Global Constants for Hive Fleet Obsidian.
"""
import os

# Default Fallbacks (if config is missing)
DEFAULT_MODEL = os.getenv("DEFAULT_MODEL", "x-ai/grok-4.1-fast")
DEFAULT_TIMEOUT = 600
