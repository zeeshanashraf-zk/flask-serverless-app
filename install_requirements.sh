#!/bin/bash

# Install Python dependencies (including pre-commit)
pip install -r requirements.txt

# Install pre-commit hook by copying it directly into the .git/hooks/
cp pre-commit .git/hooks/pre-commit

# Make sure the pre-commit hook is executable
chmod +x .git/hooks/pre-commit

echo "Pre-commit hook has been installed successfully."
