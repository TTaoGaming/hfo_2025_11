"""
---
holon:
  id: hfo-e37a5174
  type: unknown
  file: refractor_swarm.py
  status: active
---
"""
import asyncio
import os
import sqlite3
import aiofiles
from typing import List
from datetime import datetime
from dotenv import load_dotenv
from openai import AsyncOpenAI

# Load Environment
load_dotenv()

# Configuration
DB_PATH = "buds/hfo_gem_gen_63/memory/iron_ledger.db"
TARGET_DIR = "buds/hfo_gem_gen_63/grimoire/drafts"
LOG_FILE = "buds/hfo_gem_gen_63/forge/swarm.log"
MODEL_ID = "x-ai/grok-4.1-fast:free" 
CONCURRENCY = 8 
TIMEOUT = 60 

def log(message: str):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted = f"[{timestamp}] {message}"
    print(formatted)
    with open(LOG_FILE, "a") as f:
        f.write(formatted + "\n")

# Initialize Client
client = AsyncOpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    timeout=TIMEOUT
)

async def read_file_async(path: str) -> str:
    try:
        async with aiofiles.open(path, mode='r', encoding='utf-8', errors='ignore') as f:
            return await f.read()
    except Exception as e:
        log(f"❌ Error reading {path}: {e}")
        return ""

async def write_card_async(name: str, content: str):
    os.makedirs(TARGET_DIR, exist_ok=True)
    filename = f"{TARGET_DIR}/{name}.md"
    async with aiofiles.open(filename, mode='w') as f:
        await f.write(content)
    log(f"✨ Created Card: {filename}")

async def generate_card_content(file_path: str, content: str) -> str:
    filename = os.path.basename(file_path)
    card_id = filename.replace(".md", "_card")
    
    system_prompt = """
    You are the Swarmlord, an expert AI Architect.
    Your task is to 'Refract' a raw documentation file into a 'Grimoire Card'.
    
    A Grimoire Card is a structured artifact that combines:
    1. Intuition (Flavor/Philosophy)
    2. Intent (Declarative Gherkin)
    3. Implementation (Python Code Snippet)
    
    Output Format (Markdown):
    ---
    card:
      id: <card_id>
      source: <filename>
      type: Concept/Tool/Spell
    ---
    
    # 🃏 <Title>
    
    > **Intuition**: <One sentence philosophical summary>
    
    ## 📜 The Incantation (Intent)
    ```gherkin
    Feature: <Feature Name>
      Scenario: <Scenario Name>
        Given ...
        When ...
        Then ...
    ```
    
    ## 🧪 The Catalyst (Code)
    ```python
    # The Essence
    def <function_name>():
        ...
    ```
    
    ## ⚔️ Synergies
    *   <Bullet points on how this connects to other parts of the system>
    """
    
    user_prompt = f"""
    Refract this file: {filename}
    
    Content:
    {content[:8000]} # Truncate to avoid context limits if necessary
    """
    
    try:
        response = await client.chat.completions.create(
            model=MODEL_ID,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        log(f"❌ API Error on {filename}: {e}")
        return None

async def process_file(sem, file_path):
    async with sem:
        content = await read_file_async(file_path)
        if not content: return
        
        filename = os.path.basename(file_path)
        card_name = filename.replace(".md", "_card")
        
        card_content = await generate_card_content(file_path, content)
        if card_content:
            await write_card_async(card_name, card_content)

async def get_pending_files() -> List[str]:
    """Fetch all file paths from Iron Ledger that haven't been refracted yet."""
    if not os.path.exists(DB_PATH):
        log(f"❌ DB not found at {DB_PATH}")
        return []
        
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT file_path FROM holons")
    all_files = [row[0] for row in cursor.fetchall()]
    conn.close()
    
    pending = []
    for file_path in all_files:
        filename = os.path.basename(file_path)
        card_name = filename.replace(".md", "_card.md")
        target_path = os.path.join(TARGET_DIR, card_name)
        
        if not os.path.exists(target_path):
            pending.append(file_path)
            
    return pending

async def main():
    files = await get_pending_files()
    log(f"🕷️ Swarm Target: {len(files)} raw holons to refract.")
    
    sem = asyncio.Semaphore(CONCURRENCY)
    tasks = []
    
    # Process all files
    batch = files 
    
    log(f"🚀 Launching Swarm on {len(batch)} files with concurrency {CONCURRENCY}...")
    
    for file_path in batch:
        tasks.append(process_file(sem, file_path))
        
    await asyncio.gather(*tasks)
    log("✅ Batch Complete.")

if __name__ == "__main__":
    asyncio.run(main())
