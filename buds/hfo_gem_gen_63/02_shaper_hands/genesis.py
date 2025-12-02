import os
import yaml
import datetime
from typing import Optional
from pydantic import BaseModel, Field

# --- Configuration ---
BRAIN_ROOT = "buds/hfo_gem_gen_63/brain"
PROJECTS_DIR = os.path.join(BRAIN_ROOT, "1_projects")
AREAS_DIR = os.path.join(BRAIN_ROOT, "2_areas")
RESOURCES_DIR = os.path.join(BRAIN_ROOT, "3_resources")

# --- Models ---

class HolonHeader(BaseModel):
    id: str
    type: str
    status: str = "active"
    author: str = "Swarmlord"
    date: str = Field(default_factory=lambda: datetime.date.today().isoformat())
    context: str = "HFO Gen 63"

# --- Genesis Logic ---

class Genesis:
    """
    The Fractal Seed. Generates compliant Holons.
    """
    
    @staticmethod
    def create_intent(title: str, context: str = "HFO Gen 63") -> str:
        """Creates a new Intent in 1_projects."""
        slug = title.lower().replace(" ", "_")
        file_name = f"intent_{slug}.md"
        file_path = os.path.join(PROJECTS_DIR, file_name)
        
        header = HolonHeader(
            id=f"intent-{slug}",
            type="intent",
            context=context
        )
        
        content = f"""---
holon:
{yaml.dump(header.model_dump(), default_flow_style=False, indent=2)}---

# 🎯 Intent: {title}

> **Context**: {context}
> **Goal**: [Define the goal here]

## ⚡ BLUF
[Bottom Line Up Front]

## 📜 Declarative Intent (Gherkin)
```gherkin
Feature: {title}
  As the Swarmlord
  I want ...
  So that ...
```
"""
        Genesis._write_file(file_path, content)
        return file_path

    @staticmethod
    def create_design(title: str, intent_id: str) -> str:
        """Creates a new Design in 1_projects linked to an Intent."""
        slug = title.lower().replace(" ", "_")
        file_name = f"design_{slug}.md"
        file_path = os.path.join(PROJECTS_DIR, file_name)
        
        header = HolonHeader(
            id=f"design-{slug}",
            type="design",
            context=f"Linked to {intent_id}"
        )
        
        content = f"""---
holon:
{yaml.dump(header.model_dump(), default_flow_style=False, indent=2)}---

# 🧠 Design: {title}

> **Intent**: `{intent_id}`

## 🔍 Context
[Context]

## 🛠️ Options
1. Option A
2. Option B

## 🏆 Recommendation
[Verdict]
"""
        Genesis._write_file(file_path, content)
        return file_path

    @staticmethod
    def create_implementation(name: str, intent_id: str, octant: str = "shaper") -> str:
        """
        Creates a new Python Implementation (Phenotype) linked to an Intent (Genotype).
        """
        slug = name.lower().replace(" ", "_")
        file_name = f"{slug}.py"
        # Default to src/ for now, but could be octant specific
        file_path = os.path.join("buds/hfo_gem_gen_63/src", file_name)
        
        # Python Docstring Header (Stigmergy)
        header_dict = {
            "id": f"impl-{slug}",
            "type": "implementation",
            "intent_id": intent_id,
            "octant": octant,
            "status": "active",
            "author": "Swarmlord",
            "date": datetime.date.today().isoformat()
        }
        
        content = f'''"""
---
holon:
{yaml.dump(header_dict, default_flow_style=False, indent=2)}---
"""

import logging

# Setup Logging
logger = logging.getLogger("{name}")

class {name.replace("_", " ").title().replace(" ", "")}:
    """
    Implementation of {intent_id}
    """
    def __init__(self):
        logger.info("Initializing {name}...")

'''
        Genesis._write_file(file_path, content)
        return file_path

    @staticmethod
    def _write_file(path: str, content: str):
        if os.path.exists(path):
            raise FileExistsError(f"Holon already exists at {path}")
        
        # Ensure directory exists
        os.makedirs(os.path.dirname(path), exist_ok=True)
        
        with open(path, "w") as f:
            f.write(content)
        print(f"🌱 Genesis: Created Holon at {path}")

if __name__ == "__main__":
    # Simple CLI for testing
    import sys
    if len(sys.argv) < 3:
        print("Usage: python genesis.py [intent|design|impl] [title/name] [intent_id (for impl)]")
        sys.exit(1)
    
    mode = sys.argv[1]
    title = sys.argv[2]
    
    if mode == "intent":
        Genesis.create_intent(title)
    elif mode == "design":
        Genesis.create_design(title, "unknown-intent")
    elif mode == "impl":
        if len(sys.argv) < 4:
            print("Error: Implementation requires an Intent ID.")
            sys.exit(1)
        intent_id = sys.argv[3]
        Genesis.create_implementation(title, intent_id)
    else:
        print(f"Unknown mode: {mode}")
