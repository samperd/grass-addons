---
context: grass-docs
priority: high
version: 1.0
updated: 2026-04-12
---

# GRASS GIS Documentation Standards

## Purpose

Standards for documenting g.opencoder GRASS addon.

## 1. README.md Structure

````markdown
# g.opencoder

## Purpose
Brief description of what the addon does.

## Requirements
- GRASS GIS 8.x
- Python 3.8+
- Network access to OpenCode server

## Installation

### From Addons Repository
```bash
g.extension extension=g.opencoder url=<repo_url>
````

### Manual Installation
```bash
# Copy to GRASS addon path
cp g.opencoder.py $GRASS_ADDON_PATH/
```

## Usage

### Basic
```bash
g.opencoder prompt="your question"
```

### With Server
```bash
g.opencoder prompt="question" server="127.0.0.1"
```

## Configuration

Optional config file: `~/.grass/g.opencoder.conf`

## License

See LICENSE file.
````

## 2. Man Page Structure

```markdown
---
name: g.opencoder
description: OpenCode AI assistant for GRASS GIS
---

# g.opencoder

## NAME

g.opencoder - OpenCode AI assistant for GRASS GIS

## SYNOPSIS

**g.opencoder** prompt=string [server=string] [--verbose] [--quiet]

## DESCRIPTION

g.opencoder provides an AI assistant interface within GRASS GIS, allowing users to query OpenCode...

## OPTIONS

**prompt**=string [required]
: Your question or request to OpenCode

**server**=string [optional]
: IP address of OpenCode server (default: from config or 127.0.0.1)

## FLAGS

**-v**
: Verbose module output

**-q**
: Quiet module output

## EXAMPLES

Query OpenCode:
````
g.opencoder prompt="what command merges two vectors"
```

With custom server:
```
g.opencoder prompt="how do I..." server="192.168.1.100"
```

## SEE ALSO

g.parser
g.extension

## AUTHOR

Your Name
```

## 3. Code Documentation

### Module Docstring

```python
"""
g.opencoder - OpenCode AI assistant for GRASS GIS.

This module provides an AI assistant interface within GRASS GIS,
allowing users to interact with OpenCode directly from the
GRASS terminal.

Usage:
    g.opencoder prompt="your question"

Requirements:
    - GRASS GIS 8.x
    - Python 3.8+
    - Network access to OpenCode server
"""
```

### Function Docstring

```python
def query_opencode(prompt: str, server: str, timeout: int = 60) -> dict:
    """Query OpenCode server with a prompt.
    
    Args:
        prompt: The user's question or request
        server: OpenCode server address
        timeout: Request timeout in seconds
    
    Returns:
        Dictionary with 'response' and optional 'code' keys
    
    Raises:
        ConnectionError: If server is unreachable
        ValueError: If response is invalid
    
    Example:
        >>> result = query_opencode("merge vectors", "127.0.0.1")
        >>> print(result['response'])
    """
```

## 4. Changelog Format

```markdown
# Changelog

## [1.0.0] - 2026-04-12

### Added
- Initial release
- CLI with g.parser integration
- Basic OpenCode API client
- Verbose and quiet flags

### Known Issues
- None yet
```

## 5. Version Numbering

Follow Semantic Versioning (MAJOR.MINOR.PATCH):
- MAJOR: Breaking changes
- MINOR: New features (backward compatible)
- PATCH: Bug fixes

## 6. Required Files

| File | Description |
|------|-------------|
| README.md | User documentation |
| LICENSE | License terms |
| CHANGELOG.md | Version history |
| *.py | Source code |

## 7. Badges (Optional)

```markdown
[![GRASS GIS module](https://img.shields.io/badge/GRASS%20GIS-module-%23009000)](https://grass.osgeo.org/)
[![License: GPL-3](https://img.shields.io/badge/License-GPL--3-green)](LICENSE)
```