---
title: External Tools Capability
status: Active
type: Capability
tags:
  - tools
  - web-search
  - file-io
---

# 🛠️ External Tools Capability

## ⚡ BLUF (Bottom Line Up Front)
The **External Tools Capability** grants HFO agents agency beyond the LLM context window. It provides a standardized, secure interface for **Web Search** (DuckDuckGo/Tavily) and **File System Operations** (Read/Write). This capability is strictly governed by the **PREY Loop** (Perceive-React-Execute-Yield), ensuring that tool usage is intentional, observable, and reversible where possible. It transforms the swarm from a "Chatbot" into a "Cyber-Physical System" capable of manipulating its environment.

---

## 1. Tooling Architecture

The `ToolSet` class acts as the gateway between the Agent's cognitive logic and the external world.

```mermaid
graph LR
    subgraph "Agent Brain"
        A[LLM Core] -->|Intent| B(Tool Caller)
    end

    subgraph "Tooling Layer"
        B -->|Parse| C{ToolSet Router}
        C -->|Route| D[Web Search]
        C -->|Route| E[File I/O]
        C -->|Route| F[System Info]
    end

    subgraph "External World"
        D -->|Query| G((Internet))
        E -->|Read/Write| H[(Local FS)]
        F -->|Poll| I[OS Kernel]
    end

    G -->|Result| D
    H -->|Content| E
    D -->|Output| B
    E -->|Output| B
```

## 2. Execution Flow

The safe execution path for a tool call.

```mermaid
sequenceDiagram
    participant Brain
    participant ToolSet
    participant Sandbox
    participant World

    Brain->>ToolSet: execute_tool(name, args)
    ToolSet->>ToolSet: Validate Schema (Pydantic)
    alt Invalid
        ToolSet-->>Brain: Error: Invalid Schema
    else Valid
        ToolSet->>Sandbox: Run Safe Wrapper
        Sandbox->>World: Perform Action
        World-->>Sandbox: Raw Result
        Sandbox->>ToolSet: Truncate/Format
        ToolSet-->>Brain: Structured Observation
    end
```

## 3. Tool State Machine

How a tool transitions from request to result.

```mermaid
stateDiagram-v2
    [*] --> Idle
    Idle --> Validating: Request Received
    Validating --> Executing: Schema OK
    Validating --> Error: Schema Bad
    Executing --> Success: Action Complete
    Executing --> Failed: Runtime Exception
    Success --> Formatting: Raw Output
    Formatting --> Idle: Return Result
    Error --> Idle: Return Error
    Failed --> Idle: Return Traceback
```
