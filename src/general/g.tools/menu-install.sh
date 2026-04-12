#!/bin/bash

# menu-install.sh - Install g.tools menu entries in GRASS wxGUI
# This script creates the necessary XML configuration files to add User Addons to the wxGUI

# Configuration
TOOLBOX_DIR="$HOME/.grass8/toolboxes"
MODULE_NAME="g.tools"
MENU_LABEL="User Addons"
SYSTEM_MENUDATA="/usr/lib/grass84/gui/wxpython/xml/menudata.xml"

echo "Installing $MODULE_NAME menu entries..."

# 1. Create toolboxes directory if needed
mkdir -p "$TOOLBOX_DIR"

# 2. Backup ALL existing XML files (CRITICAL - menudata.xml breaks GRASS if corrupt!)
echo "Creating backups..."
[ -f "$TOOLBOX_DIR/menudata.xml" ] && cp "$TOOLBOX_DIR/menudata.xml" "$TOOLBOX_DIR/menudata.xml.backup"
[ -f "$TOOLBOX_DIR/toolboxes.xml" ] && cp "$TOOLBOX_DIR/toolboxes.xml" "$TOOLBOX_DIR/toolboxes.xml.backup"
[ -f "$TOOLBOX_DIR/main_menu.xml" ] && cp "$TOOLBOX_DIR/main_menu.xml" "$TOOLBOX_DIR/main_menu.xml.backup"
[ -f "$TOOLBOX_DIR/module_tree_menudata.xml" ] && cp "$TOOLBOX_DIR/module_tree_menudata.xml" "$TOOLBOX_DIR/module_tree_menudata.xml.backup"
echo "Backups created."

# 3. CRITICAL: Copy system menudata.xml as baseline
# menudata.xml is what wxGUI actually parses - this ensures a valid starting point
if [ -f "$SYSTEM_MENUDATA" ]; then
    cp "$SYSTEM_MENUDATA" "$TOOLBOX_DIR/menudata.xml"
    echo "Copied system menudata.xml as baseline"
else
    echo "ERROR: System menudata.xml not found at $SYSTEM_MENUDATA"
    exit 1
fi

# 4. Add User Addons menu to menudata.xml (at top level, alongside File/Settings/etc.)
# Insert User Addons menu before </menubar> (after Help menu) with proper indentation
if ! grep -q "<label>&amp;User Addons</label>" "$TOOLBOX_DIR/menudata.xml"; then
    awk '
    /<\/menubar>/ {
        print "    <menu>"
        print "      <label>&amp;User Addons</label>"
        print "      <items>"
        print "        <menuitem>"
        print "          <label>Addon Extensions</label>"
        print "          <command>g.extension</command>"
        print "          <help>Install and manage GRASS Addon extensions</help>"
        print "          <keywords>extension,addon,install</keywords>"
        print "        </menuitem>"
        print "      </items>"
        print "    </menu>"
        print ""
        print $0
        next
    }
    { print }
    ' "$TOOLBOX_DIR/menudata.xml" > "$TOOLBOX_DIR/menudata.xml.tmp"
    mv "$TOOLBOX_DIR/menudata.xml.tmp" "$TOOLBOX_DIR/menudata.xml"
    echo "Added User Addons menu to menudata.xml"
fi

# 5. Create toolboxes.xml
cat > "$TOOLBOX_DIR/toolboxes.xml" << 'EOF'
<?xml version="1.0" encoding="UTF-8"?>
<toolboxes>
  <toolbox name="UserAddons">
    <label>&amp;User Addons</label>
    <items>
      <module-item name="g.extension">
        <label>Addon Extensions</label>
      </module-item>
    </items>
  </toolbox>
</toolboxes>
EOF

echo "Created toolboxes.xml"

# 6. Create main_menu.xml to include User Addons
cat > "$TOOLBOX_DIR/main_menu.xml" << 'EOF'
<?xml version="1.0" encoding="UTF-8"?>
<toolbox name="CustomizedMainMenu">
  <label>Default GRASS GIS main menu bar</label>
  <items>
    <subtoolbox name="File"/>
    <subtoolbox name="Settings"/>
    <subtoolbox name="Raster"/>
    <subtoolbox name="Vector"/>
    <subtoolbox name="Imagery"/>
    <subtoolbox name="Volumes"/>
    <subtoolbox name="Database"/>
    <subtoolbox name="UserAddons"/>
    <subtoolbox name="Help"/>
  </items>
</toolbox>
EOF

echo "Created main_menu.xml"

echo ""
echo "========================================"
echo "$MODULE_NAME menu entries installed successfully!"
echo "========================================"
echo ""
echo "Restart GRASS wxGUI to see the new menu."
echo ""
echo "Expected menu structure:"
echo "  User Addons"
echo "  └─ Addon Extensions"