import asyncio
import nats
import os

async def main():
    nc = await nats.connect("nats://localhost:4225")
    js = nc.jetstream()
    
    try:
        consumers = await js.consumers_info("HFO_INGEST")
        print(f"Found {len(consumers)} consumers.")
        for c in consumers:
            print(f" - {c.name} (Filter: {c.config.filter_subject})")
            await js.delete_consumer("HFO_INGEST", c.name)
            print(f"   Deleted {c.name}")
    except Exception as e:
        print(f"Error: {e}")
        
    await nc.close()

if __name__ == "__main__":
    asyncio.run(main())