import asyncio
import json
from nats.aio.client import Client as NATS
from nats.js.api import RetentionPolicy


class HFOStigmergyBus:
    def __init__(self, nats_url="nats://localhost:4225"):
        self.nats_url = nats_url
        self.nc = NATS()
        self.js = None
        self.kv = None

    async def connect(self):
        await self.nc.connect(self.nats_url)
        self.js = self.nc.jetstream()
        print(f"Connected to NATS at {self.nats_url}")

    async def setup_streams(self):
        # Create the HFO stream if it doesn't exist
        try:
            # Enforce 8-Hour Retention (Power of Eight)
            await self.js.add_stream(
                name="HFO", 
                subjects=["hfo.>"], 
                retention=RetentionPolicy.LIMITS,
                max_age=8 * 3600  # 8 Hours
            )
            print("Created HFO stream with 8-hour retention.")
        except Exception as e:
            print(f"Stream HFO might already exist: {e}")
            # Try to update it
            try:
                await self.js.update_stream(
                    name="HFO", 
                    subjects=["hfo.>"], 
                    retention=RetentionPolicy.LIMITS,
                    max_age=8 * 3600
                )
                print("Updated HFO stream retention to 8 hours.")
            except Exception as update_e:
                print(f"Failed to update stream: {update_e}")

        # Create KV bucket
        try:
            self.kv = await self.js.create_key_value(bucket="hfo_pillars")
            print("Created HFO Pillars KV bucket.")
        except Exception as e:
            print(f"KV Bucket might already exist: {e}")
            self.kv = await self.js.key_value("hfo_pillars")

    async def publish(self, section: str, payload: dict):
        """
        Publish a message to one of the 8 stigmergy sections.
        section: One of 'ontos', 'logos', 'telos', 'chronos', 'pathos', 'ethos', 'topos', 'nomos'
        """
        subject = f"hfo.{section}"
        data = json.dumps(payload).encode()

        # 1. Publish to Stream (Event Log)
        ack = await self.js.publish(subject, data)
        print(f"Published to {subject}: {payload} (Seq: {ack.seq})")

        # 2. Update KV (Latest State)
        if not self.kv:
            try:
                self.kv = await self.js.key_value("hfo_pillars")
            except Exception:
                # If bucket doesn't exist, we might need to create it or fail gracefully
                pass

        if self.kv:
            await self.kv.put(section, data)
            print(f"Updated KV {section}")

        return ack

    async def get_latest_state(self, section: str):
        if not self.kv:
            self.kv = await self.js.key_value("hfo_pillars")
        try:
            entry = await self.kv.get(section)
            return json.loads(entry.value.decode())
        except Exception as e:
            print(f"Error getting KV {section}: {e}")
            return None

    async def subscribe(self, subject: str, callback):
        await self.js.subscribe(subject, cb=callback)
        print(f"Subscribed to {subject}")

    async def close(self):
        await self.nc.close()


# Example usage
if __name__ == "__main__":

    async def main():
        bus = HFOStigmergyBus()
        await bus.connect()
        await bus.setup_streams()
        await bus.publish("ontos", {"id": "test-entity", "msg": "Hello World"})
        state = await bus.get_latest_state("ontos")
        print(f"Latest state for 'ontos': {state}")
        await bus.close()

    asyncio.run(main())
