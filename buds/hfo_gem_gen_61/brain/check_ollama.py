import requests
import sys

def check_ollama(url="http://localhost:11434"):
    print(f"🔍 Checking Ollama at {url}...")
    try:
        # Check tags endpoint
        resp = requests.get(f"{url}/api/tags", timeout=2)
        if resp.status_code == 200:
            print("✅ Ollama is ONLINE.")
            models = resp.json().get('models', [])
            print(f"📚 Available Models: {[m['name'] for m in models]}")
            return True
        else:
            print(f"⚠️ Ollama responded with status: {resp.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("❌ Connection Refused. Is Ollama running?")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    success = check_ollama()
    sys.exit(0 if success else 1)
