import os

# Fix for OMP Error: Must be set before importing libraries that use OpenMP
os.environ["KMP_DUPLICATE_LIB_OK"] = "True"

import json
import time
import asyncio
from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field
import lancedb
import pyarrow as pa
# from sentence_transformers import SentenceTransformer
from openai import AsyncOpenAI
from dotenv import load_dotenv

load_dotenv()

# --- Configuration ---
DB_PATH = "buds/hfo_gem_gen_57/memory/lancedb"
MODEL_NAME = "x-ai/grok-4.1-fast:free"
EMBEDDING_MODEL = "openai/text-embedding-3-small" # Trying OpenRouter embedding
CONFIDENCE_CAP = 0.8
TAG = "HFO lvl0"
CONFIDENCE_CAP = 0.8
TAG = "HFO lvl0"

# --- Pydantic Models (The 8 Pillars) ---
class Ontos(BaseModel):
    id: str = Field(..., description="Unique Identifier")
    type: str = Field(..., description="Type of entity (e.g., code, doc, protocol)")
    owner: str = Field(..., description="Owner or Author")

class Logos(BaseModel):
    protocol: str = Field(..., description="Underlying protocol or logic")
    pattern: Optional[str] = Field(None, description="Design pattern used")

class Techne(BaseModel):
    stack: List[str] = Field(default_factory=list, description="Tech stack or dependencies")

class Chronos(BaseModel):
    status: str = Field(..., description="Current status (active, pending, etc.)")
    generation: int = Field(..., description="HFO Generation number")

class Pathos(BaseModel):
    validation: str = Field(..., description="Validation status")
    health: Optional[str] = Field(None, description="Health metric")

class Ethos(BaseModel):
    security: str = Field(..., description="Security level")
    compliance: List[str] = Field(default_factory=list, description="Compliance standards")

class Topos(BaseModel):
    path: str = Field(..., description="File path")
    links: List[str] = Field(default_factory=list, description="Linked entities")

class Telos(BaseModel):
    goal: str = Field(..., description="Primary purpose")
    viral_factor: float = Field(0.0, description="Importance/Spread factor")

class ObsidianMetadata(BaseModel):
    ontos: Ontos
    logos: Logos
    techne: Techne
    chronos: Chronos
    pathos: Pathos
    ethos: Ethos
    topos: Topos
    telos: Telos
    summary: str = Field(..., description="Concise summary of the content")

# --- The Scribe Agent ---
class Scribe:
    def __init__(self):
        self.client = AsyncOpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=os.getenv("OPENROUTER_API_KEY"),
        )
        print(f"🔌 Connected to OpenRouter. Target Model: {MODEL_NAME}")
        
        # print(f"🧠 Loading Embedding Model: {EMBEDDING_MODEL}...")
        # self.encoder = SentenceTransformer(EMBEDDING_MODEL)
        # print("✅ Embedding Model Loaded.")
        self.encoder = None

        self.db = lancedb.connect(DB_PATH)
        self.table_name = "hfo_memory_gen57"
        self.setup_table()

    def setup_table(self):
        # Define Schema
        schema = pa.schema([
            pa.field("id", pa.string()),
            pa.field("content", pa.string()),
            pa.field("vector", pa.list_(pa.float32(), 1536)),
            pa.field("source_path", pa.string()),
            pa.field("timestamp", pa.float64()),
            pa.field("confidence", pa.float64()),
            pa.field("tags", pa.list_(pa.string())),
            pa.field("metadata", pa.string()) # Storing JSON string for complex nested struct
        ])
        
        self.table = self.db.create_table(self.table_name, schema=schema, exist_ok=True)
        print(f"📂 Database Table '{self.table_name}' Ready at {DB_PATH}")

    async def get_embedding(self, text: str) -> List[float]:
        """Generates vector embedding using OpenRouter/OpenAI API."""
        try:
            response = await self.client.embeddings.create(
                model=EMBEDDING_MODEL,
                input=text[:8191] # OpenAI limit
            )
            return response.data[0].embedding
        except Exception as e:
            print(f"⚠️ Embedding Error: {e}. Using zero vector.")
            return [0.0] * 1536 # Default to 1536 dim for text-embedding-3-small

    async def analyze_file(self, file_path: str, content: str) -> ObsidianMetadata:
        system_prompt = """
        You are The Scribe, an agent of Hive Fleet Obsidian.
        Your task is to analyze the provided file content and extract the 8 Pillars of Metadata (OBSIDIAN).
        
        CRITICAL RULES:
        1. Do not hallucinate. If unknown, use "Unknown".
        2. Be concise.
        3. Output MUST be valid JSON matching the ObsidianMetadata schema below.
        4. Do NOT just return the file's YAML frontmatter. You must MAP it to the 8 Pillars.

        SCHEMA EXAMPLE:
        {
            "ontos": {"id": "...", "type": "...", "owner": "..."},
            "logos": {"protocol": "...", "pattern": "..."},
            "techne": {"stack": ["..."]},
            "chronos": {"status": "...", "generation": 57},
            "pathos": {"validation": "...", "health": "..."},
            "ethos": {"security": "...", "compliance": ["..."]},
            "topos": {"path": "...", "links": ["..."]},
            "telos": {"goal": "...", "viral_factor": 0.5},
            "summary": "..."
        }
        """
        
        user_prompt = f"""
        File Path: {file_path}
        
        Content:
        {content[:4000]} # Truncated for context window safety in this test
        
        Extract the ObsidianMetadata JSON.
        """

        response = await self.client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            response_format={"type": "json_object"},
            temperature=0.0
        )
        
        raw_json = response.choices[0].message.content
        print(f"🔍 Raw JSON from LLM:\n{raw_json}") # Debug print
        return ObsidianMetadata.model_validate_json(raw_json)

    async def ingest_file(self, file_path: str):
        print(f"🚀 Ingesting: {file_path}")
        
        # 1. Read Content
        try:
            with open(file_path, "r") as f:
                content = f.read()
        except Exception as e:
            print(f"❌ Error reading file: {e}")
            return

        # 2. Analyze (LLM)
        try:
            metadata = await self.analyze_file(file_path, content)
            print("✅ Metadata Extracted via Grok.")
        except Exception as e:
            print(f"❌ Error analyzing file: {e}")
            return

        # 3. Vectorize
        print(f"🧬 Generating Embedding with {EMBEDDING_MODEL}...")
        vector = await self.get_embedding(content)

        # 4. Construct Record
        record = {
            "id": f"mem_{int(time.time())}_{os.path.basename(file_path)}",
            "content": content,
            "vector": vector,
            "source_path": file_path,
            "timestamp": time.time(),
            "confidence": min(0.8, 0.8), # HARD CAP enforced
            "tags": [TAG, "ingestion_test"],
            "metadata": metadata.model_dump_json()
        }

        # 5. Write to DB
        self.table.add([record])
        print(f"💾 Saved to LanceDB. ID: {record['id']}")
        print(f"📊 Confidence: {record['confidence']} (Capped)")
        print(f"🏷️ Tags: {record['tags']}")
        print(f"🧩 Metadata Preview (Ontos): {metadata.ontos}")

    async def crawl_and_ingest(self, root_dir: str):
        ignore_dirs = {".git", "venv", "__pycache__", "node_modules", "lancedb", ".pytest_cache", "audit_trail"}
        ignore_extensions = {".pyc", ".png", ".jpg", ".jpeg", ".gif", ".svg", ".ico", ".zip", ".tar", ".gz", ".db", ".lance", ".parquet"}
        
        print(f"🕷️ Crawling root: {root_dir}")
        
        for root, dirs, files in os.walk(root_dir):
            # Modify dirs in-place to skip ignored directories
            dirs[:] = [d for d in dirs if d not in ignore_dirs]
            
            for file in files:
                if any(file.endswith(ext) for ext in ignore_extensions):
                    continue
                
                file_path = os.path.join(root, file)
                
                # Skip the script itself and the DB
                if "ingest_cold_forge.py" in file_path or "lancedb" in file_path:
                    continue

                await self.ingest_file(file_path)

async def main():
    scribe = Scribe()
    
    # Target the root of the workspace to consolidate everything
    workspace_root = "/home/tommytai3/hive_fleet_obsidian_2025_11"
    
    print("🔥 Starting Cold Forge Ingestion...")
    await scribe.crawl_and_ingest(workspace_root)
    print("❄️ Cold Forge Ingestion Complete.")

if __name__ == "__main__":
    asyncio.run(main())
