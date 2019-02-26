#!/bin/bash

# 
# This program created an isolated environment to have all dependencies 
#

# Get in PROJECT_FOLDER const the current folder where this program is currently running
PROJECT_FOLDER="$(pwd)"

VENV_DIR=${PROJECT_FOLDER}/./venv

# Create virtual environment directory 
./bash_scripts/create_virtual_environment.sh

# Check for virtual environment directory
if [ -d "$VENV_DIR" ]; then

    # Active virtual environment
    ./bash_scripts/active_virtual_environment.sh

    # Install requirements
    ./bash_scripts/requirements.sh

    # Upgrade Pip
    ./bash_scripts/upgrade_pip.sh
else
    echo ERROR: ./venv it\'s not a valid folder
    exit 1
fi
