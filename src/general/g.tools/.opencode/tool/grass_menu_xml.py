#!/usr/bin/env python3
"""

GRASS GIS menu XML management tool.

Provides functions to interact with GRASS wxGUI menu XML files:
- menudata.xml (wxGUI menu structure)
- toolboxes.xml (toolbox configuration)
- main_menu.xml (main menu reference)

Copyright (C) 2026 by the GRASS Development Team

This program is free software under the GNU General Public License (>=v2).
Read the file COPYING that comes with GRASS for details.

"""

import sys
import os
import shutil
import xml.etree.ElementTree as ET
from pathlib import Path
from datetime import datetime


# Standard GRASS toolboxes directory
TOOLBOXES_DIR = os.path.expanduser("~/.grass8/toolboxes")
SYSTEM_TOOLBOXES_DIR = "/usr/lib/grass84/gui/wxpython/xml"


def get_toolboxes_dir():
    """Get the user toolboxes directory, creating it if needed."""
    if not os.path.exists(TOOLBOXES_DIR):
        os.makedirs(TOOLBOXES_DIR, exist_ok=True)
    return TOOLBOXES_DIR


def backup_file(filepath):
    """Create a backup of a file.

    Args:
        filepath: Path to file to backup

    Returns:
        Path to backup file or None if original doesn't exist
    """
    if not os.path.exists(filepath):
        return None

    # Create backup with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = f"{filepath}.backup_{timestamp}"
    shutil.copy2(filepath, backup_path)
    return backup_path


def backup_menu_files():
    """Backup existing menu XML files.

    Returns:
        Dictionary with backup paths
    """
    backups = {}

    files = [
        "menudata.xml",
        "toolboxes.xml",
        "main_menu.xml",
    ]

    for filename in files:
        filepath = os.path.join(get_toolboxes_dir(), filename)
        backup_path = backup_file(filepath)
        if backup_path:
            backups[filename] = backup_path

    return backups


def parse_menu_xml(xml_string):
    """Parse menu XML string.

    Args:
        xml_string: XML content as string

    Returns:
        ElementTree root element
    """
    try:
        # Handle XML namespace
        ET.register_namespace("", "http://grass.osgeo.org")
        root = ET.fromstring(xml_string)
        return root
    except ET.ParseError as e:
        print(f"Error parsing XML: {e}", file=sys.stderr)
        return None


def read_menu_file(filename):
    """Read a menu XML file.

    Args:
        filename: Name of file (e.g., 'menudata.xml')

    Returns:
        XML content as string or None on error
    """
    # Try user toolboxes first
    filepath = os.path.join(get_toolboxes_dir(), filename)
    if os.path.exists(filepath):
        with open(filepath, "r") as f:
            return f.read()

    # Fall back to system toolboxes
    system_path = os.path.join(SYSTEM_TOOLBOXES_DIR, filename)
    if os.path.exists(system_path):
        with open(system_path, "r") as f:
            return f.read()

    return None


def write_menu_file(filename, content):
    """Write content to a menu XML file.

    Args:
        filename: Name of file (e.g., 'menudata.xml')
        content: XML content as string

    Returns:
        True on success, False on error
    """
    # Validate XML before writing
    try:
        root = ET.fromstring(content)
    except ET.ParseError as e:
        print(f"Error: Invalid XML in {filename}: {e}", file=sys.stderr)
        return False

    # Ensure directory exists
    toolboxes_dir = get_toolboxes_dir()

    # Create backup of existing file
    filepath = os.path.join(toolboxes_dir, filename)
    if os.path.exists(filepath):
        backup_file(filepath)

    # Write new content
    try:
        with open(filepath, "w") as f:
            f.write(content)
        return True
    except IOError as e:
        print(f"Error writing {filename}: {e}", file=sys.stderr)
        return False


def validate_menu_structure(xml_string):
    """Validate menu XML structure.

    Args:
        xml_string: XML content as string

    Returns:
        True if valid, False otherwise
    """
    try:
        root = ET.fromstring(xml_string)

        # Check for required elements
        # Menu structure should have <menu> elements
        menus = root.findall(".//menu")
        if not menus:
            print("Warning: No menu elements found", file=sys.stderr)
            return False

        return True
    except ET.ParseError as e:
        print(f"Error: Invalid XML structure: {e}", file=sys.stderr)
        return False


def add_menu_entry(menu_name, items):
    """Add a new menu entry to menudata.xml.

    Args:
        menu_name: Name of menu to add (e.g., 'User Addons')
        items: List of menu items to add

    Returns:
        True on success, False on error
    """
    # Read existing menudata.xml
    content = read_menu_file("menudata.xml")

    if content is None:
        # Create new structure
        root = ET.Element("GuiInterface")
        root.set("name", "menudata")
    else:
        try:
            root = ET.fromstring(content)
        except ET.ParseError as e:
            print(f"Error parsing menudata.xml: {e}", file=sys.stderr)
            return False

    # Find or create the menu
    menu_xpath = f".//menu[@name='{menu_name}']"
    menu = root.find(menu_xpath)

    if menu is None:
        # Create new menu
        menu = ET.SubElement(root, "menu")
        menu.set("name", menu_name)

    # Add items to menu
    for item in items:
        menuitem = ET.SubElement(menu, "menuitem")
        menuitem.set("guisection", item.get("guisection", menu_name))
        label = ET.SubElement(menuitem, "label")
        label.text = item.get("label", "")
        handler = ET.SubElement(menuitem, "handler")
        handler.text = item.get("handler", "")
        desc = ET.SubElement(menuitem, "description")
        desc.text = item.get("description", "")

    # Write updated content
    xml_string = ET.tostring(root, encoding="unicode")
    return write_menu_file("menudata.xml", xml_string)


def remove_menu_entry(menu_name):
    """Remove a menu entry from menudata.xml.

    Args:
        menu_name: Name of menu to remove

    Returns:
        True on success, False on error
    """
    # Read existing menudata.xml
    content = read_menu_file("menudata.xml")
    if content is None:
        print("Error: menudata.xml not found", file=sys.stderr)
        return False

    try:
        root = ET.fromstring(content)
    except ET.ParseError as e:
        print(f"Error parsing menudata.xml: {e}", file=sys.stderr)
        return False

    # Find and remove menu
    menu_xpath = f".//menu[@name='{menu_name}']"
    menu = root.find(menu_xpath)

    if menu is not None:
        root.remove(menu)

    # Write updated content
    xml_string = ET.tostring(root, encoding="unicode")
    return write_menu_file("menudata.xml", xml_string)


def list_menus():
    """List all menus in menudata.xml.

    Returns:
        List of menu names
    """
    content = read_menu_file("menudata.xml")
    if content is None:
        return []

    try:
        root = ET.fromstring(content)
    except ET.ParseError:
        return []

    menus = []
    for menu in root.findall(".//menu"):
        name = menu.get("name")
        if name:
            menus.append(name)

    return menus


def restore_backup(backup_path):
    """Restore from a backup file.

    Args:
        backup_path: Path to backup file

    Returns:
        True on success, False on error
    """
    if not os.path.exists(backup_path):
        print(f"Error: Backup file not found: {backup_path}", file=sys.stderr)
        return False

    # Extract original filename
    original_name = os.path.basename(backup_path).replace(".backup_", "").rsplit("_", 1)[0]
    if not original_name.endswith(".xml"):
        original_name += ".xml"

    target_path = os.path.join(get_toolboxes_dir(), original_name)

    try:
        shutil.copy2(backup_path, target_path)
        return True
    except IOError as e:
        print(f"Error restoring backup: {e}", file=sys.stderr)
        return False


def main():
    """Main entry point for CLI usage."""
    if len(sys.argv) < 2:
        print("Usage: grass_menu_xml.py <command> [options]")
        print("")
        print("Commands:")
        print("  list                  List all menus")
        print("  add <menu> <items>     Add a menu entry")
        print("  remove <menu>         Remove a menu entry")
        print("  backup               Backup menu files")
        print("  validate             Validate menudata.xml")
        sys.exit(1)

    command = sys.argv[1]

    if command == "list":
        menus = list_menus()
        for menu in menus:
            print(menu)
    elif command == "backup":
        backups = backup_menu_files()
        for name, path in backups.items():
            print(f"Backed up: {name} -> {path}")
    elif command == "validate":
        content = read_menu_file("menudata.xml")
        if content:
            valid = validate_menu_structure(content)
            if valid:
                print("menudata.xml is valid")
            else:
                print("menudata.xml is invalid")
                sys.exit(1)
        else:
            print("menudata.xml not found")
            sys.exit(1)
    else:
        print(f"Error: unknown command '{command}'", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()