#!/bin/bash

VENV_NAME="gym-book-env"

# Check if the virtual environment exists
if [ ! -d "$VENV_NAME" ]; then
    echo "Creating virtual environment: $VENV_NAME"
    python3.10 -m venv $VENV_NAME

    $VENV_NAME\Scripts\activate

    # Install requests package
    pip install requests selenium
fi

# Activate the virtual environment
$VENV_NAME\Scripts\activate


