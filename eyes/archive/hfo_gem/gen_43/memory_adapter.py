import json
import pandas as pd
import numpy as np
import ast
import os

# Configuration
INPUT_FILE = "./hfo_gem/gen_43/hfo_memory_backup.json"
OUTPUT_DIR = "./hfo_gem/gen_43/adapters"


def load_data(filepath):
    data = []
    with open(filepath, "r") as f:
        for line in f:
            if line.strip():
                try:
                    data.append(json.loads(line))
                except json.JSONDecodeError:
                    continue
    return pd.DataFrame(data)


def process_data(df):
    # Safe parsing helper
    def parse_embedding(x):
        if isinstance(x, str):
            try:
                return ast.literal_eval(x)
            except:
                return None
        return x

    df["embedding_vec"] = df["embedding"].apply(parse_embedding)

    # Drop rows with failed embeddings
    df = df.dropna(subset=["embedding_vec"])

    # Flatten metadata for TSV/Parquet
    def get_meta(row, key):
        meta = row.get("metadata", {})
        if isinstance(meta, dict):
            return meta.get(key, "Unknown")
        return "Unknown"

    df["filename"] = df.apply(lambda x: get_meta(x, "filename"), axis=1)
    df["level"] = df.apply(lambda x: get_meta(x, "level"), axis=1)

    # Truncate content for visualization labels
    df["content_snippet"] = (
        df["content"]
        .astype(str)
        .str.slice(0, 100)
        .str.replace("\n", " ")
        .str.replace("\t", " ")
    )

    return df


def export_tensorboard(df, output_dir):
    """
    Creates vectors.tsv and metadata.tsv for TensorBoard Embedding Projector.
    """
    tb_dir = os.path.join(output_dir, "tensorboard")
    os.makedirs(tb_dir, exist_ok=True)

    # 1. Vectors TSV
    vectors = np.stack(df["embedding_vec"].values)
    np.savetxt(os.path.join(tb_dir, "vectors.tsv"), vectors, delimiter="\t")

    # 2. Metadata TSV
    meta_df = df[["filename", "level", "content_snippet", "created_at"]]
    meta_df.to_csv(os.path.join(tb_dir, "metadata.tsv"), sep="\t", index=False)

    print(f"TensorBoard files exported to {tb_dir}")


def export_parquet(df, output_dir):
    """
    Creates a Parquet file for high-performance tools (Spotlight, Pandas, etc).
    """
    pq_path = os.path.join(output_dir, "memory.parquet")

    # Drop the original string embedding column to save space
    # Also drop complex nested columns like 'metadata' which cause Parquet issues
    export_df = df.drop(columns=["embedding", "metadata"], errors="ignore")

    try:
        export_df.to_parquet(pq_path, index=False)
        print(f"Parquet file exported to {pq_path}")
    except ImportError:
        print("Error: pyarrow or fastparquet not installed. Skipping Parquet export.")
    except Exception as e:
        print(f"Error exporting Parquet: {e}")


def main():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    print(f"Loading {INPUT_FILE}...")
    df = load_data(INPUT_FILE)

    print("Processing data...")
    df = process_data(df)

    print("Exporting adapters...")
    export_tensorboard(df, OUTPUT_DIR)
    export_parquet(df, OUTPUT_DIR)

    print("Done.")


if __name__ == "__main__":
    main()
