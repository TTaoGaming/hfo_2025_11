import psycopg2
import os
import sys
from collections import Counter
from langchain_openai import OpenAIEmbeddings

# Add HiveFleetObsidian to path
sys.path.append(os.path.join(os.getcwd(), "HiveFleetObsidian"))

try:
    from hfo_sdk.config import get_config
except ImportError:
    # Fallback if SDK not found
    class Config:
        def __init__(self):
            self.database = type(
                "obj",
                (object,),
                {"url": "postgresql://postgres:mysecretpassword@localhost/vectordb"},
            )

    def get_config():
        return Config()


def get_db_connection():
    config = get_config()
    return psycopg2.connect(config.database.url)


def explore_concepts(seed_concepts, limit=20):
    print(f"🧠 Exploring Hive Mind for concepts: {seed_concepts}")

    conn = get_db_connection()
    embeddings_model = OpenAIEmbeddings(model="text-embedding-3-small")

    results_map = {}

    for concept in seed_concepts:
        print(f"  > Searching for '{concept}'...")
        vector = embeddings_model.embed_query(concept)

        with conn.cursor() as cur:
            # Find top matches
            cur.execute(
                """
                SELECT source_path, content, 1 - (embedding <=> %s::vector) as similarity
                FROM knowledge_bank
                ORDER BY embedding <=> %s::vector
                LIMIT %s
            """,
                (vector, vector, limit),
            )

            rows = cur.fetchall()
            results_map[concept] = rows

    return results_map


def generate_report(results_map):
    report = "# 🧬 HFO Concept Map\n\n"

    all_content = []

    for concept, rows in results_map.items():
        report += f"## {concept.title()}\n"
        if not rows:
            report += "*No data found yet. Ingestion may still be in progress.*\n\n"
            continue

        for path, content, similarity in rows:
            filename = os.path.basename(path)
            report += f"- **{filename}** (Confidence: {similarity:.2f})\n"
            # Extract a snippet
            snippet = content[:200].replace("\n", " ") + "..."
            report += f"  > *{snippet}*\n"
            all_content.append(content)
        report += "\n"

    # Simple Keyword Extraction (Frequency Analysis of the found content)
    report += "## 🔗 Emergent Keywords (Co-occurrence)\n"
    words = " ".join(all_content).lower().split()
    # Filter common stop words (very basic list)
    stop_words = set(
        [
            "the",
            "and",
            "of",
            "to",
            "a",
            "in",
            "is",
            "that",
            "for",
            "it",
            "with",
            "as",
            "on",
            "are",
            "this",
            "be",
            "can",
            "or",
            "by",
            "an",
            "not",
            "from",
            "at",
            "which",
            "but",
            "we",
            "have",
            "has",
            "if",
            "they",
            "their",
            "one",
            "all",
            "will",
            "so",
            "my",
            "me",
            "hfo",
            "file",
            "files",
        ]
    )
    filtered_words = [
        w.strip(".,()[]\"'")
        for w in words
        if w.strip(".,()[]\"'") not in stop_words and len(w) > 3
    ]

    common = Counter(filtered_words).most_common(20)
    for word, count in common:
        report += f"- **{word}**: {count}\n"

    return report


if __name__ == "__main__":
    # Default concepts from user request
    seeds = [
        "hexagonal",
        "swarm",
        "adversarial co-evolution",
        "hierarchical",
        "holonic",
        "topology",
        "stigmergic",
    ]

    if len(sys.argv) > 1:
        seeds = sys.argv[1:]

    data = explore_concepts(seeds)
    report = generate_report(data)

    with open("HFO_CONCEPT_MAP.md", "w") as f:
        f.write(report)

    print("\n✅ Analysis complete. Results saved to 'HFO_CONCEPT_MAP.md'")
    print("Run 'cat HFO_CONCEPT_MAP.md' to view.")
