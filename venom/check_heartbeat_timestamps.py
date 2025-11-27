import asyncio
import json
from nats.aio.client import Client as NATS
from nats.js.api import ConsumerConfig, DeliverPolicy
import uuid


async def check_timestamps():
    nc = NATS()
    try:
        await nc.connect("nats://localhost:4225")
    except Exception as e:
        print(f"Failed to connect to NATS: {e}")
        return

    js = nc.jetstream()
    subject = "hfo.heartbeat.>"

    unique_consumer = f"venom_timestamp_checker_{uuid.uuid4().hex[:8]}"

    try:
        sub = await js.subscribe(
            subject, config=ConsumerConfig(deliver_policy=DeliverPolicy.NEW)
        )

        print("Listening for new heartbeats (30s)...")
        start = asyncio.get_event_loop().time()
        while asyncio.get_event_loop().time() - start < 30:
            try:
                msg = await sub.next_msg(timeout=1)
                data = json.loads(msg.data.decode())
                agent_id = data.get("pillars", {}).get("ontos", {}).get("id", "unknown")
                print(
                    f"LIVE | Timestamp: {data.get('timestamp')} | Agent: {agent_id} | Phase: {data.get('phase')}"
                )
            except Exception:
                pass

    except Exception as e:
        print(f"Error fetching messages: {e}")
    finally:
        await nc.close()


if __name__ == "__main__":
    asyncio.run(check_timestamps())
