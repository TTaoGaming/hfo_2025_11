import pytest
import asyncio
from body.smoke_test import test_postgres, test_nats, test_temporal, test_libraries

@pytest.mark.asyncio
async def test_infrastructure_postgres():
    """Verify Postgres and pgvector are reachable."""
    assert await test_postgres() == True

@pytest.mark.asyncio
async def test_infrastructure_nats():
    """Verify NATS JetStream is reachable and working."""
    assert await test_nats() == True

@pytest.mark.asyncio
async def test_infrastructure_temporal():
    """Verify Temporal Server is reachable."""
    assert await test_temporal() == True

def test_infrastructure_libraries():
    """Verify core libraries are installed."""
    assert test_libraries() == True
