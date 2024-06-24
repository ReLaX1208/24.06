#!/bin/bash

# Set the virtual environment name
VENV_NAME="myenv"

# Create a new virtual environment using Python 3
python3 -m venv "$VENV_NAME"

# Activate the virtual environment
source "$VENV_NAME/bin/activate"

# Upgrade pip to the latest version
pip install --upgrade pip

# Install some basic packages (optional)
pip install wheel setuptools

# Deactivate the virtual environment
deactivate
