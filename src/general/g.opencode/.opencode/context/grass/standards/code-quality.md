---
context: grass-standards
priority: critical
version: 1.0
updated: 2026-04-12
---

# GRASS GIS Python Code Quality Standards

## Purpose

These standards ensure all Python code for g.opencoder maintains consistency, quality, and proper GRASS integration.

## Core Requirements

### 1. Module Header

Every GRASS addon script MUST include a proper header:

```python
#!/usr/bin/env python3
############################################################################
#
# MODULE:       g.opencoder
# AUTHOR(S):   Your Name
# PURPOSE:     Short description of what the module does
# COPYRIGHT:   (C) 2026 Your Name, and the GRASS Development Team
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
```

### 2. g.parser Integration

ALL GRASS addons MUST use g.parser for CLI/GUI support:

```python
# %module
# % description: Your module description
# % keyword: keyword1, keyword2
# %end
# %option
# % key: option_name
# % type: string
# % description: Option description
# % required: yes
# %end
# %flag
# % key: f
# % description: Flag description
# %end

import sys
import grass.script as gs

def main():
    options, flags = gs.parser()
    # Your code here
    return 0

if __name__ == "__main__":
    sys.exit(main())
```

### 3. Imports

Organize imports in this order:

```python
# Standard library
import sys
import os
import json
from pathlib import Path
from typing import Optional, List

# Third-party (only if needed)
import requests

# GRASS modules
import grass.script as gs
import grass.lib.gis as gis
```

### 4. Error Handling

- Use `gs.fatal()` for fatal errors
- Use `gs.warning()` for warnings
- Always return meaningful error messages
- Never use raw `print()` for errors

```python
# Good
if not os.path.exists(input_file):
    gs.fatal(_("Input file does not exist: {}").format(input_file))

# Good
gs.warning(_("Optional module not found, using fallback"))
```

### 5. Output

- Use `gs.message()` for normal output
- Use `gs.verbose()` for verbose output
- Use `gs.debug()` for debug output
- Never use raw `print()` for user output

```python
gs.message(_("Processing complete"))
gs.verbose(_("Detailed progress info"))
```

### 6. Internationalization

Use GRASS translation functions:

```python
from grass.script import _

gs.message(_("Your message here"))
gs.fatal(_("Error: {}").format(error_details))
```

### 7. Type Hints

Include type hints for all function parameters and return values:

```python
def process_region(north: float, south: float, east: float, west: float) -> bool:
    """Process region bounds."""
    return True
```

## Naming Conventions

| Element | Convention | Example |
|---------|-----------|---------|
| Module | lowercase, underscore | `g_opencoder.py` |
| Function | lowercase, underscore | `main()`, `process_data()` |
| Class | PascalCase | `RegionHandler` |
| Constant | UPPERCASE | `DEFAULT_SERVER` |
| Variable | lowercase, underscore | `gisbase_path` |

## Code Structure

### Minimal Function Structure

```python
#!/usr/bin/env python3
"""g.opencoder - OpenCode AI assistant for GRASS GIS."""

import sys
import json
import urllib.request
import urllib.error

import grass.script as gs


def main():
    """Main entry point."""
    options, flags = gs.parser()
    
    prompt = options["prompt"]
    server = options.get("server", "127.0.0.1")
    
    # Build request
    data = json.dumps({"prompt": prompt}).encode("utf-8")
    
    try:
        req = urllib.request.Request(
            f"http://{server}:8080/api/query",
            data=data,
            headers={"Content-Type": "application/json"}
        )
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode("utf-8"))
            
    except urllib.error.URLError as e:
        gs.fatal(_("Cannot connect to OpenCode server: {}").format(e))
    
    gs.message(result.get("response", ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

## Linting Rules

### Must Pass

- No syntax errors
- All imports resolve
- All functions have docstrings
- Proper g.parser header

### Should Pass

- PEP8 style (max line length: 79)
- No unused imports
- Meaningful variable names

## Testing Requirements

- Unit tests for all functions
- Mock GRASS API calls
- Test error handling paths
- Test config parsing