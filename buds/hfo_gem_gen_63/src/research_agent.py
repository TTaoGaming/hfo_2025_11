import os
import sys
from openai import OpenAI
from typing import List, Dict

# Add root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.config import settings
from src.bridger import Bridger

class ResearchAgent:
    """
    The Research Agent (Gen 63).
    Combines Internal Memory (Bridger) with External Intelligence (LLM)
    to answer complex questions and propose upgrades.
    """
    def __init__(self):
        self.bridger = Bridger()
        
        api_key = settings.OPENROUTER_API_KEY or os.environ.get("OPENROUTER_API_KEY")
        if not api_key:
            raise ValueError("OPENROUTER_API_KEY not found.")
            
        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=api_key,
        )
        self.model = settings.OPENROUTER_MODEL

    def research(self, query: str) -> str:
        """
        Conducts research on a query.
        1. Search Internal Memory.
        2. Synthesize with LLM.
        """
        print(f"🕵️ Researching: {query}")
        
        # 1. Recall from Memory
        memories = self.bridger.ask(query, limit=5)
        context_str = "\n\n".join([f"--- Source: {m['source']} ---\n{m['text']}" for m in memories])
        
        if not context_str:
            context_str = "No internal memory found on this topic."
            
        # 2. Synthesize with LLM
        prompt = f"""
        You are the Obsidian Spider (Gen 63), an advanced AI system.
        
        USER QUERY: {query}
        
        INTERNAL MEMORY CONTEXT:
        {context_str}
        
        INSTRUCTIONS:
        1. Analyze the user's query.
        2. Use the internal memory to ground your answer in the current system architecture (Gen 63).
        3. If the user asks for upgrades or new features, propose a plan that fits the "Hydra Platform" philosophy (Clean, Consolidated, Stigmergic).
        4. Be specific about technical implementation (Python, NATS, Ray, etc.).
        
        RESPONSE:
        """
        
        try:
            completion = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are the Obsidian Spider. You are helpful, technical, and precise."},
                    {"role": "user", "content": prompt}
                ]
            )
            return completion.choices[0].message.content
        except Exception as e:
            return f"❌ Research Failed: {e}"

if __name__ == "__main__":
    agent = ResearchAgent()
    
    # Test with the user's specific request
    query = "I want to build a hypercasual local multiplayer game with evolutionary tuning using OpenCV/MediaPipe. How can HFO Gen 63 support this?"
    response = agent.research(query)
    print("\n🕷️ OBSIDIAN SPIDER REPORT:\n")
    print(response)
