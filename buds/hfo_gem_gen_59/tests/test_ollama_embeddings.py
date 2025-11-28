import requests
import time
import json
import numpy as np
from typing import List, Dict

# Configuration
OLLAMA_URL = "http://localhost:11434"
MODELS_TO_TEST = [
    "nomic-embed-text",       # The current open-source gold standard
    "mxbai-embed-large",      # Strong contender, often beats OpenAI
    "snowflake-arctic-embed", # Enterprise grade, very robust
    "all-minilm"              # The classic baseline (fastest)
]

# Sample Data (Simulating IronLedger Content)
SAMPLE_DOCUMENTS = [
    "The Swarmlord is the central coordinator of the Hive Fleet, responsible for strategic decisions.",
    "IronLedger is an ACID-compliant SQLite database used for storing the single source of truth.",
    "LanceDB is a vector database used for semantic search and long-term memory retrieval.",
    "The PREY loop consists of Perceive, React, Execute, and Yield phases.",
    "Gen 59 focuses on canalization and preventing AI slop through strict guardrails."
]

QUERY = "What is the role of the Swarmlord?"

def get_installed_models() -> List[str]:
    try:
        response = requests.get(f"{OLLAMA_URL}/api/tags")
        if response.status_code == 200:
            return [m['name'].split(':')[0] for m in response.json()['models']]
        return []
    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to Ollama. Is it running?")
        return []

def pull_model(model_name: str):
    print(f"⬇️  Pulling {model_name} (this may take a moment)...")
    # Note: This is a streaming request, but for simplicity we just trigger it
    # In a real script we'd handle the stream. For now, we assume the user might need to pull manually if this times out.
    try:
        response = requests.post(f"{OLLAMA_URL}/api/pull", json={"name": model_name}, stream=True)
        for line in response.iter_lines():
            if line:
                status = json.loads(line).get('status')
                if status == 'success':
                    print(f"✅ Pulled {model_name}")
                    return
    except Exception as e:
        print(f"⚠️  Failed to pull {model_name}: {e}")

def get_embedding(model: str, text: str) -> List[float]:
    response = requests.post(
        f"{OLLAMA_URL}/api/embeddings",
        json={"model": model, "prompt": text}
    )
    if response.status_code == 200:
        return response.json()['embedding']
    else:
        raise Exception(f"Error from Ollama: {response.text}")

def cosine_similarity(v1: List[float], v2: List[float]) -> float:
    vec1 = np.array(v1)
    vec2 = np.array(v2)
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

def run_benchmark():
    print(f"🚀 Starting Embedding Benchmark for HFO Memory System")
    print(f"---------------------------------------------------")
    
    installed = get_installed_models()
    print(f"📦 Installed Models: {installed}")

    results = []

    for model in MODELS_TO_TEST:
        print(f"\n🧪 Testing Model: {model}")
        
        # Check if installed, if not try to pull (or warn)
        if model not in installed and f"{model}:latest" not in installed:
            print(f"   Model not found locally.")
            # pull_model(model) # Uncomment to auto-pull, but it might be slow
            print(f"   ⚠️  Please run: 'ollama pull {model}' to test this model.")
            continue

        try:
            # 1. Speed Test (Batch)
            start_time = time.time()
            embeddings = []
            for doc in SAMPLE_DOCUMENTS:
                embeddings.append(get_embedding(model, doc))
            end_time = time.time()
            
            total_time = end_time - start_time
            avg_time = total_time / len(SAMPLE_DOCUMENTS)
            
            # 2. Dimension Check
            dim = len(embeddings[0])
            
            # 3. Retrieval Quality (Simple)
            query_vec = get_embedding(model, QUERY)
            
            # Calculate similarity with the first doc (Swarmlord) vs others
            # Doc 0 is the correct answer.
            sim_scores = [cosine_similarity(query_vec, doc_vec) for doc_vec in embeddings]
            
            # Check if the top result is actually the Swarmlord doc
            top_idx = np.argmax(sim_scores)
            is_correct = (top_idx == 0)
            
            # The "Gap" - difference between correct answer and the next best
            sorted_scores = sorted(sim_scores, reverse=True)
            confidence_gap = sorted_scores[0] - sorted_scores[1]

            print(f"   ⏱️  Avg Latency: {avg_time*1000:.2f} ms/doc")
            print(f"   📏 Dimensions:  {dim}")
            print(f"   🎯 Retrieval:   {'✅ PASS' if is_correct else '❌ FAIL'}")
            print(f"   🧠 Confidence:  {confidence_gap:.4f} (Higher is better)")
            
            results.append({
                "model": model,
                "latency": avg_time,
                "dimensions": dim,
                "gap": confidence_gap
            })

        except Exception as e:
            print(f"   ❌ Failed: {e}")

    print(f"\n🏆 Benchmark Summary")
    print(f"---------------------------------------------------")
    # Sort by Confidence Gap (Quality)
    results.sort(key=lambda x: x['gap'], reverse=True)
    
    for i, res in enumerate(results):
        print(f"{i+1}. {res['model']}")
        print(f"   Quality (Gap): {res['gap']:.4f}")
        print(f"   Speed:         {res['latency']*1000:.2f} ms")
        print(f"   Dimensions:    {res['dimensions']}")

if __name__ == "__main__":
    run_benchmark()
