#!/usr/bin/env python3
"""

GRASS GIS session management tool.

Provides functions to start GRASS GIS sessions in various modes:
- CLI (command line interface)
- GUI ( graphical user interface using wxGUI)
- tty (interactive terminal mode)

Copyright (C) 2026 by the GRASS Development Team

This program is free software under the GNU General Public License (>=v2).
Read the file COPYING that comes with GRASS for details.

"""

import sys
import os
import subprocess
import platform
from pathlib import Path


# Standard GRASS installation paths by platform
GISBASE_PATHS = {
    "Linux": [
        "/usr/lib/grass84",
        "/usr/local/lib/grass84",
        "/opt/grass84",
    ],
    "Darwin": [
        "/Applications/GRASS-8.4.app/Contents/Resources",
        "/usr/local/grass84",
    ],
    "Windows": [
        r"C:\OSGeo4W64\apps\grass\grass84",
        r"C:\OSGeo4W\apps\grass\grass84",
    ],
}


def find_gisbase(gisbase_arg=None):
    """Find GRASS GISBASE installation.

    Args:
        gisbase_arg: Optional GISBASE path provided by user

    Returns:
        Path to GISBASE directory or None if not found
    """
    system = platform.system()
    candidates = GISBASE_PATHS.get(system, [])

    # Try candidates first
    for path in candidates:
        if os.path.exists(path):
            return path

    # Try user-provided path
    if gisbase_arg and os.path.exists(gisbase_arg):
        return gisbase_arg

    # Try environment variable
    env_gisbase = os.environ.get("GISBASE")
    if env_gisbase and os.path.exists(env_gisbase):
        return env_gisbase

    # Try common commands
    try:
        result = subprocess.run(
            ["grass", "--config", "path"],
            capture_output=True,
            text=True,
            check=True,
        )
        if result.returncode == 0:
            return result.stdout.strip()
    except (subprocess.SubprocessError, FileNotFoundError):
        pass

    return None


def start_grass_session(
    gisdbase,
    location,
    mapset="PERMANENT",
    mode="gui",
    gisbase=None,
):
    """Start a GRASS GIS session.

    Args:
        gisdbase: Path to GRASS database directory
        location: Location name
        mapset: Mapset name (default: PERMANENT)
        mode: Session mode - 'cli', 'gui', or 'tty' (default: 'gui')
        gisbase: Optional GISBASE path

    Returns:
        0 on success, non-zero on error
    """
    # Validate inputs
    if not gisdbase:
        print("Error: GISDBASE path is required", file=sys.stderr)
        return 1

    if not location:
        print("Error: LOCATION is required", file=sys.stderr)
        return 1

    # Find GISBASE
    gisbase_path = find_gisbase(gisbase)
    if not gisbase_path:
        print(f"Error: Could not find GRASS GISBASE", file=sys.stderr)
        return 1

    # Validate paths exist
    location_path = os.path.join(gisdbase, location, mapset)
    if not os.path.exists(location_path):
        print(f"Error: Mapset does not exist: {location_path}", file=sys.stderr)
        return 1

    # Determine launch mode
    mode_flags = {
        "gui": ["--gui"],
        "cli": ["--shell", "bash"],
        "tty": [],
    }

    flags = mode_flags.get(mode.lower(), ["--gui"])

    # Build GRASS start command
    cmd = ["grass", flags + [location_path]]

    try:
        subprocess.run(cmd)
        return 0
    except FileNotFoundError:
        print("Error: GRASS not found in PATH", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Error starting GRASS: {e}", file=sys.stderr)
        return 1


def get_grass_config():
    """Get GRASS configuration information.

    Returns:
        Dictionary with GRASS configuration details
    """
    config = {
        "gisbase": find_gisbase(),
        "version": None,
        "arch": None,
    }

    # Try to get version
    try:
        result = subprocess.run(
            ["grass", "--version"],
            capture_output=True,
            text=True,
            check=True,
        )
        if result.returncode == 0:
            for line in result.stdout.split("\n"):
                if line.startswith("GRASS version:"):
                    config["version"] = line.split(":", 1)[1].strip()
                    break
    except (subprocess.SubprocessError, FileNotFoundError):
        pass

    # Try to get architecture
    try:
        result = subprocess.run(
            ["grass", "--config", "arch"],
            capture_output=True,
            text=True,
            check=True,
        )
        if result.returncode == 0:
            config["arch"] = result.stdout.strip()
    except (subprocess.SubprocessError, FileNotFoundError):
        pass

    return config


def main():
    """Main entry point for CLI usage."""
    if len(sys.argv) < 3:
        print("Usage: grass_session.py <gisdbase> <location> [mapset] [mode]")
        print("  mode: cli, gui, or tty (default: gui)")
        sys.exit(1)

    gisdbase = sys.argv[1]
    location = sys.argv[2]
    mapset = sys.argv[3] if len(sys.argv) > 3 else "PERMANENT"
    mode = sys.argv[4] if len(sys.argv) > 4 else "gui"

    sys.exit(start_grass_session(gisdbase, location, mapset, mode))


if __name__ == "__main__":
    main()