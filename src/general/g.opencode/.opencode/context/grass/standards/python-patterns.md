---
context: grass-patterns
priority: high
version: 1.0
updated: 2026-04-12
---

# GRASS GIS Python Patterns

## Purpose

Reference patterns for common GRASS GIS Python operations in g.opencoder.

## 1. Basic GRASS Addon Template

```python
#!/usr/bin/env python3
"""Module description."""

# %module
# % description: Short description
# % keyword: keyword1, keyword2
# %end
# %option
# % key: input
# % type: string
# % description: Input description
# % required: yes
# %end
# %option
# % key: output
# % type: string
# % description: Output description
# % required: no
# %end
# %flag
# % key: v
# % description: Verbose output
# % guisection: Output
# %end
# %flag
# % key: q
# % description: Quiet output
# % guisection: Output
# %end

import sys
import grass.script as gs


def main():
    """Main function."""
    options, flags = gs.parser()
    
    # Access options
    input_map = options["input"]
    output_map = options.get("output", "")
    
    # Check flags
    verbose = flags.get("v", False)
    quiet = flags.get("q", False)
    
    # Your logic here
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

## 2. Running GRASS Commands

### Simple Command

```python
# Run a GRASS command
gs.run_command("g.region", flags="p")

# With parameters
gs.run_command("r.mapcalc", expression="output = input * 2", overwrite=True)
```

### Command with Output

```python
# Get output as string
result = gs.read_command("g.region", flags="p")
print(result)

# Parse output
for line in result.splitlines():
    key, value = line.split(":")
    print(f"{key.strip()} = {value.strip()}")
```

### Multiple Commands

```python
# Run multiple commands
for cmd in ["g.region", "r.info"]:
    gs.run_command(cmd, map="mymap")
```

## 3. Error Handling

```python
# Check if map exists
if not gs.find_file(name, element="cell")["fullname"]:
    gs.fatal(_("Map <{}> not found").format(name))

# Check GRASS version
version = gs.version()
if version < "8.4":
    gs.fatal(_("GRASS 8.4+ required, found {}").format(version))

# Try with error handling
try:
    gs.run_command("r.clip", input=inmap, output=outmap)
except CalledProcessError:
    gs.fatal(_("r.clip failed"))
```

## 4. Config File Handling

```python
import os
from pathlib import Path


def get_config_path() -> Path:
    """Get config file path."""
    grass_user = os.environ.get("GRASS_ADDON_USER", os.path.expanduser("~/.grass"))
    return Path(grass_user) / "g.opencoder.conf"


def read_config() -> dict:
    """Read config file."""
    config_path = get_config_path()
    config = {"server": "127.0.0.1", "port": 8080}
    
    if config_path.exists():
        with open(config_path) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):
                    key, value = line.split("=", 1)
                    config[key.strip()] = value.strip()
    
    return config


def write_config(config: dict) -> None:
    """Write config file."""
    config_path = get_config_path()
    config_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(config_path, "w") as f:
        for key, value in config.items():
            f.write(f"{key} = {value}\n")
```

## 5. HTTP Client for OpenCode API

````python
import json
import urllib.request
import urllib.error


def query_opencode(prompt: str, server: str, timeout: int = 60) -> dict:
    """Query OpenCode server."""
    url = f"http://{server}:8080/api/query"
    
    payload = json.dumps({
        "prompt": prompt,
        "context": {
            "gisbase": os.environ.get("GISBASE", ""),
            "location": os.environ.get("LOCATION_NAME", ""),
            "mapset": os.environ.get("MAPSET", "PERMANENT"),
        }
    }).encode("utf-8")
    
    try:
        req = urllib.request.Request(
            url,
            data=payload,
            headers={"Content-Type": "application/json"}
        )
        with urllib.request.urlopen(req, timeout=timeout) as response:
            return json.loads(response.read().decode("utf-8"))
            
    except urllib.error.URLError as e:
        raise ConnectionError(f"Cannot connect to OpenCode server: {e}")
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid server response: {e}")


def format_response(result: dict) -> str:
    """Format OpenCode response for display."""
    if result.get("code"):
        return f"{result['response']}\n\n```bash\n{result['code']}\n```"
    return result.get("response", "No response")
````

## 6. Verbose/Quiet Output

```python
def output_message(message: str, verbose: bool = False) -> None:
    """Output message respecting verbosity settings."""
    if verbose:
        gs.verbose(message)
    else:
        gs.message(message)


def check_verbosity(flags: dict) -> tuple:
    """Check verbosity from flags."""
    verbose = flags.get("v", False)
    quiet = flags.get("q", False)
    
    # GRASS_VERBOSE values: 0=quiet, 1=WARNING, 2=PROMPT, 3=INFO, 4=DEBUG
    if quiet:
        os.environ["GRASS_VERBOSE"] = "0"
    elif verbose:
        os.environ["GRASS_VERBOSE"] = "3"
    
    return verbose, quiet
```

## 7. File Path Handling

```python
from pathlib import Path
import os


def get_gisbase() -> str:
    """Get GISBASE path."""
    gisbase = os.environ.get("GISBASE")
    if not gisbase:
        raise EnvironmentError("GISBASE not set. Please run in GRASS GIS.")
    return gisbase


def get_addon_path() -> Path:
    """Get addon installation path."""
    path = os.environ.get("GRASS_ADDON_PATH")
    if path:
        return Path(path)
    return Path(get_gisbase()) / "etc" / "python" / "script"


def ensure_directory(path: Path) -> None:
    """Ensure directory exists."""
    path.mkdir(parents=True, exist_ok=True)
```

## 8. Testing Patterns

```python
from unittest.mock import patch, MagicMock
import pytest


def test_basic_query():
    """Test basic query functionality."""
    with patch("urllib.request.urlopen") as mock_urlopen:
        mock_response = MagicMock()
        mock_response.read.return_value = b'{"response": "Answer", "status": "success"}'
        mock_urlopen.return_value.__enter__.return_value = mock_response
        
        result = query_opencode("test", "127.0.0.1")
        assert result["status"] == "success"


def test_config_parsing():
    """Test config file parsing."""
    with patch("pathlib.Path.exists", return_value=True):
        with patch("builtins.open", create=True) as mock_open:
            mock_open.return_value.__enter__.return_value.readlines.return_value = [
                "server = 192.168.1.1\n"
            ]
            config = read_config()
            assert config["server"] == "192.168.1.1"
```

## 9. Module Information

```python
def get_grass_info() -> dict:
    """Get current GRASS environment info."""
    return {
        "gisbase": gs.gisenv().get("GISBASE", ""),
        "location": gs.gisenv().get("LOCATION_NAME", ""),
        "mapset": gs.gisenv().get("MAPSET", "PERMANENT"),
        "version": gs.version(),
    }
```

## 10. List Operations

```python
def list_mapsets() -> list:
    """List available mapsets in current location."""
    result = gs.read_command("g.mapsets", flags="l")
    return [m.strip() for m in result.splitlines() if m.strip()]


def list_maps(mapset: str = "PERMANENT", element: str = "cell") -> list:
    """List raster maps in a mapset."""
    result = gs.read_command("g.list", type=element, mapset=mapset)
    return [m.strip() for m in result.splitlines() if m.strip()]
```