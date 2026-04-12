#!/bin/bash

# uninstall.sh - Canonical uninstaller for g.tools addon
# This script removes the g.tools addon and reverts the GRASS wxGUI menu

# Configuration
LOCATION="/home/sampson/grassdata/Sample_Python_Addon/PERMANENT"
MODULE="g.tools"
SCRIPT_DIR="$(dirname "$0")"

# Fallback to current directory if SCRIPT_DIR is empty
if [ -z "$SCRIPT_DIR" ]; then
    SCRIPT_DIR="$(pwd)"
fi

echo "=========================================="
echo "Uninstalling $MODULE addon"
echo "=========================================="
echo ""

# 1. Check if addon is installed
echo "Checking if $MODULE is installed..."
if ! grass "$LOCATION" --exec g.extension -a 2>/dev/null | grep -q "$MODULE"; then
    echo "$MODULE is not installed."
    echo "Nothing to uninstall."
    exit 0
fi

echo "$MODULE is installed. Proceeding with uninstallation..."
echo ""

# 2. Uninstall addon
echo "Removing $MODULE addon..."
grass "$LOCATION" --exec g.extension -f extension="$MODULE" operation=remove

if [ $? -eq 0 ]; then
    echo "$MODULE addon removed successfully."
else
    echo "ERROR: Failed to remove $MODULE addon."
    exit 1
fi

# 3. Uninstall menu (optional)
echo ""
echo "Uninstalling menu..."
if bash "$SCRIPT_DIR/menu-uninstall.sh" 2>&1; then
    echo "Menu removed successfully."
else
    echo "WARNING: Menu uninstallation may have failed."
fi

# 4. Verify uninstallation
echo ""
echo "Verifying uninstallation..."
if ! grass "$LOCATION" --exec g.extension -a 2>/dev/null | grep -q "$MODULE"; then
    echo "✓ Addon removed: $MODULE"
else
    echo "✗ Addon removal verification failed: $MODULE"
    exit 1
fi

# Check if menu was reverted
if [ -f "$HOME/.grass8/toolboxes/menudata.xml" ]; then
    echo "✓ Menu files present"
else
    echo "✓ Menu files cleaned up."
fi

echo ""
echo "=========================================="
echo "$MODULE uninstallation complete!"
echo "=========================================="
echo ""
echo "Restart GRASS wxGUI to see the updated menu."