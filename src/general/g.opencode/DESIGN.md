# g.opencode Design Specification

## Overview

g.opencode is a GRASS GIS addon that provides an AI assistant (OpenCode client) interface, allowing users to interact with OpenCode from within GRASS GIS.

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        GRASS GIS                            │
│  ┌─────────────────────────────────────────────────────┐       │
│  │              g.opencode (CLI/GUI)                │       │
│  │  ┌─────────────┐  ┌──────────────┐  ┌────────┐  │       │
│  │  │  g.parser │  │   Config   │  │  HTTP  │  │       │
│  │  │  (flags) │  │  Manager   │  │ Client │  │       │
│  │  └─────────────┘  └──────────────┘  └────────┘  │       │
│  └─────────────────────────────────────────────────────┘       │
└─────────────────────────────────────────────────────────────┘
                              │
                              │ REST/JSON (HTTP)
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                   OpenCode Server                          │
│                   (external location)                      │
│                                                             │
│         ┌──────────────┐  ┌──────────────┐                 │
│         │   REST API  │  │   AI Model   │                 │
│         │  (JSON)    │  │  (Claude,   │                 │
│         │            │  │   GPT, etc.) │                 │
│         └──────────────┘  └──────────────┘                 │
└─────────────────────────────────────────────────────────────┘
```

## Components

### 1. CLI Tool (g.opencode)

The main Python module that provides both CLI and auto-generated GUI.

**Location**: Primary addon script (e.g., `g.opencode.py`)

### 2. Config Manager

Manages configuration settings:
- Server URL/IP address
- Default options
- Session history (optional)

**Config file**: `~/.grass/g.opencode.conf` or similar

### 3. HTTP Client

Direct REST/JSON calls to OpenCode server:
- POST requests with JSON payloads
- Handle responses
- Error handling

## CLI Interface

### g.parser Header Format

```python
# %module
# % description: OpenCode AI assistant for GRASS GIS
# % keyword: ai, assistant, opencode, chat
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
```

### Usage Examples

```bash
# Basic query (uses config default for server)
g.opencode prompt="how do I merge two vectors"

# With explicit server
g.opencode prompt="how do I merge two vectors" server="127.0.0.1"

# Verbose output
g.opencode prompt="your question" --verbose

# Quiet output
g.opencode prompt="your question" --quiet

# Auto-generated GUI (no arguments)
g.opencode
```

## Configuration

### Config File Format

```ini
[default]
server = 127.0.0.1
port = 8080
model = claude
timeout = 60
```

### Config Precedence

1. CLI argument (`server="..."`)
2. Config file (`~/.grass/g.opencode.conf`)
3. Environment variable (`OPENCODE_SERVER`)
4. Default (`127.0.0.1`)

### Config Command (Future)

```bash
g.opencode config --server="192.168.1.100"
g.opencode config --show
```

## API Interaction

### Request Format

```json
{
  "prompt": "your question here",
  "context": {
    "gisbase": "/usr/lib/grass84",
    "location": "myproject",
    "mapset": "PERMANENT"
  }
}
```

### Response Format

```json
{
  "response": "You can use v.overlay with operator=and...",
  "code": "v.overlay input=map1 output=result operator=and",
  "status": "success"
}
```

## Error Handling

| Error | Handling |
|-------|----------|
| No server | Show config help message |
| Connection fail | Explain network issue |
| Invalid response | Show raw response |
| Empty prompt | g.parser validation |

## Testing Strategy

- Unit tests for config parsing
- Unit tests for API client
- Mock tests for HTTP responses
- Integration tests (when server available)

## Future Enhancements (Post-MVP)

- GUI component (wxPython)
- Session history
- Command suggestion mode
- Code generation mode
- Multi-turn conversations

## Development Guidelines

See AGENTS.md for coding standards and development process.