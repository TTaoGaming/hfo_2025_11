import os
import sys
import asyncio
import logging
import json
import instructor
from openai import AsyncOpenAI
from typing import List, Dict, Optional
from dotenv import load_dotenv

# Add root to path
sys.path.append(os.getcwd())

from buds.hfo_gem_gen_60.blood.schema import Level0Artifact, Level1Artifact, Level2Artifact, MemoryItem
from buds.hfo_gem_gen_60.memory.database import IronLedger

# Load Env
load_dotenv()

# Setup Logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger("PreySwarm")

# Constants
CHUNK_SIZE = 20000 # Characters (~5k tokens)
OVERLAP = 1000

# The 8 Metaphysical Pillars of HFO
PILLARS = {
    1: "Ontos (Being/Existence)",
    2: "Logos (Logic/Reason)",
    3: "Telos (Purpose/Goal)",
    4: "Chronos (Time/Sequence)",
    5: "Pathos (Emotion/User Experience)",
    6: "Ethos (Trust/Security)",
    7: "Topos (Location/Structure)",
    8: "Nomos (Law/Constraint)"
}

class PreySwarm:
    """
    The Swarm of 8 PREY Agents (Byzantine Quorum).
    Implements the 8-8-8-8 Logic Canalization Protocol.
    """
    def __init__(self):
        self.api_key = os.getenv("OPENROUTER_API_KEY") or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            logger.warning("⚠️ No API Key found. Prey Swarm will be dormant.")
            self.client = None
        else:
            self.client = instructor.from_openai(
                AsyncOpenAI(
                    base_url="https://openrouter.ai/api/v1",
                    api_key=self.api_key,
                ),
                mode=instructor.Mode.JSON,
            )
        
        self.ledger = IronLedger(db_path="buds/hfo_gem_gen_60/memory/hfo_gen_60_memory.db")
        self.config = self._load_config()

    def _load_config(self) -> Dict:
        """Load the Weekly Champions configuration."""
        try:
            with open("buds/hfo_gem_gen_60/memory/weekly_champions.json", "r") as f:
                config = json.load(f)
                self._validate_family_cap(config.get("quorum_models", []))
                return config
        except FileNotFoundError:
            logger.error("❌ weekly_champions.json not found! Using fallback.")
            return {
                "synthesizer_model": "x-ai/grok-4.1-fast:free",
                "quorum_models": ["google/gemini-2.0-flash-001"] * 8 # Fallback to single model
            }

    def _validate_family_cap(self, models: List[str]):
        """
        Enforce the 'Family Cap': No single provider can have > 2 seats.
        This prevents 'Monoculture Collapse' where one provider's bias dominates the quorum.
        """
        families = {}
        for m in models:
            # Extract family (e.g., 'openai' from 'openai/gpt-4')
            family = m.split("/")[0] if "/" in m else m
            families[family] = families.get(family, 0) + 1
        
        for family, count in families.items():
            if count > 2:
                logger.error(f"🚨 CANALIZATION VIOLATION: Family '{family}' has {count} seats! Max is 2.")
                logger.error("The Quorum is compromised by lack of diversity.")
                # We don't stop execution, but we flag it heavily.
            else:
                logger.info(f"✅ Family '{family}': {count}/2 seats.")

    def _split_text(self, text: str) -> List[str]:
        """Simple chunker with overlap."""
        chunks = []
        start = 0
        text_len = len(text)
        while start < text_len:
            end = start + CHUNK_SIZE
            chunks.append(text[start:end])
            start += CHUNK_SIZE - OVERLAP
        return chunks

    async def process_item(self, item: MemoryItem) -> Optional[object]:
        """
        Spawns 8 PREY Agents (Level 0) -> 1 Synthesizer (Level 1).
        Handles Recursive Reduction for large files.
        """
        if not self.client:
            logger.error("Cannot process: No Client")
            return None

        # RECURSIVE REDUCTION CHECK
        if len(item.content) > CHUNK_SIZE:
            logger.info(f"🐘 Large File Detected ({len(item.content)} chars). Initiating Recursive Reduction.")
            return await self._process_large_item(item)

        logger.info(f"🔔 Convening Prey Swarm for: {item.source_path}")
        
        # 1. Level 0: The 8 Pillars
        tasks = []
        models = self.config.get("quorum_models", [])
        
        # Ensure we have 8 models, cycle if necessary
        if len(models) < 8:
            logger.warning(f"Only {len(models)} models found. Cycling to fill 8 slots.")
            models = (models * 8)[:8]

        for i in range(1, 9):
            model = models[i-1]
            tasks.append(self._prey_task(i, model, item))
        
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        level0_artifacts = []
        for res in results:
            if isinstance(res, Level0Artifact):
                self.ledger.insert_level0(res)
                level0_artifacts.append(res)
            else:
                logger.error(f"PREY Agent failed: {res}")
        
        logger.info(f"✅ Level 0 Complete. {len(level0_artifacts)}/8 Artifacts filed.")

        # 2. Level 1: The Synthesis (Quorum)
        if len(level0_artifacts) >= 6: # Require 75% Quorum
            return await self._synthesize_quorum(item, level0_artifacts)
        else:
            logger.warning(f"⚠️ Quorum Failed. Only {len(level0_artifacts)}/8 agents reported. Synthesis aborted.")
            return None

    async def _process_large_item(self, item: MemoryItem) -> Optional[Level2Artifact]:
        """
        Handles large files by splitting them into chunks, processing each chunk,
        and then synthesizing the results (Level 2).
        """
        chunks = self._split_text(item.content)
        logger.info(f"🔪 Split into {len(chunks)} chunks.")
        
        chunk_results = []
        
        for i, chunk in enumerate(chunks):
            logger.info(f"🔄 Processing Chunk {i+1}/{len(chunks)}...")
            
            # Create a virtual sub-item
            sub_item = MemoryItem(
                source_path=f"{item.source_path}#chunk{i+1}",
                content=chunk,
                generation=item.generation,
                category=item.category,
                tags=item.tags + ["chunk"]
            )
            sub_item.compute_hash()
            
            # Insert sub-item into DB (so FKs work)
            try:
                self.ledger.insert(sub_item)
            except Exception:
                pass # Ignore if exists
            
            # Recursive Call
            result = await self.process_item(sub_item)
            if result:
                chunk_results.append(result)
        
        if not chunk_results:
            logger.error("❌ Recursive Reduction Failed: No chunks processed successfully.")
            return None

        # Synthesize Level 2
        return await self._synthesize_level2(item, chunk_results)

    async def _synthesize_level2(self, item: MemoryItem, artifacts: List[Level1Artifact]) -> Level2Artifact:
        """
        Level 2: Synthesize multiple Level 1 Artifacts into a higher-order truth.
        """
        synthesizer_model = self.config.get("synthesizer_model", "x-ai/grok-4.1-fast:free")
        logger.info(f"🪐 Synthesizing Level 2 (Fractal) with {synthesizer_model}...")
        
        summaries = []
        constituent_hashes = []
        
        for i, a in enumerate(artifacts):
            summaries.append(f"--- Chunk {i+1} Synthesis ---")
            summaries.append(a.synthesis)
            constituent_hashes.append(a.source_hash) # Use source hash of chunk as link
        
        prompt = f"""
        You are the Swarmlord (Fractal Synthesizer).
        You have received {len(artifacts)} Level 1 Reports from a large document: {item.source_path}
        
        Chunk Summaries:
        {chr(10).join(summaries)}
        
        Task:
        1. Synthesize these chunk summaries into a single, unified Master Truth for the entire document.
        2. Ensure continuity and flow between the chunks.
        3. Capture the "Grand Arc" of the content.
        
        Output strict JSON matching the Level2Artifact schema.
        """
        
        try:
            level2 = await self.client.chat.completions.create(
                model=synthesizer_model,
                messages=[
                    {"role": "system", "content": "You are the Swarmlord. Synthesize the Fractal Truth."},
                    {"role": "user", "content": prompt}
                ],
                response_model=Level2Artifact,
                max_retries=2
            )
            
            # Inject metadata
            level2.source_hash = item.content_hash
            level2.constituent_hashes = constituent_hashes
            level2.model_used = synthesizer_model
            
            self.ledger.insert_level2(level2)
            return level2
            
        except Exception as e:
            logger.error(f"❌ Level 2 Synthesis Failed: {e}")
            return None

    async def _prey_task(self, agent_id: int, model: str, item: MemoryItem) -> Level0Artifact:
        """
        A single PREY Agent's work (Level 0).
        Analyzes ALL 8 Pillars.
        """
        prompt = f"""
        You are PREY Agent #{agent_id} of the Hive Fleet Obsidian.
        
        Task: Analyze the provided file content across ALL 8 Metaphysical Pillars of HFO.
        
        Pillars:
        1. Ontos (Being/Existence)
        2. Logos (Logic/Reason)
        3. Telos (Purpose/Goal)
        4. Chronos (Time/Sequence)
        5. Pathos (Emotion/User Experience)
        6. Ethos (Trust/Security)
        7. Topos (Location/Structure)
        8. Nomos (Law/Constraint)
        
        Context:
        - File: {item.source_path}
        - Category: {item.category}
        
        Instructions:
        1. For EACH pillar, provide a summary, key findings, and a confidence score.
        2. Be precise and dense.
        
        Content:
        {item.content} 
        """
        
        try:
            # We use the Pydantic model to force structured output
            # EXECUTE PHASE
            artifact = await self.client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": "You are a precise analytical engine. Output JSON only."},
                    {"role": "user", "content": prompt}
                ],
                response_model=Level0Artifact,
                max_retries=2
            )
            
            # YIELD PHASE (Reflexion & Canalization)
            # Reflexion is handled by Instructor's validation loop (max_retries=2)
            
            # Inject metadata that the LLM might not know or might hallucinate
            artifact.source_hash = item.content_hash
            artifact.agent_id = agent_id
            artifact.model_used = model
            
            # ENFORCE ZERO TRUST: Cap Confidence at 50%
            # Even if the model is 100% sure, we only trust it 50%.
            for pillar_name in ["ontos", "logos", "telos", "chronos", "pathos", "ethos", "topos", "nomos"]:
                pillar_data = getattr(artifact, pillar_name)
                if pillar_data.confidence > 0.5:
                    pillar_data.confidence = 0.5
            
            return artifact
            
        except Exception as e:
            logger.error(f"Agent {agent_id} ({model}) crashed: {e}")
            raise e

    async def _synthesize_quorum(self, item: MemoryItem, artifacts: List[Level0Artifact]) -> Level1Artifact:
        """
        Level 1: Synthesize the 8 perspectives into one Truth.
        """
        synthesizer_model = self.config.get("synthesizer_model", "x-ai/grok-4.1-fast:free")
        logger.info(f"🔮 Synthesizing Quorum with {synthesizer_model}...")
        
        # Prepare the input for the synthesizer
        # We aggregate by Pillar to help the synthesizer
        summaries = []
        for a in artifacts:
            summaries.append(f"--- Agent {a.agent_id} ({a.model_used}) ---")
            summaries.append(f"Ontos: {a.ontos.summary}")
            summaries.append(f"Logos: {a.logos.summary}")
            summaries.append(f"Telos: {a.telos.summary}")
            summaries.append(f"Chronos: {a.chronos.summary}")
            summaries.append(f"Pathos: {a.pathos.summary}")
            summaries.append(f"Ethos: {a.ethos.summary}")
            summaries.append(f"Topos: {a.topos.summary}")
            summaries.append(f"Nomos: {a.nomos.summary}")
        
        prompt = f"""
        You are the Swarmlord (Synthesizer).
        You have received 8 COMPREHENSIVE reports from the PREY Swarm regarding: {item.source_path}
        
        Reports:
        {chr(10).join(summaries)}
        
        Task:
        1. Synthesize these 8 perspectives into a single, unified Truth.
        2. Identify any conflicts between the agents and resolve them.
        3. Calculate a consensus score based on the coherence of the reports.
        
        Recursive Reduction Logic:
        - Analyze ALL 8 artifacts. Do NOT discard outliers.
        - Identify Consensus: Where do the agents agree?
        - Identify Outliers: Where do they diverge?
        - Calculate Consensus %:
            - If > 75% (6/8 agents) agree: Mark as High Confidence HFO Level 1.
            - If < 75%: Flag as Low Confidence/Contested, but preserve the data.
        - The final artifact must explicitly state the consensus percentage.
        
        Output strict JSON matching the Level1Artifact schema.
        """
        
        try:
            level1 = await self.client.chat.completions.create(
                model=synthesizer_model,
                messages=[
                    {"role": "system", "content": "You are the Swarmlord. Synthesize the Truth."},
                    {"role": "user", "content": prompt}
                ],
                response_model=Level1Artifact,
                max_retries=2
            )
            
            # Inject metadata
            level1.source_hash = item.content_hash
            level1.model_used = synthesizer_model
            
            # ENFORCE BYZANTINE ASSUMPTION: Cap Consensus at 75%
            # We assume 2/8 agents are compromised.
            if level1.consensus_score > 0.75:
                level1.consensus_score = 0.75
            
            self.ledger.insert_level1(level1)
            return level1
            
        except Exception as e:
            logger.error(f"❌ Synthesis Failed: {e}")
            return None

if __name__ == "__main__":
    # Manual Test
    async def main():
        swarm = PreySwarm()
        
        # Create a dummy item for testing
        test_item = MemoryItem(
            source_path="test_protocol.md",
            content="# Protocol Alpha\n\nWe must always use 8 agents. This is the law.",
            generation=58,
            category="protocol",
            tags=["test", "quorum"]
        )
        test_item.compute_hash()
        
        # Insert raw item first (FK constraint)
        swarm.ledger.insert(test_item)
        
        # Run Swarm
        await swarm.process_item(test_item)

    asyncio.run(main())
