#!/bin/bash

# Set the project name
PROJECT_NAME="myproject"

# Create a new directory for the project
mkdir "$PROJECT_NAME"
cd "$PROJECT_NAME"

# Initialize a new Git repository
git init

# Create a basic directory structure
mkdir src
mkdir tests
mkdir docs
mkdir data

# Create a README file
touch README.md

# Create a basic `.gitignore` file
echo "# Ignore files" > .gitignore
echo "*.pyc" >> .gitignore
echo "__pycache__/" >> .gitignore
echo "venv/" >> .gitignore

# Create a basic `main.py` file
touch src/main.py
echo "#!/usr/bin/env python" >> src/main.py
echo "" >> src/main.py
echo "print('Hello, World!')" >> src/main.py

# Make the `main.py` file executable
chmod +x src/main.py

# Initialize the Git repository with the initial files
git add .
git commit -m "Initial commit"
