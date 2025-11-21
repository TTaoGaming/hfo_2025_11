import os

# import psycopg2
# from langchain.vectorstores import PGVector
# from langchain.embeddings import OpenAIEmbeddings


def scan_archive(archive_path):
    """
    Scans the archive for relevant files (Markdown, Python, JSON).
    """
    print(f"Scanning archive at: {archive_path}")
    files = []
    for root, dirs, filenames in os.walk(archive_path):
        for filename in filenames:
            if filename.endswith((".md", ".py", ".json", ".txt")):
                files.append(os.path.join(root, filename))
    return files


def process_file(file_path):
    """
    Reads and cleans a file.
    TODO: Implement 'AI Slop' cleaning logic here.
    """
    with open(file_path, "r", errors="ignore") as f:
        content = f.read()

    # Placeholder for cleaning logic
    # e.g., remove repetitive headers, failed code blocks, etc.
    return content


def main():
    archive_path = "../../_ARCHIVE_2025_11_19"
    files = scan_archive(archive_path)
    print(f"Found {len(files)} files to process.")

    for file in files[:5]:  # Test with first 5
        print(f"Processing: {file}")
        _ = process_file(file)
        # TODO: Embed and store in pgvector
        # store_in_memory(content)


if __name__ == "__main__":
    main()
