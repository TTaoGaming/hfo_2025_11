import re

log_file = "audit_trail/logs/heartbeat_247.log"

total_checks = 0
total_consensus = 0
start_time = None
end_time = None

print("📊 HFO Heartbeat Analysis (Last Session)")
print("-" * 40)

try:
    with open(log_file, "r") as f:
        for line in f:
            # Extract timestamp
            match = re.search(r"(\d{2}:\d{2}:\d{2})", line)
            if match:
                ts_str = match.group(1)
                if not start_time:
                    start_time = ts_str
                end_time = ts_str

            # Extract Consensus
            match = re.search(r"Consensus: (\d+)", line)
            if match:
                consensus = int(match.group(1))
                total_checks += 1
                total_consensus += consensus
                # print(f"[{ts_str}] Consensus: {consensus}/8")

    if total_checks > 0:
        avg_consensus = total_consensus / total_checks
        percentage = (avg_consensus / 8) * 100
        print(f"⏱️  Time Range: {start_time} - {end_time}")
        print(f"💓 Total Heartbeats: {total_checks}")
        print(f"📈 Average Consensus: {avg_consensus:.2f}/8")
        print(f"✅ System Health: {percentage:.1f}%")
    else:
        print("⚠️ No consensus data found in logs yet.")

except FileNotFoundError:
    print("❌ Log file not found.")
