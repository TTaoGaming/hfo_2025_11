import pytest
import os
import shutil
from buds.hfo_gem_gen_63.forge.genesis import Genesis, HolonHeader

# --- Fixtures ---

@pytest.fixture
def mock_env(tmp_path, monkeypatch):
    """Mocks the filesystem paths for Genesis."""
    brain = tmp_path / "buds/hfo_gem_gen_63/brain"
    projects = brain / "1_projects"
    projects.mkdir(parents=True)
    
    # Monkeypatch the constants in genesis.py
    monkeypatch.setattr("buds.hfo_gem_gen_63.forge.genesis.PROJECTS_DIR", str(projects))
    
    return projects

# --- Tests ---

def test_create_intent(mock_env):
    """Should create a valid Intent file with Header."""
    path = Genesis.create_intent("Test Mission")
    
    assert os.path.exists(path)
    assert "intent_test_mission.md" in path
    
    with open(path, "r") as f:
        content = f.read()
        assert "holon:" in content
        assert "id: intent-test_mission" in content
        assert "type: intent" in content
        assert "# 🎯 Intent: Test Mission" in content

def test_create_design(mock_env):
    """Should create a valid Design file linked to an Intent."""
    path = Genesis.create_design("Test Architecture", "intent-test_mission")
    
    assert os.path.exists(path)
    assert "design_test_architecture.md" in path
    
    with open(path, "r") as f:
        content = f.read()
        assert "type: design" in content
        assert "Linked to intent-test_mission" in content

def test_prevent_overwrite(mock_env):
    """Should raise error if file exists."""
    Genesis.create_intent("Duplicate")
    with pytest.raises(FileExistsError):
        Genesis.create_intent("Duplicate")
