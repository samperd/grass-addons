# AGENTS.md - g.opencode Development Guidelines

This document provides essential guidelines for AI coding agents working on the g.opencode GRASS GIS addon project.

## Project Overview

g.opencode is a GRASS GIS addon that provides an OpenCode AI assistant interface, allowing users to query OpenCode directly from within GRASS GIS.

## Context Files

When implementing this project, always load context from:

- `.opencode/context/grass/standards/code-quality.md` - GRASS Python standards (MANDATORY)
- `.opencode/context/grass/standards/python-patterns.md` - Reference patterns
- `.opencode/context/grass/standards/documentation.md` - Documentation standards

See `.opencode/context/grass/navigation.md` for full context navigation.

## Build, Lint, and Test Commands

### Installation and Setup
This project requires GRASS GIS 8 and Python 3.8+:

```bash
# Install GRASS GIS 8 (platform-specific)
# Ensure Python 3.8+ is available

# Create virtual environment for development tools
python3 -m venv venv
source venv/bin/activate

# Install linting/testing tools
pip install ruff pytest

# Deactivate when done
deactivate
```

### Linting
Follow GRASS Programming Style Guide with Ruff:

```bash
# Lint all Python files
ruff check .

# Fix auto-fixable issues
ruff check --fix .

# Format code
ruff format .
```

### Testing
Use pytest for testing:

```bash
# Run all tests
pytest testsuite/

# Run specific test file
pytest testsuite/test_g_opencode.py

# Run tests with coverage
pytest --cov=. testsuite/

# Run in verbose mode
pytest -v testsuite/
```

### Running Inside GRASS
```bash
# Test the addon in GRASS
g.opencode --help

# Run with a prompt
g.opencode prompt="what command merges two vectors"
```

## Code Style Guidelines

### General Principles
- Follow PEP 8 for Python code style
- Prioritize readability and maintainability
- Use consistent naming and formatting
- Include documentation for complex logic

### Imports
```python
# Standard library imports first
import os
import sys
from pathlib import Path

# Third-party imports second (only if needed)
import requests

# GRASS modules last
import grass.script as gs
```

### Module Structure
ALL GRASS addons MUST use g.parser:

```python
#!/usr/bin/env python3

# %module
# % description: OpenCode AI assistant for GRASS GIS
# % keyword: ai, assistant, opencode
# %end
# %option
# % key: prompt
# % type: string
# % description: Your question or request to OpenCode
# % required: yes
# %end
# %flag
# % key: v
# % description: Verbose module output
# % guisection: Output
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

### Output
- Use `gs.message()` for normal output
- Use `gs.verbose()` for verbose output
- Use `gs.fatal()` for errors
- Never use raw `print()` for GRASS output

### Error Handling
```python
# Good
if not server:
    gs.fatal(_("Server address is required"))

# Good
gs.warning(_("Using default server address"))
```

## Documentation

- Use triple-quoted docstrings for modules, classes, and functions
- Follow PEP 257 conventions
- Include purpose, parameters, return values, and examples

```python
def query_opencode(prompt: str, server: str) -> dict:
    """Query OpenCode server with a prompt.
    
    Args:
        prompt: The user's question or request
        server: OpenCode server address
    
    Returns:
        Dictionary with 'response' and optional 'code' keys
    
    Raises:
        ConnectionError: If server is unreachable
    """
```

## Best Practices

- Write tests for new functionality using pytest
- Use version control (Git) for all changes
- Avoid hardcoding values; use configuration files
- Validate inputs and handle edge cases
- Follow OpenCode tool structure patterns

## Security Considerations

- Never commit secrets or API keys
- Use environment variables for sensitive data
- Validate and sanitize user inputs

## Git Workflow

- Create feature branches for new work
- Write descriptive commit messages
- Use pull requests for code review
- Keep commits atomic and focused

## Related Files

- `README.md` - User documentation
- `DESIGN.md` - Architecture and design specification
- `.opencode/context/grass/` - GRASS-specific context files

---

This AGENTS.md serves as a living document. Update it as the project evolves.