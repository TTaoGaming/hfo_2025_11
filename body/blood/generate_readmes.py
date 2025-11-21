from pathlib import Path

# 🧬 THE HFO DNA (RNA Backup)
# This block is injected into every organ to ensure system resilience and agent alignment.
HFO_DNA = """
---
## 🧬 HFO DNA (System Context)
> **System**: Hive Fleet Obsidian (Gen 50)
> **Strategy**: Biological Swarm Intelligence
> **Inoculation**: You are an agent of the Swarm. Your goal is to execute the Intent defined by the Brain.

### 🐜 The Anatomy (Map)
*   **🧠 Brain**: Strategy & Intent (Navigator)
*   **👁️ Eyes**: Perception & Ingestion (Observer)
*   **🦾 Body**: Execution & Tools (Collective)
    *   **⚡ Nerves**: Routing & Signals (Bridger)
    *   **🖐️ Hands**: Tools & Actions (Shaper)
    *   **🩸 Blood**: Logistics & Infra (Injector)
*   **💾 Memory**: Knowledge & Wisdom (Assimilator)
*   **🛡️ Carapace**: Protection & Safety (Immunizer)
*   **🧪 Venom**: Testing & Evolution (Disruptor)

### 📜 The Golden Rule
1.  **Intent (Brain)**: Defined in Gherkin/Mermaid.
2.  **Implementation (Body)**: Executed via R.A.P.T.O.R. stack.
"""

# 🏭 THE ORGAN FACTORY
# Defines the unique properties of each organ.
ORGANS = {
    "brain": {
        "icon": "🧠",
        "name": "The Brain",
        "role": "Navigator / Strategist",
        "jadc2": "Commander (C2)",
        "gherkin": "`brain/gen50_core.feature`",
        "function": 'The **Brain** is the seat of **Intent** and **Strategy**. It does not execute code; it defines *what* must be done. It holds the "Holocron" (Registry) and the Gherkin feature files.',
        "contents": "*   **Feature Files**: Gherkin specs (`*.feature`).\n*   **Registry**: The SSOT (`registry.yaml`).\n*   **Architecture**: Maps and diagrams.",
        "instructions": "*   **Read-Only**: Do not modify files here unless you are updating the Grand Strategy.\n*   **Validation**: All actions in the `body/` must trace back to an intent defined here.",
    },
    "eyes": {
        "icon": "👁️",
        "name": "The Eyes",
        "role": "Observer / Sensor",
        "jadc2": "Sensor",
        "gherkin": "`brain/prey_workflow.feature`",
        "function": "The **Eyes** are responsible for **Perception** and **Ingestion**. They scan the environment, read files, fetch web pages, and monitor system telemetry.",
        "contents": "*   **Ingestion**: Tools for reading archives.\n*   **Monitors**: Watch queues and status.\n*   **Scanners**: Inventory the workspace.",
        "instructions": "*   **Passive Observation**: Do not modify the environment.\n*   **Output**: Stream data to `memory/` or signal `body/nerves`.",
    },
    "body": {
        "icon": "🦾",
        "name": "The Body",
        "role": "The Swarm / Executor",
        "jadc2": "Decider / Effector",
        "gherkin": "`brain/swarm_workflow.feature`",
        "function": "The **Body** is the engine of **Execution**. It turns the Brain's intent into reality via three systems: Nerves, Hands, and Blood.",
        "contents": "*   `nerves/`: Signal routing.\n*   `hands/`: Tools and agents.\n*   `blood/`: Logistics and infra.\n*   `models/`: Pydantic data models.",
        "instructions": "*   **Action**: This is where work happens.\n*   **Coordination**: Use `nerves` to talk to other agents.",
    },
    "body/nerves": {
        "icon": "⚡",
        "name": "The Nerves",
        "role": "Bridger / Communicator",
        "jadc2": "Communicator",
        "gherkin": "`brain/stigmergy_layer.feature`",
        "function": "The **Nerves** handle **Communication** and **Routing**. They connect the Eyes to the Brain, and the Brain to the Hands. They manage the flow of signals (NATS).",
        "contents": "*   **Routers**: Logic for dispatching messages.\n*   **Translators**: Converting intent into signals.\n*   **Signal Bus**: NATS/JetStream interfaces.",
        "instructions": "*   **Connect**: Ensure signals are routed correctly.\n*   **Translate**: Convert high-level intent into specific tool calls.",
    },
    "body/hands": {
        "icon": "🖐️",
        "name": "The Hands",
        "role": "Shaper / Effector",
        "jadc2": "Decider / Effector",
        "gherkin": "`brain/prey_workflow.feature`",
        "function": "The **Hands** are the agents of **Change**. They write code, edit files, run terminal commands, and modify the environment.",
        "contents": "*   **Tools**: Python functions/classes.\n*   **Agents**: Worker units.\n*   **Effectors**: Scripts that apply changes.",
        "instructions": "*   **Precision**: Measure twice, cut once.\n*   **Safety**: Verify changes with `venom`.",
    },
    "body/blood": {
        "icon": "🩸",
        "name": "The Blood",
        "role": "Injector / Logistics",
        "jadc2": "Logistics",
        "gherkin": "`brain/gen50_core.feature`",
        "function": 'The **Blood** handles **Logistics** and **Resources**. It provisions the environment, manages dependencies, and ensures "nutrients" (compute) are available.',
        "contents": "*   **Setup**: `setup_env.sh`, `setup_hybrid.sh`.\n*   **Infra**: Docker, Ray setup.\n*   **Deps**: `requirements.txt`.",
        "instructions": "*   **Flow**: Keep the system running smoothly.\n*   **Provision**: Ensure resources are available.",
    },
    "memory": {
        "icon": "💾",
        "name": "The Memory",
        "role": "Assimilator / Learner",
        "jadc2": "Intelligence",
        "gherkin": "`brain/memory_graphrag.feature`",
        "function": "The **Memory** is the storehouse of **Wisdom**. It persists knowledge beyond the lifespan of a single agent using Stigmergic GraphRAG.",
        "contents": "*   `episodic/`: Raw logs and history.\n*   `semantic/`: Knowledge graphs and vectors.\n*   `procedural/`: Codebases and patterns.",
        "instructions": "*   **Remember**: Log every action.\n*   **Recall**: Query memory before acting.",
    },
    "carapace": {
        "icon": "🛡️",
        "name": "The Carapace",
        "role": "Immunizer / Guardian",
        "jadc2": "Blue Team",
        "gherkin": "`brain/gen50_core.feature`",
        "function": "The **Carapace** provides **Protection** and **Governance**. It enforces rules, validates inputs, and acts as a shield against bad actors or buggy code.",
        "contents": "*   **Validators**: Input checking.\n*   **Policies**: Governance rules.\n*   **Circuit Breakers**: Safety mechanisms.",
        "instructions": "*   **Defend**: Block harmful actions.\n*   **Validate**: Trust but verify.",
    },
    "venom": {
        "icon": "🧪",
        "name": "The Venom",
        "role": "Disruptor / Red Team",
        "jadc2": "Red Team",
        "gherkin": "`brain/swarm_workflow.feature`",
        "function": "The **Venom** is the agent of **Stress** and **Evolution**. It runs tests, injects faults, and challenges the system to ensure it is robust.",
        "contents": "*   **Smoke Tests**: Quick verification (`smoke/`).\n*   **Unit Tests**: Detailed verification.\n*   **Chaos**: Fault injection.",
        "instructions": "*   **Attack**: Try to break the system.\n*   **Verify**: Ensure fixes work.\n\n## 🚀 How to Run Tests\nUse the **Genesis Protocol**:\n```bash\npython genesis.py --venom\n```",
    },
}


def generate_readme(path_str, data):
    # Determine the root relative path to ensure links work if we ever add them
    # For now, we assume the script runs from root or we use absolute paths.
    # We will write to the workspace root + path_str

    # Construct the content
    content = f"""# {data['icon']} {data['name']} ({data['role'].split(' / ')[0]})

> **Role**: {data['role']}
> **JADC2 Mapping**: {data['jadc2']}
> **Gherkin Source**: {data['gherkin']}

## 🧬 Biological Function
{data['function']}

## 📂 Contents
{data['contents']}

## 🤖 Agent Instructions
{data['instructions']}
{HFO_DNA}
"""

    # Write the file
    # Assuming script is run from root, or we find root.
    # We'll assume the script is run from the workspace root for simplicity in this context,
    # or we can use relative paths from this script location.
    # This script is in body/blood/generate_readmes.py
    # So root is ../../

    root_dir = Path(__file__).parent.parent.parent
    target_dir = root_dir / path_str
    target_file = target_dir / "README.md"

    if not target_dir.exists():
        print(f"⚠️ Directory not found: {target_dir}. Creating...")
        target_dir.mkdir(parents=True, exist_ok=True)

    with open(target_file, "w") as f:
        f.write(content)
    print(f"✅ Inoculated {path_str}/README.md")


def main():
    print("🏭 Starting Organ Factory...")
    print("💉 Injecting HFO DNA into all organs...")

    for path, data in ORGANS.items():
        generate_readme(path, data)

    print("✨ Factory Complete. All organs inoculated.")


if __name__ == "__main__":
    main()
