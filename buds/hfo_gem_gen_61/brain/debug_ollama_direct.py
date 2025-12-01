import sys
import os
import logging
import requests
import time

# Add root to path
sys.path.append(os.getcwd())

# Setup Logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger("DebugAssimilator")

def test_ollama_embedding():
    logger.info("1. Testing Ollama Embedding (Single Request)...")
    url = "http://localhost:11434/api/embeddings"
    payload = {
        "model": "nomic-embed-text",
        "prompt": "The quick brown fox jumps over the lazy dog."
    }
    
    try:
        start = time.time()
        resp = requests.post(url, json=payload, timeout=10)
        duration = time.time() - start
        
        if resp.status_code == 200:
            embedding = resp.json().get('embedding')
            if embedding and len(embedding) > 0:
                logger.info(f"✅ Embedding successful! Vector length: {len(embedding)}. Time: {duration:.2f}s")
                return True
            else:
                logger.error("❌ Embedding returned empty list.")
        else:
            logger.error(f"❌ Ollama returned status {resp.status_code}: {resp.text}")
            
    except requests.exceptions.Timeout:
        logger.error("❌ Ollama request TIMED OUT (10s).")
    except Exception as e:
        logger.error(f"❌ Exception: {e}")
    
    return False

if __name__ == "__main__":
    test_ollama_embedding()
