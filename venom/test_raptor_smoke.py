import pytest
import ray
import langgraph
import temporalio
import ribs
import langsmith
from pydantic import BaseModel


def test_pydantic_import():
    """Verify Pydantic is working."""

    class TestModel(BaseModel):
        foo: str

    m = TestModel(foo="bar")
    assert m.foo == "bar"


def test_ray_import():
    """Verify Ray can be imported.
    Note: Full Ray init might be too heavy for a unit test without a cluster,
    but we can check version."""
    assert ray.__version__ is not None


def test_langgraph_import():
    """Verify LangGraph import."""
    assert langgraph.__name__ == "langgraph"


def test_temporal_import():
    """Verify Temporal import."""
    assert temporalio.__name__ == "temporalio"


def test_ribs_import():
    """Verify Ribs (pyribs) import."""
    assert ribs.__name__ == "ribs"


def test_langsmith_import():
    """Verify LangSmith import."""
    assert langsmith.__name__ == "langsmith"


@pytest.mark.asyncio
async def test_ray_local_init():
    """Attempt a lightweight local Ray init."""
    if not ray.is_initialized():
        ray.init(ignore_reinit_error=True, num_cpus=1)

    @ray.remote
    def square(x):
        return x * x

    ref = square.remote(2)
    result = ray.get(ref)
    assert result == 4
    ray.shutdown()
