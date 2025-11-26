"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: ed53d062-76b6-491a-9edc-b05668f0055b
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T10:21:31.616516+00:00'
    generation: 51
  topos:
    address: tests/test_hexagon.py
    links: []
  telos:
    viral_factor: 0.0
    meme: test_hexagon.py
"""

from body.models.hexagon import (
    Hexagon,
    Ontos,
    Telos,
    Chronos,
    Topos,
    HolonType,
    HolonStatus,
)


def test_hexagon_creation():
    """Test that a Hexagon can be created with valid data."""
    hex = Hexagon(
        ontos=Ontos(type=HolonType.MISSION, owner="Brain.Navigator"),
        telos=Telos(meme="Test Meme", bluf="Test BLUF"),
        chronos=Chronos(urgency=0.9),
        topos=Topos(address="1.0.0"),
    )
    assert hex.ontos.type == HolonType.MISSION
    assert hex.chronos.urgency == 0.9
    assert hex.topos.address == "1.0.0"


def test_crystalline_adapter():
    """Test conversion to YAML-ready dict."""
    hex = Hexagon(
        ontos=Ontos(type=HolonType.CODE, owner="Body.Builder"),
        telos=Telos(meme="Code is Law", bluf="Implements the law"),
        chronos=Chronos(),
        topos=Topos(address="2.1.0"),
    )
    data = hex.to_yaml_dict()
    assert "hexagon" in data
    assert data["hexagon"]["ontos"]["type"] == "code"


def test_liquid_adapter():
    """Test conversion to NATS Signal (CloudEvent)."""
    hex = Hexagon(
        ontos=Ontos(type=HolonType.SIGNAL, owner="Nerves.Relay"),
        telos=Telos(meme="Fast Signal", bluf="Move fast"),
        chronos=Chronos(urgency=1.0),
        topos=Topos(address="3.0.0"),
    )
    payload = {"foo": "bar"}
    signal = hex.to_signal(payload)

    assert signal["specversion"] == "1.0"
    assert signal["type"] == "hfo.signal.signal"
    assert signal["data"]["payload"]["foo"] == "bar"
    assert signal["data"]["hexagon"]["chronos"]["urgency"] == 1.0


def test_sedimentary_adapter():
    """Test conversion to Vector DB metadata."""
    hex = Hexagon(
        ontos=Ontos(type=HolonType.ARTIFACT, owner="Memory.Scribe"),
        telos=Telos(meme="Deep Memory", bluf="Remember forever"),
        chronos=Chronos(status=HolonStatus.FROZEN),
        topos=Topos(address="4.0.0"),
    )
    meta = hex.to_vector_meta()

    assert meta["type"] == "artifact"
    assert meta["meme"] == "Deep Memory"
    assert meta["status"] == "frozen"
