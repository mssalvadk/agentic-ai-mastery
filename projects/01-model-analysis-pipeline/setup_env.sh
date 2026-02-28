#!/bin/bash

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

echo "🚀 Starting Environment Setup in: $SCRIPT_DIR"

# 1. Create Virtual Environment
python -m venv venv
echo "✅ Virtual environment created."

# 2. Activate Environment
source venv/Scripts/activate
echo "✅ Virtual environment activated."

# 3. Upgrade Pip (The Windows-safe way)
python -m pip install --upgrade pip

# 4. Install Dependencies
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
    echo "✅ Dependencies installed successfully."
else
    echo "❌ requirements.txt not found in $SCRIPT_DIR!"
    exit 1
fi

# 5. Handle .env
if [ ! -f ".env" ]; then
    if [ -f ".env.example" ]; then
        cp .env.example .env
        echo "⚠️ Created .env from template."
    fi
fi

echo "🎉 Setup Complete!"