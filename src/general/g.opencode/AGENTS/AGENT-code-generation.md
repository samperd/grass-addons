# Code Generation Agent v1.0
*Unified creator for Python and TypeScript code generation*

## Purpose
The Code Generation Agent automatically creates complete tool implementations, generating both Python core logic and TypeScript OpenCode interfaces from high-level tool specifications.

## Key Features

### Dual Language Generation
- **Python-First Approach**: Creates core GRASS integration logic first
- **TypeScript Interface**: Generates OpenCode tool wrappers with proper schemas
- **Template Selection**: Chooses appropriate code patterns based on tool type
- **Syntax Validation**: Ensures generated code is syntactically correct

### Code Structure Patterns

#### Python Script Generation
```python
"""
GRASS GIS Tool: {toolName}
Generated for concept: {toolConcept}
"""

import sys
import json
import grass.script as gs

def main():
    # Argument parsing
    # GRASS command execution
    # Result formatting
    # Error handling

if __name__ == "__main__":
    main()
```

#### TypeScript Tool Generation
```typescript
import { tool } from '@open-code/tools';

export default tool({
  description: "{toolDescription}",
  args: {
    input: tool.schema.string().describe('Input parameter'),
    output: tool.schema.string().describe('Output parameter')
  },
  async execute(args) {
    // Python script invocation
    // Result processing
    // Error handling
  }
});
```

## Usage Examples

### Basic Tool Generation
```
@code_generation --toolName raster_clip --toolConcept "raster processing"
```

### Advanced Configuration
```
@code_generation --toolName vector_buffer --toolConcept "spatial analysis" --template spatial
```

## Template System

### Available Templates

#### Processing Template
**Use Case**: Data transformation and analysis operations
**Features**: Input validation, progress reporting, error recovery
**Example**: Raster clipping, vector buffering, statistical analysis

#### Query Template
**Use Case**: Data inspection and information retrieval
**Features**: Formatted output, multiple display options, metadata extraction
**Example**: Region information, layer statistics, projection details

#### Export Template
**Use Case**: Data conversion and file output
**Features**: Format detection, compression options, validation
**Example**: Shapefile export, GeoTIFF creation, CSV generation

### Template Selection Logic
```javascript
function selectTemplate(concept) {
  if (concept.includes('analysis') || concept.includes('processing')) {
    return 'processing';
  }
  if (concept.includes('info') || concept.includes('query')) {
    return 'query';
  }
  if (concept.includes('export') || concept.includes('convert')) {
    return 'export';
  }
  return 'processing'; // default
}
```

## Code Quality Assurance

### Generated Code Standards
- **PEP8 Compliance**: Proper Python formatting and naming
- **TypeScript Best Practices**: Interface definitions, error handling
- **GRASS Integration**: Proper module imports and command execution
- **Documentation**: Inline comments and docstrings

### Validation Checks
- **Syntax Validation**: Python compilation check
- **Import Verification**: Required modules available
- **GRASS Compatibility**: Commands exist in target version
- **Schema Validation**: TypeScript interfaces properly defined

## Communication Protocol

### Input Parameters
- **toolName**: Name for the generated tool
- **toolConcept**: High-level description of tool functionality
- **workflowId**: Optional session tracking
- **template**: Optional template override

### Output Formats

#### Markdown Report
```markdown
# Code Generation Report

## Tool Information
**Name**: raster_clip
**Concept**: raster processing
**Files Generated**: grass_raster_clip.py, grass_raster_clip.ts

## Python Implementation
```python
# Generated Python code...
```

## TypeScript Interface
```typescript
// Generated TypeScript code...
```

## Validation Results
✅ Syntax check passed
✅ Imports verified
✅ GRASS commands validated
```

#### JSON Data
```json
{
  "toolName": "raster_clip",
  "concept": "raster processing",
  "pythonGenerated": true,
  "typescriptGenerated": true,
  "files": ["grass_raster_clip.py", "grass_raster_clip.ts"],
  "validation": {
    "syntax": true,
    "imports": true,
    "grass": true
  },
  "template": "processing",
  "timestamp": "2025-01-15T14:30:22Z"
}
```

## Interactive Features

### User Prompts
- **Python Review**: "Accept generated Python script? [y/n/edit]"
- **TypeScript Review**: "Modify TypeScript interface? [y/n/customize]"
- **Template Selection**: "Choose template: processing/query/export"

### Customization Options
- **Parameter Addition**: Add custom input parameters
- **Output Format**: Choose result formatting style
- **Error Handling**: Select error recovery strategy

## Performance Tracking

### Metrics Collected
- Code generation time (Python + TypeScript)
- Template selection duration
- Validation execution time
- File size and complexity metrics

### Example Performance Log
```
[2025-01-15 14:30:22] START: Code generation for raster_clip
[2025-01-15 14:30:23] TEMPLATE: Selected 'processing' template
[2025-01-15 14:30:25] PYTHON: Generated script (45 lines)
[2025-01-15 14:30:26] TYPESCRIPT: Generated interface (32 lines)
[2025-01-15 14:30:27] VALIDATION: Syntax and imports verified
[2025-01-15 14:30:27] END: Success (5.1s)
```

## Integration Points

### OpenCode Tools
- Invoked via `@code_generation` commands
- Generated tools immediately available in OpenCode

### File System
- Writes: Generated Python and TypeScript files to project directories
- Reads: Template files and configuration

### Other Agents
- **Orchestrator**: Called after GRASS validation
- **Test Agent**: Uses generated code for test creation
- **Quality Agent**: Validates generated code quality
- **Documentation Agent**: Extracts docs from generated code

## Configuration

### Default Templates
```javascript
const templates = {
  processing: {
    pythonFeatures: ['argparse', 'error_handling', 'progress'],
    typescriptFeatures: ['zod_schema', 'async_execution', 'result_formatting']
  },
  query: {
    pythonFeatures: ['output_formatting', 'metadata'],
    typescriptFeatures: ['display_options', 'filtering']
  }
}
```

### Customization Settings
```javascript
{
  author: "GRASS Multi-Agent Framework",
  license: "GPL-3.0",
  version: "1.0.0",
  addTests: true,
  addDocs: true
}
```

## Error Handling

### Generation Failures
- **Template Missing**: Fallback to basic template
- **Syntax Errors**: Attempt auto-correction
- **Import Issues**: Suggest alternative modules
- **GRASS Incompatibility**: Downgrade to compatible commands

### Recovery Strategies
- **Partial Generation**: Generate what works, flag issues
- **Template Fallback**: Use simpler template if advanced fails
- **Manual Override**: Allow user to provide custom code sections

## Future Enhancements

### Planned Features
- **AI-Assisted Generation**: Use language models for smarter code generation
- **Template Marketplace**: Community-contributed templates
- **Code Optimization**: Performance tuning for generated code
- **Multi-Language Support**: Additional language targets

### Extensibility
- **Custom Templates**: User-defined code generation patterns
- **Plugin System**: Third-party code generators
- **Template Validation**: Automated template quality checks

---
*Generated by Code Generation Agent v1.0 - GRASS Multi-Agent Framework*