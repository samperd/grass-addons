"""
GRASS Mapset Management Tool

Provides simple interface for listing GRASS mapsets using keyword matching.

Copyright (c) 2026 David Sampson
"""

import sys
import os
import subprocess
import json

# Add tool directory to path for import
sys.path.insert(0, os.path.dirname(__file__))
import config

def run_grass_command(cmd_args):
    """Run a GRASS command with proper environment."""
    env = os.environ.copy()
    env['GISBASE'] = config.GISBASE
    env['GISDBASE'] = config.GRASS_GISDBASE
    env['LOCATION_NAME'] = config.GRASS_LOCATION
    env['MAPSET'] = config.GRASS_MAPSET

    # Use grass command to execute
    full_cmd = ['grass', f'{config.GRASS_GISDBASE}/{config.GRASS_LOCATION}/{config.GRASS_MAPSET}', '--exec'] + cmd_args

    try:
        result = subprocess.run(full_cmd, capture_output=True, text=True, env=env, timeout=30)
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            return f"Error: {result.stderr.strip()}"
    except subprocess.TimeoutExpired:
        return "Error: Command timed out"
    except Exception as e:
        return f"Error: {str(e)}"

def interpret_action(action):
    """Simple keyword matching for actions."""
    action_lower = action.lower()
    if 'list' in action_lower:
        return ['g.mapset', '-l']
    elif 'print' in action_lower or 'current' in action_lower:
        return ['g.mapset', '-p']
    elif 'create' in action_lower:
        # Extract mapset name (assume last word)
        words = action.split()
        if len(words) >= 2:
            mapset_name = words[-1]
            return ['g.mapset', '-c', mapset_name]
        else:
            return None
    else:
        return None

def main():
    if len(sys.argv) < 2:
        print(json.dumps({'error': 'Usage: python grass_g_mapset.py "<action>"'}))
        sys.exit(1)

    action = sys.argv[1]
    cmd = interpret_action(action)

    if cmd:
        output = run_grass_command(cmd)
        print(json.dumps({'command': cmd, 'output': output}))
    else:
        print(json.dumps({'error': f'Could not interpret action: {action}. Try "list mapsets" or "print current mapset".'}))

if __name__ == "__main__":
    main()