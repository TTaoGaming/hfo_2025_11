import hashlib
from datetime import datetime, timezone
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field, field_validator

class MemoryItem(BaseModel):
    """
    The Strict Contract for Memory Ingestion.
    AI Agents must produce this exact structure.
    """
    source_path: str = Field(..., description="Absolute path to the source file")
    content: str = Field(..., description="The raw text content")
    generation: int = Field(..., description="The HFO Generation number (e.g., 55, 58)")
    
    # Metadata (The "Context")
    category: str = Field(..., description="e.g., 'code', 'documentation', 'protocol'")
    tags: List[str] = Field(default_factory=list, description="Searchable tags")
    
    # Calculated Fields (AI cannot touch these)
    content_hash: str = Field(default="", description="SHA256 of content")
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('generation')
    def validate_generation(cls, v):
        if not (1 <= v <= 100):
            raise ValueError("Generation must be between 1 and 100")
        return v

    def compute_hash(self):
        self.content_hash = hashlib.sha256(self.content.encode('utf-8')).hexdigest()

class PillarAnalysis(BaseModel):
    """
    A single Pillar's analysis within an Agent's report.
    """
    summary: str = Field(..., description="Summary relevant to this pillar")
    key_findings: List[str] = Field(..., description="Specific findings")
    confidence: float = Field(..., ge=0.0, le=1.0)

class Level0Artifact(BaseModel):
    """
    Level 0: A single PREY Agent's COMPREHENSIVE perspective.
    Contains analysis for ALL 8 Pillars.
    """
    source_hash: str = Field(..., description="Link to the Raw MemoryItem")
    agent_id: int = Field(..., ge=1, le=8, description="ID of the Agent (1-8)")
    model_used: str = Field(..., description="The LLM model used")
    
    # The 8 Pillars (Strict Canalization)
    ontos: PillarAnalysis = Field(..., description="Being/Existence")
    logos: PillarAnalysis = Field(..., description="Logic/Reason")
    telos: PillarAnalysis = Field(..., description="Purpose/Goal")
    chronos: PillarAnalysis = Field(..., description="Time/Sequence")
    pathos: PillarAnalysis = Field(..., description="Emotion/UX")
    ethos: PillarAnalysis = Field(..., description="Trust/Security")
    topos: PillarAnalysis = Field(..., description="Location/Structure")
    nomos: PillarAnalysis = Field(..., description="Law/Constraint")
    
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class Level1Artifact(BaseModel):
    """
    Level 1: The Synthesized Truth (Byzantine Quorum Result).
    Condensed from 8 Level 0 Artifacts.
    """
    source_hash: str = Field(..., description="Link to the Raw MemoryItem")
    consensus_score: float = Field(..., ge=0.0, le=1.0, description="Percentage of agents in agreement")
    
    # The Synthesis
    synthesis: str = Field(..., description="The unified truth")
    resolved_conflicts: List[str] = Field(default_factory=list, description="Conflicts resolved during quorum")
    
    model_used: str = Field(..., description="The synthesizer model (Grok)")
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
