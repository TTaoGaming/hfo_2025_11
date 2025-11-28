"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: 550e8400-e29b-41d4-a716-446655440011
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-26T12:00:00.000000Z'
    generation: 51
  topos:
    address: venom/guard_heartbeat.py
    links: []
  telos:
    viral_factor: 0.0
    meme: guard_heartbeat.py
"""

import time
import signal
import sys
from datetime import datetime

HEARTBEAT_INTERVAL = 5  # seconds
MAX_MISSED_HEARTBEATS = 3


def send_heartbeat():
    """Send a heartbeat signal."""
    print(f"Heartbeat sent at {datetime.now()}")


def handle_timeout(signum, frame):
    """Handle the timeout signal."""
    print(
        f"Timeout! No heartbeat received for {HEARTBEAT_INTERVAL * MAX_MISSED_HEARTBEATS} seconds."
    )
    sys.exit(1)


# Set the signal handler for SIGALRM
signal.signal(signal.SIGALRM, handle_timeout)

# Main loop
if __name__ == "__main__":
    print("Guard heartbeat started.")
    while True:
        # Reset the alarm
        signal.alarm(HEARTBEAT_INTERVAL * MAX_MISSED_HEARTBEATS)

        # Send a heartbeat
        send_heartbeat()

        # Wait for the next interval
        time.sleep(HEARTBEAT_INTERVAL)
