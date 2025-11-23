"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: d351dc54-0923-44f7-b637-4a27b1f4a57e
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T10:21:31.583113+00:00'
    generation: 51
  topos:
    address: eyes/tools/query_unified.py
    links: []
  telos:
    viral_factor: 0.0
    meme: query_unified.py
"""

import os
import sys
import psycopg2

# Add HiveFleetObsidian to path to use existing config
sys.path.append(os.path.join(os.getcwd(), "HiveFleetObsidian"))

try:
    from hfo_sdk.config import get_config
    from langchain_openai import OpenAIEmbeddings
except ImportError:
    print("Could not import hfo_sdk.")
    sys.exit(1)


def query_knowledge(query_text, limit=5):
    config = get_config()
    conn = psycopg2.connect(config.database.url)
    cur = conn.cursor()

    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    query_vector = embeddings.embed_query(query_text)

    print(f"\nSearching for: '{query_text}'\n" + "=" * 50)

    cur.execute(
        """
        SELECT source_path, content, metadata, 1 - (embedding <=> %s::vector) as similarity
        FROM knowledge_bank
        ORDER BY embedding <=> %s::vector
        LIMIT %s
    """,
        (query_vector, query_vector, limit),
    )

    results = cur.fetchall()

    for path, content, meta, sim in results:
        print(f"\n[Similarity: {sim:.4f}] {path}")
        print(f"Metadata: {meta}")
        print("-" * 20)
        print(content[:200] + "..." if len(content) > 200 else content)
        print("\n")

    conn.close()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        query_knowledge(sys.argv[1])
    else:
        print("Usage: python3 query_unified.py 'your search query'")
