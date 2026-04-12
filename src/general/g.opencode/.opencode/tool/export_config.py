"""
Export config.py variables as JSON for use by TypeScript tools.

Copyright (c) 2026 David Sampson
"""

import json
import sys
import os

# Add tool directory to path for import
sys.path.insert(0, os.path.dirname(__file__))

try:
    import config
    data = {
        'GISBASE': config.GISBASE,
        'GRASS_HOME': config.GRASS_HOME,
        'GRASS_USER': config.GRASS_USER,
        'GRASS_GISDBASE': config.GRASS_GISDBASE,
        'GRASS_LOCATION': config.GRASS_LOCATION,
        'GRASS_MAPSET': config.GRASS_MAPSET,
        'GRASS_REGIONS_OUTPUT_FORMAT': config.GRASS_REGIONS_OUTPUT_FORMAT,
        'GRASS_REGIONS_FLAG': config.GRASS_REGIONS_FLAG
    }
    print(json.dumps(data, indent=2))
except ImportError as e:
    print(json.dumps({'error': f'Failed to import config: {str(e)}'}))
    sys.exit(1)
except Exception as e:
    print(json.dumps({'error': f'Config export failed: {str(e)}'}))
    sys.exit(1)