import requests  # type: ignore
import time
import concurrent.futures
import statistics

MODEL = "gemma3:270m"
CONCURRENCY = 8
PROMPT = "Generate a unique 10-word sentence about swarms."


def query_ollama(id):
    url = "http://localhost:11434/api/generate"
    data = {
        "model": MODEL,
        "prompt": f"{PROMPT} (ID: {id})",  # Add ID to make prompt slightly unique to avoid caching if any
        "stream": False,
    }
    start = time.time()
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()
        duration = time.time() - start
        return {
            "id": id,
            "status": "success",
            "duration": duration,
            "text": response.json().get("response", "").strip(),
        }
    except Exception as e:
        duration = time.time() - start
        return {"id": id, "status": "error", "duration": duration, "error": str(e)}


def run_stress_test():
    print(f"--- Starting Swarm Concurrency Test (N={CONCURRENCY}) ---")
    print(f"Model: {MODEL}")
    print("Sending 8 requests simultaneously...")

    start_total = time.time()
    results = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=CONCURRENCY) as executor:
        futures = [executor.submit(query_ollama, i) for i in range(CONCURRENCY)]
        for future in concurrent.futures.as_completed(futures):
            results.append(future.result())

    end_total = time.time()
    total_time = end_total - start_total

    # Analysis
    successes = [r for r in results if r["status"] == "success"]
    errors = [r for r in results if r["status"] == "error"]
    durations = [r["duration"] for r in successes]

    print("\n=== Results ===")
    print(f"Total Wall Time: {total_time:.2f}s")
    print(f"Successful Requests: {len(successes)}/{CONCURRENCY}")

    if errors:
        print(f"Errors: {len(errors)}")
        for e in errors:
            print(f"  [{e['id']}] Error: {e['error']}")

    if durations:
        print(f"Average Latency: {statistics.mean(durations):.2f}s")
        print(f"Min Latency: {min(durations):.2f}s")
        print(f"Max Latency: {max(durations):.2f}s")

        # Check for true parallelism
        # If total time is close to max latency, it was parallel.
        # If total time is close to sum of latencies, it was serial.
        sum_latencies = sum(durations)
        print("\nParallelism Efficiency:")
        print(f"  Sum of individual times: {sum_latencies:.2f}s")
        print(f"  Actual wall time: {total_time:.2f}s")

        if total_time < (sum_latencies * 0.6):
            print(
                "  ✅ TRUE PARALLELISM DETECTED (Server is handling multiple requests at once)"
            )
        else:
            print("  ⚠️ SERIAL EXECUTION DETECTED (Requests were queued)")
            print("  (Did you restart Ollama with OLLAMA_NUM_PARALLEL=8?)")

    print("\nSample Outputs:")
    for r in successes[:3]:
        print(f"  [{r['id']}] ({r['duration']:.2f}s): {r['text'][:50]}...")


if __name__ == "__main__":
    run_stress_test()
