import pytest
import sys
import os

# Ensure body is in path
sys.path.append(os.getcwd())


def test_gitops_agent_structure():
    print("\n🧪 SMOKE TEST: GitOps Agent Structure")

    try:
        from body.hands.infrastructure_gitops import GitOpsAgent

        agent = GitOpsAgent()
        assert hasattr(agent, "check_guards")
        assert hasattr(agent, "generate_commit_message")
        assert hasattr(agent, "execute_cycle")
        assert hasattr(agent, "is_slop")

        print("   ✅ GitOpsAgent class loaded and verified.")

    except ImportError as e:
        pytest.fail(f"Failed to import GitOpsAgent: {e}")
    except Exception as e:
        pytest.fail(f"GitOpsAgent structure check failed: {e}")


if __name__ == "__main__":
    test_gitops_agent_structure()
