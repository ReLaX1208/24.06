#!/bin/bash

# Set the project directory
PROJECT_DIR="myproject"

# Set the virtual environment name
VENV_NAME="myenv"

# Activate the virtual environment
source "$VENV_NAME/bin/activate"

# Change into the project directory
cd "$PROJECT_DIR"

# Run the main script (assuming it's a Python script)
python src/main.py

# Deactivate the virtual environment
deactivate
