"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: c62e4f57-7be3-4062-b7de-d22a4a91b00b
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T10:21:31.349322+00:00'
    generation: 51
  topos:
    address: body/models/stigmergy.py
    links: []
  telos:
    viral_factor: 0.0
    meme: stigmergy.py
"""

from enum import Enum
from typing import List, Optional
from pydantic import BaseModel, Field
from datetime import datetime
import uuid


class ArtifactType(str, Enum):
    REPORT = "report"
    CODE = "code"
    PLAN = "plan"
    LOG = "log"
    PHEROMONE = "pheromone"


# --- The 8 Metaphysical Pillars of Stigmergy ---


class Ontos(BaseModel):
    """Being/Identity: What is this?"""

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    type: str
    owner: str
    version: str = "1.0.0"


class Chronos(BaseModel):
    """Time/State: When is this?"""

    created: datetime = Field(default_factory=datetime.utcnow)
    status: str = "active"
    urgency: float = Field(default=0.5, ge=0.0, le=1.0)
    decay: float = Field(default=0.1, ge=0.0, le=1.0)


class Topos(BaseModel):
    """Space/Location: Where is this?"""

    address: str
    links: List[str] = Field(default_factory=list)
    location: Optional[str] = None


class Telos(BaseModel):
    """Purpose/Goal: Why is this?"""

    meme: str
    intent_hash: Optional[str] = None
    viral_factor: float = Field(default=0.0, ge=0.0, le=1.0)


class Logos(BaseModel):
    """Logic/Structure: How is this structured?"""

    schema_v: str = "1.0"
    signature: Optional[str] = None
    validators: List[str] = Field(default_factory=list)


class Pathos(BaseModel):
    """Emotion/Quality: How good is this?"""

    sentiment: str = "neutral"
    quality_score: float = Field(default=0.5, ge=0.0, le=1.0)
    review_status: str = "pending"


class Ethos(BaseModel):
    """Trust/Security: Who trusts this?"""

    author_signature: Optional[str] = None
    consensus_score: float = Field(default=0.0, ge=0.0, le=1.0)
    access_level: str = "public"


class Nomos(BaseModel):
    """Law/Governance: What rules apply?"""

    license: str = "MIT"
    constraints: List[str] = Field(default_factory=list)
    jurisdiction: str = "hfo"


class Hexagon(BaseModel):
    """The Standard Stigmergy Header (8 Pillars)."""

    ontos: Ontos
    chronos: Chronos
    topos: Topos
    telos: Telos
    logos: Optional[Logos] = None
    pathos: Optional[Pathos] = None
    ethos: Optional[Ethos] = None
    nomos: Optional[Nomos] = None


class ClaimCheck(BaseModel):
    """Pointer to the heavy payload in Cold Storage."""

    storage: str = "postgres"
    pointer: str  # UUID or Path
    hash: Optional[str] = None


class RichMetadata(BaseModel):
    """Qualitative and Quantitative Stigmergy Data."""

    type: ArtifactType
    quality_score: float = Field(default=0.5, ge=0.0, le=1.0)
    dispersion: float = Field(
        default=0.0, ge=0.0, le=1.0, description="Broadcast Radius"
    )
    evaporation_rate: float = Field(
        default=0.1, ge=0.0, le=1.0, description="Decay per tick"
    )
    urgency: str = "normal"
    context_tags: List[str] = Field(default_factory=list)


class StigmergySignal(BaseModel):
    """The Signal emitted to NATS (Hot Storage)."""

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    producer_id: str
    claim_check: ClaimCheck
    metadata: RichMetadata
