import asyncio
import os
import json
import curses
import nats
from datetime import datetime

# --- Configuration ---
NATS_URL = os.getenv("NATS_URL", "nats://localhost:4225")


async def main(stdscr):
    # Setup Curses
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)

    # Connect to NATS
    try:
        nc = await nats.connect(NATS_URL)
    except Exception as e:
        stdscr.addstr(0, 0, f"Error connecting to NATS: {e}")
        stdscr.refresh()
        await asyncio.sleep(5)
        return

    # State
    agents = {}
    logs = []

    async def handler(msg):
        try:
            data = json.loads(msg.data.decode())
            agent_id = data.get("agent_id")
            agents[agent_id] = {
                "phase": data.get("phase"),
                "timestamp": datetime.now().strftime("%H:%M:%S"),
                "quorum": data.get("quorum_status", "Unknown"),
                "content": data.get("content", "")[:50],
            }
            logs.append(
                f"[{datetime.now().strftime('%H:%M:%S')}] {agent_id}: {data.get('phase')}"
            )
            if len(logs) > 10:
                logs.pop(0)
        except:
            pass

    await nc.subscribe("hfo.heartbeat.>", cb=handler)

    # UI Loop
    while True:
        stdscr.clear()

        # Header
        stdscr.addstr(0, 0, "🦅 HFO OCTARCHY SWARM MONITOR (Live)", curses.A_BOLD)
        stdscr.addstr(1, 0, "=" * 60)

        # Agent Table
        row = 3
        stdscr.addstr(
            row, 0, f"{'AGENT ID':<15} {'PHASE':<10} {'QUORUM':<15} {'LAST SEEN':<10}"
        )
        row += 1
        stdscr.addstr(row, 0, "-" * 60)
        row += 1

        sorted_agents = sorted(
            agents.keys(), key=lambda x: int(x.split("_")[1]) if "_" in x else 0
        )

        for agent_id in sorted_agents:
            info = agents[agent_id]
            phase = info["phase"]
            quorum = info["quorum"]

            # Color coding
            attr = curses.A_NORMAL
            if phase == "Execute":
                attr = curses.A_BOLD
            if quorum == "QUORUM_REACHED":
                attr = attr | curses.A_UNDERLINE

            stdscr.addstr(
                row,
                0,
                f"{agent_id:<15} {phase:<10} {quorum:<15} {info['timestamp']:<10}",
                attr,
            )
            row += 1

        # Logs
        row += 2
        stdscr.addstr(row, 0, "Recent Activity:")
        row += 1
        for log in logs:
            stdscr.addstr(row, 0, log, curses.A_DIM)
            row += 1

        stdscr.refresh()

        # Exit check
        c = stdscr.getch()
        if c == ord("q"):
            break

        await asyncio.sleep(0.1)


if __name__ == "__main__":
    try:
        curses.wrapper(lambda stdscr: asyncio.run(main(stdscr)))
    except KeyboardInterrupt:
        pass
