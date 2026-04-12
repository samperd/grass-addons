# AGENTS.md - OpenCode Repository Guidelines

This document provides essential guidelines and commands for AI coding agents working on the opencode_grass_tools repository. The opencode_grass_tools project develops custom OpenCode tools for use with the GRASS GIS application.

## Build, Lint, and Test Commands

### Installation and Setup
This project develops custom OpenCode tools for GRASS GIS, so GRASS 8 must be installed. For development:

```bash
# Install GRASS GIS 8 (platform-specific, e.g., via package manager or source)
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
Follow GRASS Programming Style Guide (PEP8-based) with Ruff for automation:

```bash
# Lint all Python files
ruff check .

# Fix auto-fixable issues
ruff check --fix .

# Format code
ruff format .

# Lint specific tool file
ruff check .opencode/tool/*.py

# Format specific tool file
ruff format .opencode/tool/*.py
```

### Testing
Use pytest for testing OpenCode tools:

```bash
# Run all tests
pytest testsuite/

# Run specific test file
pytest testsuite/test_grass_region.py

# Run a single test function
pytest testsuite/test_grass_region.py::TestGrassRegion::test_main_with_insufficient_args

# Run tests with coverage
pytest --cov=. testsuite/

# Run in verbose mode
pytest -v testsuite/
```

### Build Commands
Custom OpenCode tools can be installed locally in GRASS:

```bash
# Install locally in GRASS (for addon-based tools)
# g.extension extension=tool_name url=/path/to/opencode_grass_tools operation=add

# For official contribution, integrate into grass-addons repo
# Follow: https://grass.osgeo.org/development/code-submission/
```

### Other Useful Commands
```bash
# Check Python syntax
python -m py_compile .opencode/tool/*.py

# Run script outside GRASS (for parameter parsing test)
python .opencode/tool/grass_region.py --help

# Check GRASS imports (in GRASS env)
python -c "import grass.script as gs; print('GRASS available')"

# Profile execution (in GRASS)
python -m cProfile .opencode/tool/grass_region.py
```

## Code Style Guidelines

### General Principles
- Follow PEP 8 for Python code style
- Prioritize readability and maintainability
- Use consistent naming and formatting
- Include documentation for complex logic
- Write code that can be easily tested

### Imports
```python
# Standard library imports first
import os
import sys
from pathlib import Path

# Third-party imports second
import grass.script as gs

# Local imports last
from .config import GISBASE
```

- Use absolute imports over relative imports when possible
- Group imports logically with blank lines
- Avoid wildcard imports (`from module import *`)
- Sort imports alphabetically within groups

### Formatting
- Use 4 spaces for indentation (no tabs)
- Maximum line length: 79 characters for code, 72 for docstrings/comments
- Use hanging indents for long function calls
- Add blank lines between logical sections

```python
# Good
def long_function_name(
    var_one, var_two, var_three,
    var_four
):
    print(var_one)
```

### Types
- Use type hints for function parameters and return values
- Import from `typing` module as needed

```python
from typing import List, Optional

def process_data(data: List[str]) -> Optional[dict]:
    """Process list of strings into dictionary."""
    if not data:
        return None
    return {"processed": data}
```

### Naming Conventions
- **Modules**: short, all-lowercase (underscores if needed): `grass_region.py`
- **Functions/Methods**: lowercase with underscores: `process_data()`, `get_user_input()`
- **Classes**: PascalCase: `TestGrassRegion`
- **Constants**: UPPERCASE: `GISBASE = "/usr/lib/grass84"`
- **Variables**: lowercase with underscores: `user_input`
- **Private attributes/methods**: leading underscore: `_private_method()`

### Error Handling
- Use specific exception types over generic `Exception`
- Provide meaningful error messages
- Use context managers (`with` statements) for resource management

```python
try:
    with open('file.txt', 'r') as f:
        data = f.read()
except FileNotFoundError:
    print("File not found. Please check the path.")
except PermissionError:
    print("Permission denied. Cannot read file.")
```

### Documentation
- Use triple-quoted docstrings for modules, classes, and functions
- Follow PEP 257 conventions
- Include purpose, parameters, return values, and examples

```python
def calculate_average(numbers: List[float]) -> float:
    """
    Calculate the average of a list of numbers.

    Args:
        numbers: List of float values

    Returns:
        The arithmetic mean of the numbers

    Raises:
        ValueError: If the list is empty
    """
    if not numbers:
        raise ValueError("Cannot calculate average of empty list")
    return sum(numbers) / len(numbers)
```

### Code Structure
- Use `if __name__ == "__main__":` guard for script execution
- Organize code into functions/classes for reusability
- Keep functions focused on single responsibilities
- For GRASS addons: Include module header comments for parser, use gs.parser() and gs.message()

```python
def main():
    """Main entry point for the script."""
    options, unused_flags = gs.parser()
    message = options["message"]
    gs.message(message)
    return 0

if __name__ == "__main__":
    sys.exit(main())
```

### TypeScript Guidelines (for OpenCode tools)
- Use ES6+ features and modern TypeScript patterns
- Follow consistent naming conventions (camelCase for variables/functions)
- Include JSDoc comments for complex functions
- Use async/await for asynchronous operations
- Validate inputs and handle errors gracefully

```typescript
export default tool({
  description: "Query GRASS GIS region information",
  args: {
    gisbase: tool.schema.string().optional().describe("Path to GRASS GIS installation"),
    flags: tool.schema.string().optional().default("p").describe("Flags for g.region command"),
  },
  async execute(args) {
    // Implementation here
  },
})
```

### Best Practices
- Write tests for new functionality using pytest
- Use version control (Git) for all changes
- Commit frequently with clear messages
- Avoid hardcoding values; use configuration files
- Use gs.message() for output in GRASS addons instead of print
- Validate inputs and handle edge cases
- Follow OpenCode tool structure: TypeScript/Python scripts in .opencode/tool/

### Security Considerations
- Never commit secrets or API keys
- Use environment variables for sensitive data
- Validate and sanitize user inputs
- Avoid executing untrusted code
- Keep dependencies updated

### Git Workflow
- Create feature branches for new work
- Write descriptive commit messages
- Use pull requests for code review
- Keep commits atomic and focused

## Project-Specific Notes
- This project develops custom OpenCode tools for GRASS GIS version 8
- Tools are written in both Python (for GRASS integration) and TypeScript (for OpenCode interface)
- Focus on clean, maintainable code following GRASS conventions
- Always run linting and tests before committing changes

## Cursor Rules
No Cursor rules (.cursor/rules/ or .cursorrules) are currently defined in this repository.

## Copilot Rules
No Copilot rules (.github/copilot-instructions.md) are currently defined in this repository.

This AGENTS.md serves as a living document. Update it as the project evolves and new guidelines are established.