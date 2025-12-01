import asyncio
import logging
import os
import sys
from typing import List, Dict, Any
from pydantic import BaseModel, Field

# Add root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.config import settings
from src.research_agent import ResearchAgent

# Setup Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("HydraSwarm")

class PillarOpinion(BaseModel):
    pillar: str
    perspective: str
    vote: str = Field(description="YES, NO, or ABSTAIN")
    reasoning: str

class CouncilResult(BaseModel):
    topic: str
    consensus: str
    opinions: List[PillarOpinion]
    action_plan: str

class HydraSwarm:
    """
    The Hydra Swarm (Gen 63).
    A Council of 8 Pillars that debate and decide on upgrades.
    """
    def __init__(self):
        self.researcher = ResearchAgent()
        self.pillars = {
            1: "Navigator (Strategy/Goal)",
            2: "Observer (Input/Sensor)",
            3: "Bridger (Connection/Memory)",
            4: "Shaper (Tool/Action)",
            5: "Injector (Timing/Pulse)",
            6: "Disruptor (Test/Red Team)",
            7: "Immunizer (Security/Blue Team)",
            8: "Assimilator (Storage/Record)"
        }

    async def consult_pillar(self, pillar_id: int, topic: str, context: str) -> PillarOpinion:
        """
        Asks a specific Pillar for their opinion.
        """
        pillar_name = self.pillars[pillar_id]
        logger.info(f"🗣️ Consulting Pillar {pillar_id}: {pillar_name}")
        
        prompt = f"""
        You are the {pillar_name} of the Hive Fleet Obsidian.
        
        TOPIC: {topic}
        
        CONTEXT:
        {context}
        
        YOUR ROLE:
        Analyze this topic strictly from the perspective of {pillar_name}.
        
        OUTPUT FORMAT (JSON):
        {{
            "pillar": "{pillar_name}",
            "perspective": "Your analysis...",
            "vote": "YES/NO/ABSTAIN",
            "reasoning": "Why you voted this way..."
        }}
        """
        
        try:
            # We use the researcher's client for raw completion for now
            # In a full implementation, we'd use instructor for strict JSON
            completion = self.researcher.client.chat.completions.create(
                model=self.researcher.model,
                messages=[
                    {"role": "system", "content": f"You are the {pillar_name}."},
                    {"role": "user", "content": prompt}
                ],
                response_format={"type": "json_object"}
            )
            content = completion.choices[0].message.content
            return PillarOpinion.model_validate_json(content)
        except Exception as e:
            logger.error(f"Pillar {pillar_id} failed: {e}")
            return PillarOpinion(pillar=pillar_name, perspective="Error", vote="ABSTAIN", reasoning=str(e))

    async def convene_council(self, topic: str) -> CouncilResult:
        """
        Convenes the Council of 8 to debate a topic.
        """
        logger.info(f"🔔 Convening Council on: {topic}")
        
        # 1. Gather Context (Research)
        context = self.researcher.research(topic)
        
        # 2. Consult Pillars (Parallel)
        tasks = [self.consult_pillar(i, topic, context) for i in range(1, 9)]
        opinions = await asyncio.gather(*tasks)
        
        # 3. Synthesize Consensus
        yes_votes = sum(1 for o in opinions if o.vote == "YES")
        no_votes = sum(1 for o in opinions if o.vote == "NO")
        
        consensus = "APPROVED" if yes_votes > no_votes else "REJECTED"
        if yes_votes == no_votes:
            consensus = "DEADLOCK"
            
        action_plan = f"The Council has spoken. {yes_votes} YES, {no_votes} NO.\n"
        action_plan += "Summary of Perspectives:\n"
        for op in opinions:
            action_plan += f"- **{op.pillar}**: {op.reasoning}\n"
            
        return CouncilResult(
            topic=topic,
            consensus=consensus,
            opinions=opinions,
            action_plan=action_plan
        )

if __name__ == "__main__":
    swarm = HydraSwarm()
    
    # Test the Council
    topic = "Should we integrate MediaPipe for Gesture Control in Gen 63?"
    result = asyncio.run(swarm.convene_council(topic))
    
    print(f"\n🏛️ COUNCIL RESULT: {result.consensus}")
    print(result.action_plan)
