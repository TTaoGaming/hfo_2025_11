import pytest
from body.smoke_test import test_postgres, test_nats, test_temporal, test_libraries


@pytest.mark.asyncio
async def test_infrastructure_postgres():
    """Verify Postgres and pgvector are reachable."""
    assert await test_postgres() is True


@pytest.mark.asyncio
async def test_infrastructure_nats():
    """Verify NATS JetStream is reachable and working."""
    assert await test_nats() is True


@pytest.mark.asyncio
async def test_infrastructure_temporal():
    """Verify Temporal Server is reachable."""
    assert await test_temporal() is True


def test_infrastructure_libraries():
    """Verify core libraries are installed."""
    assert test_libraries() is True
