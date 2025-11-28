"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: 4d2393ec-2212-4f92-bfab-1ae4349dfc3a
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T11:07:34.907671Z'
    generation: 51
  topos:
    address: body/models/hexagon.py
    links: []
  telos:
    viral_factor: 0.0
    meme: hexagon.py
"""

from typing import List, Dict, Any, Optional, Union
from enum import Enum
from datetime import datetime, timezone
from uuid import UUID, uuid4
from pydantic import BaseModel, Field

# --- Enums ---


class HolonType(str, Enum):
    INTENT = "intent"
    DESIGN = "design"
    CODE = "code"
    ARTIFACT = "artifact"
    SIGNAL = "signal"
    MISSION = "mission"
    CONCEPT = "concept"


class HolonStatus(str, Enum):
    ACTIVE = "active"
    DRAFT = "draft"
    DEPRECATED = "deprecated"
    FROZEN = "frozen"
    GERMINATING = "germinating"


class LinkRelation(str, Enum):
    DEFINES = "defines"
    IMPLEMENTS = "implements"
    EVOLVES = "evolves"
    CONTRADICTS = "contradicts"
    RELATES_TO = "relates_to"
    REQUIRES = "requires"
    TESTS = "tests"


# --- Dimensions ---


class Ontos(BaseModel):
    """
    North: Identity & Type.
    Who am I?
    """

    id: UUID = Field(default_factory=uuid4, description="Universally Unique Identifier")
    type: HolonType = Field(..., description="The fundamental category of the Holon")
    owner: str = Field(
        ...,
        description="The Agent or Role responsible for this Holon (e.g., 'Brain.Navigator')",
    )
    version: str = Field(default="1.0.0", description="Semantic Version")


class Telos(BaseModel):
    """
    South: Purpose & Intent.
    Why am I here?
    """

    meme: str = Field(..., description="The slogan or sticky idea (Short)")
    bluf: str = Field(..., description="Bottom Line Up Front (Summary)")
    viral_factor: float = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
        description="Likelihood of propagation (0.0 to 1.0)",
    )
    intent_hash: Optional[str] = Field(
        None, description="Hash of the Gherkin intent if applicable"
    )


class Chronos(BaseModel):
    """
    East: Time & Energy.
    How long do I live?
    """

    created: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    last_touched: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    status: HolonStatus = Field(default=HolonStatus.ACTIVE)
    urgency: float = Field(
        default=0.5, ge=0.0, le=1.0, description="Priority of attention (0.0 to 1.0)"
    )
    decay: float = Field(
        default=0.1,
        ge=0.0,
        le=1.0,
        description="Evaporation rate per unit time (0.0 to 1.0)",
    )
    ttl: Optional[int] = Field(
        None, description="Time To Live in seconds (for Signals)"
    )


class Link(BaseModel):
    id: Union[UUID, str]
    rel: LinkRelation
    weight: float = Field(default=1.0, ge=0.0, le=1.0)


class Topos(BaseModel):
    """
    West: Space & Connectivity.
    Who am I connected to?
    """

    address: str = Field(..., description="Fractal Address (e.g., '1.4.2')")
    links: List[Link] = Field(
        default_factory=list, description="Edges in the Knowledge Graph"
    )
    location: Optional[str] = Field(
        None, description="Physical location (URI, Filepath)"
    )


class Logos(BaseModel):
    """
    Up: Logic & Truth.
    Is my code valid?
    """

    schema_v: str = Field(default="1.0", description="Version of the Hexagon Schema")
    content_hash: Optional[str] = Field(None, description="SHA256 of the content")
    signature: Optional[str] = Field(
        None, description="Cryptographic signature of the owner"
    )
    validators: List[str] = Field(
        default_factory=list,
        description="List of passed validators (e.g., 'mypy', 'ruff')",
    )


class Pathos(BaseModel):
    """
    Down: Quality & Sentiment.
    How do I feel?
    """

    sentiment: Optional[str] = Field(
        None, description="Emotional vibe (e.g., 'confident', 'cautious')"
    )
    quality_score: float = Field(
        default=100.0, ge=0.0, le=100.0, description="Automated quality metric"
    )
    review_status: Optional[str] = Field(
        None, description="Human or Peer review status"
    )


# --- The Hexagon ---


class Hexagon(BaseModel):
    """
    The Hexagonal Holon.
    The Universal Adapter for Hive Fleet Obsidian.
    """

    ontos: Ontos
    telos: Telos
    chronos: Chronos
    topos: Topos
    logos: Logos = Field(default_factory=Logos)
    pathos: Pathos = Field(default_factory=Pathos)

    # --- Adapters ---

    def to_yaml_dict(self) -> Dict[str, Any]:
        """
        Adapter for Crystalline State (Filesystem).
        Returns a dict suitable for YAML frontmatter.
        """
        data = self.model_dump(mode="json", exclude_none=True)
        # Flatten for readability if needed, or keep nested under 'hexagon'
        return {"hexagon": data}

    def to_signal(self, payload: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Adapter for Liquid State (NATS).
        Returns a CloudEvent-compatible dictionary.
        """
        signal = {
            "specversion": "1.0",
            "type": f"hfo.{self.ontos.type.value}.signal",
            "source": self.ontos.owner,
            "id": str(self.ontos.id),
            "time": self.chronos.created.isoformat(),
            "datacontenttype": "application/json",
            "data": {
                "hexagon": self.model_dump(mode="json", exclude_none=True),
                "payload": payload or {},
            },
        }
        return signal

    def to_vector_meta(self) -> Dict[str, Any]:
        """
        Adapter for Sedimentary State (Vector DB).
        Returns a flat dictionary for metadata filtering.
        """
        return {
            "id": str(self.ontos.id),
            "type": self.ontos.type.value,
            "owner": self.ontos.owner,
            "meme": self.telos.meme,
            "urgency": self.chronos.urgency,
            "status": self.chronos.status.value,
            "address": self.topos.address,
            "quality": self.pathos.quality_score,
        }

    def to_graph_node(self) -> Dict[str, Any]:
        """
        Adapter for Holographic State (Knowledge Graph).
        Returns node properties.
        """
        return self.model_dump(mode="json", exclude_none=True)
