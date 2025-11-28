#!/bin/bash
# HFO Heartbeat 24/7 Runner
# Restarts the Octarchy Swarm if it crashes.

LOG_FILE="audit_trail/logs/heartbeat_247.log"
mkdir -p audit_trail/logs

echo "💓 HFO Heartbeat 24/7 Service Starting..." | tee -a "$LOG_FILE"
echo "   Mode: Hexadex Chant (16 Verses)" | tee -a "$LOG_FILE"
echo "   Agents: 8 (Octarchy)" | tee -a "$LOG_FILE"

while true; do
    echo "🚀 [$(date)] Launching Swarm..." | tee -a "$LOG_FILE"

    # Run the heartbeat
    make heartbeat-247 >> "$LOG_FILE" 2>&1

    EXIT_CODE=$?
    echo "⚠️ [$(date)] Swarm exited with code $EXIT_CODE. Restarting in 5 seconds..." | tee -a "$LOG_FILE"
    sleep 5
done
