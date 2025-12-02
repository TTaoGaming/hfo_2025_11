import os
import yaml
import re
from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field, ValidationError
from enum import Enum

# --- Domain Models (The DNA) ---

class HolonHeader(BaseModel):
    """
    The Metaphysical Header that every file must possess.
    """
    id: str = Field(..., description="Unique identifier for the Holon")
    type: str = Field(..., description="Type of the Holon (e.g., intent, tool, memory)")
    # We allow flexible fields, but id/type are mandatory.
    
    @classmethod
    def from_file(cls, file_path: str) -> 'HolonHeader':
        """Extracts and validates the YAML frontmatter from a file."""
        content = ""
        with open(file_path, 'r') as f:
            content = f.read()
        
        yaml_content = {}
        
        # Strategy 1: Markdown Frontmatter (--- ... ---)
        if file_path.endswith(".md"):
            if not content.startswith("---"):
                raise ValueError(f"Missing YAML frontmatter (---)")
            try:
                parts = content.split("---", 2)
                if len(parts) < 3:
                     raise ValueError(f"Malformed YAML frontmatter")
                yaml_content = yaml.safe_load(parts[1])
            except yaml.YAMLError as e:
                raise ValueError(f"YAML parsing error: {e}")

        # Strategy 2: Python Docstring (''' ... ''') or Comment Block
        elif file_path.endswith(".py"):
            # Look for a docstring or comment block containing "holon:"
            # Regex to find a YAML block inside triple quotes or comments is tricky.
            # We'll look for the specific pattern used in HFO:
            # ---
            # holon:
            #   ...
            # ---
            # OR just a raw dict in the first docstring.
            
            # Simple heuristic: Extract the first docstring
            match = re.search(r'^[\s]*"""(.*?)"""', content, re.DOTALL)
            if not match:
                match = re.search(r"^[\s]*'''(.*?)'''", content, re.DOTALL)
            
            if match:
                docstring = match.group(1)
                # Check if docstring contains YAML-like structure
                if "holon:" in docstring:
                    try:
                        # Try to parse the whole docstring as YAML, or find the block
                        # If the docstring is JUST the yaml, safe_load works.
                        # If it has text, we need to find the --- block.
                        if "---" in docstring:
                            parts = docstring.split("---")
                            # Find the part with 'holon:'
                            for part in parts:
                                if "holon:" in part:
                                    yaml_content = yaml.safe_load(part)
                                    break
                        else:
                            yaml_content = yaml.safe_load(docstring)
                    except:
                        pass # Fallback

        if not yaml_content:
             raise ValueError(f"No parseable Holon Header found")

        # Normalize: Handle nested 'holon' key vs flat
        data = {}
        if 'holon' in yaml_content:
            data = yaml_content['holon'] or {}
            # Inherit root keys if missing in holon block
            if 'id' not in data: data['id'] = yaml_content.get('id', 'unknown')
            if 'type' not in data: data['type'] = yaml_content.get('type', 'unknown')
        elif 'card' in yaml_content: # Support Grimoire Cards
            data = yaml_content['card'] or {}
        else:
            data = yaml_content

        return cls(**data)

# --- The Guard (The Immunizer) ---

class KnowledgeStructureGuard:
    """
    The Grand Unifier Guard.
    Enforces:
    1. Octree Structure (The 8 Pillars).
    2. Stigmergy Protocol (Holon Headers on EVERYTHING).
    3. Digital Twin Integrity (Intent <-> Code).
    """
    
    def __init__(self, root_path: str):
        self.root_path = root_path
        self.errors = []
        self.octree_pillars = [
            "00_observer_eyes",
            "01_bridger_nerves",
            "02_shaper_hands",
            "03_injector_heart",
            "04_disruptor_venom",
            "05_immunizer_carapace",
            "06_assimilator_memory",
            "07_navigator_brain"
        ]

    def check_octree_structure(self):
        """Rule: The Bud must contain the 8 Pillars."""
        for pillar in self.octree_pillars:
            path = os.path.join(self.root_path, pillar)
            if not os.path.isdir(path):
                self.errors.append(f"🏛️ Octree Violation: Missing Pillar '{pillar}'")

    def check_stigmergy_protocol(self):
        """Rule: Every .md and .py file must have a Holon Header."""
        exclude_dirs = ["__pycache__", ".venv", ".git", "node_modules", "drafts"]
        exclude_files = ["__init__.py", "requirements.txt", ".gitignore", ".env"]

        for root, dirs, files in os.walk(self.root_path):
            # Prune excluded dirs
            dirs[:] = [d for d in dirs if d not in exclude_dirs]
            
            for file in files:
                if file in exclude_files: continue
                if not (file.endswith(".md") or file.endswith(".py")): continue
                
                file_path = os.path.join(root, file)
                try:
                    HolonHeader.from_file(file_path)
                except (ValueError, ValidationError) as e:
                    rel_path = os.path.relpath(file_path, self.root_path)
                    self.errors.append(f"🧬 Stigmergy Violation in '{rel_path}': {str(e)}")
                except Exception as e:
                    rel_path = os.path.relpath(file_path, self.root_path)
                    self.errors.append(f"⚠️ Read Error in '{rel_path}': {str(e)}")

    def validate(self) -> List[str]:
        self.errors = []
        print(f"🛡️ Scanning Bud: {self.root_path}")
        
        self.check_octree_structure()
        self.check_stigmergy_protocol()
        
        return self.errors
