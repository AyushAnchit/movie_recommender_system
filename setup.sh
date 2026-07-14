#!/bin/bash

# Exit on any error
set -e

echo "Setting up Movie Recommender System..."

# 1. Create Streamlit configuration directory and file
mkdir -p ~/.streamlit/

echo "[server]
headless = true
port = \${PORT:-8501}
enableCORS = false
" > ~/.streamlit/config.toml

echo "Streamlit configuration created in ~/.streamlit/config.toml."

# 2. Local environment setup
if [ -f "requirements.txt" ]; then
    echo "Setting up local Python virtual environment..."
    if [ ! -d ".venv" ]; then
        echo "Creating virtual environment .venv..."
        python3 -m venv .venv
    fi
    
    echo "Activating virtual environment..."
    source .venv/bin/activate
    
    echo "Installing required Python dependencies..."
    pip install --upgrade pip
    pip install -r requirements.txt
    
    echo "--------------------------------------------------"
    echo "Setup completed successfully!"
    echo "To run the application locally, run:"
    echo "  source .venv/bin/activate"
    echo "  streamlit run app.py"
    echo "--------------------------------------------------"
else
    echo "Warning: requirements.txt not found. Skipping dependency installation."
fi
