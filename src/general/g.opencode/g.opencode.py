#!/usr/bin/env python

############################################################################
#
# MODULE:       g.opencode
# AUTHOR(S):   Dave Sampson <hello@world.com>
# PURPOSE:    OpenCode AI assistant for GRASS GIS
# COPYRIGHT:   (C) 2026 Dave Sampson, and the GRASS Development Team
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
############################################################################

"""Interact with Opencode for local AI coding within GRASS"""

# %module
# % label: OpenCode AI assistant for GRASS GIS.
# % description: Interact with Opencode for local AI coding within GRASS
# % keyword: general
# % keyword: opencode
# % keyword: Artificial Intelligence (AI)
# % keyword: Large Language Model (LLM)
# % keyword: Assistant
# % keyword: Chat
# % keyword: Agentic AI
# %end
# %option
# % key: prompt
# % type: string
# % required: yes
# % multiple: no
# % label: Prompt
# % description: Your question or request to OpenCode
# % guisection: Input
# %end
# %option
# % key: server
# % type: string
# % required: no
# % multiple: no
# % label: Server address
# % description: IP address or hostname of OpenCode server
# % guisection: Configuration
# %end
# %flag
# % key: g
# % description: Launch GUI dialog instead of command line output
# % guisection: Interface
# %end
# %flag
# % key: v
# % description: Verbose module output
# % guisection: Output
# %end
# %flag
# % key: q
# % description: Quiet module output
# % guisection: Output
# %end

# Notes
#
# Find inspiration for next steps here:
#    https://discourse.osgeo.org/t/proposal-for-gsoc-2025-ai-powered-natural-language-interface-for-grass-gis/113468/29


# To Do
# [] Review https://discourse.osgeo.org/t/proposal-for-gsoc-2025-ai-powered-natural-language-interface-for-grass-gis/113468/29


import sys
import os
import json
import urllib.request
import urllib.error

import grass.script as gs


# Default configuration
DEFAULT_SERVER = "127.0.0.1"
DEFAULT_PORT = 8080
DEFAULT_TIMEOUT = 60


def get_config_path():
    """Get config file path."""
    grass_user = os.path.expanduser("~/.grass")
    return os.path.join(grass_user, "g.opencode.conf")


def read_config():
    """Read configuration from file."""
    config_path = get_config_path()
    config = {
        "server": DEFAULT_SERVER,
        "port": DEFAULT_PORT,
    }
    
    if os.path.exists(config_path):
        try:
            with open(config_path) as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#"):
                        if "=" in line:
                            key, value = line.split("=", 1)
                            config[key.strip()] = value.strip()
        except IOError as e:
            gs.warning(_("Cannot read config: {}").format(e))
    
    return config


def get_server_address(options, flags):
    """Get server address from config or option."""
    # Priority: CLI option > config file > default
    if options.get("server"):
        return options["server"]
    
    config = read_config()
    return config.get("server", DEFAULT_SERVER)


def build_request_payload(prompt):
    """Build request payload for OpenCode API."""
    # Include GRASS context if available
    context = {}
    
    try:
        gis_env = gs.gisenv()
        context = {
            "gisbase": gis_env.get("GISBASE", ""),
            "location": gis_env.get("LOCATION_NAME", ""),
            "mapset": gis_env.get("MAPSET", "PERMANENT"),
        }
    except Exception:
        pass
    
    payload = {
        "prompt": prompt,
        "context": context,
    }
    
    return json.dumps(payload).encode("utf-8")


def query_opencode(prompt, server, timeout=DEFAULT_TIMEOUT):
    """Query OpenCode server."""
    url = f"http://{server}:{DEFAULT_PORT}/api/query"
    
    payload = build_request_payload(prompt)
    
    verbose = gs.get_verbosity() >= 3
    if verbose:
        gs.verbose(_("Connecting to OpenCode server: {}").format(url))
    
    try:
        req = urllib.request.Request(
            url,
            data=payload,
            headers={"Content-Type": "application/json"}
        )
        with urllib.request.urlopen(req, timeout=timeout) as response:
            result = json.loads(response.read().decode("utf-8"))
            
            if verbose:
                gs.verbose(_("Response received"))
            
            return result
            
    except urllib.error.URLError as e:
        gs.fatal(_("Cannot connect to OpenCode server: {}").format(e))
    except urllib.error.HTTPError as e:
        gs.fatal(_("Server error: {} {}").format(e.code, e.reason))
    except json.JSONDecodeError as e:
        gs.fatal(_("Invalid server response: {}").format(e))
    except Exception as e:
        gs.fatal(_("Error: {}").format(e))


def format_response(result, verbose=False):
    """Format response for display."""
    response = result.get("response", "")
    code = result.get("code", "")
    
    if verbose:
        status = result.get("status", "")
        gs.verbose(_("Status: {}").format(status))
    
    # Output response
    gs.message(response)
    
    # Output code if available
    if code:
        gs.message("")
        gs.message("```bash")
        gs.message(code)
        gs.message("```")


def main():
    """Main entry point."""
    #### Required g.parser content ####
    flag_f = flags['f']
    option1 = options['option1']
    raster = options['raster']
    vector = options['vector']

    #### Custom module code ####
    
    # Get verbosity level
    verbose = gs.get_verbosity() >= 3
    
    # Validate prompt
    prompt = options.get("prompt", "").strip()
    if not prompt:
        gs.fatal(_("Prompt is required"))
    
    # Get server address
    server = get_server_address(options, flags)
    
    if verbose:
        gs.verbose(_("Server: {}").format(server))
    
    # Query OpenCode
    result = query_opencode(prompt, server)
    
    # Display response
    format_response(result, verbose)
    
    #### Required g.parser return ####
    return 0


if __name__ == "__main__":
    options, flags = gs.parser()
    sys.exit(main())
