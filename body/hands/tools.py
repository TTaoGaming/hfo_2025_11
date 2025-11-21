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
        Mock web search for now.
        In production, connect to Tavily/SerpAPI.
        """
        return f"Mock Search Result for '{query}': The answer is 42."
