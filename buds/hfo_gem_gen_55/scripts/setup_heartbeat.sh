#!/bin/bash
# HFO Heartbeat Setup Script
# Installs Ollama and pulls Gemma 3 4B

echo "🦅 HFO Heartbeat Setup: Initializing..."

# 1. Install Ollama (if not present)
if ! command -v ollama &> /dev/null; then
    echo "Installing Ollama..."
    curl -fsSL https://ollama.com/install.sh | sh
else
    echo "Ollama is already installed."
fi

# 2. Start Ollama Service (Background)
# On Chromebook/Linux, it might be a systemd service, but let's ensure it's running.
if ! pgrep -x "ollama" > /dev/null; then
    echo "Starting Ollama server..."
    ollama serve &
    sleep 5 # Wait for startup
fi

# 3. Pull Gemma 3 4B
echo "Pulling Gemma 3 4B model..."
ollama pull gemma3:4b

# 4. Verify
echo "Verifying installation..."
ollama list | grep gemma3

echo "✅ Heartbeat Setup Complete. Run 'ollama run gemma3:4b' to test."
