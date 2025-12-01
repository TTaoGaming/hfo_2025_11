import asyncio
import nats
from nats.errors import ConnectionClosedError, TimeoutError, NoServersError
import sys
import os

# Add root to path to import config
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.config import settings

async def verify_nats():
    """
    Verifies NATS connection and JetStream functionality.
    Corresponds to: buds/hfo_gem_gen_63/brain/verify_nats.feature
    """
    print(f"🔌 Connecting to NATS at {settings.NATS_URL}...")
    
    try:
        # 1. Connect
        nc = await nats.connect(settings.NATS_URL)
        print("✅ Connected to NATS Server.")
        
        # 2. Create JetStream Context
        js = nc.jetstream()
        print("✅ JetStream Context Created.")
        
        # 3. Subscribe
        sub = await nc.subscribe("hfo.gen63.heartbeat")
        print("✅ Subscribed to 'hfo.gen63.heartbeat'.")
        
        # 4. Publish
        payload = b"Gen 63 Pulse"
        await nc.publish("hfo.gen63.heartbeat", payload)
        print(f"📤 Published: {payload.decode()}")
        
        # 5. Receive
        try:
            msg = await sub.next_msg(timeout=2)
            print(f"📥 Received: {msg.data.decode()}")
            if msg.data == payload:
                print("✅ Verification SUCCESS: Loopback complete.")
            else:
                print("❌ Verification FAILED: Payload mismatch.")
        except TimeoutError:
            print("❌ Verification FAILED: Timeout waiting for message.")
            
        # 6. Close
        await nc.close()
        
    except NoServersError:
        print(f"❌ Verification FAILED: No NATS servers available at {settings.NATS_URL}")
    except Exception as e:
        print(f"❌ Verification FAILED: {e}")

if __name__ == "__main__":
    asyncio.run(verify_nats())
