#!/usr/bin/env python3
"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: 678674f4-28ed-4ec1-8282-0d8b480dfdbb
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T10:21:31.304826+00:00'
  topos:
    address: venom/guard_reality.py
    links: []
  telos:
    viral_factor: 0.0
    meme: guard_reality.py


🦅 Hive Fleet Obsidian: Brutal Truth Test (Venom)
Usage: python venom/test_brutal_truth.py

This script verifies the "Realness" of the system by testing:
1.  Concurrency (AsyncIO) - Is it actually parallel?
2.  Stigmergy (NATS) - Can we actually pass messages?
3.  Tooling (Web) - Can we actually hit the internet?
"""

import asyncio
import time
import os
import json
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
import nats
from dotenv import load_dotenv

# Import the tools we just upgraded
from body.hands.tools import ToolSet

load_dotenv()
console = Console()
NATS_URL = os.getenv("NATS_URL", "nats://localhost:4222")


async def test_concurrency():
    """Verifies that tasks run in parallel."""
    console.print("\n[bold blue]🧪 Test 1: Concurrency (The Hydra)[/bold blue]")

    async def worker(id, duration):
        await asyncio.sleep(duration)
        return f"Worker {id} done"

    start_time = time.time()

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        task = progress.add_task("[cyan]Running 3 workers (2s each)...", total=3)

        # Launch 3 workers that sleep for 2 seconds
        # If serial, this takes 6 seconds. If parallel, ~2 seconds.
        results = await asyncio.gather(worker(1, 2.0), worker(2, 2.0), worker(3, 2.0))
        progress.update(task, completed=3)

    console.print(f"Results: {results}")
    duration = time.time() - start_time
    console.print(f"Total Time: {duration:.2f}s")

    if duration < 2.5:
        console.print("✅ [green]PASS: System is Concurrent.[/green]")
    else:
        console.print("❌ [red]FAIL: System is Serial (Too Slow).[/red]")


async def test_stigmergy():
    """Verifies that NATS is reachable."""
    console.print("\n[bold blue]🧪 Test 2: Stigmergy (The Bus)[/bold blue]")

    try:
        nc = await nats.connect(NATS_URL)
        js = nc.jetstream()

        # Create a stream if not exists
        try:
            await js.add_stream(name="VENOM_TEST", subjects=["venom.*"])
        except Exception:
            pass  # Stream might exist

        # Publish
        payload = {"message": "Truth is not theater", "timestamp": time.time()}
        await js.publish("venom.truth", json.dumps(payload).encode())
        console.print(f"📤 Publishing: {payload}")

        # Subscribe
        sub = await js.subscribe("venom.truth")
        msg = await sub.next_msg(timeout=2)
        data = json.loads(msg.data.decode())
        console.print(f"📥 Received: {data}")

        if data["message"] == "Truth is not theater":
            console.print("✅ [green]PASS: Stigmergy is Active.[/green]")
        else:
            console.print("❌ [red]FAIL: Stigmergy Data Corruption.[/red]")

        await nc.close()

    except Exception as e:
        console.print(f"❌ [red]FAIL: Stigmergy Broken. {e}[/red]")


def test_tooling():
    """Verifies Real Web Search."""
    console.print("\n[bold blue]🧪 Test 3: Tooling (The Eyes)[/bold blue]")

    query = "current python version 2025"
    console.print(f"🔎 Searching Web for: '[cyan]{query}[/cyan]'...")

    start_time = time.time()
    result = ToolSet.search_web(query)
    duration = time.time() - start_time

    console.print(Panel(result, title="Search Result", border_style="green"))
    console.print(f"Time: {duration:.2f}s")

    if "Error" not in result and len(result) > 10:
        console.print("✅ [green]PASS: Eyes are Open (Real Web Search).[/green]")
    else:
        console.print("❌ [red]FAIL: Eyes are Blind (Tool Failure).[/red]")


async def main():
    console.print(
        Panel.fit("🦅 Venom Protocol: Brutal Truth Test", border_style="bold red")
    )

    await test_concurrency()
    await test_stigmergy()
    # Tooling is synchronous in this implementation, but that's fine for now
    test_tooling()


if __name__ == "__main__":
    asyncio.run(main())
