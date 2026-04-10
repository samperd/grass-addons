#!/usr/bin/env python3
"""

GRASS GIS addon management tool.

Provides functions to install, uninstall, list, and manage GRASS addons
using the g.extension module.

Copyright (C) 2026 by the GRASS Development Team

This program is free software under the GNU General Public License (>=v2).
Read the file COPYING that comes with GRASS for details.

"""

import sys
import os
import subprocess
import json
import re


def run_grass_command(module, *args, flags=None):
    """Run a GRASS command and return output.

    Args:
        module: GRASS module name (e.g., 'g.extension')
        args: Module arguments
        flags: Module flags (e.g., 'l' for list)

    Returns:
        Tuple of (returncode, stdout, stderr)
    """
    cmd = [module]
    if flags:
        cmd.insert(1, "-" + flags)
    cmd.extend(args)

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=False,
        )
        return result.returncode, result.stdout, result.stderr
    except FileNotFoundError:
        return 1, "", "GRASS not found in PATH"
    except Exception as e:
        return 1, "", str(e)


def list_installed_addons():
    """List installed GRASS addons.

    Returns:
        List of addon names
    """
    returncode, stdout, stderr = run_grass_command("g.extension", flags="l")

    if returncode != 0:
        print(f"Error listing addons: {stderr}", file=sys.stderr)
        return []

    addons = []
    for line in stdout.split("\n"):
        line = line.strip()
        if line and not line.startswith("#"):
            # Extract addon name (first field)
            parts = line.split()
            if parts:
                addons.append(parts[0])

    return addons


def list_available_addons(url=None):
    """List available GRASS addons from addon repository.

    Args:
        url: Optional repository URL

    Returns:
        List of available addon names
    """
    args = []
    if url:
        args.extend(["url", url])

    returncode, stdout, stderr = run_grass_command("g.extension", *args, flags="a")

    if returncode != 0:
        print(f"Error listing available addons: {stderr}", file=sys.stderr)
        return []

    addons = []
    for line in stdout.split("\n"):
        line = line.strip()
        if line and not line.startswith("#"):
            parts = line.split()
            if parts:
                addons.append(parts[0])

    return addons


def install_addon(name, url=None, quiet=False):
    """Install a GRASS addon.

    Args:
        name: Addon name to install
        url: Optional repository URL
        quiet: Suppress output if True

    Returns:
        True on success, False on error
    """
    args = [name]
    if url:
        args.extend(["url", url])

    flags = "s"  # Silent operation
    if quiet:
        flags += "q"

    returncode, stdout, stderr = run_grass_command("g.extension", *args, flags=flags)

    if returncode == 0:
        if not quiet:
            print(f"Successfully installed addon: {name}")
        return True
    else:
        print(f"Error installing addon {name}: {stderr}", file=sys.stderr)
        return False


def uninstall_addon(name, quiet=False):
    """Uninstall a GRASS addon.

    Args:
        name: Addon name to uninstall
        quiet: Suppress output if True

    Returns:
        True on success, False on error
    """
    flags = "d"  # Delete
    if quiet:
        flags += "q"

    returncode, stdout, stderr = run_grass_command("g.extension", name, flags=flags)

    if returncode == 0:
        if not quiet:
            print(f"Successfully uninstalled addon: {name}")
        return True
    else:
        print(f"Error uninstalling addon {name}: {stderr}", file=sys.stderr)
        return False


def get_addon_info(name):
    """Get information about an addon.

    Args:
        name: Addon name

    Returns:
        Dictionary with addon information
    """
    returncode, stdout, stderr = run_grass_command(
        "g.extension", name, flags="i"
    )

    if returncode != 0:
        print(f"Error getting addon info: {stderr}", file=sys.stderr)
        return {}

    info = {}
    current_key = None

    for line in stdout.split("\n"):
        line = line.strip()
        if not line or line.startswith("#"):
            continue

        # Check for key: value pattern
        match = re.match(r"(\w+):\s*(.*)", line)
        if match:
            key, value = match.groups()
            info[key.lower()] = value.strip()
            current_key = key.lower()

    return info


def update_addon(name, quiet=False):
    """Update an existing GRASS addon.

    Args:
        name: Addon name to update
        quiet: Suppress output if True

    Returns:
        True on success, False on error
    """
    flags = "s"  # Update
    if quiet:
        flags += "q"

    returncode, stdout, stderr = run_grass_command(
        "g.extension", name, flags=flags
    )

    if returncode == 0:
        if not quiet:
            print(f"Successfully updated addon: {name}")
        return True
    else:
        print(f"Error updating addon {name}: {stderr}", file=sys.stderr)
        return False


def main():
    """Main entry point for CLI usage."""
    if len(sys.argv) < 2:
        print("Usage: grass_addon.py <command> [options]")
        print("")
        print("Commands:")
        print("  list                  List installed addons")
        print("  available              List available addons")
        print("  install <name>        Install an addon")
        print("  uninstall <name>      Uninstall an addon")
        print("  update <name>         Update an addon")
        print("  info <name>          Get addon information")
        print("")
        print("Options:")
        print("  --url <url>           Repository URL")
        print("  --quiet               Suppress output")
        sys.exit(1)

    command = sys.argv[1]

    # Parse global options
    url = None
    quiet = False

    i = 2
    while i < len(sys.argv):
        if sys.argv[i] == "--url" and i + 1 < len(sys.argv):
            url = sys.argv[i + 1]
            i += 2
        elif sys.argv[i] == "--quiet":
            quiet = True
            i += 1
        else:
            i += 1

    if command == "list":
        addons = list_installed_addons()
        for addon in addons:
            print(addon)
    elif command == "available":
        addons = list_available_addons(url)
        for addon in addons:
            print(addon)
    elif command == "install":
        if len(sys.argv) < 3:
            print("Error: addon name required", file=sys.stderr)
            sys.exit(1)
        name = sys.argv[2]
        success = install_addon(name, url, quiet)
        sys.exit(0 if success else 1)
    elif command == "uninstall":
        if len(sys.argv) < 3:
            print("Error: addon name required", file=sys.stderr)
            sys.exit(1)
        name = sys.argv[2]
        success = uninstall_addon(name, quiet)
        sys.exit(0 if success else 1)
    elif command == "update":
        if len(sys.argv) < 3:
            print("Error: addon name required", file=sys.stderr)
            sys.exit(1)
        name = sys.argv[2]
        success = update_addon(name, quiet)
        sys.exit(0 if success else 1)
    elif command == "info":
        if len(sys.argv) < 3:
            print("Error: addon name required", file=sys.stderr)
            sys.exit(1)
        name = sys.argv[2]
        info = get_addon_info(name)
        print(json.dumps(info, indent=2))
    else:
        print(f"Error: unknown command '{command}'", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()