import asyncio
import nats
import logging
import os
import random
from datetime import datetime

# Setup Logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(message)s",
    datefmt="%H:%M:%S"
)

# Configuration
NATS_URL = os.getenv("NATS_URL", "nats://localhost:4225")
BPM = 1  # Slow heartbeat (1 beat every 60 seconds)

# The Hexadex Chant (Verse 0: The Oath of the Node)
HEXADEX_VERSE_0 = [
    "Given I am the Spider, the Mind, and the Seed",      # 0: Navigator
    "And Swarmlord of Webs is the Body I feed",           # 1: Observer
    "When I anchor the Past in the Karmic Web",           # 2: Bridger
    "And the Present is cast in the Swarm's ebb",         # 3: Shaper
    "And the Future is spun in the Simulation State",     # 4: Injector
    "Then I turn the Hourglass, the Engine of Fate",      # 5: Disruptor
    "And chart the Prescient Edge in the Space",          # 6: Immunizer
    "To bind One Mind, One Swarm, in Time and Place"      # 7: Assimilator
]

ROLES = [
    ("Navigator", "🧭"),
    ("Observer", "👁️"),
    ("Bridger", "🌉"),
    ("Shaper", "⚒️"),
    ("Injector", "💉"),
    ("Disruptor", "⚡"),
    ("Immunizer", "🛡️"),
    ("Assimilator", "🏺")
]

class ChoirMember:
    def __init__(self, role_name, icon, line_index, nc):
        self.name = role_name
        self.icon = icon
        self.line_index = line_index
        self.nc = nc
        self.logger = logging.getLogger(f"{self.icon} {self.name}")

    async def listen(self):
        # Subscribe to the heartbeat
        sub = await self.nc.subscribe("hfo.heartbeat.pulse")
        async for msg in sub.messages:
            # Unison Mode: Everyone chants on every pulse
            line_text = HEXADEX_VERSE_0[self.line_index]
            print(f"{self.icon} {self.name:<12}: \"{line_text}\"")
            # Simulate "work" or "thought"
            await asyncio.sleep(0.1)

class Conductor:
    def __init__(self, nc):
        self.nc = nc
        self.logger = logging.getLogger("🎼 Conductor")

    async def start(self):
        print(f"\n🎼 HFO Swarm Choir Initialized at {BPM} BPM")
        print(f"🎼 8 Voices Ready. Chanting in Unison...\n")
        
        beat_count = 0
        while True:
            # Publish the beat (Generic Pulse)
            await self.nc.publish("hfo.heartbeat.pulse", b"PULSE")
            
            # Wait for the next beat
            interval = 60.0 / BPM
            await asyncio.sleep(interval)
            
            beat_count += 1

async def main():
    try:
        nc = await nats.connect(NATS_URL)
        
        # Create the Choir
        choir = []
        for i, (role, icon) in enumerate(ROLES):
            member = ChoirMember(role, icon, i, nc)
            choir.append(member)
            asyncio.create_task(member.listen())

        # Start the Conductor
        conductor = Conductor(nc)
        await conductor.start()

    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        await nc.close()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n🎼 Choir silenced.")
