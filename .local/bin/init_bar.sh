#!/bin/sh

WORKING_DIR="/home/$USER/.local/src/fabric"

source "$WORKING_DIR/venv/bin/activate"
python "$WORKING_DIR/bar.py" && deactivate
