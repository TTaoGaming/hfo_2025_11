"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: af6ca03d-5fd5-415b-97bf-c67b000ce3e0
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T10:21:31.252411+00:00'
  topos:
    address: venom/test_infrastructure.py
    links: []
  telos:
    viral_factor: 0.0
    meme: test_infrastructure.py
"""

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
