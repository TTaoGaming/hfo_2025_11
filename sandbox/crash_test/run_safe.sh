#!/bin/bash

# 🛡️ BLAST SHIELD PROTOCOL
# Runs the AI Swarm in a memory-constrained Docker container.

MEMORY=${1:-"1g"}
CPUS=${2:-"2.0"}

# 1. Build the Crash Dummy
echo "👷 Building Crash Test Dummy..."
docker build -t hfo-crash-dummy -f sandbox/crash_test/Dockerfile .

# 2. Run with Safety Limits
echo "🚀 Launching Swarm in Blast Shield (Limit: $MEMORY RAM, $CPUS CPUs)..."
docker run --rm -it \
    --name hfo-experiment \
    --memory="$MEMORY" \
    --cpus="$CPUS" \
    --network="host" \
    -v $(pwd)/memory:/app/memory \
    hfo-crash-dummy \
    python sandbox/crash_test/evaluate_models.py

echo "✅ Experiment Complete. If it crashed, it was contained."
