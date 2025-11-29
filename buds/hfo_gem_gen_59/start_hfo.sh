#!/bin/bash
# HFO Gen 59 Startup Script
# Launches Heartbeat, Assimilator, and Scanner in daemon mode.

# 1. Start NATS (if not running)
# Assuming NATS is running via docker-compose or locally.
# If not, we might need to start it.
# ./setup_hybrid.sh starts it.

# 2. Start Heartbeat
echo "💓 Starting Heartbeat..."
python3 -m buds.hfo_gem_gen_59.nerves.heartbeat > hfo_heartbeat.log 2>&1 &
HEARTBEAT_PID=$!

# 3. Start Assimilator (Daemon)
echo "🧠 Starting Assimilator (Daemon)..."
python3 -m buds.hfo_gem_gen_59.brain.assimilator --daemon > hfo_assimilator.log 2>&1 &
ASSIMILATOR_PID=$!

# 4. Start Ingest Scanner (Daemon)
echo "👀 Starting Ingest Scanner (Daemon)..."
python3 -m buds.hfo_gem_gen_59.brain.ingest_scanner --target buds/hfo_gem_gen_59 --daemon > hfo_scanner.log 2>&1 &
SCANNER_PID=$!

# 5. Start Hydra Swarm (Async Agent)
echo "🐉 Starting Hydra Swarm (Async Agent)..."
python3 -m buds.hfo_gem_gen_59.hydra.hydra_swarm > hfo_hydra.log 2>&1 &
HYDRA_PID=$!

echo "✅ HFO Gen 59 Active."
echo "PIDs: Heartbeat=$HEARTBEAT_PID, Assimilator=$ASSIMILATOR_PID, Scanner=$SCANNER_PID, Hydra=$HYDRA_PID"
echo "Press Ctrl+C to stop all."

trap "kill $HEARTBEAT_PID $ASSIMILATOR_PID $SCANNER_PID $HYDRA_PID; exit" SIGINT SIGTERM

wait
