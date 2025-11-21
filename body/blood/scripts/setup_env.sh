#!/bin/bash
echo "Setting up Hive Fleet Obsidian (Gen 50) Environment..."

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

echo "Environment setup complete."
echo "Activate with: source venv/bin/activate"
