import json
import sys
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import plotly.express as px

BACKUP_FILE = "hfo_memory_backup.json"
OUTPUT_FILE = "hfo_memory_viz.html"


def load_data():
    print(f"📂 Loading memory backup: {BACKUP_FILE}...")
    data = []
    try:
        with open(BACKUP_FILE, "r", encoding="utf-8") as f:
            for line in f:
                try:
                    record = json.loads(line)
                    # Parse embedding string to list
                    if "embedding" in record and isinstance(record["embedding"], str):
                        record["embedding"] = json.loads(record["embedding"])

                    if record.get("embedding"):
                        data.append(record)
                except Exception:
                    continue
    except FileNotFoundError:
        print("❌ Backup file not found.")
        sys.exit(1)

    print(f"   └── Loaded {len(data)} records with embeddings.")
    return data


def process_data(data):
    print("🧠 Processing embeddings...")

    # Extract embeddings and metadata
    embeddings = np.array([d["embedding"] for d in data])

    # Metadata for hover
    ids = [d.get("id", "N/A") for d in data]
    contents = [
        d.get("content", "")[:200] + "..." for d in data
    ]  # Truncate for display
    sources = [d.get("source_id", "Unknown") for d in data]
    types = [d.get("memory_type", "Unknown") for d in data]

    # Dimensionality Reduction (PCA) -> 3D
    print("   └── Reducing dimensions (1536 -> 3)...")
    pca = PCA(n_components=3)
    components = pca.fit_transform(embeddings)

    # Clustering (K-Means) -> 8 Clusters (Obsidian Roles?)
    print("   └── Clustering concepts...")
    kmeans = KMeans(n_clusters=8, random_state=42)
    clusters = kmeans.fit_predict(embeddings)

    # Create DataFrame
    df = pd.DataFrame(components, columns=["x", "y", "z"])
    df["id"] = ids
    df["content"] = contents
    df["source"] = sources
    df["type"] = types
    df["cluster"] = clusters.astype(str)

    return df


def generate_plot(df):
    print(f"🎨 Generating interactive plot: {OUTPUT_FILE}...")

    fig = px.scatter_3d(
        df,
        x="x",
        y="y",
        z="z",
        color="cluster",
        symbol="type",
        hover_data=["id", "source", "content"],
        title="Hive Fleet Obsidian: Memory Topology (Gen 43)",
        opacity=0.7,
        size_max=5,
    )

    fig.update_layout(margin=dict(l=0, r=0, b=0, t=40))

    fig.write_html(OUTPUT_FILE)
    print("✅ Visualization complete.")


if __name__ == "__main__":
    data = load_data()
    if data:
        df = process_data(data)
        generate_plot(df)
    else:
        print("❌ No data found to visualize.")
