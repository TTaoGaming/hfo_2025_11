#!/bin/bash
# 🦅 Hive Fleet Obsidian: Hybrid Setup Script
# Launches Infrastructure (Docker) and sets up Agent Environment (Local)

echo "🦅 Initiating Phoenix Protocol (Hybrid Setup)..."

# 1. Launch Infrastructure
echo "🏗️  Launching Infrastructure (NATS, Postgres, Temporal)..."
docker-compose up -d

echo "⏳ Waiting for services to stabilize..."
sleep 5

# 2. Setup Python Environment
if [ ! -d "venv" ]; then
    echo "🐍 Creating Virtual Environment..."
    python3 -m venv venv
fi

echo "📦 Installing Dependencies..."
source venv/bin/activate
pip install -r requirements.txt

# 3. Create .env if missing
if [ ! -f ".env" ]; then
    echo "📝 Creating .env from template..."
    echo "NATS_URL=nats://localhost:4225" >> .env
    echo "DATABASE_URL=postgresql://hfo:hfo_password@localhost:5435/hfo_memory" >> .env
    echo "TEMPORAL_URL=localhost:7235" >> .env
    echo "# OPENROUTER_API_KEY=sk-..." >> .env
    echo "⚠️  Please update .env with your OPENROUTER_API_KEY"
fi

echo "✅ Hybrid Environment Ready."
echo "   - NATS: nats://localhost:4225"
echo "   - Postgres: localhost:5435"
echo "   - Temporal: localhost:7235"
echo ""
echo "👉 Run 'source venv/bin/activate' to enter the hive."
