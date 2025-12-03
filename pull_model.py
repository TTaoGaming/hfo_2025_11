
import ollama
import sys

model_name = "nomic-embed-text" # Try the standard one first
# Or check what the error said: "nomic-embed-text-v2"

print(f"Pulling {model_name}...")
try:
    ollama.pull(model_name)
    print(f"✅ Successfully pulled {model_name}")
except Exception as e:
    print(f"❌ Failed to pull {model_name}: {e}")
    
    # Try v1.5 or just 'nomic-embed-text' if v2 failed
    print("Trying 'nomic-embed-text'...")
    try:
        ollama.pull("nomic-embed-text")
        print("✅ Successfully pulled nomic-embed-text")
    except Exception as e2:
        print(f"❌ Failed to pull nomic-embed-text: {e2}")
