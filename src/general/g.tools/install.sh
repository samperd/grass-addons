#!/bin/bash

# install.sh - Canonical installer for g.tools addon
# This script installs the g.tools addon and integrates it into the GRASS wxGUI menu

# Configuration
LOCATION="/home/sampson/grassdata/Sample_Python_Addon/PERMANENT"
MODULE="g.tools"
SCRIPT_DIR="$(dirname "$0")"

# Fallback to current directory if SCRIPT_DIR is empty
if [ -z "$SCRIPT_DIR" ]; then
    SCRIPT_DIR="$(pwd)"
fi

echo "========================================"
echo "Installing $MODULE addon"
echo "========================================"
echo ""

# 1. Check if addon is already installed
echo "Checking if $MODULE is already installed..."
if grass "$LOCATION" --exec g.extension -a 2>/dev/null | grep -q "$MODULE"; then
    echo "$MODULE is already installed."
    echo "Skipping addon installation."
    ADDON_ALREADY_INSTALLED=true
else
    # 2. Install addon
    echo ""
    echo "Installing $MODULE addon..."
    grass "$LOCATION" --exec g.extension extension="$MODULE" url="$SCRIPT_DIR" operation=add
    
    if [ $? -eq 0 ]; then
        echo "$MODULE addon installed successfully."
    else
        echo "ERROR: Failed to install $MODULE addon."
        exit 1
    fi
    
    ADDON_ALREADY_INSTALLED=false
fi

# 3. Install menu (on first install only)
if [ "$ADDON_ALREADY_INSTALLED" = false ]; then
    echo ""
    echo "Installing User Addons menu..."
    if bash "$SCRIPT_DIR/menu-install.sh" 2>&1; then
        echo "Menu installed successfully."
    else
        echo "WARNING: Menu installation may have failed."
    fi
fi

# 4. Verify installation
echo ""
echo "Verifying installation..."
if grass "$LOCATION" --exec g.extension -a 2>/dev/null | grep -q "$MODULE"; then
    echo "✓ Addon installed: $MODULE"
else
    echo "✗ Addon verification failed: $MODULE"
    exit 1
fi

echo ""
echo "========================================"
echo "$MODULE installation complete!"
echo "========================================"
echo ""
echo "Restart GRASS wxGUI to see the new menu."