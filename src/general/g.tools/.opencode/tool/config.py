#!/usr/bin/env python3
"""

GRASS GIS configuration management tool.

Provides functions to manage GRASS configuration:
- GISRC file
- GRASS variables
- Database and mapset settings
- Display settings

Copyright (C) 2026 by the GRASS Development Team

This program is free software under the GNU General Public License (>=v2).
Read the file COPYING that comes with GRASS for details.

"""

import sys
import os
import platform
from pathlib import Path


# Standard GRASS configuration file
GISRC_FILE = os.path.expanduser("~/.grassrc")

# GRASS version
GRASS_VERSION = "8"


def get_grass_vars():
    """Get current GRASS environment variables.

    Returns:
        Dictionary of GRASS variables
    """
    grass_vars = {}

    # Common GRASS variables
    var_names = [
        "GISBASE",
        "GISDBASE",
        "LOCATION_NAME",
        "MAPSET",
        "GUI",
        "GRASS_GUI",
        "GRASS_ADDON_PATH",
        "GRASS_PROJSHARE",
        "GRASS_PYTHON",
    ]

    for var_name in var_names:
        value = os.environ.get(var_name)
        if value:
            grass_vars[var_name] = value

    # Parse GISRC file if it exists
    if os.path.exists(GISRC_FILE):
        with open(GISRC_FILE, "r") as f:
            for line in f:
                line = line.strip()
                if line and "=" in line:
                    key, value = line.split("=", 1)
                    grass_vars[key.strip()] = value.strip()

    return grass_vars


def set_grass_var(key, value):
    """Set a GRASS environment variable.

    Args:
        key: Variable name
        value: Variable value

    Returns:
        True on success
    """
    os.environ[key] = value
    return True


def get_gisbase():
    """Get GRASS GISBASE path.

    Returns:
        Path to GISBASE or None
    """
    # Check environment
    gisbase = os.environ.get("GISBASE")
    if gisbase:
        return gisbase

    # Check common locations
    system = platform.system()
    candidates = {
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

    for path in candidates.get(system, []):
        if os.path.exists(path):
            return path

    return None


def get_gisdbase():
    """Get GRASS database directory path.

    Returns:
        Path to GISDBASE or default ~/grassdata
    """
    # Check environment
    gisdbase = os.environ.get("GISDBASE")
    if gisdbase:
        return gisdbase

    # Return default
    return os.path.expanduser("~/grassdata")


def get_location_mapset():
    """Get current location and mapset.

    Returns:
        Tuple of (location_name, mapset) or (None, None)
    """
    location = os.environ.get("LOCATION_NAME")
    mapset = os.environ.get("MAPSET")

    if location and mapset:
        return location, mapset

    # Try to read from GISRC
    if os.path.exists(GISRC_FILE):
        with open(GISRC_FILE, "r") as f:
            for line in f:
                if line.startswith("LOCATION_NAME="):
                    location = line.split("=", 1)[1].strip()
                elif line.startswith("MAPSET="):
                    mapset = line.split("=", 1)[1].strip()

    return location, mapset


def write_gisrc(gisdbase, location, mapset):
    """Write GISRC file with new location/mapset.

    Args:
        gisdbase: Path to GRASS database
        location: Location name
        mapset: Mapset name

    Returns:
        True on success, False on error
    """
    gisbase = get_gisbase()
    if not gisbase:
        print("Error: Could not determine GISBASE", file=sys.stderr)
        return False

    try:
        with open(GISRC_FILE, "w") as f:
            f.write(f"GisBASE={gisbase}\n")
            f.write(f"GisDBASE={gisdbase}\n")
            f.write(f"LOCATION_NAME={location}\n")
            f.write(f"MAPSET={mapset}\n")
        return True
    except IOError as e:
        print(f"Error writing GISRC: {e}", file=sys.stderr)
        return False


def get_config_path():
    """Get the GRASS config directory path.

    Returns:
        Path to config directory
    """
    version = GRASS_VERSION.split(".")[0]
    return os.path.expanduser(f"~/.grass{version}")


def ensure_config_dir():
    """Ensure GRASS config directory exists.

    Returns:
        Path to config directory
    """
    config_dir = get_config_path()
    os.makedirs(config_dir, exist_ok=True)
    return config_dir


def get_toolboxes_path():
    """Get the GRASS toolboxes directory path.

    Returns:
        Path to toolboxes directory
    """
    return get_toolboxes_dir()


def get_toolboxes_dir():
    """Get the GRASS toolboxes directory path."""
    config_dir = get_config_path()
    return os.path.join(config_dir, "toolboxes")


def list_locations(gisdbase=None):
    """List available locations in GISDBASE.

    Args:
        gisdbase: Path to GRASS database (default: from config)

    Returns:
        List of location names
    """
    if not gisdbase:
        gisdbase = get_gisdbase()

    if not os.path.exists(gisdbase):
        return []

    locations = []
    for item in os.listdir(gisdbase):
        item_path = os.path.join(gisdbase, item)
        if os.path.isdir(item_path):
            # Check for PERMANENT mapset
            perm_mapset = os.path.join(item_path, "PERMANENT")
            if os.path.isdir(perm_mapset):
                locations.append(item)

    return locations


def list_mapsets(gisdbase, location):
    """List available mapsets in a location.

    Args:
        gisdbase: Path to GRASS database
        location: Location name

    Returns:
        List of mapset names
    """
    location_path = os.path.join(gisdbase, location)

    if not os.path.exists(location_path):
        return []

    mapsets = []
    for item in os.listdir(location_path):
        item_path = os.path.join(location_path, item)
        if os.path.isdir(item_path):
            mapsets.append(item)

    return mapsets


def get_system_info():
    """Get system and GRASS information.

    Returns:
        Dictionary with system information
    """
    info = {
        "platform": platform.system(),
        "platform_release": platform.release(),
        "architecture": platform.machine(),
        "python_version": platform.python_version(),
        "gisbase": get_gisbase(),
        "gisdbase": get_gisdbase(),
        "config_dir": get_config_path(),
        "toolboxes_dir": get_toolboxes_dir(),
    }

    location, mapset = get_location_mapset()
    info["location"] = location
    info["mapset"] = mapset

    return info


def main():
    """Main entry point for CLI usage."""
    if len(sys.argv) < 2:
        print("Usage: config.py <command> [options]")
        print("")
        print("Commands:")
        print("  vars                  Show GRASS variables")
        print("  locations             List available locations")
        print("  mapsets <location>   List mapsets in location")
        print("  info                 Show system and GRASS info")
        print("  ensure               Ensure config directories exist")
        sys.exit(1)

    command = sys.argv[1]

    if command == "vars":
        vars_dict = get_grass_vars()
        for key, value in vars_dict.items():
            print(f"{key}={value}")
    elif command == "locations":
        locations = list_locations()
        for loc in locations:
            print(loc)
    elif command == "mapsets":
        if len(sys.argv) < 3:
            print("Error: location required", file=sys.stderr)
            sys.exit(1)
        gisdbase = get_gisdbase()
        mapsets = list_mapsets(gisdbase, sys.argv[2])
        for mapset in mapsets:
            print(mapset)
    elif command == "info":
        info = get_system_info()
        for key, value in info.items():
            print(f"{key}: {value}")
    elif command == "ensure":
        config_dir = ensure_config_dir()
        print(f"Config directory: {config_dir}")
    else:
        print(f"Error: unknown command '{command}'", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()