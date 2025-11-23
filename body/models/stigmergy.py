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
