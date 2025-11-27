import asyncio
import time
import aiohttp
import statistics
import os

# Configuration
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "gemma3:270m"
PROMPT = "Write a haiku about rust."
TIMEOUT = 30  # Seconds before we consider it a failure (too slow)


async def send_request(session, req_id):
    start = time.time()
    try:
        async with session.post(
            OLLAMA_URL,
            json={"model": MODEL, "prompt": PROMPT, "stream": False},
            timeout=TIMEOUT,
        ) as resp:
            if resp.status != 200:
                return None
            await resp.json()
    except Exception:
        return None
    end = time.time()
    return end - start


async def run_batch(batch_size):
    print(f"--- Testing Concurrency: {batch_size} ---")
    async with aiohttp.ClientSession() as session:
        tasks = [send_request(session, i) for i in range(batch_size)]
        start_batch = time.time()
        results = await asyncio.gather(*tasks)
        end_batch = time.time()

    # Filter failures
    latencies = [r for r in results if r is not None]
    failures = batch_size - len(latencies)

    if failures > 0:
        print(f"❌ Failed: {failures}/{batch_size} requests failed or timed out.")
        return False

    total_time = end_batch - start_batch
    avg_latency = statistics.mean(latencies)

    print(f"✅ Success: {batch_size} agents.")
    print(f"   Total Time: {total_time:.2f}s")
    print(f"   Avg Latency: {avg_latency:.2f}s")

    # Heuristic: If avg latency > 5s, it's too slow for a heartbeat
    if avg_latency > 5.0:
        print("⚠️  Warning: Latency is high. System is struggling.")

    return True


async def main():
    print(f"🦅 Venom: Finding Max Concurrency for {MODEL}")
    print(f"   CPUs Available: {os.cpu_count()}")

    # Warmup
    print("🔥 Warming up...")
    await run_batch(1)

    max_stable = 1
    for size in [2, 3, 4, 5, 6, 7, 8, 10, 12, 16]:
        success = await run_batch(size)
        if success:
            max_stable = size
            time.sleep(1)  # Cool down
        else:
            print(f"\n💥 System Buckled at {size} agents.")
            break

    print(f"\n🏆 Max Stable Concurrency: {max_stable} Agents")


if __name__ == "__main__":
    asyncio.run(main())
