import os
import json
import asyncio
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field
import instructor
from openai import OpenAI
from duckduckgo_search import DDGS

# Fix for relative import when running as script
if __name__ == "__main__":
    import sys
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../..")))
    from buds.hfo_gem_gen_63.src.config import settings
else:
    from ..config import settings

# --- Data Models ---

class SearchResult(BaseModel):
    title: str
    href: str
    body: str

class Perception(BaseModel):
    topic: str
    raw_data: List[SearchResult]
    summary: str

class PillarOpinion(BaseModel):
    pillar_name: str
    role: str
    perspective: str
    critique: str
    score: int = Field(..., description="Relevance score 1-10")

class ChantVerse(BaseModel):
    topic: str
    opinions: List[PillarOpinion]
    synthesis: str

class DigestArtifact(BaseModel):
    id: str
    timestamp: str
    topic: str
    perception: Perception
    chant: ChantVerse
    final_verdict: str

# --- Workflow Class ---

class ResearchWorkflow:
    def __init__(self):
        api_key = settings.OPENROUTER_API_KEY or os.getenv("OPENROUTER_API_KEY")
        if not api_key:
            print("[!] WARNING: OPENROUTER_API_KEY not found. LLM calls will fail.")
        
        self.client = instructor.from_openai(
            OpenAI(
                base_url="https://openrouter.ai/api/v1",
                api_key=api_key,
            ),
            mode=instructor.Mode.JSON,
        )
        self.model = settings.MODEL_REASONING

    def perceive(self, topic: str) -> Perception:
        print(f"[*] Perceiving: {topic}...")
        results = []
        try:
            with DDGS() as ddgs:
                # Get top 5 results
                ddg_results = list(ddgs.text(topic, max_results=5))
                for r in ddg_results:
                    results.append(SearchResult(title=r['title'], href=r['href'], body=r['body']))
        except Exception as e:
            print(f"[!] Search failed: {e}")
        
        # Summarize with LLM
        summary_prompt = f"Summarize these search results for '{topic}':\n" + "\n".join([f"- {r.title}: {r.body}" for r in results])
        
        try:
            summary = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are the Observer (Ontos). Summarize the raw data."},
                    {"role": "user", "content": summary_prompt}
                ],
                response_model=str
            )
        except Exception as e:
            print(f"[!] LLM Summary failed: {e}")
            summary = "Summary unavailable due to LLM error."
        
        return Perception(topic=topic, raw_data=results, summary=summary)

    def chant(self, perception: Perception) -> ChantVerse:
        print(f"[*] Chanting (8 Pillars)...")
        
        pillars = [
            ("Navigator", "Strategy & Teleology"),
            ("Observer", "Empiricism & Sensing"),
            ("Bridger", "Connection & Context"),
            ("Shaper", "Execution & Tooling"),
            ("Injector", "Timing & Momentum"),
            ("Disruptor", "Critique & Stress Testing"),
            ("Immunizer", "Security & Ethics"),
            ("Assimilator", "Memory & Integration")
        ]
        
        opinions = []
        
        for name, role in pillars:
            print(f"  - {name} ({role}) speaking...")
            try:
                opinion = self.client.chat.completions.create(
                    model=self.model,
                    messages=[
                        {"role": "system", "content": f"You are the {name}. Your role is {role}. Analyze the perception data provided."},
                        {"role": "user", "content": f"Topic: {perception.topic}\nData Summary: {perception.summary}\n\nProvide your perspective, critique, and a relevance score (1-10)."}
                    ],
                    response_model=PillarOpinion
                )
                # Enforce name consistency
                opinion.pillar_name = name
                opinion.role = role
                opinions.append(opinion)
            except Exception as e:
                print(f"  [!] {name} failed to speak: {e}")
                opinions.append(PillarOpinion(pillar_name=name, role=role, perspective="Silence.", critique="Error.", score=0))
            
        # Synthesis
        print(f"[*] Synthesizing...")
        try:
            synthesis = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are the Swarmlord. Synthesize the 8 opinions into a cohesive chant."},
                    {"role": "user", "content": "\n".join([f"{o.pillar_name}: {o.perspective}" for o in opinions])}
                ],
                response_model=str
            )
        except Exception as e:
            synthesis = "Synthesis failed."

        return ChantVerse(topic=perception.topic, opinions=opinions, synthesis=synthesis)

    def run(self, topic: str) -> DigestArtifact:
        perception = self.perceive(topic)
        chant = self.chant(perception)
        
        artifact = DigestArtifact(
            id=f"digest_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            timestamp=datetime.now().isoformat(),
            topic=topic,
            perception=perception,
            chant=chant,
            final_verdict=chant.synthesis
        )
        
        return artifact

    def save_artifact(self, artifact: DigestArtifact):
        # Ensure directory exists
        output_dir = "buds/hfo_gem_gen_63/digest"
        os.makedirs(output_dir, exist_ok=True)
        
        filename = f"{output_dir}/{artifact.id}.md"
        
        md_content = f"""# 🕷️ HFO Digest: {artifact.topic}
**ID**: `{artifact.id}`
**Timestamp**: {artifact.timestamp}

## 1. Perception (Observer)
**Summary**: {artifact.perception.summary}

### Raw Sources
{chr(10).join([f"- [{r.title}]({r.href})" for r in artifact.perception.raw_data])}

## 2. The Chant (8 Pillars)
"""
        for op in artifact.chant.opinions:
            md_content += f"""
### {op.pillar_name} ({op.role}) - Score: {op.score}/10
> {op.perspective}

**Critique**: _{op.critique}_
"""

        md_content += f"""
## 3. Synthesis (Swarmlord)
{artifact.chant.synthesis}
"""
        
        with open(filename, "w") as f:
            f.write(md_content)
        print(f"[*] Artifact saved to {filename}")

if __name__ == "__main__":
    wf = ResearchWorkflow()
    # Default test topic
    print("Starting 1181 Research Workflow...")
    artifact = wf.run("The future of agentic coding frameworks 2025")
    wf.save_artifact(artifact)
