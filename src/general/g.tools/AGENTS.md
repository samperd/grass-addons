# AGENTS.md - g.tools

## Project Type

GRASS GIS Python addon (CLI + wxPython GUI). Uses standard GRASS Makefile system.

## Build

```bash
cd src
make MODULE_TOPDIR=/path/to/grass
```

## Run

```bash
g.tools                     # Show status
g.tools action=install     # Install User Addons menu
g.tools action=list        # List available menus
g.tools -g                 # Launch GUI dialog
```

## Test

```bash
cd grass-addons/src
../.github/workflows/test.sh --config ../.gunittest.cfg
```

Or run specific test:
```bash
python -m pytest path/to/test.py
```

## Key Files

- `g.tools.py` - Main module (CLI + GUI using grass.script)
- `g.tools.md` - Module manual page (Markdown source)
- `g.tools.html` - Generated HTML manual
- `Makefile` - Uses `Script.make` for Python modules

## Dependencies

- `grass.script` (import as `gs`) - GRASS Python API
- `wx` (optional) - Only if wxPython available, falls back gracefully

## Non-obvious Conventions

- Uses `gs.parser()` for standard GRASS argument handling
- Menu XML stored in `~/.grass8/toolboxes/menudata.xml`
- Import wxPython conditionally (check `WXPYTHON_AVAILABLE`)
- Use `gs.message()`, `gs.warning()`, `gs.fatal()` for output

## CI/Build Commands

- Runs on `main`, `releasebranch_8_5`, `releasebranch_8_4` GRASS versions
- Requires compiled GRASS to build addons
- Uses `flake8` and `super-linter` for linting (see `.github/workflows/`)
