#!/bin/bash

# update.sh - Update/reinstall g.tools addon
# This script handles both fresh installs and updates by running uninstall then install

# Configuration
LOCATION="/home/sampson/grassdata/Sample_Python_Addon/PERMANENT"
MODULE="g.tools"
SCRIPT_DIR="$(dirname "$0")"

# Fallback to current directory if SCRIPT_DIR is empty
if [ -z "$SCRIPT_DIR" ]; then
    SCRIPT_DIR="$(pwd)"
fi

echo "========================================"
echo "Updating $MODULE addon"
echo "========================================"
echo ""

# 1. Check if addon exists
echo "Checking if $MODULE is already installed..."
if grass "$LOCATION" --exec g.extension -a 2>/dev/null | grep -q "$MODULE"; then
    # 2. If exists, uninstall first
    echo "$MODULE is installed. Running uninstall first..."
    bash "$SCRIPT_DIR/uninstall.sh"
    
    if [ $? -ne 0 ]; then
        echo "ERROR: Uninstallation failed."
        exit 1
    fi
    echo "Uninstallation complete."
    echo ""
fi

# 3. Run fresh installation
echo "Running installation..."
bash "$SCRIPT_DIR/install.sh"

if [ $? -eq 0 ]; then
    echo ""
    echo "========================================"
    echo "$MODULE update complete!"
    echo "========================================"
    echo ""
    echo "Restart GRASS wxGUI to see the updated menu."
else
    echo "ERROR: Installation failed."
    exit 1
fi