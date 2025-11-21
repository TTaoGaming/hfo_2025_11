#!/bin/bash
echo "🦅 Setting up HFO Hybrid Stability Environment..."

# 1. Check for Python 3.10+
python3 --version

# 2. Create Virtual Environment if not exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# 3. Activate and Install
source venv/bin/activate
echo "Installing dependencies..."
pip install -r requirements.txt

# 4. Launch Infrastructure
echo "Launching Infrastructure (Docker)..."
# We use the compose file from .devcontainer but only launch the backing services
# Try 'docker compose' first (v2), fallback to 'docker-compose' (v1)
if docker compose version >/dev/null 2>&1; then
    docker compose -f .devcontainer/docker-compose.yml up -d db temporal nats
else
    docker-compose -f .devcontainer/docker-compose.yml up -d db temporal nats
fi

echo "---------------------------------------------------"
echo "✅ Setup Complete!"
echo "1. Activate env: source venv/bin/activate"
echo "2. Run Smoke Test: python src/smoke_test.py"
echo "---------------------------------------------------"
