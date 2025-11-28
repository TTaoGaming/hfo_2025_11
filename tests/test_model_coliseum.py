"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: 550e8400-e29b-41d4-a716-446655440017
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-26T12:00:00.000000Z'
    generation: 51
  topos:
    address: tests/test_model_coliseum.py
    links: []
  telos:
    viral_factor: 0.0
    meme: test_model_coliseum.py
"""

import pytest

from coliseum import model


@pytest.fixture
def simple_model():
    m = model.Model()
    m.add_node("A")
    m.add_node("B")
    m.add_edge("A", "B", weight=1.0)
    return m


def test_add_node(simple_model):
    simple_model.add_node("C")
    assert "C" in simple_model.nodes


def test_add_edge(simple_model):
    simple_model.add_edge("A", "C", weight=2.0)
    assert ("A", "C") in simple_model.edges


def test_remove_node(simple_model):
    simple_model.remove_node("B")
    assert "B" not in simple_model.nodes


def test_remove_edge(simple_model):
    simple_model.remove_edge("A", "B")
    assert ("A", "B") not in simple_model.edges


def test_node_degree(simple_model):
    assert simple_model.node_degree("A") == 1
    assert simple_model.node_degree("B") == 0


def test_edge_weight(simple_model):
    assert simple_model.edge_weight("A", "B") == 1.0


def test_graph_repr(simple_model):
    assert repr(simple_model) == "Model(nodes=['A', 'B'], edges=[('A', 'B')])"
