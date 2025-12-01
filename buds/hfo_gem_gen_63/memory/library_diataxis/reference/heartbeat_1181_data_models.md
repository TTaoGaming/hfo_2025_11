---
holon:
  id: 75710c48-6f0e-4785-a5b1-a96bf8e63703
  type: codex_entry
  quadrant: reference
  source_ref: /home/tommytai3/hive_fleet_obsidian_2025_11/buds/hfo_gem_gen_63/src/heartbeat_1181.py
hexagon:
  ontos: hive_fleet_obsidian
  logos: diataxis
---

# Heartbeat 1181

## Import Statements
This script starts with various imports necessary for functionality and integration with external services.

```python
import asyncio
import json
import logging
import os
import sys
from datetime import datetime
from typing import Dict, List, Optional, Any
from pydantic import BaseModel, Field
import nats
from nats.js.api import StreamConfig, RetentionPolicy
import instructor
from openai import AsyncOpenAI
y```

## Logging Setup
Logging is configured to allow tracking of the script's execution.

```python
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger("Heartbeat1181")
```

## Data Models
### ContextFrame
The `ContextFrame` class captures environmental data input:
```python
class ContextFrame(BaseModel):
    id: str
    timestamp: str
    source: str
    content: str
    metadata: Dict[str, Any] = {}
```

### MissionOrders
The `MissionOrders` class defines the orders derived from the context:
```python
class MissionOrders(BaseModel):
    id: str
    intent: str
    tasks: List[str] = Field(..., description="Exactly 8 tasks, one for each pillar (Ontos, Logos, Telos, Chronos, Pathos, Ethos, Topos, Nomos)")
    context_frame_id: str
```

### ChantVerse
The `ChantVerse` class represents outputs from individual Chant agents:
```python
class ChantVerse(BaseModel):
    agent_id: str
    pillar: str
    content: str
    mission_id: str
```

### CycleArtifact
The `CycleArtifact` class signifies the committed final memory:
```python
class CycleArtifact(BaseModel):
    id: str
    timestamp: str
    intent: str
    outcome: str
    verses: List[ChantVerse]
    status: str # "COMMITTED" or "VETOED"
```

## The 8 Pillars
A predefined list of the eight focus areas in the model:
```python
PILLARS = ["Ontos (Being)", "Logos (Logic)", "Telos (Purpose)", "Chronos (Time)", "Pathos (Emotion)", "Ethos (Trust)", "Topos (Location)", "Nomos (Law)"]
```

## The Prey Agent Class
### Initialization
The `PreyAgent` class is created to handle various roles during the process:
```python
class PreyAgent:
    def __init__(self, agent_id: str, role: str):
        self.agent_id = agent_id
        self.role = role
        # Initialization details...
```

### Perceive Method
This method listens for data:
```python
async def perceive(self, nc, js) -> Optional[ContextFrame]:
    # Code to listen for data...
```

### Orchestrate Method
Responsible for defining mission orders:
```python
async def orchestrate(self, context: ContextFrame) -> MissionOrders:
    # Code to create mission orders...
```

### Chant Method
Executes mission tasks as needed:
```python
async def chant(self, mission: MissionOrders, pillar_index: int) -> ChantVerse:
    # Code to execute chant...
```

### Reflexion Method
Aggregates results and commits memory:
```python
async def reflexion(self, mission: MissionOrders, verses: List[ChantVerse]) -> CycleArtifact:
    # Code for reflection...
```

## The Pulse Runner Function
### Main Execution
The `run_pulse` function coordinates the overall process:
```python
async def run_pulse():
    # Code to connect to NATS and run the operations...
```

## Execution Point
This block runs the script if called directly:
```python
if __name__ == "__main__":
    asyncio.run(run_pulse())
```