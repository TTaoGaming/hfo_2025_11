"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: 13cd8809-f2e3-443c-af39-dea4f9781646
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T11:07:35.747248Z'
    generation: 51
  topos:
    address: eyes/archive/hfo_gem/gen_43/generate_mermaid_knowledge.py
    links: []
  telos:
    viral_factor: 0.0
    meme: generate_mermaid_knowledge.py
"""

import pandas as pd
import os


def generate_mermaid_diagrams():
    # Load the parquet file
    parquet_path = "hfo_gem/gen_43/adapters/memory.parquet"
    if not os.path.exists(parquet_path):
        print(f"Error: {parquet_path} not found. Please run memory_adapter.py first.")
        return

    df = pd.read_parquet(parquet_path)

    output_dir = "hfo_gem/gen_43/knowledge"
    os.makedirs(output_dir, exist_ok=True)

    # 1. Source File Mindmap
    # Group by source file to show where memory is coming from
    generate_source_mindmap(df, output_dir)

    # 2. Content Type Distribution (Pie Chart)
    generate_content_type_pie(df, output_dir)

    # 3. High Signal Clusters (Graph)
    # This is a heuristic: we'll link items that share the same source file
    # and have high token counts (implying "high signal" or density)
    generate_high_signal_graph(df, output_dir)

    print(f"Mermaid diagrams generated in {output_dir}")


def sanitize_label(text):
    """Clean text for Mermaid labels"""
    if not isinstance(text, str):
        return "Unknown"
    # Take first 30 chars, remove special chars
    clean = (
        text.replace('"', "'")
        .replace("(", "")
        .replace(")", "")
        .replace("[", "")
        .replace("]", "")
    )
    return clean[:30] + "..." if len(clean) > 30 else clean


def generate_source_mindmap(df, output_dir):
    """
    Creates a mindmap grouping memories by their source directory/file.
    """
    mermaid_content = ["mindmap", "  root((HFO Memory))"]

    # Extract directory structure from source paths
    # Use 'filename' if available, otherwise extract from 'source_id'

    def get_display_name(row):
        fname = str(row.get("filename", ""))
        if fname and fname.lower() != "none" and fname != "nan" and fname != "Unknown":
            return fname

        # Fallback to source_id
        sid = str(row.get("source_id", ""))
        if sid and sid.lower() != "none":
            # source_id might be a path like 'hfo_gem/gen_29/file.md' or 'file.md#chunk1'
            # We want the file part
            clean_path = sid.split("#")[0]  # Remove chunk anchor
            return clean_path.split("/")[-1]

        return "Unknown"

    # Apply the logic to create a temporary 'display_source' column
    df["display_source"] = df.apply(get_display_name, axis=1)

    # Get top 20 sources by count
    top_sources = df["display_source"].value_counts().head(20)

    for source, count in top_sources.items():
        # Simple hierarchy: just the filename
        mermaid_content.append(f"    {source} ({count})")

    with open(f"{output_dir}/memory_sources_mindmap.md", "w") as f:
        f.write("```mermaid\n")
        f.write("\n".join(mermaid_content))
        f.write("\n```")


def generate_content_type_pie(df, output_dir):
    """
    Creates a pie chart of memory types.
    """
    mermaid_content = ["pie title Memory Distribution by Type"]

    # Use 'memory_type' column if available, else fallback to filename
    col_to_use = "memory_type" if "memory_type" in df.columns else "filename"

    top_types = df[col_to_use].value_counts().head(10)

    for type_name, count in top_types.items():
        clean_name = str(type_name)
        mermaid_content.append(f'    "{clean_name}" : {count}')

    with open(f"{output_dir}/memory_distribution_pie.md", "w") as f:
        f.write("```mermaid\n")
        f.write("\n".join(mermaid_content))
        f.write("\n```")


def generate_high_signal_graph(df, output_dir):
    """
    Creates a graph linking high-content memories.
    """
    mermaid_content = ["graph LR"]

    # Filter for "high signal" - let's assume longer content = higher signal for now
    # or just take a sample.
    if "content" in df.columns:
        # Create a length column
        df["content_length"] = df["content"].str.len()
        high_signal = df.nlargest(15, "content_length")

        for idx, row in high_signal.iterrows():
            node_id = f"node{idx}"
            label = sanitize_label(row["content"])
            source = str(row["filename"])

            mermaid_content.append(f'    {node_id}["{label}"]')
            mermaid_content.append(f"    Source_{hash(source)}[{source}] --> {node_id}")

    with open(f"{output_dir}/high_signal_graph.md", "w") as f:
        f.write("```mermaid\n")
        f.write("\n".join(mermaid_content))
        f.write("\n```")


if __name__ == "__main__":
    generate_mermaid_diagrams()
