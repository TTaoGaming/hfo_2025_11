#!/usr/bin/env python3
"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: d59653df-28b3-4490-96ba-24025d0d2542
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-24T14:28:48.579410Z'
    generation: 51
  topos:
    address: hfo.py
    links: []
  telos:
    viral_factor: 0.0
    meme: hfo.py

# ==================================================================
# 🦅 HIVE FLEET OBSIDIAN: SINGULAR ON-RAMP (Gen 52)
# ==================================================================
hexagon:
  ontos:
    id: hfo-cli-gen52
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 1.0
    decay: 0.0
    created: '2025-11-23T12:00:00+00:00'
    generation: 52
  topos:
    address: hfo.py
    links: []
  telos:
    viral_factor: 1.0
    meme: The Singular On-Ramp
"""

import argparse
import asyncio
import hashlib
import json
import shutil
import sys
import uuid
from datetime import datetime
from pathlib import Path

import psycopg2
from rich.console import Console
from rich.panel import Panel
from rich.progress import track

# Ensure we can import from body
sys.path.append(str(Path(__file__).parent))
from body.hands.research_swarm import run_swarm  # noqa: E402
from body.hands.prey_agent import PreyAgent, AgentRole  # noqa: E402

# Initialize Rich Console
console = Console()

# Configuration
DB_CONFIG = {
    "dbname": "hfo_unified_memory",
    "user": "hfo_admin",
    "password": "phoenix_password",
    "host": "localhost",
    "port": "5435",
}
ARCHIVE_ROOT = Path("memory/episodic")
BRAIN_ROOT = Path("brain")


def get_db_connection():
    """Connect to the HFO Memory (Postgres)."""
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        return conn
    except Exception as e:
        console.print(f"[bold red]❌ Database Connection Failed:[/bold red] {e}")
        return None


def init_db(conn):
    """Initialize the brain_snapshots table."""
    with conn.cursor() as cur:
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS brain_snapshots (
                id UUID PRIMARY KEY,
                generation INTEGER,
                filepath TEXT,
                content TEXT,
                hash TEXT,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """
        )
        conn.commit()


def calculate_hash(content):
    """Calculate SHA-256 hash of content."""
    return hashlib.sha256(content.encode("utf-8")).hexdigest()


def archive_brain(generation: int):
    """Archive the current brain state to Filesystem and Database."""
    console.print(
        Panel(
            f"🦅 [bold cyan]Archiving Brain - Generation {generation}[/bold cyan]",
            expand=False,
        )
    )

    # 1. Filesystem Archive
    archive_dir = ARCHIVE_ROOT / f"gen_{generation}_archive" / "brain"
    if archive_dir.exists():
        console.print(
            f"[yellow]⚠️  Archive directory {archive_dir} already exists. Overwriting...[/yellow]"
        )
        shutil.rmtree(archive_dir.parent)

    archive_dir.mkdir(parents=True, exist_ok=True)

    # Copy files
    files_to_archive = list(BRAIN_ROOT.glob("**/*"))
    files_to_archive = [f for f in files_to_archive if f.is_file()]

    console.print(f"📂 Found {len(files_to_archive)} files in {BRAIN_ROOT}")

    # 2. Database Archive
    conn = get_db_connection()
    if conn:
        init_db(conn)
    else:
        console.print(
            "[yellow]⚠️  Proceeding with Filesystem Archive only (DB unavailable)[/yellow]"
        )

    # Process Files
    archived_count = 0

    for file_path in track(files_to_archive, description="Archiving..."):
        # Read Content
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
        except UnicodeDecodeError:
            console.print(f"[red]❌ Skipping binary file: {file_path}[/red]")
            continue

        # 1. Copy to Filesystem
        rel_path = file_path.relative_to(BRAIN_ROOT)
        dest_path = archive_dir / rel_path
        dest_path.parent.mkdir(parents=True, exist_ok=True)
        with open(dest_path, "w", encoding="utf-8") as f:
            f.write(content)

        # 2. Write to DB
        if conn:
            file_hash = calculate_hash(content)
            try:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        INSERT INTO brain_snapshots (id, generation, filepath, content, hash, timestamp)
                        VALUES (%s, %s, %s, %s, %s, %s)
                        """,
                        (
                            str(uuid.uuid4()),
                            generation,
                            str(rel_path),
                            content,
                            file_hash,
                            datetime.now(),
                        ),
                    )
                conn.commit()
            except Exception as e:
                console.print(f"[red]❌ DB Insert Failed for {rel_path}: {e}[/red]")

        archived_count += 1

    if conn:
        conn.close()

    # 3. JSON Dump (Fallback/Portable Archive)
    manifest_path = archive_dir.parent / "brain_manifest.json"
    console.print(f"[yellow]📦 Generating Portable Manifest: {manifest_path}[/yellow]")

    manifest_data = []
    for file_path in files_to_archive:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                rel_path = str(file_path.relative_to(BRAIN_ROOT))
                manifest_data.append(
                    {
                        "id": str(uuid.uuid4()),
                        "generation": generation,
                        "filepath": rel_path,
                        "content": content,
                        "hash": calculate_hash(content),
                        "timestamp": datetime.now().isoformat(),
                    }
                )
        except Exception:
            continue  # Skip binary/error files

    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest_data, f, indent=2)

    console.print(
        f"✅ [bold green]Archive Complete![/bold green] {archived_count} files archived to {archive_dir.parent}"
    )
    if conn:
        console.print("✅ [bold green]Database Snapshot Secured.[/bold green]")
    else:
        console.print(
            "✅ [bold green]Database Snapshot Failed (Saved as JSON Manifest).[/bold green]"
        )


async def run_prey_task(task: str):
    """Run a single Prey Agent."""
    console.print(
        Panel(
            f"🦅 [bold green]Launching Prey Agent[/bold green]\nTask: {task}",
            expand=False,
        )
    )
    agent = PreyAgent(f"prey-{uuid.uuid4().hex[:8]}", AgentRole.OBSERVER)
    try:
        result = await agent.run(task)
        console.print(
            Panel(
                f"[bold]Final Result:[/bold]\n{result.get('final_output', 'No output')}",
                title="Mission Complete",
            )
        )
    finally:
        await agent.close()


def main():
    parser = argparse.ArgumentParser(
        description="Hive Fleet Obsidian: Singular On-Ramp"
    )
    subparsers = parser.add_subparsers(dest="command", help="Command to execute")

    # Archive Command
    archive_parser = subparsers.add_parser(
        "archive", help="Archive the current brain state"
    )
    archive_parser.add_argument(
        "--gen", type=int, required=True, help="Generation number (e.g., 51)"
    )

    # Swarm Command
    swarm_parser = subparsers.add_parser("swarm", help="Launch a Swarm Mission")
    swarm_parser.add_argument(
        "--mission", type=str, required=True, help="Mission description"
    )

    # Prey Command
    prey_parser = subparsers.add_parser("prey", help="Launch a Prey Agent")
    prey_parser.add_argument("--task", type=str, required=True, help="Task description")

    args = parser.parse_args()

    if args.command == "archive":
        archive_brain(args.gen)
    elif args.command == "swarm":
        asyncio.run(run_swarm(args.mission))
    elif args.command == "prey":
        asyncio.run(run_prey_task(args.task))
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
