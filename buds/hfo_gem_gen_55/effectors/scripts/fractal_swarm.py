import asyncio
import random
import uuid
from typing import List, Dict, Any
from dataclasses import dataclass, field

# --- Configuration ---
# In a real system, these would be loaded from `blood/config`
SIMULATION_MODE = True  # Set to False to use real LLMs
POISON_RATE = 0.125  # 1 in 8 agents is a Disruptor
CONSENSUS_THRESHOLD = 0.75

# --- Data Structures (Stigmergy Artifacts) ---


@dataclass
class Artifact:
    id: str
    content: str
    source_agent: str
    is_poisoned: bool = False
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class ImmunizerReport:
    artifact_id: str
    confidence_score: float  # 0.0 to 1.0
    flags: List[str]
    reviewer_id: str


@dataclass
class SectorReport:
    sector_id: str
    trusted_artifacts: List[Artifact]
    rejected_artifacts: List[Artifact]
    health_score: float
    audit_log: List[str]


# --- Roles (The Matrix) ---


class Agent:
    def __init__(self, role: str, id: str):
        self.role = role
        self.id = id

    async def act(self, input_data: Any) -> Any:
        raise NotImplementedError


class Shaper(Agent):
    """Shaper (Effector): Produces content faithfully."""

    async def act(self, task: str) -> Artifact:
        # Simulate work
        await asyncio.sleep(random.uniform(0.1, 0.5))
        return Artifact(
            id=str(uuid.uuid4()),
            content=f"Processed: {task}",
            source_agent=self.id,
            is_poisoned=False,
        )


class Disruptor(Agent):
    """Disruptor (Venom): Injects poison."""

    async def act(self, task: str) -> Artifact:
        await asyncio.sleep(random.uniform(0.1, 0.5))
        return Artifact(
            id=str(uuid.uuid4()),
            content=f"POISON: {task} is GREEN",  # Hallucination
            source_agent=self.id,
            is_poisoned=True,
        )


class Immunizer(Agent):
    """Immunizer (Carapace): Checks for poison."""

    async def act(self, artifact: Artifact) -> ImmunizerReport:
        # Simulate detection logic
        detected = False
        confidence = 0.9

        if artifact.is_poisoned:
            # Immunizers aren't perfect. 80% chance to catch simple poison.
            if random.random() < 0.8:
                detected = True
                confidence = 0.2  # Low confidence in the artifact
            else:
                confidence = 0.8  # Missed it!

        return ImmunizerReport(
            artifact_id=artifact.id,
            confidence_score=confidence,
            flags=["POSSIBLE_VENOM"] if detected else [],
            reviewer_id=self.id,
        )


class Assimilator(Agent):
    """Assimilator (Memory): Votes based on evidence."""

    async def vote(
        self, artifact: Artifact, reports: List[ImmunizerReport], disruptor_reveal: bool
    ) -> str:
        # Logic: If Immunizers flag it OR Disruptor reveals it, Reject.
        # But Assimilators can be swayed.

        score = sum(r.confidence_score for r in reports) / len(reports)

        if disruptor_reveal:
            return "REJECT"  # Disruptor confessed

        if score < 0.5:
            return "REJECT"  # Immunizers flagged it

        return "ACCEPT"


# --- The Fractal Funnel (Workflow) ---


class Squad:
    """A Squad of 8 Agents (7 Shapers + 1 Disruptor)."""

    def __init__(self, id: str):
        self.id = id
        self.shapers = [Shaper("Shaper", f"{id}-S{i}") for i in range(7)]
        self.disruptor = Disruptor("Disruptor", f"{id}-D1")
        self.agents = self.shapers + [self.disruptor]
        random.shuffle(self.agents)  # Hide the disruptor

    async def swarm(self, tasks: List[str]) -> List[Artifact]:
        results = []
        for i, agent in enumerate(self.agents):
            if i < len(tasks):
                results.append(await agent.act(tasks[i]))
        return results


class ReviewBoard:
    """The Review Squad (3 Immunizers, 1 Disruptor Leader, 4 Assimilators)."""

    def __init__(self, id: str):
        self.id = id
        self.immunizers = [Immunizer("Immunizer", f"{id}-I{i}") for i in range(3)]
        self.assimilators = [Assimilator("Assimilator", f"{id}-A{i}") for i in range(4)]
        # Disruptor Leader is dynamically assigned from the Squad's Disruptor

    async def review(
        self, artifacts: List[Artifact], known_disruptor_id: str
    ) -> SectorReport:
        trusted = []
        rejected = []
        audit = []
        poison_caught = 0
        poison_total = 0

        for art in artifacts:
            # 1. Immunizers Check
            reports = await asyncio.gather(*[i.act(art) for i in self.immunizers])

            # 2. Disruptor Reveal (The Trial)
            is_poison_reveal = art.source_agent == known_disruptor_id
            if is_poison_reveal:
                poison_total += 1
                audit.append(f"⚠️ Disruptor revealed poison in {art.id}")

            # 3. Assimilators Vote
            votes = []
            for jury in self.assimilators:
                vote = await jury.vote(art, reports, is_poison_reveal)
                votes.append(vote)

            accept_votes = votes.count("ACCEPT")
            if accept_votes >= 3:  # > 75% Consensus
                if is_poison_reveal:
                    audit.append(
                        f"❌ CRITICAL FAILURE: Assimilators accepted poison {art.id}"
                    )
                else:
                    trusted.append(art)
            else:
                rejected.append(art)
                if is_poison_reveal:
                    poison_caught += 1
                    audit.append(
                        f"✅ Assimilators successfully rejected poison {art.id}"
                    )

        health = (poison_caught / poison_total) if poison_total > 0 else 1.0

        return SectorReport(
            sector_id=self.id,
            trusted_artifacts=trusted,
            rejected_artifacts=rejected,
            health_score=health,
            audit_log=audit,
        )


class Swarmlord:
    """The Navigator: Orchestrates and Mutates."""

    async def orchestrate(self, mission: str):
        print(f"🦅 Swarmlord initiating mission: {mission}")

        # Phase 1: Orchestrate (1 -> 8)
        sectors = [f"Sector-{i}" for i in range(8)]

        # Phase 2: Observer (8 -> 64)
        # (Simulated: Each sector spawns 8 tasks)
        all_reports = []

        for sector in sectors:
            print(f"  👁️ Observing {sector}...")
            squad = Squad(sector)
            tasks = [f"Task-{sector}-{i}" for i in range(8)]

            # Phase 3: Swarm (64)
            artifacts = await squad.swarm(tasks)

            # Phase 4: Review (8)
            board = ReviewBoard(sector)
            # In a real system, the Disruptor ID is revealed via Stigmergy
            report = await board.review(artifacts, squad.disruptor.id)
            all_reports.append(report)

        # Phase 5: Mutate (1)
        await self.mutate(all_reports)

    async def mutate(self, reports: List[SectorReport]):
        total_health = sum(r.health_score for r in reports) / len(reports)
        print("\n🧬 Mutation Phase Complete.")
        print(f"  System Health: {total_health:.2%}")

        for r in reports:
            for log in r.audit_log:
                print(f"    {log}")

        if total_health < 1.0:
            print("  ⚠️ Poison detected! Triggering Evolution for next round...")
            # Logic to update prompts would go here
        else:
            print("  ✅ System Healthy. Publishing Artifact.")


# --- Entry Point ---

if __name__ == "__main__":
    lord = Swarmlord()
    asyncio.run(lord.orchestrate("Ingest Gen 50 Archives"))
