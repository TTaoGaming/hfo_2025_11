"""
---
holon:
  id: hfo-bf141b37
  type: unknown
  file: fetch_pricing.py
  status: active
---
"""
from duckduckgo_search import DDGS
import json

def search(query):
    print(f"Searching for: {query}")
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=3))
            print(json.dumps(results, indent=2))
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    search("current LLM API pricing comparison 2024 2025")
    search("xAI Grok API pricing")
    search("Anthropic Claude 3.5 Sonnet API pricing")
    search("OpenAI GPT-4o API pricing")
    search("Google Gemini 1.5 Pro API pricing")
