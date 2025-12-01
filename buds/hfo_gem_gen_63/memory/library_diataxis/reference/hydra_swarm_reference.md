---
holon:
  id: f0eb2f6c-1cf0-49f5-a742-63a3b89c3eb0
  type: codex_entry
  quadrant: reference
  source_ref: /home/tommytai3/hive_fleet_obsidian_2025_11/buds/hfo_gem_gen_63/src/swarm.py
hexagon:
  ontos: owner
  logos: diataxis

---

# HydraSwarm Module Documentation

## Classes

### `PillarOpinion`

#### Description
Represents an opinion from a council pillar regarding a specific topic.

#### Attributes
- **pillar** (str): The name of the pillar.
- **perspective** (str): The analysis provided by the pillar.
- **vote** (str): Voting status, can be `YES`, `NO`, or `ABSTAIN`. (default is `ABSTAIN`)
- **reasoning** (str): Explanation for the vote.

### `CouncilResult`

#### Description
Represents the result of a council meeting regarding a specific topic.

#### Attributes
- **topic** (str): The topic of discussion.
- **consensus** (str): The overall decision made by the council (`APPROVED`, `REJECTED`, or `DEADLOCK`).
- **opinions** (List[PillarOpinion]): The opinions from each pillar regarding the topic.
- **action_plan** (str): A summary of the council’s decision and perspectives shared.

### `HydraSwarm`

#### Description
This class represents the Hydra Swarm (Gen 63), which consists of a council of 8 pillars that debate and decide on upgrades.

#### Methods
- **`__init__`**(): Initializes a new `HydraSwarm` instance containing a `ResearchAgent` and the 8 pillars.
- **`consult_pillar`**(pillar_id: int, topic: str, context: str) -> PillarOpinion:
  - Asks a specific pillar for their opinion on a topic.
- **`convene_council`**(topic: str) -> CouncilResult:
  - Convenes the council of pillars to debate a specific topic and reach a consensus.

## Example Usage
```python
if __name__ == "__main__":
    swarm = HydraSwarm()
    
    # Test the Council
    topic = "Should we integrate MediaPipe for Gesture Control in Gen 63?"
    result = asyncio.run(swarm.convene_council(topic))
    
    print(f"\n🏛️ COUNCIL RESULT: {result.consensus}")
    print(result.action_plan)
```