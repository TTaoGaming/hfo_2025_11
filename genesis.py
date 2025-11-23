#!/usr/bin/env python3
"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: fd425bd0-c5a5-4219-8dfd-f396d5738213
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T11:06:38.159072Z'
    generation: 51
  topos:
    address: genesis.py
    links: []
  telos:
    viral_factor: 0.0
    meme: genesis.py
"""

import sys
import yaml
import re
import uuid
import datetime
import hashlib
import subprocess
from pathlib import Path
from rich.console import Console
from rich.tree import Tree

# Ensure we can import from body
sys.path.append(str(Path(__file__).parent))
from body.models.hexagon import (  # noqa: E402
    Hexagon,
    Ontos,
    Telos,
    Chronos,
    Topos,
    Logos,
    Pathos,
    HolonType,
    HolonStatus,
)

console = Console()


class GenesisScanner:
    """The Observer: Validates the health of the Hive."""

    def __init__(self):
        self.registry_path = Path("brain/registry.yaml")

    def scan(self):
        """Validates that the biological organs exist."""
        console.print("[bold blue]🔍 Scanning HFO Anatomy...[/bold blue]")

        # Load the Holocron
        try:
            with open(self.registry_path, "r") as f:
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
        self._check_environment()

        if not all_healthy:
            console.print(
                "\n[bold red]⚠️  The Hive is wounded. Please repair missing organs.[/bold red]"
            )
            sys.exit(1)
        else:
            console.print(
                "\n[bold green]✨ The Hive is biologically sound.[/bold green]"
            )

    def _check_environment(self):
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


class GenesisFactory:
    """The Evolutionary Forge: Turns Intent into Implementation."""

    def __init__(self):
        self.brain_path = Path("brain")
        self.body_path = Path("body")

    def evolve(self):
        console.print(
            "[bold purple]🧬 Initiating Genesis Evolution (Byzantine Swarm Mode)...[/bold purple]"
        )
        features = list(self.brain_path.glob("*.feature"))

        for feature_file in features:
            self._process_feature(feature_file)

    def _process_feature(self, feature_file: Path):
        """
        Processes a single Gherkin feature file using Swarm Principles.
        1. Perceive: Read the Intent (Gherkin).
        2. React: Check if implementation exists and is stale (Lazy Loading).
        3. Execute: Generate/Update the Hexagonal Holon (Stigmergy).
        4. Yield: Apply Hive Guards.
        """
        console.print(f"  🐜 Processing Intent: [cyan]{feature_file.name}[/cyan]")

        # 1. Perceive (Read Intent)
        intent_content = feature_file.read_text()
        intent_hash = hashlib.sha256(intent_content.encode()).hexdigest()

        # Determine target file (Simple mapping for now: brain/X.feature -> body/X.py)
        # In a real swarm, this mapping would be dynamic or looked up in a registry.
        target_name = feature_file.stem.replace("architecture_", "").replace(
            "design_", ""
        )
        target_file = self.body_path / f"{target_name}.py"

        # 2. React (Lazy Loading & Byzantine Check)
        if target_file.exists():
            if self._is_up_to_date(target_file, intent_hash):
                console.print(
                    f"    ⏭️  [dim]Skipping (Up to date): {target_file.name}[/dim]"
                )
                return
            else:
                console.print(
                    f"    🔄 [yellow]Drift Detected. Regenerating: {target_file.name}[/yellow]"
                )
        else:
            console.print(
                f"    ✨ [green]Germinating New Holon: {target_file.name}[/green]"
            )

        # 3. Execute (Generate Hexagon)
        hexagon = self._forge_hexagon(feature_file, intent_hash, target_file)

        # 4. Yield (Apply Hive Guards & Write)
        self._write_holon(target_file, hexagon, intent_content)

    def _is_up_to_date(self, target_file: Path, intent_hash: str) -> bool:
        """Checks if the target file matches the current intent hash (Lazy Loading)."""
        try:
            content = target_file.read_text()
            # Extract the Hexagon YAML from the docstring or header
            # This is a simplified check. In reality, we'd parse the YAML.
            if f"intent_hash: {intent_hash}" in content:
                return True
        except Exception:
            pass
        return False

    def _forge_hexagon(
        self, feature_file: Path, intent_hash: str, target_file: Path
    ) -> Hexagon:
        """Forges a new Hexagonal Holon based on the Intent."""

        # Extract title/bluf from feature file (naive parsing)
        content = feature_file.read_text()
        title_match = re.search(r"Feature: (.+)", content)
        title = title_match.group(1) if title_match else feature_file.stem

        bluf_match = re.search(r"\"\"\"(.*?)\"\"\"", content, re.DOTALL)
        bluf = (
            bluf_match.group(1).strip()
            if bluf_match
            else "Auto-generated implementation."
        )

        # Create the Hexagon
        hexagon = Hexagon(
            ontos=Ontos(
                type=HolonType.CODE,
                owner="Genesis.Factory",  # The Swarm Leader for this op
                version="1.0.0",
            ),
            telos=Telos(
                meme=title,
                bluf=bluf,
                viral_factor=0.5,
                intent_hash=intent_hash,
            ),
            chronos=Chronos(status=HolonStatus.ACTIVE, urgency=0.8, decay=0.1),
            topos=Topos(
                address=f"1.X.{target_file.stem}",  # Placeholder address
                location=str(target_file),
            ),
            logos=Logos(
                validators=["hive_guard_v1", "genesis_integrity_check"],
                signature=f"sig_{uuid.uuid4().hex[:8]}",
            ),
            pathos=Pathos(
                sentiment="neutral",
                quality_score=100.0,
                review_status="pending_consensus",  # Adversarial: Needs review
            ),
        )
        return hexagon

    def _write_holon(self, target_file: Path, hexagon: Hexagon, intent_content: str):
        """Writes the Holon to disk with the Hexagonal Header."""

        # Convert Hexagon to YAML Frontmatter style (but inside Python docstring)
        header_dict = hexagon.to_yaml_dict()
        header_yaml = yaml.dump(header_dict, sort_keys=False)

        # Indent YAML for docstring
        header_yaml_indented = "\n".join(
            f"    {line}" for line in header_yaml.splitlines()
        )

        file_content = f"""\"\"\"
{header_yaml_indented}
\"\"\"

# 🛡️ HIVE GUARD: ACTIVE
# ---------------------
# This file is protected by the Hive Fleet Obsidian Immunizer.
# Any manual changes to the header may be overwritten by the Genesis Protocol.
#
# INTENT SOURCE: {hexagon.telos.meme}

def implementation():
    \"\"\"
    Stubs for: {hexagon.telos.bluf}
    \"\"\"
    pass

# End of Holon
"""
        target_file.write_text(file_content)
        console.print(
            "    🔒 [green]Hive Guards Applied. Stigmergy Link Established.[/green]"
        )

    def crystallize(self):
        """Injects the Hexagonal Holon Header into all Markdown files."""
        console.print("[bold cyan]💎 Initiating Great Crystallization...[/bold cyan]")

        # Scan Brain and Body for Markdown files
        targets = list(self.brain_path.rglob("*.md")) + list(
            self.body_path.rglob("*.md")
        )
        console.print(f"Found {len(targets)} potential crystals.")

        for file_path in targets:
            self._process_markdown(file_path)

    def _process_markdown(self, file_path: Path):
        try:
            content = file_path.read_text(encoding="utf-8")

            # Split YAML frontmatter
            if not content.startswith("---"):
                # console.print(f"[dim]  Skipping {file_path.name} (No frontmatter)[/dim]")
                return

            parts = content.split("---", 2)
            if len(parts) < 3:
                return

            yaml_text = parts[1]
            body = parts[2]

            # Parse Face
            try:
                face = yaml.safe_load(yaml_text)
            except yaml.YAMLError:
                console.print(f"[red]❌ Invalid YAML in {file_path.name}[/red]")
                return

            if not isinstance(face, dict):
                return

            if "hexagon" in face:
                # console.print(f"[dim]  ✨ {file_path.name} already crystallized.[/dim]")
                return

            # Generate Hexagon
            hexagon = self._generate_hexagon(face, file_path)

            # Merge and Write
            face["hexagon"] = hexagon

            # Reconstruct File
            new_yaml = yaml.dump(face, sort_keys=False, allow_unicode=True)

            # Add comments for visual separation
            new_yaml = new_yaml.replace(
                "hexagon:",
                "\n# ==================================================================\n# 🤖 THE HEXAGON (System Generated)\n# ==================================================================\nhexagon:",
            )

            new_content = f"---\n{new_yaml}---\n{body}"
            file_path.write_text(new_content, encoding="utf-8")
            console.print(f"[green]  💎 Crystallized: {file_path.name}[/green]")

        except Exception as e:
            console.print(f"[red]  ❌ Error processing {file_path.name}: {e}[/red]")

    def _generate_hexagon(self, face_data: dict, file_path: Path) -> dict:
        """Computes the Hexagon based on the Face and File Context."""

        # 1. ONTOS (Identity)
        ontos = {
            "id": str(uuid.uuid4()),
            "type": "doc",  # Default to doc for markdown
            "owner": "Swarmlord",  # Default owner
        }

        # 2. CHRONOS (Thermodynamics)
        tags = face_data.get("tags", [])
        urgency = 0.1 if "test" in tags else 0.5
        chronos = {
            "status": "active",
            "urgency": urgency,
            "decay": 0.5,
            "created": datetime.datetime.utcnow().isoformat() + "Z",
        }

        # 3. TOPOS (Connectivity)
        # Map directory structure to address
        # brain -> 1, body -> 2, carapace -> 3
        parts = file_path.parts
        address = "0.0.0"
        if "brain" in parts:
            address = "1.0.0"
        elif "body" in parts:
            address = "2.0.0"
        elif "carapace" in parts:
            address = "3.0.0"

        topos = {"address": address, "links": []}

        # 4. TELOS (Purpose)
        # Viral factor based on BLUF length
        bluf_len = len(face_data.get("bluf", ""))
        viral = min(1.0, bluf_len / 100)
        telos = {"viral_factor": viral, "meme": face_data.get("title", "Untitled")}

        return {"ontos": ontos, "chronos": chronos, "topos": topos, "telos": telos}

    def swarm_crystallize(self, target_file: str):
        """Invokes the Header Swarm Workflow via Temporal."""
        console.print(
            f"[bold purple]🦅 Launching Temporal Swarm for {target_file}...[/bold purple]"
        )

        # We need to run this in an async context
        import asyncio
        from temporalio.client import Client
        from body.config import Config
        from body.temporal.header_workflow import HeaderSwarmWorkflow

        async def run_workflow():
            try:
                # Connect to Temporal
                client = await Client.connect(Config.TEMPORAL_ADDRESS)

                # Execute Workflow
                result = await client.execute_workflow(
                    HeaderSwarmWorkflow.run,
                    target_file,
                    id=f"header-swarm-{uuid.uuid4()}",
                    task_queue="header-swarm-queue",
                )
                console.print(f"[green]{result}[/green]")

            except Exception as e:
                console.print(f"[red]❌ Temporal Workflow failed: {e}[/red]")
                console.print(
                    "[yellow]Ensure Temporal server is running and Worker is active.[/yellow]"
                )

        asyncio.run(run_workflow())


def main():
    if len(sys.argv) > 1:
        cmd = sys.argv[1]
        if cmd == "evolve":
            factory = GenesisFactory()
            factory.evolve()
        elif cmd == "crystallize":
            factory = GenesisFactory()
            factory.crystallize()
        elif cmd == "swarm":
            if len(sys.argv) < 3:
                console.print("[red]Usage: python genesis.py swarm <file_path>[/red]")
            else:
                factory = GenesisFactory()
                factory.swarm_crystallize(sys.argv[2])
        elif cmd == "scan":
            scanner = GenesisScanner()
            scanner.scan()
        else:
            console.print(f"[red]Unknown command: {cmd}[/red]")
            console.print("Usage: python genesis.py [scan|evolve|crystallize]")
    else:
        scanner = GenesisScanner()
        scanner.scan()

        # Optional: Run smoke tests if requested
        if "--venom" in sys.argv:
            console.print("\n[bold blue]🧪 Venom Protocol[/bold blue]")
            console.print("[bold]🚀 Injecting Venom...[/bold]")
            subprocess.run(["make", "test-all"])


if __name__ == "__main__":
    main()
