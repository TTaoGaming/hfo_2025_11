#!/bin/bash
# 🕸⛰🔔 HFO CHANT SYSTEM LAUNCHER
# Runs the Octarchy Swarm and the Assimilator

# Ensure we are in the root directory
cd "$(dirname "$0")/.."

# Activate venv if it exists
if [ -d "venv" ]; then
    source venv/bin/activate
fi

echo "🚀 Starting HFO Chant System..."

# 1. Start Assimilator (The Listener)
echo "👂 Launching Assimilator..."
nohup python3 body/digestion/chant_assimilator.py > audit_trail/logs/assimilator.log 2>&1 &
ASSIMILATOR_PID=$!
echo "   PID: $ASSIMILATOR_PID"

# 2. Start Swarm (The Chanters)
echo "🕸 Launching Octarchy Swarm (8 Agents)..."
nohup python3 body/hands/chant_swarm.py > audit_trail/logs/swarm.log 2>&1 &
SWARM_PID=$!
echo "   PID: $SWARM_PID"

echo "✅ System Online."
echo "   Logs: audit_trail/logs/assimilator.log"
echo "   Logs: audit_trail/logs/swarm.log"
echo "   Report: audit_trail/logs/chant_report.log"

# Monitor PIDs
wait $ASSIMILATOR_PID $SWARM_PID
