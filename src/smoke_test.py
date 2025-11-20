import asyncio
import os
import sys
import psycopg2
import nats
from temporalio.client import Client
from langchain import __version__ as lc_version
import pydantic

# Configuration (Defaults match docker-compose.yml service names)
# When running inside the container, these hostnames resolve automatically.
PG_DSN = os.getenv("PG_DSN", "postgresql://hfo_admin:phoenix_password@db:5432/hfo_unified_memory")
NATS_URL = os.getenv("NATS_URL", "nats://nats:4222")
TEMPORAL_URL = os.getenv("TEMPORAL_URL", "temporal:7233")

async def test_postgres():
    print(f"\n🐘 Testing Postgres Connection...")
    print(f"   Target: {PG_DSN}")
    try:
        conn = psycopg2.connect(PG_DSN)
        cur = conn.cursor()
        cur.execute("SELECT 1;")
        print("   ✅ Connection Successful")
        
        cur.execute("SELECT * FROM pg_extension WHERE extname = 'vector';")
        if cur.fetchone():
            print("   ✅ pgvector Extension Found")
        else:
            print("   ❌ pgvector Extension MISSING")
        conn.close()
        return True
    except Exception as e:
        print(f"   ❌ Postgres Failed: {e}")
        return False

async def test_nats():
    print(f"\n⚡ Testing NATS JetStream...")
    print(f"   Target: {NATS_URL}")
    try:
        nc = await nats.connect(NATS_URL)
        js = nc.jetstream()
        print("   ✅ Connection Successful")
        
        # Create a stream (idempotent)
        try:
            await js.add_stream(name="SMOKE_TEST", subjects=["smoke.*"])
            print("   ✅ Stream 'SMOKE_TEST' Verified")
        except Exception as e:
            # Stream might already exist
            print(f"   ℹ️  Stream Check: {e}")

        # Publish/Subscribe Roundtrip
        sub = await js.subscribe("smoke.test")
        await js.publish("smoke.test", b'Hello Phoenix')
        msg = await sub.next_msg(timeout=2)
        if msg.data == b'Hello Phoenix':
            print(f"   ✅ Message Roundtrip Successful: '{msg.data.decode()}'")
        else:
            print(f"   ❌ Message Mismatch: {msg.data}")
        
        await nc.close()
        return True
    except Exception as e:
        print(f"   ❌ NATS Failed: {e}")
        return False

async def test_temporal():
    print(f"\n⏳ Testing Temporal...")
    print(f"   Target: {TEMPORAL_URL}")
    try:
        # Connect to Temporal Server
        client = await Client.connect(TEMPORAL_URL)
        print("   ✅ Connection Successful")
        print(f"   ✅ Connected to Namespace: '{client.namespace}'")
        return True
    except Exception as e:
        print(f"   ❌ Temporal Failed: {e}")
        return False

def test_libraries():
    print("\n📚 Testing Core Libraries...")
    print(f"   ✅ LangChain Version: {lc_version}")
    print(f"   ✅ Pydantic Version: {pydantic.VERSION}")
    return True

async def main():
    print("🚀 STARTING HFO PHOENIX SMOKE TESTS 🚀")
    print("========================================")
    
    results = {
        "Libraries": test_libraries(),
        "Postgres": await test_postgres(),
        "NATS": await test_nats(),
        "Temporal": await test_temporal()
    }
    
    print("\n========================================")
    print("📊 TEST SUMMARY")
    all_passed = True
    for name, passed in results.items():
        status = "PASS" if passed else "FAIL"
        icon = "✅" if passed else "❌"
        print(f"{icon} {name}: {status}")
        if not passed:
            all_passed = False
            
    if all_passed:
        print("\n✨ ALL SYSTEMS GO. READY FOR GEN 50. ✨")
        sys.exit(0)
    else:
        print("\n⚠️  SOME SYSTEMS FAILED. CHECK LOGS. ⚠️")
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())
