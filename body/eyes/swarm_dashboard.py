"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: 36d47c2f-67b7-48fb-a15e-db81c404658e
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T10:21:31.447672+00:00'
  topos:
    address: body/eyes/swarm_dashboard.py
    links: []
  telos:
    viral_factor: 0.0
    meme: swarm_dashboard.py
"""

import asyncio
import json
from datetime import datetime
from typing import Dict, List

from dotenv import load_dotenv
from rich.console import Console
from rich.layout import Layout
from rich.live import Live
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

import nats
from body.config import Config

# Setup
load_dotenv()
console = Console()

# Configuration
NATS_URL = Config.NATS_URL
SUBJECT_WILDCARD = "hfo.mission.>"


class SwarmDashboard:
    def __init__(self):
        self.agents: Dict[str, Dict] = {}
        self.logs: List[str] = []
        self.nc = None
        self.js = None

    async def connect(self):
        try:
            self.nc = await nats.connect(NATS_URL)
            self.js = self.nc.jetstream()

            # Subscribe to all mission events
            await self.nc.subscribe(SUBJECT_WILDCARD, cb=self.on_message)
            self.log("✅ Connected to NATS Stigmergy Layer")
        except Exception as e:
            self.log(f"❌ Connection Failed: {e}")

    async def on_message(self, msg):
        try:
            subject = msg.subject
            data = json.loads(msg.data.decode())

            # Parse Subject: hfo.mission.<agent_id>.<type>
            parts = subject.split(".")
            if len(parts) >= 4:
                agent_id = parts[2]
                msg_type = parts[3]  # yield, heartbeat, etc.

                if agent_id not in self.agents:
                    self.agents[agent_id] = {
                        "status": "Active",
                        "last_seen": datetime.now(),
                        "role": "Unknown",
                    }

                self.agents[agent_id]["last_seen"] = datetime.now()

                if msg_type == "yield":
                    self.agents[agent_id]["status"] = "Yielded"
                    self.agents[agent_id]["confidence"] = data.get("confidence", 0.0)
                    self.agents[agent_id]["strategy"] = data.get("strategy", "Unknown")
                    self.log(
                        f"📥 {agent_id} yielded with {data.get('confidence', 0.0):.2f} confidence"
                    )

        except Exception:
            pass

    def log(self, message: str):
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.logs.append(f"[{timestamp}] {message}")
        if len(self.logs) > 20:
            self.logs.pop(0)

    def generate_layout(self) -> Layout:
        layout = Layout()
        layout.split_column(
            Layout(name="header", size=3),
            Layout(name="main", ratio=1),
            Layout(name="footer", size=3),
        )
        layout["main"].split_row(
            Layout(name="agents", ratio=2), Layout(name="logs", ratio=1)
        )
        return layout

    def generate_agent_table(self) -> Table:
        table = Table(title="🦅 Active Agents", expand=True)
        table.add_column("Agent ID", style="cyan")
        table.add_column("Status", style="magenta")
        table.add_column("Strategy", style="green")
        table.add_column("Confidence", justify="right")
        table.add_column("Last Seen", justify="right")

        for agent_id, info in self.agents.items():
            last_seen = info["last_seen"].strftime("%H:%M:%S")
            table.add_row(
                agent_id,
                info["status"],
                info.get("strategy", "-"),
                f"{info.get('confidence', 0.0):.2f}",
                last_seen,
            )
        return table

    def generate_log_panel(self) -> Panel:
        text = Text("\n".join(self.logs))
        return Panel(text, title="📜 Stigmergy Logs", border_style="blue")

    def generate_header(self) -> Panel:
        return Panel(
            "🦅 Hive Fleet Obsidian: Swarm Dashboard (NATS)", style="bold white on blue"
        )

    async def run(self):
        await self.connect()

        layout = self.generate_layout()
        layout["header"].update(self.generate_header())

        with Live(layout, refresh_per_second=4, screen=True):
            while True:
                layout["agents"].update(self.generate_agent_table())
                layout["logs"].update(self.generate_log_panel())
                await asyncio.sleep(0.25)


if __name__ == "__main__":
    dashboard = SwarmDashboard()
    try:
        asyncio.run(dashboard.run())
    except KeyboardInterrupt:
        print("Dashboard closed.")
