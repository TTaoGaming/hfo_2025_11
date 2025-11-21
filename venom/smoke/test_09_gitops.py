import subprocess
import pytest

def test_gitops_smoke():
    print("\n🧪 SMOKE TEST: GitOps (Pre-commit) Layer")
    
    try:
        # Check if pre-commit is installed (use venv path)
        pre_commit_path = "./venv/bin/pre-commit"
        if not os.path.exists(pre_commit_path):
             pytest.fail(f"pre-commit binary not found at {pre_commit_path}")

        result = subprocess.run([pre_commit_path, "--version"], capture_output=True, text=True)
        if result.returncode != 0:
            pytest.fail("pre-commit is not installed")
        
        print(f"   ✅ pre-commit version: {result.stdout.strip()}")
        
        # Check if config exists
        if not os.path.exists(".pre-commit-config.yaml"):
            pytest.fail(".pre-commit-config.yaml missing")
            
        print("   ✅ GitOps Config: OK")
        
    except Exception as e:
        pytest.fail(f"GitOps check failed: {e}")

import os
if __name__ == "__main__":
    test_gitops_smoke()
