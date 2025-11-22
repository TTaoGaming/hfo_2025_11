import logging
from typing import Dict, Any, Callable
from body.hands.tools import ToolSet
from body.hands.external_tools import ExternalTools
from body.hands.cognitive_tools import SequentialThinkingTool

"""
🦅 Hive Fleet Obsidian: Tool Registry
Intent: Central registry for all agent capabilities.
Linked to: brain/capability_external_tools.feature
"""

logger = logging.getLogger("tool_registry")


class ToolRegistry:
    def __init__(self):
        self.tools: Dict[str, Callable] = {}
        self.definitions: Dict[str, str] = {}

        # Initialize Standard Tools
        self.basic_tools = ToolSet()
        self.register(
            "read_file",
            self.basic_tools.read_file,
            "read_file(file_path: str): Read content of a file.",
        )
        self.register(
            "write_file",
            self.basic_tools.write_file,
            "write_file(file_path: str, content: str): Write content to a file.",
        )
        self.register(
            "search_brain",
            self.basic_tools.search_web,
            "search_brain(query: str): Search the internal knowledge base (Brain).",
        )
        self.register(
            "list_directory",
            self.basic_tools.list_directory,
            "list_directory(path: str): List files in a folder.",
        )
        self.register(
            "grep_files",
            self.basic_tools.grep_files,
            "grep_files(pattern: str, path: str): Search for text in files.",
        )

        # Initialize External Tools
        self.external_tools = ExternalTools()
        self.register(
            "search_web",
            self.external_tools.search_web,
            "search_web(query: str): Search the real internet using DuckDuckGo.",
        )
        self.register(
            "calculator",
            self.external_tools.calculator,
            "calculator(expression: str): Evaluate a mathematical expression.",
        )

        # Initialize Cognitive Tools
        self.thinking_tool = SequentialThinkingTool()
        self.register(
            "sequential_thinking",
            self.thinking_tool.think,
            "sequential_thinking(thought: str, needs_more_time: bool, next_step_hint: str): Record a thought step.",
        )

    def register(self, name: str, func: Callable, definition: str):
        self.tools[name] = func
        self.definitions[name] = definition

    async def load_mcp_server(self, command: str, args: list):
        """
        Connects to an MCP server via stdio and registers its tools.
        (Placeholder for future implementation using 'mcp' library)
        """
        # TODO: Implement MCP Client
        # client = await mcp.Client.connect_stdio(command, args)
        # tools = await client.list_tools()
        # for tool in tools:
        #     self.register(tool.name, tool.func, tool.description)
        pass

    def get_definitions_str(self) -> str:
        return "\n".join([f"- {desc}" for desc in self.definitions.values()])

    def execute(self, tool_name: str, args: Dict[str, Any]) -> str:
        if tool_name not in self.tools:
            return f"Error: Tool '{tool_name}' not found."

        try:
            func = self.tools[tool_name]
            # Simple argument unpacking - in a robust system we'd use inspect or Pydantic
            # For now, we assume the LLM matches the signature or we pass **args
            # But our ToolSet methods have specific args.
            # Let's try to match args by name if possible, or just pass **args if the function accepts it.
            # Given the current simple implementation in tools.py, they take specific args.
            # We'll do a simple mapping for now, or update ToolSet to accept **kwargs.

            # Hack: Inspect the function to see what args it takes?
            # Or just try calling with **args.
            return func(**args)
        except TypeError as e:
            return f"Error executing '{tool_name}': {str(e)}"
        except Exception as e:
            return f"Error executing '{tool_name}': {str(e)}"
