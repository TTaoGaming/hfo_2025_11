import asyncio
import nats
import os
import json
import time
import logging
import uuid
from datetime import datetime, timezone
from nats.errors import TimeoutError

# Setup Logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%H:%M:%S"
)
logger = logging.getLogger("HFO_1181")

# Configuration
NATS_URL = os.getenv("NATS_URL", "nats://localhost:4225")
BPM = 1  # 1 Beat Per Minute

# Topics
TOPIC_PULSE = "hfo.1181.pulse"
TOPIC_PERCEIVE = "hfo.1181.perceive"
TOPIC_ORCHESTRATE = "hfo.1181.orchestrate"
TOPIC_CHANT = "hfo.1181.chant"
TOPIC_ARTIFACT = "hfo.1181.artifact"

class PreyAgent:
    def __init__(self, name, role, nc, js):
        self.name = name
        self.role = role
        self.nc = nc
        self.js = js
        self.id = str(uuid.uuid4())[:8]
        self.logger = logging.getLogger(f"{self.role}:{self.name}")

    async def start(self):
        pass

class Observer(PreyAgent):
    async def start(self):
        sub = await self.nc.subscribe(TOPIC_PULSE)
        self.logger.info("Listening for Pulse...")
        async for msg in sub.messages:
            pulse_data = json.loads(msg.data.decode())
            self.logger.info(f"👁️ PREY Step 1: Perceive Pulse: {pulse_data['id']}")
            
            # 1. Perceive: Create Context Frame
            context_frame = {
                "id": str(uuid.uuid4()),
                "type": "context_frame",
                "pulse_id": pulse_data['id'],
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "environment": "simulated_normal",
                "hot_signals": ["nats_stream_active", "system_nominal"]
            }
            
            # Handoff to Orchestrator
            await self.js.publish(TOPIC_PERCEIVE, json.dumps(context_frame).encode())
            self.logger.info("➡️ Handoff to Orchestrator (React)")

class Orchestrator(PreyAgent):
    async def start(self):
        sub = await self.nc.subscribe(TOPIC_PERCEIVE)
        self.logger.info("Listening for Context...")
        async for msg in sub.messages:
            context = json.loads(msg.data.decode())
            self.logger.info(f"🧠 PREY Step 2: React (Orchestrate) for Context: {context['id']}")
            
            # 2. React: Create Mission Orders
            mission_id = str(uuid.uuid4())
            mission_orders = {
                "id": mission_id,
                "type": "mission_orders",
                "context_id": context['id'],
                "intent": "maintain_system_homeostasis",
                "tasks": [f"task_{i}" for i in range(8)]
            }
            
            # Handoff to Swarm (Fan-out)
            await self.js.publish(TOPIC_ORCHESTRATE, json.dumps(mission_orders).encode())
            self.logger.info(f"📣 Broadcasting Mission {mission_id} to Swarm (Execute)")

class Chanter(PreyAgent):
    def __init__(self, name, index, nc, js):
        super().__init__(name, "Chanter", nc, js)
        self.index = index

    async def start(self):
        sub = await self.nc.subscribe(TOPIC_ORCHESTRATE)
        self.logger.info(f"Ready to Execute (Voice {self.index})...")
        async for msg in sub.messages:
            orders = json.loads(msg.data.decode())
            
            # 3. Execute: Work concurrently
            # Simulate variable work time (Async Stigmergy)
            work_time = 0.1 + (self.index * 0.05) 
            await asyncio.sleep(work_time)
            
            verse = {
                "id": str(uuid.uuid4()),
                "type": "artifact_lvl0",
                "agent_id": self.id,
                "voice_index": self.index,
                "mission_id": orders['id'],
                "content": f"Verse {self.index} of the Hexadex",
                "status": "success"
            }
            
            # Publish Verse
            await self.js.publish(TOPIC_CHANT, json.dumps(verse).encode())
            self.logger.info(f"🎵 PREY Step 3: Execute (Chant) Verse {self.index}")

class Auditor(PreyAgent):
    async def start(self):
        sub = await self.nc.subscribe(TOPIC_CHANT)
        self.logger.info("Listening for Verses...")
        
        current_mission = None
        collected_verses = []
        collection_start = 0
        
        while True:
            try:
                msg = await sub.next_msg(timeout=1.0)
                verse = json.loads(msg.data.decode())
                
                # Simple aggregation logic (reset on new mission flow for demo)
                # In prod, we'd use a proper windowing or state machine
                if current_mission != verse['mission_id']:
                    if collected_verses:
                        self.logger.warning("⚠️ Incomplete batch discarded (New Mission Detected)")
                    current_mission = verse['mission_id']
                    collected_verses = []
                    collection_start = time.time()
                
                collected_verses.append(verse)
                self.logger.info(f"📥 Collected {len(collected_verses)}/8 Verses")
                
                if len(collected_verses) == 8:
                    await self.finalize_audit(current_mission, collected_verses)
                    collected_verses = []
                    current_mission = None
                    
            except TimeoutError:
                # Check for "Slowest Hiker" timeout
                if collected_verses and (time.time() - collection_start > 5.0):
                     self.logger.warning(f"⏳ Timeout! Proceeding with Partial Consensus ({len(collected_verses)}/8)")
                     await self.finalize_audit(current_mission, collected_verses)
                     collected_verses = []
                     current_mission = None
                continue

    async def finalize_audit(self, mission_id, verses):
        # 4. Yield: Audit and Create Level 1 Artifact
        self.logger.info("⚖️  PREY Step 4: Yield (Audit) Cycle...")
        
        # Check for Veto (Mock logic: if any verse fails)
        failed = [v for v in verses if v.get("status") != "success"]
        
        if failed:
            self.logger.error(f"🚫 VETO! {len(failed)} verses failed.")
            return

        artifact_lvl1 = {
            "id": str(uuid.uuid4()),
            "type": "artifact_lvl1",
            "mission_id": mission_id,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "consensus": "quorum",
            "verse_count": len(verses),
            "verses": [v['id'] for v in verses] # Linking to Lvl0
        }
        
        await self.js.publish(TOPIC_ARTIFACT, json.dumps(artifact_lvl1).encode())
        self.logger.info(f"✅ COMMIT: Level 1 Artifact {artifact_lvl1['id']} created with {len(verses)} verses.")

async def pulse_generator(nc):
    logger.info(f"💓 Heartbeat Generator Started ({BPM} BPM)")
    while True:
        pulse = {
            "id": str(uuid.uuid4()),
            "timestamp": datetime.now(timezone.utc).isoformat()
        }
        await nc.publish(TOPIC_PULSE, json.dumps(pulse).encode())
        logger.info("--- PULSE ---")
        await asyncio.sleep(60.0 / BPM)

import traceback

# ... (imports)

# ... (classes)

async def main():
    try:
        nc = await nats.connect(NATS_URL)
        js = nc.jetstream()
        
        # Ensure Streams Exist
        try:
            await js.add_stream(name="HFO_1181", subjects=["hfo.1181.*"])
            logger.info("🌊 JetStream 'HFO_1181' configured.")
        except Exception as e:
            logger.warning(f"Stream setup note: {e}")

        agents = []
        
        # 1. Observer
        agents.append(Observer("Ontos", "Observer", nc, js))
        
        # 2. Orchestrator
        agents.append(Orchestrator("Telos", "Orchestrator", nc, js))
        
        # 3. Chanters (8 Voices)
        for i in range(8):
            agents.append(Chanter(f"Prey Agent {i}", i, nc, js))
            
        # 4. Auditor
        agents.append(Auditor("Ethos", "Auditor", nc, js))

        # Start all agents
        tasks = [asyncio.create_task(a.start()) for a in agents]
        
        # Start Pulse
        tasks.append(asyncio.create_task(pulse_generator(nc)))
        
        await asyncio.gather(*tasks)

    except Exception as e:
        logger.error(f"❌ System Error: {e}")
        traceback.print_exc()
    finally:
        if 'nc' in locals():
            await nc.close()

if __name__ == "__main__":
    print("🕷️ HFO 1181 Heartbeat: Anti-Fragile Mode Engaged.")
    while True:
        try:
            asyncio.run(main())
        except KeyboardInterrupt:
            print("\n🛑 HFO 1181 Stopped by User.")
            break
        except Exception as e:
            print(f"⚠️ Critical Failure: {e}")
        
        print("🔄 Restarting HFO 1181 Heartbeat in 5 seconds...")
        time.sleep(5)
