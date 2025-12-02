---
card:
  id: f353e740-45ae-4eae-9a0a-dda084cf9b52
  source: capability_external_tools.md
  type: Tool
---

# 🃏 External Tools Capability

> **Intuition**: This capability liberates agents from the confines of the LLM context window, forging a secure bridge to the external world through intentional, observable tool invocations governed by the PREY Loop.

## 📜 The Incantation (Intent)
```gherkin
Feature: External Tools Capability

  Scenario: Safely execute an external tool call
    Given an agent brain issues a tool request with name and arguments
    When the ToolSet validates the schema using Pydantic
    And routes to the appropriate sandboxed executor (Web Search or File I/O)
    Then it performs the action in isolation
    And returns a truncated, structured observation or error
```

## 🧪 The Catalyst (Code)
```python
# The Essence
from pydantic import validate_model  # Simplified; assumes ToolSchema registry

class ToolSet:
    def execute_tool(self, name: str, args: dict) -> str:
        """
        Gateway for safe external tool execution via PREY Loop.
        """
        # 1. Schema Validation
        tool_schema = self._get_tool_schema(name)
        try:
            validated_args = tool_schema(**args)
        except ValidationError as e:
            return f"Error: Invalid Schema - {e}"
        
        # 2. Sandboxed Execution
        try:
            if name == "web_search":
                result = self._duckduckgo_or_tavily(validated_args.query)
            elif name == "file_io":
                result = self._safe_fs_op(validated_args.path, validated_args.mode)
            else:
                raise ValueError(f"Unknown tool: {name}")
            
            # 3. Format & Truncate
            observation = self._truncate_and_structure(result)
            return observation
        except Exception as e:
            return f"Execution Failed: {traceback.format_exc()}"
```

## ⚔️ Synergies
*   Integrates with **PREY Loop** (Perceive-React-Execute-Yield) for reversible, observable agency in HFO agents.
*   Connects **Agent Brain** (LLM Core + Tool Caller) to **External World** (Internet, Local FS, OS Kernel).
*   Enables **Web Search** (DuckDuckGo/Tavily) and **File I/O** (Read/Write) as core primitives.
*   Powers swarm evolution from "Chatbot" to "Cyber-Physical System" via ToolSet Router and State Machine.