# GRASS Interaction Agent v1.0
*Domain expert for GRASS GIS operations and validation*

## Purpose
The GRASS Interaction Agent serves as the domain expert for all GRASS GIS operations, providing validation, recommendations, and integration support for geospatial tool development.

## Key Features

### GRASS Environment Validation
- **Installation Detection**: Scans common GRASS installation paths across platforms
- **Version Verification**: Confirms GRASS version and compatibility
- **Command Testing**: Validates core GRASS commands are accessible
- **Path Resolution**: Auto-detects GISBASE and other critical paths

### Module Recommendations
- **Tool Concept Analysis**: Analyzes requested tool functionality
- **GRASS Module Matching**: Recommends appropriate GRASS modules based on use case
- **Workflow Suggestions**: Provides step-by-step GRASS operation sequences
- **Documentation Links**: Supplies relevant GRASS manual references

### Platform Support
- **Linux**: Checks `/usr/lib/grass84`, `/usr/local/lib/grass84`, `/opt/grass84`
- **macOS**: Checks `/Applications/GRASS-8.4.app/Contents/Resources`, `/usr/local/grass84`
- **Windows**: Checks `C:\OSGeo4W64\apps\grass\grass84`, `C:\OSGeo4W\apps\grass\grass84`

## Usage Examples

### Basic Validation
```
@grass_interaction --toolConcept "raster analysis"
```

### Detailed Analysis
```
@grass_interaction --toolConcept "vector processing" --validateOnly false
```

## Validation Process

### Installation Check
```bash
# Agent checks these locations in order:
which grass
/usr/bin/grass
/usr/local/bin/grass
/opt/grass/bin/grass
# Platform-specific paths...
```

### Version Detection
```javascript
const versionOutput = execSync('grass --version');
const version = versionOutput.match(/GRASS GIS (\d+\.\d+\.?\d*)/)?.[1];
```

### Command Testing
```bash
grass --version --quiet  # Version check
grass --help | head -5   # Basic functionality
```

## Recommendation Engine

### Tool Concept Categories

#### Raster Analysis
**Input**: "raster analysis", "image processing", "grid operations"
**Modules**: `r.mapcalc`, `r.stats`, `r.resample`, `r.clip`, `r.mask`
**Workflow**:
1. `r.import` - Load raster data
2. `r.mapcalc` - Perform calculations
3. `r.stats` - Generate statistics
4. `r.out.gdal` - Export results

#### Vector Processing
**Input**: "vector analysis", "geometry operations", "spatial queries"
**Modules**: `v.info`, `v.db.select`, `v.extract`, `v.overlay`, `v.clean`
**Workflow**:
1. `v.import` - Load vector data
2. `v.clean` - Fix topology
3. `v.overlay` - Spatial operations
4. `v.out.ogr` - Export results

#### Region Management
**Input**: "region", "boundary", "computational area"
**Modules**: `g.region`, `g.proj`, `r.mask`, `v.in.region`
**Workflow**:
1. `g.region` - Set computational region
2. `r.mask` - Apply mask if needed
3. Validate region settings

### Example Recommendations Output

```
GRASS GIS Validation & Recommendations
=====================================

GRASS Installation Status
-------------------------
✅ Installed: Yes
📋 Version: 8.4.0
📍 Path: /usr/lib/grass84
🛠️ Available Commands: 15

Module Recommendations
---------------------
Primary Modules:
• r.mapcalc - Raster algebra and statistics
• r.stats - Raster statistics
• r.resample - Resample raster maps

Related Modules:
• r.clip - Clip raster maps
• r.mask - Create mask for raster operations

Suggested Workflow:
1. Import raster data with r.import or r.external
2. Perform analysis with r.mapcalc
3. Validate results with r.info and r.stats
4. Export results with r.out.gdal

Validation Checklist
-------------------
□ Verify GRASS region is set appropriately
□ Check data projections match
□ Validate input data exists and is readable
□ Ensure output locations are writable
□ Test commands with small datasets first

Documentation Links
------------------
• https://grass.osgeo.org/grass84/manuals/raster.html
• https://grass.osgeo.org/grass84/manuals/r.mapcalc.html
```

## Error Handling

### Common Issues & Solutions

#### GRASS Not Found
```
Error: GRASS GIS executable not found
Solution: Install GRASS 8.4+ from your package manager or grass.osgeo.org
```

#### Version Incompatibility
```
Warning: GRASS 7.x detected, 8.x recommended
Solution: Upgrade to GRASS 8.4 for full OpenCode compatibility
```

#### Permission Issues
```
Error: Cannot execute GRASS commands
Solution: Check file permissions and PATH environment
```

## Communication Protocol

### Input Parameters
- **toolConcept**: Description of desired tool functionality
- **workflowId**: Optional session tracking ID
- **validateOnly**: Skip recommendations, validation only

### Output Formats

#### Markdown Report
```markdown
# GRASS GIS Validation & Recommendations

## GRASS Installation Status
**Installed**: ✅ Yes
**Version**: 8.4.0
**Path**: /usr/lib/grass84

## Module Recommendations
**Primary Modules**:
- r.mapcalc
- r.stats
- r.resample

## Suggested Workflow
1. Import data
2. Process with r.mapcalc
3. Validate results
4. Export output
```

#### JSON Data
```json
{
  "validation": {
    "installed": true,
    "version": "8.4.0",
    "path": "/usr/lib/grass84",
    "error": null
  },
  "recommendations": {
    "primaryModules": ["r.mapcalc", "r.stats"],
    "relatedModules": ["r.clip", "r.mask"],
    "suggestedWorkflow": [
      "Import raster data with r.import",
      "Perform analysis with r.mapcalc"
    ],
    "documentationLinks": [
      "https://grass.osgeo.org/grass84/manuals/raster.html"
    ]
  },
  "timestamp": "2025-01-15T14:30:22Z"
}
```

## Performance Tracking

### Metrics Collected
- Installation detection time
- Command execution times
- Recommendation generation duration
- Memory usage during analysis

### Example Performance Log
```
[2025-01-15 14:30:22] START: GRASS validation
[2025-01-15 14:30:23] VALIDATION: GRASS 8.4.0 found at /usr/lib/grass84
[2025-01-15 14:30:25] ANALYSIS: Generated recommendations for "raster analysis"
[2025-01-15 14:30:25] END: Success (3.2s)
```

## Integration Points

### OpenCode Tools
- Invoked via `@grass_interaction` commands
- Results used by Code Generation Agent for module selection

### File System
- Reads: GRASS installation paths and configurations
- Writes: Validation reports and recommendations

### Other Agents
- **Orchestrator**: Called first in workflow to validate environment
- **Code Generation**: Uses recommendations for module integration
- **Documentation**: Provides GRASS-specific documentation links

## Configuration

### Default Settings
```javascript
{
  toolConcept: null,
  workflowId: null,
  validateOnly: false,
  maxValidationTime: 30000, // 30 seconds
  testCommands: ['g.version', 'g.list', 'r.info', 'v.info']
}
```

### Platform-Specific Paths
```javascript
const candidatePaths = {
  linux: ['/usr/lib/grass84', '/usr/local/lib/grass84', '/opt/grass84'],
  darwin: ['/Applications/GRASS-8.4.app/Contents/Resources'],
  win32: ['C:\\OSGeo4W64\\apps\\grass\\grass84']
}
```

## Future Enhancements

### Planned Features
- **Module Testing**: Execute test GRASS commands to verify functionality
- **Performance Profiling**: Benchmark different GRASS configurations
- **Custom Module Detection**: Identify user-installed GRASS extensions
- **Integration Testing**: Validate tool compatibility with recommended modules

### Extensibility
- **Custom Validators**: Plugin system for specialized GRASS validations
- **Module Database**: Comprehensive GRASS module knowledge base
- **Workflow Templates**: Predefined sequences for common GIS operations

---
*Generated by GRASS Interaction Agent v1.0 - GRASS Multi-Agent Framework*