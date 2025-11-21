import asyncio
import asyncpg
import pytest

@pytest.mark.asyncio
async def test_pgvector_smoke():
    print("\n🧪 SMOKE TEST: Postgres & PGVector Layer")
    try:
        conn = await asyncpg.connect("postgresql://hfo_admin:phoenix_password@localhost:5435/hfo_unified_memory")
        
        # Check extension
        val = await conn.fetchval("SELECT count(*) FROM pg_extension WHERE extname = 'vector'")
        if val == 0:
            print("   ⚠️ pgvector extension NOT found. Attempting to create...")
            try:
                await conn.execute("CREATE EXTENSION IF NOT EXISTS vector")
                print("   ✅ pgvector extension created.")
            except Exception as e:
                pytest.fail(f"Could not create pgvector extension: {e}")
        else:
            print("   ✅ pgvector extension: Installed")
            
        await conn.close()
    except Exception as e:
        pytest.fail(f"Postgres failed: {e}")

if __name__ == "__main__":
    asyncio.run(test_pgvector_smoke())
