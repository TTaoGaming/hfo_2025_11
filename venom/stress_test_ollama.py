import asyncio
import time
import aiohttp
import statistics

OLLAMA_URL = "http://localhost:11435/api/generate"
MODEL = "gemma3:270m"
PROMPT = "Write a haiku about rust."


async def send_request(session, req_id):
    start = time.time()
    async with session.post(
        OLLAMA_URL, json={"model": MODEL, "prompt": PROMPT, "stream": False}
    ) as resp:
        await resp.json()
    end = time.time()
    return end - start


async def run_batch(batch_size):
    print(f"--- Testing Batch Size: {batch_size} ---")
    async with aiohttp.ClientSession() as session:
        tasks = [send_request(session, i) for i in range(batch_size)]
        start_batch = time.time()
        latencies = await asyncio.gather(*tasks)
        end_batch = time.time()

    total_time = end_batch - start_batch
    avg_latency = statistics.mean(latencies)
    tps_per_req = 1.0 / avg_latency  # Rough estimate
    total_throughput = batch_size / total_time

    print(f"Total Time: {total_time:.2f}s")
    print(f"Avg Latency: {avg_latency:.2f}s")
    print(f"Throughput: {total_throughput:.2f} req/s")
    return total_throughput


async def main():
    print("🦅 Venom: Stress Testing Ollama Parallelism (Port 11435)")

    # Warmup
    await run_batch(1)

    results = {}
    for size in [1, 2, 4, 8]:
        throughput = await run_batch(size)
        results[size] = throughput
        time.sleep(1)  # Cool down

    print("\n--- Analysis ---")
    base_throughput = results[1]
    for size in [2, 4, 8]:
        throughput = results[size]
        scaling_factor = throughput / base_throughput
        print(f"Batch {size}: {throughput:.2f} req/s (Scaling: {scaling_factor:.2f}x)")

    if results[8] > results[1] * 4:
        print("✅ Verdict: Excellent Parallelism")
    elif results[8] > results[1] * 1.5:
        print("⚠️ Verdict: Partial Parallelism (Resource Constrained)")
    else:
        print("❌ Verdict: Sequential Processing (No Parallelism)")


if __name__ == "__main__":
    asyncio.run(main())
