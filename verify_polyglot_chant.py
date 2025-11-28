import asyncio
import nats
import json
import os


async def main():
    nc = await nats.connect("nats://localhost:4225")
    js = nc.jetstream()

    print("Listening for Heartbeat...")

    async def message_handler(msg):
        data = json.loads(msg.data.decode())
        artifact = data.get("artifact", "")

        if "Part 2: The Octet of the Artifact (Polyglot)" in artifact:
            print("\n✅ POLYGLOT HEADER FOUND!")

            # Check for specific languages
            checks = {
                "Gherkin": "Feature: The Root (Ontos)",
                "Mermaid": "graph LR",
                "Chinese": "三拍为叶",
                "Hindi": "चार ताल रस के लिए",
                "Binary": "01010100 01000101",
                "Math": "∀e ∈ Entropy",
                "SQL": "SELECT * FROM World",
                "English": "Eight beats for the Crown",
            }

            all_passed = True
            for lang, text in checks.items():
                if text in artifact:
                    print(f"  - {lang}: DETECTED")
                else:
                    print(f"  - {lang}: MISSING ❌")
                    all_passed = False

            if all_passed:
                print("\n🎉 SUCCESS: All Polyglot Verses Verified!")
            else:
                print("\n⚠️ FAILURE: Some verses are missing.")

            await nc.close()
            os._exit(0)

    await nc.subscribe("hfo.heartbeat.>", cb=message_handler)

    # Keep running until message received
    while True:
        await asyncio.sleep(1)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
