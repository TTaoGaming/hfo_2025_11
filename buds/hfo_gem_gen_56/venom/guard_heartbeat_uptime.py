import os
import re
from datetime import datetime, timedelta

# Adjust path to find the log file in the root
# This script is in venom/, so root is ../
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
LOG_FILE = os.path.join(ROOT_DIR, "hfo_heartbeat_247.log")
MAX_GAP_SECONDS = 120  # 2 minutes gap allowed


def calculate_uptime() -> float:
    if not os.path.exists(LOG_FILE):
        return 0.00

    now = datetime.now()
    window_start = now - timedelta(hours=24)

    timestamps = []

    # Regex to match: 2025-11-27 04:38:57,781
    pattern = re.compile(r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})")

    try:
        with open(LOG_FILE, "r") as f:
            for line in f:
                match = pattern.match(line)
                if match:
                    ts_str = match.group(1)
                    try:
                        ts = datetime.strptime(ts_str, "%Y-%m-%d %H:%M:%S")
                        if ts >= window_start:
                            timestamps.append(ts)
                    except ValueError:
                        continue
    except Exception:
        # print(f"Error reading log: {e}", file=sys.stderr)
        return 0.00

    if not timestamps:
        return 0.00

    timestamps.sort()

    uptime_seconds = 0.0

    # Iterate and sum up gaps < MAX_GAP
    for i in range(1, len(timestamps)):
        gap = (timestamps[i] - timestamps[i - 1]).total_seconds()
        if gap <= MAX_GAP_SECONDS:
            uptime_seconds += gap

    # Add the last segment if it's recent (system is currently up)
    last_gap = (now - timestamps[-1]).total_seconds()
    if last_gap <= MAX_GAP_SECONDS:
        uptime_seconds += last_gap

    percent = (uptime_seconds / (24 * 3600)) * 100
    # Cap at 100.00
    if percent > 100.0:
        percent = 100.0

    return percent


if __name__ == "__main__":
    print(f"{calculate_uptime():.2f}")
