import asyncio
import time
import aiohttp
import json
import re
import statistics

# Configuration
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELS = ["gemma3:270m", "llama3.2:1b", "qwen2.5:1.5b", "gemma2:2b"]
CONCURRENCY = 4  # Test with a small squad
TIMEOUT = 45

# --- Tasks ---

TASKS = [
    {
        "name": "The Parser",
        "prompt": """You are a log parser. Extract the following into JSON: {"level": "str", "component": "str", "message": "str"}.
Log: [INFO] [Stigmergy] Connection established to NATS.""",
        "validator": lambda x: "level" in x
        and "component" in x
        and x["level"] == "INFO",
    },
    {
        "name": "The Decider",
        "prompt": """You are a system controller. Return JSON: {"heartbeat_interval": int, "status": "str"}.
Context: RAM is low (500MB). Cynefin state is Chaotic.""",
        "validator": lambda x: "heartbeat_interval" in x
        and isinstance(x["heartbeat_interval"], int),
    },
    {
        "name": "The Router",
        "prompt": """Classify this message into one of: Ontos, Telos, Chronos. Return JSON: {"category": "str"}.
Message: "The system must survive for 100 years." """,
        "validator": lambda x: x.get("category") in ["Ontos", "Telos", "Chronos"],
    },
]


async def query_model(session, model, prompt):
    start = time.time()
    try:
        async with session.post(
            OLLAMA_URL,
            json={
                "model": model,
                "prompt": prompt + "\nRespond in pure JSON.",
                "stream": False,
                "options": {"temperature": 0.1},  # Low temp for logic
            },
            timeout=TIMEOUT,
        ) as resp:
            if resp.status != 200:
                return {"error": f"HTTP {resp.status}", "duration": time.time() - start}
            data = await resp.json()
            return {
                "response": data.get("response", ""),
                "duration": time.time() - start,
                "error": None,
            }
    except Exception as e:
        return {"error": str(e), "duration": time.time() - start}


def extract_json(text):
    # Try to find JSON block
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if match:
        try:
            return json.loads(match.group(0))
        except:
            pass
    return None


async def evaluate_model(model):
    print(f"\n🤖 Evaluating Model: {model}")
    print(f"   Concurrency: {CONCURRENCY}")

    score = 0
    total_tasks = len(TASKS) * CONCURRENCY
    latencies = []

    async with aiohttp.ClientSession() as session:
        for task in TASKS:
            print(f"   Task: {task['name']}...", end="", flush=True)

            # Run concurrent batch
            tasks = [
                query_model(session, model, task["prompt"]) for _ in range(CONCURRENCY)
            ]
            results = await asyncio.gather(*tasks)

            task_success = 0
            for res in results:
                if res["error"]:
                    continue

                latencies.append(res["duration"])
                json_out = extract_json(res["response"])

                if json_out and task["validator"](json_out):
                    task_success += 1

            score += task_success
            print(f" {task_success}/{CONCURRENCY} Passed.")

    success_rate = (score / total_tasks) * 100
    avg_latency = statistics.mean(latencies) if latencies else 0

    print(f"   🏁 Score: {score}/{total_tasks} ({success_rate:.1f}%)")
    print(f"   ⏱️ Avg Latency: {avg_latency:.2f}s")

    return {"model": model, "score": success_rate, "latency": avg_latency}


async def main():
    print("🏟️  The Model Coliseum: Stigmergy Eval")
    print("=======================================")

    results = []
    for model in MODELS:
        res = await evaluate_model(model)
        results.append(res)
        time.sleep(2)  # Cool down

    print("\n🏆 Final Scoreboard")
    print("===================")
    print(f"{'Model':<20} | {'Score':<10} | {'Latency':<10}")
    print("-" * 46)

    # Sort by Score (Desc), then Latency (Asc)
    results.sort(key=lambda x: (-x["score"], x["latency"]))

    for r in results:
        print(f"{r['model']:<20} | {r['score']:.1f}%     | {r['latency']:.2f}s")


if __name__ == "__main__":
    asyncio.run(main())
