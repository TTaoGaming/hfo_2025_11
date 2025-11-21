import os
import asyncio
import ray
import logging
import uuid
import random
import json
import argparse
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import instructor
from openai import OpenAI
from body.hands.tools import ToolSet

# --- Setup ---
load_dotenv()
logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger("fractal_swarm")

# --- DNA (Pydantic Models) ---


class Persona(BaseModel):
    """Evolutionary Unit: Defines HOW the agent thinks."""

    role: str
    style: str  # e.g., "Academic", "Tabloid", "Skeptical"
    temperature: float
    model: str


class StigmergySignal(BaseModel):
    """A unit of information on the Blackboard."""

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    round: int
    topic: str
    content: str
    confidence: float
    source_agent: str
    type: str = "FINDING"  # FINDING, REFUTATION, QUERY


class ResearchResult(BaseModel):
    content: str
    confidence: float = Field(..., description="Confidence score 0.0-1.0")
    source: str = Field(..., description="Source of the information (Tool used)")


class SquadReport(BaseModel):
    squad_id: str
    domain: str
    findings: str
    consensus_score: float
    key_evidence: List[str]


class FinalDigest(BaseModel):
    mission_id: str
    executive_summary: str
    detailed_analysis: Dict[str, str]  # Domain -> Analysis
    overall_confidence: float
    recommendation: str


# --- Infrastructure Layer (Ray Actors) ---


@ray.remote
class StigmergyBoard:
    """
    The Global Blackboard (Simulating NATS).
    All Squads and Agents can read/write here.
    """

    def __init__(self):
        self.signals: List[StigmergySignal] = []

    def publish(self, signal_data: Dict[str, Any]):
        signal = StigmergySignal(**signal_data)
        self.signals.append(signal)
        return True

    def get_signals(
        self, topic: Optional[str] = None, min_round: int = 0
    ) -> List[Dict[str, Any]]:
        # Return dicts because Pydantic objects can be tricky across Ray boundaries sometimes
        filtered = [
            s.model_dump()
            for s in self.signals
            if (topic is None or s.topic == topic) and s.round >= min_round
        ]
        return filtered

    def get_all_signals(self) -> List[Dict[str, Any]]:
        return [s.model_dump() for s in self.signals]


class EvolutionaryForge:
    """
    MAP-Elites Implementation for Agent Personas.
    """

    def __init__(self):
        self.gene_pool = [
            Persona(
                role="Academic Researcher",
                style="Formal, rigorous, citation-heavy",
                temperature=0.2,
                model="x-ai/grok-4.1-fast",
            ),
            Persona(
                role="Investigative Journalist",
                style="Narrative, connecting dots, skeptical",
                temperature=0.7,
                model="x-ai/grok-4.1-fast",
            ),
            Persona(
                role="Data Scientist",
                style="Analytical, numbers-focused, structured",
                temperature=0.1,
                model="x-ai/grok-4.1-fast",
            ),
            Persona(
                role="Futurist",
                style="Speculative, trend-focused, visionary",
                temperature=0.8,
                model="x-ai/grok-4.1-fast",
            ),
        ]

    def select_persona(self) -> Persona:
        return random.choice(self.gene_pool)

    def mutate(self, persona: Persona) -> Persona:
        """Create a variant of the persona."""
        new_temp = max(0.0, min(1.0, persona.temperature + random.uniform(-0.1, 0.1)))
        return Persona(
            role=persona.role,
            style=persona.style,
            temperature=new_temp,
            model=persona.model,
        )


# --- The Virtual Agent (Level 0 - The Cell) ---
class AgentStep(BaseModel):
    thought: str = Field(..., description="Reasoning for the current step")
    tool_name: Optional[str] = Field(
        None, description="Tool to use: 'read_file', 'search_files', 'list_dir'"
    )
    tool_args: Optional[str] = Field(None, description="Arguments for the tool")
    final_answer: Optional[str] = Field(
        None, description="The final research finding if task is complete"
    )
    confidence: Optional[float] = Field(
        None, description="Confidence score 0.0-1.0 (only for final answer)"
    )


class VirtualAgent:
    def __init__(
        self,
        agent_id: str,
        persona: Persona,
        task: str,
        domain: str,
        stigmergy_handle,
        agent_dir: Path,
    ):
        self.agent_id = agent_id
        self.persona = persona
        self.task = task
        self.domain = domain
        self.stigmergy = stigmergy_handle
        self.agent_dir = agent_dir
        self.agent_dir.mkdir(parents=True, exist_ok=True)
        self.client = instructor.from_openai(
            OpenAI(
                base_url=os.getenv("OPENROUTER_BASE_URL"),
                api_key=os.getenv("OPENROUTER_API_KEY"),
            ),
            mode=instructor.Mode.JSON,
        )

    async def execute_round(self, round_id: int) -> ResearchResult:
        # 1. Perceive (Stigmergy)
        context = ""
        if round_id > 1:
            signals = await self.stigmergy.get_signals.remote(
                topic=self.domain, min_round=round_id - 1
            )
            if signals:
                context = "Context from previous round (Stigmergy):\n" + "\n".join(
                    [
                        f"- [{s['type']}] {s['content']} (Conf: {s['confidence']})"
                        for s in signals
                    ]
                )

        # 2. React (Loop with Tools)
        # Inject File System Map for context
        fs_map = ToolSet.list_directory(".")

        system_prompt = (
            f"You are a {self.persona.role}. Style: {self.persona.style}.\n"
            f"Task: {self.task}\n"
            f"Round: {round_id}. {context}\n"
            f"Current Directory Structure: {fs_map}\n"
            "You have access to local files. Use 'list_dir', 'read_file', 'search_files' to investigate.\n"
            "If you need to explore 'eyes/archive' or 'memory', use 'list_dir' on those paths first.\n"
            "Iterate up to 3 times using tools before providing a final answer."
        )

        messages = [
            {"role": "system", "content": system_prompt},
            {
                "role": "user",
                "content": "Begin research. Use tools if necessary to find ground truth in the files.",
            },
        ]

        final_result = None

        for step_i in range(4):  # Max 4 steps (3 tools + 1 final)
            try:
                # Simulating "Thinking"
                await asyncio.sleep(0.1)

                step_response = self.client.chat.completions.create(
                    model=self.persona.model,
                    response_model=AgentStep,
                    messages=messages,
                    temperature=self.persona.temperature,
                )

                # Log the step
                messages.append(
                    {"role": "assistant", "content": str(step_response.model_dump())}
                )
                self._save_audit(round_id, messages, step_response, step_i)

                if step_response.final_answer:
                    final_result = ResearchResult(
                        content=step_response.final_answer,
                        confidence=step_response.confidence or 0.5,
                        source="Local Files + Analysis",
                    )
                    break

                # Execute Tool
                tool_result = "Error: No tool specified"
                if step_response.tool_name == "read_file":
                    tool_result = ToolSet.read_file(step_response.tool_args)
                elif step_response.tool_name == "list_dir":
                    tool_result = ToolSet.list_directory(step_response.tool_args or ".")
                elif step_response.tool_name == "search_files":
                    tool_result = ToolSet.grep_files(step_response.tool_args)

                messages.append(
                    {
                        "role": "user",
                        "content": f"Tool Output ({step_response.tool_name}): {tool_result}",
                    }
                )

            except Exception as e:
                print(f"Agent {self.agent_id} error: {e}")
                final_result = ResearchResult(
                    content=f"Error: {str(e)}", confidence=0.0, source="System"
                )
                break

        if not final_result:
            final_result = ResearchResult(
                content="Agent failed to reach conclusion.",
                confidence=0.0,
                source="System",
            )

        # 3. Yield (Publish to Stigmergy)
        await self.stigmergy.publish.remote(
            {
                "round": round_id,
                "topic": self.domain,
                "content": final_result.content,
                "confidence": final_result.confidence,
                "source_agent": self.agent_id,
                "type": "REFUTATION"
                if "refut" in final_result.content.lower()
                else "FINDING",
            }
        )

        return final_result

    def _save_audit(self, round_id, messages, step_response, step_num):
        filename = self.agent_dir / f"round_{round_id}_step_{step_num}.md"
        with open(filename, "w") as f:
            f.write(
                f"# Audit Log: {self.agent_id} - Round {round_id} - Step {step_num}\n"
            )
            f.write(f"**Timestamp**: {datetime.now().isoformat()}\n")
            f.write(f"**Thought**: {step_response.thought}\n")
            if step_response.tool_name:
                f.write(
                    f"**Tool**: {step_response.tool_name}('{step_response.tool_args}')\n"
                )
            if step_response.final_answer:
                f.write(f"**Final Answer**: {step_response.final_answer}\n")
            f.write("\n## Full Context\n")
            for m in messages:
                f.write(f"### {m['role'].upper()}\n")
                f.write(f"```text\n{m['content']}\n```\n\n")


# --- The Squad Leader (Level 1 - The Holon) ---
@ray.remote
class SquadLeader:
    def __init__(
        self,
        squad_id: str,
        domain: str,
        sub_questions: List[str],
        stigmergy_handle,
        mission_path: str,
    ):
        self.squad_id = squad_id
        self.domain = domain
        self.sub_questions = sub_questions
        self.stigmergy = stigmergy_handle
        self.mission_path = Path(mission_path)
        self.squad_path = self.mission_path / "squads" / self.squad_id
        self.squad_path.mkdir(parents=True, exist_ok=True)
        (self.squad_path / "agents").mkdir(exist_ok=True)

        self.forge = EvolutionaryForge()  # Each squad has a local forge for now
        self.client = instructor.from_openai(
            OpenAI(
                base_url=os.getenv("OPENROUTER_BASE_URL"),
                api_key=os.getenv("OPENROUTER_API_KEY"),
            ),
            mode=instructor.Mode.JSON,
        )

    async def run_squad(self) -> SquadReport:
        print(f"   🛡️ Squad {self.squad_id} mobilizing for domain: {self.domain}...")

        # 1. Spawn Virtual Agents with Evolved Personas
        agents = []
        for i, q in enumerate(self.sub_questions):
            persona = self.forge.select_persona()
            # Mutate slightly for diversity
            persona = self.forge.mutate(persona)
            agent_dir = self.squad_path / "agents" / f"{self.squad_id}-Ag{i}"
            agent = VirtualAgent(
                agent_id=f"{self.squad_id}-Ag{i}",
                persona=persona,
                task=q,
                domain=self.domain,
                stigmergy_handle=self.stigmergy,
                agent_dir=agent_dir,
            )
            agents.append(agent)

        # 2. Iterative Cycles (Temporal Dilation)
        # Round 1: Exploration
        print(f"   🔄 Squad {self.squad_id} - Round 1: Exploration")
        _ = await asyncio.gather(*[a.execute_round(1) for a in agents])

        # Round 2: Refinement (Reading Stigmergy)
        print(f"   🔄 Squad {self.squad_id} - Round 2: Refinement & Debate")
        results_r2 = await asyncio.gather(*[a.execute_round(2) for a in agents])

        # 3. Synthesize (The Consensus)
        valid_results = [r for r in results_r2 if r.confidence > 0.5]

        if not valid_results:
            return SquadReport(
                squad_id=self.squad_id,
                domain=self.domain,
                findings="No valid findings.",
                consensus_score=0.0,
                key_evidence=[],
            )

        # Synthesis LLM Call
        synthesis_prompt = f"Synthesize these {len(valid_results)} findings into a cohesive report on {self.domain}."
        findings_text = "\n".join(
            [f"- {r.content} (Conf: {r.confidence})" for r in valid_results]
        )

        messages = [
            {
                "role": "system",
                "content": "You are a Squad Leader. Synthesize the findings of your agents.",
            },
            {
                "role": "user",
                "content": f"{synthesis_prompt}\n\nData:\n{findings_text}",
            },
        ]

        synthesis = self.client.chat.completions.create(
            model="x-ai/grok-4.1-fast", response_model=SquadReport, messages=messages
        )
        synthesis.squad_id = self.squad_id
        synthesis.domain = self.domain

        self._save_squad_report(synthesis)
        self._save_audit(messages, synthesis)
        print(
            f"   ✅ Squad {self.squad_id} reporting in. Score: {synthesis.consensus_score}"
        )
        return synthesis

    def _save_audit(self, messages, result):
        filename = self.squad_path / "synthesis_audit.md"
        with open(filename, "w") as f:
            f.write(f"# Audit Log: Squad {self.squad_id} Synthesis\n")
            f.write(f"**Timestamp**: {datetime.now().isoformat()}\n\n")
            f.write("## Prompts\n")
            for m in messages:
                f.write(f"### {m['role'].upper()}\n")
                f.write(f"```text\n{m['content']}\n```\n\n")
            f.write("## Output\n")
            f.write(f"**Consensus Score**: {result.consensus_score}\n")
            f.write(f"**Findings**: {result.findings}\n")

    def _save_squad_report(self, report):
        filename = self.squad_path / "squad_report.md"
        with open(filename, "w") as f:
            f.write(f"# Squad {report.squad_id} Report: {report.domain}\n")
            f.write(f"**Consensus Score**: {report.consensus_score}\n\n")
            f.write("## Findings\n")
            f.write(report.findings)
            f.write("\n\n## Key Evidence\n")
            for ev in report.key_evidence:
                f.write(f"- {ev}\n")


# --- The Commander (Level 2 - The Overmind) ---
class FractalResearchSwarm:
    def __init__(self):
        if not ray.is_initialized():
            ray.init(ignore_reinit_error=True)
        self.client = instructor.from_openai(
            OpenAI(
                base_url=os.getenv("OPENROUTER_BASE_URL"),
                api_key=os.getenv("OPENROUTER_API_KEY"),
            ),
            mode=instructor.Mode.JSON,
        )
        # Initialize Global Stigmergy Board
        self.stigmergy = StigmergyBoard.remote()

    async def execute_mission(
        self, query: str, num_domains: int = 3, agents_per_domain: int = 5
    ) -> FinalDigest:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        short_id = str(uuid.uuid4())[:8]
        mission_id = f"{timestamp}_{short_id}"
        mission_dir = Path(f"memory/missions/{mission_id}")
        mission_dir.mkdir(parents=True, exist_ok=True)

        print(f"🦅 Fractal Swarm Activated. Mission ID: {mission_id}")
        print(f"📂 Mission Output: {mission_dir}")
        print(f"📜 Query: {query}")
        print(
            f"🔢 Scale: {num_domains} Squads x {agents_per_domain} Agents = {num_domains * agents_per_domain} Total Agents"
        )

        # 1. Strategic Decomposition (Commander)
        print("\n🧠 Commander: Decomposing Mission...")

        # Dynamic Domain Generation
        if num_domains == 3:
            domains = ["Historical Context", "Current State", "Future Implications"]
        else:
            # If scaling up, we need the LLM to generate N domains
            print(f"   Generating {num_domains} research domains...")
            domains_resp = self.client.chat.completions.create(
                model="x-ai/grok-4.1-fast",
                response_model=List[str],
                messages=[
                    {
                        "role": "system",
                        "content": f"Generate exactly {num_domains} distinct research domains/perspectives to comprehensively analyze the user's query.",
                    },
                    {"role": "user", "content": query},
                ],
            )
            domains = domains_resp[:num_domains]

        # 2. Tactical Decomposition (Platoon Leaders -> Squads)
        squad_actors = []
        for i, domain in enumerate(domains):
            sub_questions = [
                f"Investigate aspect {j} of {domain} related to '{query}'"
                for j in range(1, agents_per_domain + 1)
            ]

            # Spawn Remote Ray Actor with Stigmergy Handle
            actor = SquadLeader.remote(  # type: ignore
                squad_id=f"Sq-{i+1}",
                domain=domain,
                sub_questions=sub_questions,
                stigmergy_handle=self.stigmergy,
                mission_path=str(mission_dir),
            )
            squad_actors.append(actor)

        # 3. Parallel Execution (The Swarm)
        print(
            f"\n🚀 Launching {len(squad_actors)} Squads (Total {len(squad_actors)*agents_per_domain} Virtual Agents)..."
        )
        squad_reports = await asyncio.gather(
            *[actor.run_squad.remote() for actor in squad_actors]
        )

        # 4. Final Synthesis (The Digest)
        print("\n📝 Commander: Synthesizing Final Digest...")

        avg_confidence = sum([r.consensus_score for r in squad_reports]) / len(
            squad_reports
        )

        messages = [
            {
                "role": "system",
                "content": "You are the Overmind. Produce a Final Intelligence Digest from these Squad Reports.",
            },
            {"role": "user", "content": str([r.model_dump() for r in squad_reports])},
        ]

        digest = self.client.chat.completions.create(
            model="x-ai/grok-4.1-fast", response_model=FinalDigest, messages=messages
        )
        digest.mission_id = mission_id
        digest.overall_confidence = avg_confidence

        self._save_final_digest(digest, mission_dir)
        self._save_audit(messages, digest, mission_dir)

        # Save Stigmergy Log
        signals = await self.stigmergy.get_all_signals.remote()
        with open(mission_dir / "stigmergy_log.json", "w") as f:
            json.dump(signals, f, indent=2)

        return digest

    def _save_audit(self, messages, result, mission_dir):
        filename = mission_dir / "commander_audit.md"
        with open(filename, "w") as f:
            f.write("# Audit Log: Commander Synthesis\n")
            f.write(f"**Timestamp**: {datetime.now().isoformat()}\n\n")
            f.write("## Prompts\n")
            for m in messages:
                f.write(f"### {m['role'].upper()}\n")
                f.write(f"```text\n{m['content']}\n```\n\n")
            f.write("## Output\n")
            f.write(f"**Overall Confidence**: {result.overall_confidence}\n")
            f.write(f"**Summary**: {result.executive_summary}\n")

    def _save_final_digest(self, digest, mission_dir):
        with open(mission_dir / "final_digest.md", "w") as f:
            f.write(f"# Mission Digest: {digest.mission_id}\n")
            f.write(f"**Overall Confidence**: {digest.overall_confidence}\n")
            f.write(f"**Recommendation**: {digest.recommendation}\n\n")
            f.write("## Executive Summary\n")
            f.write(digest.executive_summary)
            f.write("\n\n## Detailed Analysis\n")
            for domain, analysis in digest.detailed_analysis.items():
                f.write(f"### {domain}\n")
                f.write(analysis)
                f.write("\n\n")


# --- Entrypoint ---
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fractal Research Swarm")
    parser.add_argument(
        "query",
        nargs="?",
        default="What is the current state of Autonomous AI Agents in late 2025?",
        help="Research query",
    )
    parser.add_argument(
        "--domains", type=int, default=3, help="Number of research domains (Squads)"
    )
    parser.add_argument(
        "--agents", type=int, default=5, help="Number of agents per domain"
    )

    args = parser.parse_args()

    async def main():
        swarm = FractalResearchSwarm()
        result = await swarm.execute_mission(
            args.query, num_domains=args.domains, agents_per_domain=args.agents
        )

        print("\n🏁 FINAL INTELLIGENCE DIGEST 🏁")
        print("===============================")
        print(f"Confidence: {result.overall_confidence}")
        print(f"Summary: {result.executive_summary}")
        print("\nDetailed Analysis:")
        for domain, analysis in result.detailed_analysis.items():
            print(f"\n[{domain}]:\n{analysis}")

    asyncio.run(main())
