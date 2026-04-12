#!/bin/bash

# menu-uninstall.sh - Remove g.tools menu entries from GRASS wxGUI
# This script restores the backed-up configuration files to remove User Addons from the menu

# Configuration
TOOLBOX_DIR="$HOME/.grass8/toolboxes"
MODULE_NAME="g.tools"

echo "Uninstalling $MODULE_NAME menu entries..."

# 1. Restore ALL backed-up files (in order of priority)
echo "Restoring from backups..."

if [ -f "$TOOLBOX_DIR/menudata.xml.backup" ]; then
    cp "$TOOLBOX_DIR/menudata.xml.backup" "$TOOLBOX_DIR/menudata.xml"
    echo "Restored menudata.xml from backup"
else
    # No backup - remove User Addons menu entries manually
    echo "WARNING: No menudata.xml backup found. Attempting manual cleanup."
    if [ -f "$TOOLBOX_DIR/menudata.xml" ]; then
        # Remove User Addons menu block
        sed -i '/<menu name="User Addons">/,/<\/menu>/d' "$TOOLBOX_DIR/menudata.xml"
        echo "Removed User Addons menu from menudata.xml"
    fi
fi

if [ -f "$TOOLBOX_DIR/toolboxes.xml.backup" ]; then
    cp "$TOOLBOX_DIR/toolboxes.xml.backup" "$TOOLBOX_DIR/toolboxes.xml"
    echo "Restored toolboxes.xml from backup"
else
    # Remove User Addons toolbox
    if [ -f "$TOOLBOX_DIR/toolboxes.xml" ]; then
        sed -i '/<toolbox name="UserAddons">/,/<\/toolbox>/d' "$TOOLBOX_DIR/toolboxes.xml"
    fi
fi

if [ -f "$TOOLBOX_DIR/main_menu.xml.backup" ]; then
    cp "$TOOLBOX_DIR/main_menu.xml.backup" "$TOOLBOX_DIR/main_menu.xml"
    echo "Restored main_menu.xml from backup"
fi

if [ -f "$TOOLBOX_DIR/module_tree_menudata.xml.backup" ]; then
    cp "$TOOLBOX_DIR/module_tree_menudata.xml.backup" "$TOOLBOX_DIR/module_tree_menudata.xml"
    echo "Restored module_tree_menudata.xml from backup"
fi

# 2. Remove backup files created by install
echo "Cleaning up backup files..."
rm -f "$TOOLBOX_DIR/menudata.xml.backup"
rm -f "$TOOLBOX_DIR/toolboxes.xml.backup"
rm -f "$TOOLBOX_DIR/main_menu.xml.backup"
rm -f "$TOOLBOX_DIR/module_tree_menudata.xml.backup"
rm -f "$TOOLBOX_DIR/menudata.xml.tmp"

echo ""
echo "=========================================="
echo "$MODULE_NAME menu entries removed successfully!"
echo "=========================================="
echo ""
echo "Restart GRASS wxGUI to see the updated menu."