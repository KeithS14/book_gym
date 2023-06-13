#!/bin/bash

VENV_NAME="gym-book-env"

# Check if the virtual environment exists
if [ ! -d "$VENV_NAME" ]; then
    echo "Creating virtual environment: $VENV_NAME"
    python3.10 -m venv $VENV_NAME

    source $VENV_NAME/bin/activate

    # Install requests package
    pip install requests selenium 
    pip install --force-reinstall python-telegram-bot
fi

# Activate the virtual environment
source $VENV_NAME/bin/activate