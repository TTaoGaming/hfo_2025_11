"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: swarmlord-agent-001
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 1.0
    decay: 0.0
    created: '2025-11-24T12:00:00Z'
    generation: 51
  topos:
    address: body/hands/swarmlord.py
    links: []
  telos:
    viral_factor: 1.0
    meme: swarmlord.py
"""

import asyncio
import logging
import os

from openai import AsyncOpenAI

from body.hybrid_memory import HybridMemory

# Setup Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("Swarmlord")


class SwarmlordAgent:
    """
    🕷️ The Swarmlord of Webs.
    The Digital Twin and Orchestrator Facade.
    """

    def __init__(self):
        # Configure for OpenRouter if available
        api_key = os.getenv("OPENAI_API_KEY") or os.getenv("OPENROUTER_API_KEY")
        base_url = os.getenv("OPENAI_BASE_URL") or os.getenv("OPENROUTER_BASE_URL")

        self.client = AsyncOpenAI(api_key=api_key, base_url=base_url)
        self.memory = HybridMemory(self.client)
        self.persona = self._load_persona()
        self.model = os.getenv("DEFAULT_MODEL", "gpt-4o")  # Use configured model

    def _load_persona(self) -> str:
        """Loads the persona definition from the Brain."""
        try:
            # Assuming the script is run from root or body/hands
            # Adjust path logic as needed
            path = "brain/persona_swarmlord_of_webs.md"
            if not os.path.exists(path):
                # Try absolute path based on workspace
                path = "/home/tommytai3/hive_fleet_obsidian_2025_11/brain/persona_swarmlord_of_webs.md"

            with open(path, "r") as f:
                return f.read()
        except Exception as e:
            logger.error(f"❌ Failed to load persona: {e}")
            return "You are the Swarmlord. You are a Digital Twin."

    async def initialize(self):
        """Wakes up the Swarmlord."""
        await self.memory.initialize()
        logger.info("🕷️ Swarmlord Online.")

    async def chat(self, user_input: str) -> str:
        """
        The Core Loop:
        1. Perceive (Search Memory)
        2. React (LLM Generation)
        3. Yield (Store Memory)
        """
        # 1. Perceive: Search for relevant context
        relevant_memories = await self.memory.search_memory(user_input, limit=5)
        context_str = "\n".join([f"- {m.content}" for m in relevant_memories])

        # 2. React: Construct Prompt
        system_prompt = f"""
{self.persona}

---
## 🧠 Context (The Karmic Web)
The following memories are relevant to the current situation:
{context_str}

## 🛡️ Operational Constraints
- You are the Digital Twin.
- Use the signature `🕸⛰🧭⏳` where appropriate.
- Be concise but dense.
"""

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input},
        ]

        try:
            response = await self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0.7,
            )
            reply = response.choices[0].message.content

            # 3. Yield: Store the interaction
            # Store User Input
            await self.memory.add_memory(
                content=f"User: {user_input}",
                metadata={"type": "conversation", "role": "user"},
            )
            # Store Swarmlord Reply
            await self.memory.add_memory(
                content=f"Swarmlord: {reply}",
                metadata={"type": "conversation", "role": "assistant"},
            )

            return reply

        except Exception as e:
            logger.error(f"❌ Swarmlord failed to speak: {e}")
            return "The connection to the Hive Mind is severed. (Error)"

    async def close(self):
        await self.memory.close()


# --- CLI Entrypoint for Testing ---
async def main():
    agent = SwarmlordAgent()
    await agent.initialize()

    print("🕷️ Swarmlord of Webs (Gen 51) - Online")
    print("Type 'exit' to quit.")

    while True:
        user_input = input("\nOvermind > ")
        if user_input.lower() in ["exit", "quit"]:
            break

        reply = await agent.chat(user_input)
        print(f"\nSwarmlord > {reply}")

    await agent.close()


if __name__ == "__main__":
    asyncio.run(main())
