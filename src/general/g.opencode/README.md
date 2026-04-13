# g.opencode - OpenCode AI Assistant for GRASS GIS

[![GRASS GIS module](https://img.shields.io/badge/GRASS%20GIS-module-%23009000)](https://grass.osgeo.org/)

g.opencode is a GRASS GIS addon that provides an AI assistant interface, allowing users to interact with OpenCode directly from within the GRASS GIS environment.

## Purpose

g.opencode brings OpenCode AI assistance to GRASS GIS users:

- **Ask questions** about GRASS commands and workflows
- **Get help** building GRASS GIS addons
- **Automate** GIS analysis with AI assistance

Example usage:
```
g.opencode prompt="what command should I use to find the intersection of two vectors"
g.opencode prompt="how do I merge two raster maps" server="127.0.0.1"
```

## Features

- **CLI Interface** - Run from GRASS terminal with `g.opencode`
- **Auto-GUI** - Graphical interface generated automatically via g.parser
- **Configurable** - Store server settings for reusability
- **Verbose/Quiet modes** - Control output verbosity

## Requirements

- GRASS GIS 8.x
- Python 3.8+
- Network access to OpenCode server (local or remote)

## Installation

### Option 1: From GRASS Addons (when published)

```bash
g.extension extension=g.opencode url=<addon_repo_url>
```

### Option 2: Development Installation

```bash
# Copy g.opencode to your GRASS addon path
cp -r g.opencode $GRASS_ADDON_PATH/

# Or use the included install.sh
bash install.sh
```

## Configuration

### Config File

Create a config file to store default server settings:

```bash
# Default location: ~/.grass/g.opencode.conf
```

Or set via command:
```
g.opencode server="127.0.0.1" prompt="your question"
```

## Usage

### Basic Query

```bash
g.opencode prompt="how do I merge two vector maps"
```

### With Custom Server

```bash
g.opencode prompt="your question" server="192.168.1.100"
```

### Verbose Output

```bash
g.opencode prompt="your question" --verbose
```

### Quiet Output

```bash
g.opencode prompt="your question" --quiet
```

### Help

```bash
g.opencode --help
```

## Project Structure

```
g.opencode/
├── README.md              # This file
├── DESIGN.md              # Architecture and design
├── AGENTS.md             # Development guidelines
├── install.sh            # Installation script
├── man-pages/            # Module documentation
├── testsuite/            # Test suite
└── .opencode/           # OpenCode configuration
```

## Documentation

- [g.opencode Manual](man-pages/g.opencode.md)
- [GRASS GIS](https://grass.osgeo.org/)
- [OpenCode](https://opencode.ai/)

## License

See LICENSE file for details.

## Contributing

Fork the repository and submit a pull request or open an issue.