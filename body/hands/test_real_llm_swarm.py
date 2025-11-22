import asyncio
import os
import json
import logging
from datetime import datetime
import nats
from nats.js.api import StreamConfig, RetentionPolicy
from dotenv import load_dotenv
from pydantic import UUID4, BaseModel, Field
import instructor
from openai import OpenAI
from body.config import Config

# Import our SSOT models
from body.models.intent import MissionIntent
from body.models.signals import MissionSignal, ResultSignal
from body.models.state import AgentRole

# Setup
load_dotenv()
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(name)s] %(levelname)s: %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger("Real-Hydra")

# Configuration
NATS_URL = Config.NATS_URL
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
STREAM_NAME = "HIVE_MIND"
SUBJECT_MISSION = "hfo.mission.new"
SUBJECT_RESULT = "hfo.mission.result"

# Cheap but smart model for testing
MODEL_ID = "google/gemini-2.0-flash-001"


class AgentResponse(BaseModel):
    """Structured output from the LLM."""

    analysis: str = Field(
        ..., description="The direct answer or analysis of the mission."
    )
    confidence: float = Field(
        ..., description="Self-assessed confidence score (0.0-1.0)."
    )
    reasoning: str = Field(..., description="Brief explanation of the thought process.")


def get_llm_client():
    if not OPENROUTER_API_KEY:
        raise ValueError("OPENROUTER_API_KEY is not set in .env")

    return instructor.from_openai(
        OpenAI(
            base_url=OPENROUTER_BASE_URL,
            api_key=OPENROUTER_API_KEY,
        ),
        mode=instructor.Mode.JSON,
    )


async def setup_jetstream(nc):
    js = nc.jetstream()
    try:
        await js.add_stream(
            name=STREAM_NAME,
            subjects=["hfo.mission.*"],
            config=StreamConfig(
                retention=RetentionPolicy.LIMITS, max_age=3600, storage="file"
            ),
        )
    except Exception:
        pass  # Stream likely exists
    return js


async def swarmlord_publisher(js, mission_text: str) -> UUID4:
    intent = MissionIntent(
        description=mission_text, rationale="Testing Real LLM Integration", swarm_size=1
    )
    signal = MissionSignal(
        producer_id="Swarmlord-Real", mission=intent, target_roles=[AgentRole.SHAPER]
    )
    payload = signal.model_dump_json().encode()
    await js.publish(SUBJECT_MISSION, payload)
    logger.info(f"👑 Swarmlord: Published Mission: '{mission_text}'")
    return intent.id


async def agent_worker(nc, agent_id: str, role: AgentRole):
    js = nc.jetstream()
    psub = await js.pull_subscribe(SUBJECT_MISSION, durable=f"worker_{agent_id}")
    client = get_llm_client()

    logger.info(f"🧠 Agent {agent_id} ({MODEL_ID}): Online and waiting...")

    try:
        while True:
            try:
                msgs = await psub.fetch(1, timeout=5)
                for msg in msgs:
                    data = json.loads(msg.data.decode())
                    signal = MissionSignal(**data)

                    logger.info(
                        f"   ⚡ {agent_id}: Processing: '{signal.mission.description}'"
                    )

                    # --- REAL LLM CALL ---
                    try:
                        response = client.chat.completions.create(
                            model=MODEL_ID,
                            response_model=AgentResponse,
                            messages=[
                                {
                                    "role": "system",
                                    "content": f"You are Agent {agent_id}, a {role.value} in Hive Fleet Obsidian. Be concise.",
                                },
                                {"role": "user", "content": signal.mission.description},
                            ],
                        )

                        logger.info(f"   🤖 {agent_id} Thought: {response.reasoning}")

                        result = ResultSignal(
                            producer_id=agent_id,
                            mission_id=signal.mission.id,
                            content=response.analysis,
                            confidence=response.confidence,
                            metadata={
                                "reasoning": response.reasoning,
                                "model": MODEL_ID,
                            },
                        )

                        await js.publish(
                            SUBJECT_RESULT, result.model_dump_json().encode()
                        )
                        logger.info(f"   📤 {agent_id}: Sent Result.")

                    except Exception as e:
                        logger.error(f"   ❌ {agent_id} LLM Error: {e}")

                    await msg.ack()

            except nats.errors.TimeoutError:
                continue
            except Exception as e:
                logger.error(f"❌ {agent_id} Loop Error: {e}")
                await asyncio.sleep(1)

    except asyncio.CancelledError:
        logger.info(f"🛑 Agent {agent_id} shutting down.")


async def assimilator_collector(js, target_mission_id: UUID4):
    logger.info(
        f"🧠 Assimilator: Listening for results for Mission {target_mission_id}..."
    )
    sub = await js.subscribe(SUBJECT_RESULT)

    start_time = datetime.now()

    while (datetime.now() - start_time).seconds < 15:
        try:
            msg = await sub.next_msg(timeout=2)
            data = json.loads(msg.data.decode())
            signal = ResultSignal(**data)

            if signal.mission_id == target_mission_id:
                print("\n--- 🏁 REAL LLM RESULT ---")
                print(f"Agent: {signal.producer_id}")
                print(f"Model: {signal.metadata.get('model')}")
                print(f"Confidence: {signal.confidence}")
                print(f"Reasoning: {signal.metadata.get('reasoning')}")
                print(f"Answer: {signal.content}")
                print("--------------------------\n")
                return True
            else:
                logger.info(
                    f"   🗑️ Assimilator: Ignoring result for old mission {signal.mission_id}"
                )

        except nats.errors.TimeoutError:
            continue

    logger.warning("⚠️  Assimilator: Timed out waiting for LLM response.")
    return False


async def main():
    nc = None
    worker = None
    try:
        nc = await nats.connect(NATS_URL, connect_timeout=5)
        js = await setup_jetstream(nc)

        # 1. Start ONE real worker
        worker = asyncio.create_task(
            agent_worker(nc, "Gemini-Worker", AgentRole.SHAPER)
        )

        # 2. Publish a real question
        await asyncio.sleep(1)
        mission_id = await swarmlord_publisher(
            js, "Explain the concept of 'Stigmergy' in 10 words or less."
        )

        # 3. Collect result
        await assimilator_collector(js, mission_id)

    except Exception as e:
        logger.error(f"💥 Fatal: {e}")
    finally:
        if worker:
            worker.cancel()
            try:
                await worker
            except asyncio.CancelledError:
                pass
        if nc:
            await nc.close()


if __name__ == "__main__":
    asyncio.run(main())
