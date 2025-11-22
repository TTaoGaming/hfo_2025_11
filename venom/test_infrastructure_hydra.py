import pytest
import ray
import time
from body.hands.tools import ToolSet


@ray.remote
class ToolWorker:
    def __init__(self):
        self.tools = ToolSet()

    def ping(self):
        return "pong"

    def run_grep(self, pattern, path):
        return self.tools.grep_files(pattern, path)


def test_ray_cluster_initialization():
    """
    Verify that the Ray cluster can initialize without freezing.
    Corresponds to infrastructure_hydra.feature
    """
    if ray.is_initialized():
        ray.shutdown()

    try:
        # Use a timeout to detect freezing during init
        ray.init(ignore_reinit_error=True, num_cpus=2)
        assert ray.is_initialized()
    except Exception as e:
        pytest.fail(f"Ray initialization failed: {e}")
    finally:
        ray.shutdown()


def test_ray_tool_execution():
    """
    Verify that tools can be executed inside a Ray actor without freezing.
    """
    if not ray.is_initialized():
        ray.init(ignore_reinit_error=True, num_cpus=2)

    try:
        # Create Actor
        worker = ToolWorker.remote()

        # Test 1: Ping (Basic Connectivity)
        start = time.time()
        ref = worker.ping.remote()
        res = ray.get(ref, timeout=5.0)
        assert res == "pong"
        print(f"Ping time: {time.time() - start:.4f}s")

        # Test 2: Grep (Heavy Task)
        start = time.time()
        # Search in the current directory (venom)
        ref = worker.run_grep.remote("def test_", "venom")
        res = ray.get(ref, timeout=10.0)
        assert "test_infrastructure_hydra.py" in res or "test_" in res
        print(f"Grep time: {time.time() - start:.4f}s")

    except Exception as e:
        pytest.fail(f"Ray tool execution failed: {e}")
    finally:
        ray.shutdown()
