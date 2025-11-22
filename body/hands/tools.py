import os


class ToolSet:
    """
    Basic Toolset for PreyAgents.
    """

    @staticmethod
    def read_file(file_path: str) -> str:
        """Reads a file from the local filesystem."""
        try:
            if not os.path.exists(file_path):
                return f"Error: File not found at {file_path}"
            with open(file_path, "r") as f:
                return f.read()
        except Exception as e:
            return f"Error reading file: {str(e)}"

    @staticmethod
    def write_file(file_path: str, content: str) -> str:
        """Writes content to a file, creating directories if needed."""
        try:
            directory = os.path.dirname(file_path)
            if directory:
                os.makedirs(directory, exist_ok=True)
            with open(file_path, "w") as f:
                f.write(content)
            return f"Successfully wrote to {file_path}"
        except Exception as e:
            return f"Error writing file: {str(e)}"

    @staticmethod
    def search_web(query: str) -> str:
        """
        Searches the local 'brain/' directory for concepts.
        (Simulates a 'Web Search' over the internal Knowledge Base).
        """
        results = []
        search_root = "brain"
        if not os.path.exists(search_root):
            return "Error: Brain directory not found."

        try:
            for root, _, files in os.walk(search_root):
                for file in files:
                    if file.endswith(".md") or file.endswith(".feature"):
                        path = os.path.join(root, file)
                        with open(path, "r") as f:
                            content = f.read()
                            if query.lower() in content.lower():
                                snippet = content[:200].replace("\n", " ") + "..."
                                results.append(f"Found in {path}: {snippet}")

            if not results:
                return f"No results found for '{query}' in local brain archives."
            return "\n".join(results[:5])  # Return top 5 matches
        except Exception as e:
            return f"Search failed: {str(e)}"

    @staticmethod
    def list_directory(path: str = ".") -> str:
        """Lists files in a directory."""
        try:
            if not os.path.exists(path):
                return f"Error: Path {path} does not exist."
            items = os.listdir(path)
            # Filter out hidden files and __pycache__
            items = [
                i for i in items if not i.startswith(".") and "__pycache__" not in i
            ]
            return "\n".join(items)
        except Exception as e:
            return f"Error listing directory: {str(e)}"

    @staticmethod
    def grep_files(pattern: str, path: str = ".") -> str:
        """Simple grep-like search in files."""
        results = []
        try:
            for root, _, files in os.walk(path):
                if "__pycache__" in root or ".git" in root:
                    continue
                for file in files:
                    if file.endswith((".md", ".py", ".txt", ".json", ".yaml")):
                        full_path = os.path.join(root, file)
                        try:
                            with open(full_path, "r", errors="ignore") as f:
                                content = f.read()
                                if pattern.lower() in content.lower():
                                    results.append(full_path)
                        except Exception:
                            continue
            return "\n".join(results[:20])  # Limit to 20 hits
        except Exception as e:
            return f"Error searching files: {str(e)}"
