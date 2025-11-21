import asyncio
import nats
import pytest
import uuid


@pytest.mark.asyncio
async def test_nats_smoke():
    print("\n🧪 SMOKE TEST: NATS Stigmergy Layer")
    try:
        nc = await nats.connect("nats://localhost:4225")
        js = nc.jetstream()

        # Create stream if not exists
        try:
            await js.add_stream(name="SMOKE_STREAM", subjects=["smoke.*"])
        except Exception:
            pass  # Stream might exist

        # Pub/Sub with unique subject
        unique_id = str(uuid.uuid4())
        subject = f"smoke.{unique_id}"
        payload = f"Hello NATS {unique_id}".encode()

        sub = await js.subscribe(subject)
        await js.publish(subject, payload)

        msg = await sub.next_msg(timeout=2)
        print(f"   Received: {msg.data}")
        assert msg.data == payload
        print("   ✅ NATS JetStream: OK")

        await nc.close()
    except Exception as e:
        pytest.fail(f"NATS failed: {e}")


if __name__ == "__main__":
    asyncio.run(test_nats_smoke())
