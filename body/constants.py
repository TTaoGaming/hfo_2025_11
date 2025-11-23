"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: be55db29-06ab-4ff2-a6a1-81013f9347eb
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T10:21:31.336735+00:00'
  topos:
    address: body/constants.py
    links: []
  telos:
    viral_factor: 0.0
    meme: constants.py


Global Constants for Hive Fleet Obsidian.
"""
import os

# Default Fallbacks (if config is missing)
DEFAULT_MODEL = os.getenv("DEFAULT_MODEL", "x-ai/grok-4.1-fast")
DEFAULT_TIMEOUT = 600
