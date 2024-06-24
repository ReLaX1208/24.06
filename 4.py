#!/bin/bash

# Freeze dependencies using pip
pip freeze > requirements.txt

# Optional: Sort the dependencies in the requirements file
sort -o requirements.txt requirements.txt
