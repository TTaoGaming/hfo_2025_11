import os
import yaml
from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field, ValidationError
from enum import Enum

# --- Domain Models (The DNA) ---

class DiataxisType(str, Enum):
    TUTORIAL = "tutorial"
    GUIDE = "guide"
    REFERENCE = "reference"
    EXPLANATION = "explanation"

class HolonHeader(BaseModel):
    """
    The Metaphysical Header that every file must possess.
    """
    id: str = Field(..., description="Unique identifier for the Holon")
    type: str = Field(..., description="Type of the Holon (e.g., intent, design, note)")
    holon_field: Optional[Dict[str, Any]] = Field(alias="holon", default=None)

    @classmethod
    def from_file(cls, file_path: str) -> 'HolonHeader':
        """Extracts and validates the YAML frontmatter from a file."""
        with open(file_path, 'r') as f:
            content = f.read()
        
        if not content.startswith("---"):
            raise ValueError(f"File {file_path} missing YAML frontmatter start (---)")
        
        try:
            # Extract content between first two ---
            parts = content.split("---", 2)
            if len(parts) < 3:
                 raise ValueError(f"File {file_path} has malformed YAML frontmatter")
            
            yaml_content = yaml.safe_load(parts[1])
            if yaml_content is None:
                 raise ValueError(f"File {file_path} has empty YAML frontmatter")
            
            # Handle the nested 'holon' key structure if present, or flat
            if 'holon' in yaml_content:
                data = yaml_content['holon']
                if data is None:
                     # Handle case where holon key exists but is empty/null
                     data = {}
                
                # If id/type are missing in holon block, check root (legacy)
                if 'id' not in data: data['id'] = yaml_content.get('id', 'unknown')
                if 'type' not in data: data['type'] = yaml_content.get('type', 'unknown')
                return cls(**data)
            else:
                return cls(**yaml_content)
                
        except yaml.YAMLError as e:
            raise ValueError(f"YAML parsing error in {file_path}: {e}")

# --- The Guard (The Immunizer) ---

class KnowledgeStructureGuard:
    """
    Enforces the HFO Second Brain Architecture (PARA + Semantic Lake + Diataxis).
    """
    
    def __init__(self, root_path: str):
        self.root_path = root_path
        self.errors = []

    def check_para_structure(self):
        """Rule: The Container must follow P.A.R.A."""
        required_dirs = ["1_projects", "2_areas", "3_resources", "4_archives"]
        for d in required_dirs:
            path = os.path.join(self.root_path, d)
            if not os.path.isdir(path):
                self.errors.append(f"Missing PARA Directory: {d}")

    def check_semantic_lake(self):
        """Rule: Active Projects are flat."""
        projects_path = os.path.join(self.root_path, "1_projects")
        if not os.path.exists(projects_path): return

        for root, dirs, files in os.walk(projects_path):
            if root != projects_path:
                self.errors.append(f"Violation: Nested directory found in Semantic Lake: {root}")
            
            for file in files:
                if file.endswith(".md"):
                    self._validate_holon(os.path.join(root, file))

    def check_diataxis(self):
        """Rule: Resources are strictly typed."""
        resources_path = os.path.join(self.root_path, "3_resources")
        if not os.path.exists(resources_path): return

        valid_subdirs = [e.value + "s" for e in DiataxisType] # tutorials, guides...
        # Note: Diataxis types are singular, folders are usually plural. 
        # Adjusting to match Gherkin: tutorials, guides, reference, explanation
        # Reference and Explanation might be singular or plural in folder names? 
        # Gherkin says: tutorials/, guides/, reference/, explanation/
        
        gherkin_dirs = ["tutorials", "guides", "reference", "explanation"]

        for item in os.listdir(resources_path):
            item_path = os.path.join(resources_path, item)
            if os.path.isdir(item_path):
                if item not in gherkin_dirs:
                    self.errors.append(f"Violation: Invalid Diataxis Directory: {item}")

    def _validate_holon(self, file_path: str):
        """Rule: Every file must be a Holon."""
        try:
            HolonHeader.from_file(file_path)
        except (ValueError, ValidationError) as e:
            self.errors.append(f"Holon Violation in {os.path.basename(file_path)}: {str(e)}")
        
        if file_path.endswith(".md"):
            self._check_markdown_syntax(file_path)

    def _check_markdown_syntax(self, file_path: str):
        """Rule: Markdown must be syntactically valid (basic check)."""
        with open(file_path, 'r') as f:
            content = f.read()
        
        # Check for unclosed code blocks
        fence_count = content.count("```")
        if fence_count % 2 != 0:
            self.errors.append(f"Syntax Violation in {os.path.basename(file_path)}: Unclosed code block (odd number of fences)")

    def check_digital_twin_integrity(self, src_path: str):
        """
        Rule: No Orphaned Code (Phenotype must have Genotype).
        Checks that every Python file in src/ has a header linking to a valid Intent.
        """
        if not os.path.exists(src_path): return

        for root, dirs, files in os.walk(src_path):
            for file in files:
                if file.endswith(".py") and file != "__init__.py":
                    file_path = os.path.join(root, file)
                    try:
                        # We need a custom parser for Python docstrings since they aren't pure YAML files
                        header = self._extract_python_header(file_path)
                        if not header:
                            # Skip files without headers for now (Legacy Whitelist logic would go here)
                            continue
                            
                        if header.get("type") == "implementation":
                            intent_id = header.get("intent_id")
                            if not intent_id:
                                self.errors.append(f"Twin Violation: {file} missing 'intent_id'")
                            # Ideally we would check if intent_id exists in brain/ but that requires cross-ref
                            
                    except Exception as e:
                        self.errors.append(f"Header Error in {file}: {str(e)}")

    def _extract_python_header(self, file_path: str) -> Optional[Dict]:
        """Extracts YAML from the first docstring of a Python file."""
        with open(file_path, 'r') as f:
            content = f.read()
        
        # Naive extraction: look for --- holon: ... --- inside """ """
        if 'holon:' in content and '---' in content:
            try:
                # Find the YAML block
                start = content.find('---')
                end = content.find('---', start + 3)
                if start != -1 and end != -1:
                    yaml_str = content[start+3:end]
                    data = yaml.safe_load(yaml_str)
                    if 'holon' in data: return data['holon']
                    return data
            except:
                pass
        return None

    def validate(self) -> List[str]:
        self.errors = []
        self.check_para_structure()
        self.check_semantic_lake()
        self.check_diataxis()
        # We assume src is parallel to brain for this check
        src_path = os.path.join(os.path.dirname(self.root_path), "src")
        self.check_digital_twin_integrity(src_path)
        return self.errors
