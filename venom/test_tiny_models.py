import requests  # type: ignore
import time


def query_ollama(model, prompt):
    url = "http://localhost:11434/api/generate"
    data = {"model": model, "prompt": prompt, "stream": False}
    try:
        start_time = time.time()
        response = requests.post(url, json=data)
        end_time = time.time()
        response.raise_for_status()
        result = response.json()
        return result.get("response", ""), end_time - start_time
    except Exception as e:
        return f"Error: {e}", 0


def evaluate_prey_adherence(response_text):
    score = 0
    details = []

    response_lower = response_text.lower()

    if "perceive" in response_lower:
        score += 1
        details.append("Found 'Perceive'")
    if "react" in response_lower:
        score += 1
        details.append("Found 'React'")
    if "execute" in response_lower:
        score += 1
        details.append("Found 'Execute'")
    if "yield" in response_lower:
        score += 1
        details.append("Found 'Yield'")

    return score, details


def run_eval():
    models = ["gemma3:270m", "qwen2.5:0.5b"]

    tests = [
        {
            "name": "Simple Summarization",
            "prompt": (
                "Summarize the following text in one sentence:\n"
                "Hive Fleet Obsidian is a swarm of AI agents designed to work together. "
                "They use a biological metaphor, with different agents acting as organs like the Brain, Eyes, and Hands. "
                "The goal is to create a resilient, antifragile system that can evolve over time."
            ),
        },
        {
            "name": "Few-Shot PREY Report",
            "prompt": (
                "You are an agent. Submit a status report using this format:\n"
                "Perceive: [What you see]\n"
                "React: [What you think]\n"
                "Execute: [What you do]\n"
                "Yield: [What you return]\n\n"
                "Example:\n"
                "Perceive: System CPU is high.\n"
                "React: I need to cool down.\n"
                "Execute: Sleep for 5 seconds.\n"
                "Yield: Status Normal.\n\n"
                "Now you:\n"
                "Context: RAM is low (1GB).\n"
            ),
        },
    ]

    print("--- Starting Tiny Model Eval Round 2 ---\n")

    for model in models:
        print(f"Testing {model}...")
        for test in tests:
            print(f"  Running {test['name']}...")
            response, duration = query_ollama(model, test["prompt"])

            score = 0
            details = []
            if test["name"] == "Few-Shot PREY Report":
                score, details = evaluate_prey_adherence(response)

            print(f"  Time: {duration:.2f}s")
            if test["name"] == "Few-Shot PREY Report":
                print(f"  Score: {score}/4")
            print(f"  Output: {response.strip()[:200]}...")  # Truncate for readability
            print(f"  {'-'*10}")
        print("=" * 40 + "\n")


if __name__ == "__main__":
    run_eval()
