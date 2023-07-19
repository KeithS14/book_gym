#!/bin/bash

VENV_NAME="gym-book-env"

# Check if the virtual environment exists
if [ ! -d "$VENV_NAME" ]; then
    echo "Creating virtual environment: $VENV_NAME"
    python3 -m venv $VENV_NAME

    source $VENV_NAME/bin/activate

    # Install required packages
    pip install requests selenium telegram python-telegram-bot
else
    echo "Virtual environment $VENV_NAME already exists."
fi

# Activate the virtual environment
source $VENV_NAME/bin/activate