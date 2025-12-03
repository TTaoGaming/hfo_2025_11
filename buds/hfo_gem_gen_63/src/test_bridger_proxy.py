import asyncio
import sys
import os

# Add root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.bridger import bridger

async def test_bridger():
    print("🕷️ Testing Bridger Proxy...")
    print(f"Bridger Instance: {bridger}")
    print(f"NATS URL: {bridger.url}")
    # We won't connect because NATS might not be running or we don't want to block
    print("✅ Bridger Proxy Loaded Successfully.")

if __name__ == "__main__":
    asyncio.run(test_bridger())
