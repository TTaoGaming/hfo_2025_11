"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: c3a5c4c0-9680-4d5c-90b6-5386e5f22aa5
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T10:21:31.307097+00:00'
  topos:
    address: venom/guard_stigmergy.py
    links: []
  telos:
    viral_factor: 0.0
    meme: guard_stigmergy.py
"""

import asyncio
import os
import yaml
import json
import nats
from rich.console import Console
from rich.table import Table

console = Console()


async def guard_stigmergy():
    console.print("[bold blue]🛡️  Hive Guard: Stigmergy Verification[/bold blue]")

    nats_url = os.getenv("NATS_URL", "nats://localhost:4225")
    try:
        nc = await nats.connect(nats_url)
        console.print(f"[green]✅ Connected to NATS at {nats_url}[/green]")
    except Exception as e:
        console.print(f"[red]❌ Failed to connect to NATS: {e}[/red]")
        return

    received_signals = []

    async def message_handler(msg):
        subject = msg.subject
        data = json.loads(msg.data.decode())
        console.print(f"[cyan]📡 Signal Detected:[/cyan] {subject}")
        received_signals.append(data)

    # Subscribe to all swarm artifact events
    sub = await nc.subscribe("swarm.artifact.>", cb=message_handler)
    console.print("[yellow]👀 Listening for Swarm Pheromones (10s)...[/yellow]")

    # Wait for signals (The swarm is running in background)
    await asyncio.sleep(10)

    await sub.unsubscribe()
    await nc.close()

    if not received_signals:
        console.print("[red]⚠️  No signals detected in 10s. Is the swarm active?[/red]")
    else:
        console.print(f"[green]✅ Captured {len(received_signals)} signals.[/green]")

        # Verify Static Layer (Files)
        table = Table(title="Stigmergy Artifact Verification")
        table.add_column("Role", style="cyan")
        table.add_column("File Exists", style="green")
        table.add_column("YAML Header", style="magenta")
        table.add_column("Path", style="dim")

        for sig in received_signals:
            path = sig.get("path")
            role = sig.get("role")

            exists = os.path.exists(path)
            has_yaml = False

            if exists:
                try:
                    with open(path, "r") as f:
                        content = f.read()
                        if content.startswith("---"):
                            # Basic check for YAML frontmatter
                            try:
                                _, frontmatter, _ = content.split("---", 2)
                                yaml.safe_load(frontmatter)
                                has_yaml = True
                            except Exception:
                                pass
                except Exception:
                    pass

            table.add_row(
                role,
                "✅" if exists else "❌",
                "✅" if has_yaml else "❌",
                os.path.basename(path),
            )

        console.print(table)


if __name__ == "__main__":
    asyncio.run(guard_stigmergy())
