import asyncio
import subprocess
import sys
import os
import time

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from nerves.bus.nats_client import HFOStigmergyBus  # noqa: E402
from memory.lancedb_store import HFOStigmergyMemory  # noqa: E402


async def test_stigmergy():
    print("=== Testing HFO Stigmergy System (Gen 55) ===")

    # 1. Setup
    print("\n[1] Running Setup...")
    subprocess.run(
        [sys.executable, "scripts/setup_stigmergy.py"],
        check=True,
        cwd=os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")),
    )

    # 2. Start Assimilator
    print("\n[2] Starting Assimilator...")
    assimilator = subprocess.Popen(
        [sys.executable, "scripts/run_assimilator.py"],
        cwd=os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    # Give it a moment to connect
    await asyncio.sleep(2)

    # 3. Publish Messages (Hot Stigmergy)
    print("\n[3] Publishing to 8 Stigmergy Sections (Hot)...")
    bus = HFOStigmergyBus()
    await bus.connect()

    sections = [
        "ontos",
        "logos",
        "telos",
        "chronos",
        "pathos",
        "ethos",
        "topos",
        "nomos",
    ]

    test_id = f"test-{int(time.time())}"

    for section in sections:
        payload = {
            "id": f"{test_id}-{section}",
            "msg": f"Testing {section} pillar",
            "value": 42,
        }
        await bus.publish(section, payload)

    await bus.close()

    # 4. Wait for Assimilation (Cold Stigmergy)
    print("\n[4] Waiting for Assimilation (Cold)...")
    await asyncio.sleep(3)

    # 5. Verify KV (Hot Stigmergy State)
    print("\n[5a] Verifying NATS KV (Hot State)...")
    await bus.connect()  # Reconnect
    kv_success = 0
    for section in sections:
        state = await bus.get_latest_state(section)
        if state and state.get("id") == f"{test_id}-{section}":
            print(f"✅ KV {section}: Verified")
            kv_success += 1
        else:
            print(f"❌ KV {section}: Not found or mismatch")
    await bus.close()

    # 6. Verify LanceDB Storage
    print("\n[5b] Verifying LanceDB Storage (Cold Memory)...")
    # Use absolute path or path relative to workspace root
    db_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../../memory/lancedb")
    )
    mem = HFOStigmergyMemory(db_path=db_path)

    lancedb_success = 0
    for section in sections:
        df = mem.query(section, limit=100)
        # Filter by our test_id to avoid old data
        # Note: payload is stored as string, so we check if test_id is in it
        found = False
        for _, row in df.iterrows():
            if test_id in row["payload"]:
                found = True
                break

        if found:
            print(f"✅ {section}: Verified")
            lancedb_success += 1
        else:
            print(f"❌ {section}: Not found")

    # 7. Cleanup
    print("\n[6] Cleanup...")
    assimilator.terminate()
    try:
        outs, errs = assimilator.communicate(timeout=2)
        print("Assimilator Output:", outs.decode())
        if errs:
            print("Assimilator Errors:", errs.decode())
    except subprocess.TimeoutExpired:
        assimilator.kill()

    if lancedb_success == 8 and kv_success == 8:
        print("\n🎉 SUCCESS: All 8 Stigmergy Pillars verified (KV + LanceDB)!")
        sys.exit(0)
    else:
        print(f"\n⚠️ FAILURE: KV: {kv_success}/8, LanceDB: {lancedb_success}/8")
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(test_stigmergy())
