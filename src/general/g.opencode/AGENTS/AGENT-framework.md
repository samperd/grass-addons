# Agent Framework & Registry v1.0
*Shared infrastructure and agent discovery system*

## Purpose
The Agent Framework provides common utilities for all agents, while the Agent Registry manages agent discovery, versioning, and system health monitoring.

## Agent Framework Components

### File Communication System
- **Dual Format Outputs**: Markdown (human-readable) + JSON (machine-readable)
- **Persistent Storage**: Files remain for review and debugging
- **Naming Convention**: `{agent_name}_{timestamp}_{step}.md/json`
- **Location**: `temp/agent_outputs/{workflow_id}/`

### Logging Infrastructure
- **Structured Logs**: Timestamped entries with context
- **Multiple Levels**: INFO, WARN, ERROR with appropriate detail
- **File Storage**: `logs/agent_{session_id}.log`
- **Performance Tracking**: Execution time, memory usage, success metrics

### Error Recovery System
- **Retry Logic**: Configurable retry attempts with exponential backoff
- **Context Preservation**: Maintains error context for troubleshooting
- **Graceful Degradation**: Continues with partial results when possible

## Agent Registry Features

### Agent Discovery
- **Centralized Registration**: All agents register capabilities and metadata
- **Dynamic Loading**: Runtime agent discovery and status checking
- **Version Management**: Tracks agent versions for compatibility

### Health Monitoring
- **System Status**: Overall agent system health
- **Individual Status**: Per-agent active/stub/inactive status
- **Capability Mapping**: Find agents by specific functions

### Registry Data Structure
```javascript
const agentRegistry = {
  orchestrator: {
    name: 'orchestrator',
    version: '1.0',
    status: 'active',
    capabilities: ['orchestration', 'workflow-management'],
    dependencies: []
  },
  grass_interaction: {
    name: 'grass_interaction',
    version: '1.0',
    status: 'active',
    capabilities: ['grass-validation', 'module-recommendation'],
    dependencies: ['orchestrator']
  }
  // ... other agents
}
```

## Framework Usage Examples

### Basic Agent Setup
```typescript
import { AgentFramework } from './agent_base';

const framework = new AgentFramework('my_agent', 'workflow_001');
```

### File Communication
```typescript
// Write human-readable report
await framework.writeMarkdownReport(markdownContent);

// Write machine-readable data
await framework.writeJsonData(structuredData);

// Read previous agent output
const previousData = await framework.readAgentOutput('other_agent');
```

### Performance Tracking
```typescript
const result = await framework.trackPerformance(async () => {
  // Agent logic here
  return someResult;
});
console.log(`Completed in ${result.performance.duration}ms`);
```

### Error Recovery
```typescript
import { withErrorRecovery } from './agent_base';

const result = await withErrorRecovery(
  () => riskyOperation(),
  'Risky operation',
  3 // max retries
);
```

## Registry Usage Examples

### Agent Registration
```typescript
import AgentRegistry from './agent_registry';

AgentRegistry.register({
  name: 'my_agent',
  version: '1.0',
  status: 'active',
  capabilities: ['data-processing', 'validation'],
  dependencies: ['orchestrator']
});
```

### Agent Discovery
```typescript
// Find all active agents
const activeAgents = AgentRegistry.getActiveAgents();

// Find agents by capability
const validators = AgentRegistry.getAgentsByCapability('validation');

// Check system health
const health = AgentRegistry.getAgentHealth();
// { total: 7, active: 3, stub: 4 }
```

## Integration Patterns

### Inter-Agent Communication
```typescript
// Agent A writes output
await framework.writeJsonData({ result: 'data' });

// Agent B reads and processes
const inputData = await framework.readAgentOutput('agent_a');
const processedData = processData(inputData.result);
```

### Workflow State Management
```typescript
// Track workflow progress
framework.log('Starting phase 1');
const phase1Result = await executePhase1();
await framework.writeJsonData(phase1Result, 'phase1');

framework.log('Starting phase 2');
const phase1Data = await framework.readAgentOutput('current_agent', workflowId);
const phase2Result = await executePhase2(phase1Data);
```

## Configuration

### Framework Settings
```javascript
{
  logLevel: 'INFO',
  maxRetries: 2,
  retryDelay: 1000, // base delay in ms
  tempDirectory: 'temp/agent_outputs',
  logDirectory: 'logs'
}
```

### Registry Settings
```javascript
{
  autoDiscovery: true,
  versionChecking: true,
  healthMonitoring: true,
  dependencyValidation: true
}
```

## Best Practices

### File Communication
- Always write both Markdown and JSON formats
- Include timestamps in filenames for uniqueness
- Clean up old files periodically (manual or automated)

### Logging
- Use appropriate log levels (INFO for normal flow, WARN for issues, ERROR for failures)
- Include context in log messages
- Structure logs for easy parsing/filtering

### Error Recovery
- Implement retry logic for network/external operations
- Preserve error context for debugging
- Use exponential backoff for retries

### Agent Registration
- Register all capabilities accurately
- Specify dependencies clearly
- Update version numbers on changes
- Mark stub agents appropriately during development

## Future Enhancements

### Framework Extensions
- **Plugin System**: Dynamic agent loading
- **Metrics Dashboard**: Real-time performance visualization
- **Distributed Execution**: Multi-machine agent coordination
- **Caching Layer**: Result caching for repeated operations

### Registry Improvements
- **Agent Marketplace**: Community-contributed agents
- **Version Compatibility**: Automatic compatibility checking
- **Dependency Resolution**: Automatic dependency installation
- **Agent Templates**: Standardized agent creation patterns

---
*Generated by Agent Framework & Registry v1.0 - GRASS Multi-Agent Framework*