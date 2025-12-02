import pytest
import os
import shutil
from buds.hfo_gem_gen_63.carapace.guard_knowledge_structure import KnowledgeStructureGuard

# --- Fixtures ---

@pytest.fixture
def mock_brain(tmp_path):
    """Creates a temporary brain structure for testing."""
    brain = tmp_path / "brain"
    brain.mkdir()
    return brain

# --- Tests ---

def test_para_structure_missing_dirs(mock_brain):
    """Should fail if PARA directories are missing."""
    guard = KnowledgeStructureGuard(str(mock_brain))
    errors = guard.validate()
    assert any("Missing PARA Directory" in e for e in errors)
    assert len(errors) == 4 # All 4 missing

def test_para_structure_valid(mock_brain):
    """Should pass if PARA directories exist."""
    for d in ["1_projects", "2_areas", "3_resources", "4_archives"]:
        (mock_brain / d).mkdir()
    
    guard = KnowledgeStructureGuard(str(mock_brain))
    errors = guard.validate()
    assert len(errors) == 0

def test_semantic_lake_flatness(mock_brain):
    """Should fail if 1_projects has subdirectories."""
    (mock_brain / "1_projects").mkdir()
    (mock_brain / "1_projects" / "nested_folder").mkdir()
    
    guard = KnowledgeStructureGuard(str(mock_brain))
    errors = guard.validate()
    assert any("Nested directory found" in e for e in errors)

def test_holon_header_validation(mock_brain):
    """Should fail if a file lacks a valid Holon header."""
    p = mock_brain / "1_projects"
    p.mkdir()
    
    # Bad File
    bad_file = p / "bad.md"
    bad_file.write_text("# Just a title")
    
    # Good File
    good_file = p / "good.md"
    good_file.write_text("---\nholon:\n  id: test-1\n  type: note\n---\n# Good content")
    
    guard = KnowledgeStructureGuard(str(mock_brain))
    errors = guard.validate()
    
    assert any("Holon Violation" in e and "bad.md" in e for e in errors)
    # Ensure good file didn't trigger error (checking count or specific message)
    assert not any("good.md" in e for e in errors)

def test_diataxis_structure(mock_brain):
    """Should fail if 3_resources contains invalid folders."""
    r = mock_brain / "3_resources"
    r.mkdir()
    
    (r / "tutorials").mkdir() # Valid
    (r / "random_stuff").mkdir() # Invalid
    
    guard = KnowledgeStructureGuard(str(mock_brain))
    errors = guard.validate()
    assert any("Invalid Diataxis Directory" in e for e in errors)
