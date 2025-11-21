import json
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import ast

# --- Configuration ---
DATA_PATH = "./hfo_gem/gen_43/hfo_memory_backup.json"
OUTPUT_HTML = "./hfo_gem/gen_43/hfo_memory_dashboard.html"
SAMPLE_SIZE = 2000  # Downsample for speed if needed, set to None for full data

print("Loading data...")
data = []
with open(DATA_PATH, "r") as f:
    for line in f:
        if line.strip():
            try:
                data.append(json.loads(line))
            except json.JSONDecodeError:
                print(f"Skipping invalid JSON line: {line[:50]}...")

df = pd.DataFrame(data)

# Parse embeddings (they are strings in the JSON)
print("Parsing embeddings...")
df["embedding_vec"] = df["embedding"].apply(lambda x: ast.literal_eval(x))
embeddings = np.array(df["embedding_vec"].tolist())

# Parse metadata
print("Parsing metadata...")


def get_meta(x, key, default="Unknown"):
    if isinstance(x, dict):
        return x.get(key, default)
    return default


df["filename"] = df["metadata"].apply(lambda x: get_meta(x, "filename"))
df["level"] = df["metadata"].apply(lambda x: get_meta(x, "level"))
df["path"] = df["metadata"].apply(lambda x: get_meta(x, "path"))
df["created_at"] = pd.to_datetime(df["created_at"])

# Downsample if necessary for performance
if SAMPLE_SIZE and len(df) > SAMPLE_SIZE:
    print(f"Downsampling to {SAMPLE_SIZE} records for visualization performance...")
    indices = np.random.choice(len(df), SAMPLE_SIZE, replace=False)
    df = df.iloc[indices].reset_index(drop=True)
    embeddings = embeddings[indices]

# --- Analysis ---

# 1. PCA (Global Structure)
print("Running PCA...")
pca = PCA(n_components=3)
pca_result = pca.fit_transform(embeddings)
df["pca_x"] = pca_result[:, 0]
df["pca_y"] = pca_result[:, 1]
df["pca_z"] = pca_result[:, 2]
explained_variance = pca.explained_variance_ratio_

# 2. t-SNE (Local Clusters)
print("Running t-SNE...")
tsne = TSNE(n_components=2, random_state=42, perplexity=30)
tsne_result = tsne.fit_transform(embeddings)
df["tsne_x"] = tsne_result[:, 0]
df["tsne_y"] = tsne_result[:, 1]

# 3. Clustering (for coloring if needed)
print("Running KMeans...")
kmeans = KMeans(n_clusters=10, random_state=42)
df["cluster"] = kmeans.fit_predict(embeddings)
df["cluster"] = df["cluster"].astype(str)

# --- Visualization ---
print("Generating Dashboard...")

# Create the figure
fig = go.Figure()

# View 1: 2D t-SNE (The "Map")
# Good for: Seeing distinct topics and local relationships.
# Tradeoff: Distances are distorted; global structure is lost.
fig.add_trace(
    go.Scatter(
        x=df["tsne_x"],
        y=df["tsne_y"],
        mode="markers",
        marker=dict(
            size=5,
            color=df["cluster"].astype(int),  # Color by cluster
            colorscale="Viridis",
            showscale=True,
            colorbar=dict(title="Cluster ID"),
        ),
        text=df["filename"],
        customdata=np.stack((df["level"], df["content"].str[:100]), axis=-1),
        hovertemplate="<b>%{text}</b><br>Level: %{customdata[0]}<br>Snippet: %{customdata[1]}...<extra></extra>",
        name="t-SNE (Local Clusters)",
        visible=True,  # Default view
    )
)

# View 2: 3D PCA (The "Shape")
# Good for: Seeing the "shape" of the data and outliers.
# Tradeoff: Hard to navigate on 2D screens; depth perception issues.
fig.add_trace(
    go.Scatter3d(
        x=df["pca_x"],
        y=df["pca_y"],
        z=df["pca_z"],
        mode="markers",
        marker=dict(
            size=3, color=df["cluster"].astype(int), colorscale="Viridis", opacity=0.8
        ),
        text=df["filename"],
        hovertemplate="<b>%{text}</b><br>PCA View<extra></extra>",
        name="PCA (Global Shape)",
        visible=False,
    )
)

# View 3: Time Series (The "History")
# Good for: Seeing when knowledge was ingested.
# Tradeoff: Ignores semantic content.
# We'll aggregate by date for a bar chart
time_counts = df["created_at"].dt.date.value_counts().sort_index()
fig.add_trace(
    go.Bar(
        x=time_counts.index,
        y=time_counts.values,
        name="Ingestion Timeline",
        visible=False,
    )
)

# --- Layout & Menus ---

fig.update_layout(
    title="Hive Fleet Obsidian Memory Dashboard",
    template="plotly_dark",
    height=800,
    updatemenus=[
        dict(
            type="buttons",
            direction="left",
            buttons=list(
                [
                    dict(
                        label="2D t-SNE (Topics)",
                        method="update",
                        args=[
                            {"visible": [True, False, False]},
                            {
                                "title": "2D t-SNE: Local Semantic Clusters (Good for finding topics)",
                                "xaxis": {
                                    "visible": True,
                                    "showgrid": False,
                                    "zeroline": False,
                                    "showticklabels": False,
                                },
                                "yaxis": {
                                    "visible": True,
                                    "showgrid": False,
                                    "zeroline": False,
                                    "showticklabels": False,
                                },
                                "scene": {"visible": False},
                            },
                        ],
                    ),
                    dict(
                        label="3D PCA (Structure)",
                        method="update",
                        args=[
                            {"visible": [False, True, False]},
                            {
                                "title": f"3D PCA: Global Variance (Explained Variance: {sum(explained_variance):.2f})",
                                "scene": {"visible": True},
                                "xaxis": {"visible": False},
                                "yaxis": {"visible": False},
                            },
                        ],
                    ),
                    dict(
                        label="Timeline (History)",
                        method="update",
                        args=[
                            {"visible": [False, False, True]},
                            {
                                "title": "Ingestion Timeline: When memories were created",
                                "xaxis": {
                                    "visible": True,
                                    "title": "Date",
                                    "type": "date",
                                },
                                "yaxis": {"visible": True, "title": "Count"},
                                "scene": {"visible": False},
                            },
                        ],
                    ),
                ]
            ),
            pad={"r": 10, "t": 10},
            showactive=True,
            x=0.05,
            xanchor="left",
            y=1.15,
            yanchor="top",
        ),
    ],
)

# Add annotations for educational value
fig.add_annotation(
    text="<b>Tradeoff Note:</b><br>t-SNE preserves local neighbors but distorts global distances.<br>PCA preserves global variance but loses local detail.<br>Use t-SNE to find similar files, PCA to see the dataset's spread.",
    xref="paper",
    yref="paper",
    x=0.0,
    y=-0.1,
    showarrow=False,
    font=dict(size=12, color="gray"),
    align="left",
)

print(f"Saving dashboard to {OUTPUT_HTML}...")
fig.write_html(OUTPUT_HTML)
print("Done!")
