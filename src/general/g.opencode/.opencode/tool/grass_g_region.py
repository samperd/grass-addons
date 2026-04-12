"""

Python script to query GRASS GIS region information using grass.script API.

Copyright (c) 2026 David Sampson

"""

import sys
import os
import platform
import subprocess
import json
import config

def handle_create(gisbase, gisdbase, location_name, epsg, n, s, e, w):
    env = os.environ.copy()
    env['GISBASE'] = gisbase
    env['GISDBASE'] = gisdbase

    # Create location
    cmd = ['g.proj', '-c', f'epsg={epsg}', f'location={location_name}']
    result = subprocess.run(cmd, capture_output=True, text=True, env=env, timeout=30)
    if result.returncode != 0:
        return f"Error creating location: {result.stderr.strip()}"

    # Set region in the new location (PERMANENT mapset is auto-created)
    env['LOCATION_NAME'] = location_name
    env['MAPSET'] = 'PERMANENT'
    cmd2 = ['grass', f'{gisdbase}/{location_name}/PERMANENT', '--exec', 'g.region', f'n={n}', f's={s}', f'e={e}', f'w={w}']
    result2 = subprocess.run(cmd2, capture_output=True, text=True, env=env, timeout=30)
    if result2.returncode != 0:
        return f"Error setting region: {result2.stderr.strip()}"

    return f"Location '{location_name}' created with EPSG {epsg} and bounds n={n} s={s} e={e} w={w}"

def handle_set(gisbase, gisdbase, project, mapset, n, s, e, w, res):
    env = os.environ.copy()
    env['GISBASE'] = gisbase
    env['GISDBASE'] = gisdbase
    env['LOCATION_NAME'] = project
    env['MAPSET'] = mapset

    cmd = ['grass', f'{gisdbase}/{project}/{mapset}', '--exec', 'g.region', f'n={n}', f's={s}', f'e={e}', f'w={w}', f'res={res}']
    result = subprocess.run(cmd, capture_output=True, text=True, env=env, timeout=30)
    if result.returncode != 0:
        return f"Error setting region: {result.stderr.strip()}"

    return f"Region set to n={n} s={s} e={e} w={w} res={res}"

def handle_query(gisbase, gisdbase, project, mapset, flags, output_format):
    # Platform detection
    system = platform.system()

    # GISBASE candidates
    gisbase_candidates = {
        "Linux": ["/usr/lib/grass84", "/usr/local/lib/grass84", "/opt/grass84"],
        "Darwin": ["/Applications/GRASS-8.4.app/Contents/Resources", "/usr/local/grass84"],
        "Windows": ["C:\\OSGeo4W64\\apps\\grass\\grass84", "C:\\OSGeo4W\\apps\\grass\\grass84"],
    }.get(system, [])

    # Find valid GISBASE
    gisbase = gisbase if os.path.exists(gisbase) else None
    if not gisbase:
        for path in gisbase_candidates:
            if os.path.exists(path):
                gisbase = path
                break
    if not gisbase:
        gisbase = config.GISBASE

    # Validate paths
    location_path = os.path.join(gisdbase, project)
    mapset_path = os.path.join(location_path, mapset)
    if not os.path.exists(location_path):
        return f"Error: GRASS location does not exist: {location_path}"
    if not os.path.exists(mapset_path):
        return f"Error: Mapset does not exist: {mapset_path}"

    # Run g.region
    env = os.environ.copy()
    env['GISBASE'] = gisbase
    env['GISDBASE'] = gisdbase
    env['LOCATION_NAME'] = project
    env['MAPSET'] = mapset

    cmd = ['grass', f'{gisdbase}/{project}/{mapset}', '--exec', 'g.region']
    for flag in flags:
        cmd.append(f'-{flag}')

    result = subprocess.run(cmd, capture_output=True, text=True, env=env, timeout=30)
    if result.returncode != 0:
        return f"Error: {result.stderr.strip()}"

    output = result.stdout

    # Format output
    if output_format == "raw_text":
        return output
    elif output_format == "parsed_dict":
        lines = output.strip().split("\n")
        result_dict = {}
        for line in lines:
            if ":" in line:
                key, value = line.split(":", 1)
                result_dict[key.strip()] = value.strip()
        return result_dict
    elif output_format == "json":
        lines = output.strip().split("\n")
        result_dict = {}
        for line in lines:
            if ":" in line:
                key, value = line.split(":", 1)
                result_dict[key.strip()] = value.strip()
        return result_dict  # Will be JSON dumped in main
    else:
        return f"Error: Unknown output format: {output_format}"

def main():
    # Handle help flags - check this first before accessing argv
    if len(sys.argv) == 2 and sys.argv[1] in ['--help', '-h', 'help']:
        print("GRASS Region Management Tool")
        print("Queries, sets, and creates GRASS GIS regions using g.region and g.proj commands")
        print()
        print("Usage:")
        print("  Query: python grass_g_region.py <gisbase> <gisdbase> <project> <mapset> <flags> <output_format>")
        print("  Create: python grass_g_region.py create <gisbase> <gisdbase> <location_name> <epsg> <n> <s> <e> <w>")
        print("  Set: python grass_g_region.py set <gisbase> <gisdbase> <project> <mapset> <n> <s> <e> <w> <res>")
        print()
        print("Arguments:")
        print("  gisbase     - Path to GRASS GIS installation (e.g., /usr/lib/grass84)")
        print("  gisdbase    - Path to GRASS database directory (e.g., /home/user/grassdata)")
        print("  project     - GRASS project/location name (e.g., Sample_Python_Addon)")
        print("  mapset      - GRASS mapset name (e.g., PERMANENT)")
        print("  flags       - Flags for g.region command (e.g., 'p' for print)")
        print("  output_format - Output format: raw_text, parsed_dict, or json")
        print("  location_name - Name for new location")
        print("  epsg        - EPSG code for new location (default 4326)")
        print("  n/s/e/w     - Bounds for region")
        print("  res         - Resolution for region")
        print()
        print("Examples:")
        print("  Query: python grass_g_region.py /usr/lib/grass84 /home/user/grassdata myproject PERMANENT p raw_text")
        print("  Create: python grass_g_region.py create /usr/lib/grass84 /home/user/grassdata Ottawa 4326 46 44 -74 -76")
        print("  Set: python grass_g_region.py set /usr/lib/grass84 /home/user/grassdata myproject PERMANENT 46 44 -74 -76 0.01")
        sys.exit(0)

    # Handle different modes
    if len(sys.argv) >= 2 and sys.argv[1] == "create":
        if len(sys.argv) != 10:
            print("Usage for create: python grass_g_region.py create <gisbase> <gisdbase> <location_name> <epsg> <n> <s> <e> <w>")
            sys.exit(1)
        mode = "create"
        gisbase_arg = sys.argv[2]
        gisdbase_arg = sys.argv[3]
        location_name = sys.argv[4]
        epsg = int(sys.argv[5])
        n = float(sys.argv[6])
        s = float(sys.argv[7])
        e = float(sys.argv[8])
        w = float(sys.argv[9])
    elif len(sys.argv) >= 2 and sys.argv[1] == "set":
        if len(sys.argv) != 11:
            print("Usage for set: python grass_g_region.py set <gisbase> <gisdbase> <project> <mapset> <n> <s> <e> <w> <res>")
            sys.exit(1)
        mode = "set"
        gisbase_arg = sys.argv[2]
        gisdbase_arg = sys.argv[3]
        project_arg = sys.argv[4]
        mapset_arg = sys.argv[5]
        n = float(sys.argv[6])
        s = float(sys.argv[7])
        e = float(sys.argv[8])
        w = float(sys.argv[9])
        res = float(sys.argv[10])
    else:
        # Query mode
        if len(sys.argv) != 7:
            print("Usage for query: python grass_g_region.py <gisbase> <gisdbase> <project> <mapset> <flags> <output_format>")
            print("Use --help for detailed information")
            sys.exit(1)
        mode = "query"
        gisbase_arg = sys.argv[1]
        gisdbase_arg = sys.argv[2]
        project_arg = sys.argv[3]
        mapset_arg = sys.argv[4]
        flags = sys.argv[5]
        output_format = sys.argv[6]

    if mode == "create":
        output = handle_create(gisbase_arg, gisdbase_arg, location_name, epsg, n, s, e, w)
    elif mode == "set":
        output = handle_set(gisbase_arg, gisdbase_arg, project_arg, mapset_arg, n, s, e, w, res)
    else:
        output = handle_query(gisbase_arg, gisdbase_arg, project_arg, mapset_arg, flags, output_format)

    print(json.dumps({"mode": mode, "output": output}))


if __name__ == "__main__":
    main()
