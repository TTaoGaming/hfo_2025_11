#!/usr/bin/env python3
"""
🦅 Hive Fleet Obsidian: Genesis Protocol
Usage: python genesis.py

This script bootstraps the HFO environment, validates the biological anatomy,
and prepares the swarm for operation.
"""

import sys
import yaml
import subprocess
from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from rich.tree import Tree

console = Console()


def check_anatomy():
    """Validates that the biological organs exist."""
    console.print("[bold blue]🔍 Scanning HFO Anatomy...[/bold blue]")

    # Load the Holocron
    try:
        with open("brain/registry.yaml", "r") as f:
            registry = yaml.safe_load(f)
    except FileNotFoundError:
        console.print(
            "[bold red]❌ CRITICAL: The Brain (brain/registry.yaml) is missing![/bold red]"
        )
        sys.exit(1)

    anatomy_tree = Tree("🦅 [bold]Hive Fleet Obsidian[/bold]")

    all_healthy = True

    for organ_name, data in registry.get("organs", {}).items():
        path = Path(data["path"])
        if path.exists():
            status = "✅ [green]Healthy[/green]"
        else:
            status = "❌ [red]Missing[/red]"
            all_healthy = False

        organ_node = anatomy_tree.add(f"{organ_name.capitalize()} ({status})")
        organ_node.add(f"Role: [cyan]{data.get('primary_seat', 'Unknown')}[/cyan]")
        organ_node.add(
            f"Function: [yellow]{data.get('biological_function', 'Unknown')}[/yellow]"
        )

    console.print(anatomy_tree)

    if not all_healthy:
        console.print(
            "\n[bold red]⚠️  The Hive is wounded. Please repair missing organs.[/bold red]"
        )
        sys.exit(1)
    else:
        console.print("\n[bold green]✨ The Hive is biologically sound.[/bold green]")


def check_environment():
    """Checks if the Python environment is correctly set up."""
    console.print("\n[bold blue]🔍 Checking Environment...[/bold blue]")

    # Check Python version
    py_version = sys.version.split()[0]
    console.print(f"Python Version: [green]{py_version}[/green]")

    # Check if inside venv
    in_venv = sys.prefix != sys.base_prefix
    if in_venv:
        console.print("Virtual Environment: [green]Active[/green]")
    else:
        console.print(
            "Virtual Environment: [yellow]Inactive (Recommended to use venv)[/yellow]"
        )


def run_smoke_tests():
    """Offers to run the smoke tests."""
    console.print("\n[bold blue]🧪 Venom Protocol[/bold blue]")

    if "--venom" in sys.argv:
        response = "y"
        console.print("Running tests automatically due to --venom flag.")
    else:
        response = console.input("Do you want to run the smoke tests (Venom)? [y/N]: ")

    if response.lower() == "y":
        console.print("[bold]🚀 Injecting Venom...[/bold]")
        subprocess.run(["make", "test-all"])
    else:
        console.print("[yellow]Skipping tests.[/yellow]")


def execute_mission(mission_file: str):
    """
    Parses a Gherkin feature file and executes the corresponding Body code.
    This is the 'Genesis Bridge' (Word -> Flesh).
    """
    console.print(
        "[bold purple]🔮 Genesis Protocol: Materializing Intent...[/bold purple]"
    )
    console.print(f"Intent Source: [cyan]{mission_file}[/cyan]")

    path = Path(mission_file)
    if not path.exists():
        console.print(f"[bold red]❌ Intent file not found: {mission_file}[/bold red]")
        return

    # Simple Intent Mapping (Registry)
    # In the future, this should be dynamic or use a proper registry file.
    intent_map = {
        "mission_ingest_gems.feature": "body/digestion/swarm_spinner.py",
        "mission_evolutionary_loop.feature": "body/hands/run_evolution.py",
    }

    script_path = intent_map.get(path.name)

    if not script_path:
        console.print(
            f"[bold red]❌ No physical body found for intent: {path.name}[/bold red]"
        )
        console.print("Please register the mapping in genesis.py")
        return

    console.print(f"Physical Body: [green]{script_path}[/green]")
    console.print("[bold]🚀 Spawning Agent Swarm...[/bold]")

    # Execute the script with the correct environment
    try:
        # Ensure PYTHONPATH includes current directory
        env = sys.modules[__name__].__dict__.get("os", {}).get("environ", {}).copy()
        # We need to import os if it's not imported, but subprocess uses the current env by default.
        # Let's just pass a modified env.
        import os

        env = os.environ.copy()
        env["PYTHONPATH"] = os.getcwd()

        subprocess.run([sys.executable, script_path], env=env, check=True)
        console.print("[bold green]✅ Mission Accomplished.[/bold green]")
    except subprocess.CalledProcessError as e:
        console.print(
            f"[bold red]💥 Mission Failed with exit code {e.returncode}[/bold red]"
        )
    except Exception as e:
        console.print(f"[bold red]💥 Execution Error: {e}[/bold red]")


def main():
    console.print(
        Panel.fit(
            "[bold yellow]🦅 Hive Fleet Obsidian: Genesis Protocol (Gen 51)[/bold yellow]",
            subtitle="The Word becomes Flesh",
        )
    )

    # Check for Mission Flag
    if len(sys.argv) > 1 and sys.argv[1] == "--mission":
        if len(sys.argv) < 3:
            console.print(
                "[red]Usage: python genesis.py --mission <feature_file>[/red]"
            )
            sys.exit(1)
        execute_mission(sys.argv[2])
        sys.exit(0)

    check_anatomy()
    check_environment()
    run_smoke_tests()


if __name__ == "__main__":
    main()

    console.print("\n[bold magenta]🦅 Swarm Ready. Awaiting Directives.[/bold magenta]")


if __name__ == "__main__":
    main()
