# Orchestrator Agent v1.0
*Core coordinator for GRASS GIS multi-agent workflow system*

## Purpose
The Orchestrator Agent manages the entire tool development workflow, coordinating specialized agents to automate GRASS GIS tool creation from concept to completion.

This documents explains the expected behaviour of the orchestrator_agent.py agent.

Responsible opencode agent: ../opencode/tool/agents/base/orchestrator_agent.py agent.

## Key Features

### Workflow Management
- **Request Parsing**: Analyzes user requests and determines required workflow steps
- **Agent Sequencing**: Calls agents in correct order with proper error handling
- **Progress Tracking**: Monitors workflow status and provides real-time updates
- **Result Aggregation**: Combines outputs from all agents into comprehensive reports

### Session Management
- **Unique Sessions**: Generates `grass_agent_orchestrator_{workflow_id}_{timestamp}` IDs
- **State Tracking**: Maintains workflow state across agent calls
- **Logging**: Detailed activity logs in `logs/orchestrator_{session_id}.log`

### Error Recovery
- **Medium Granularity**: Auto-retries common issues, logs context for troubleshooting
- **Workflow Continuation**: Continues with remaining agents on non-critical failures
- **User Prompts**: Interactive prompts for major decisions

## Supported Workflow Types

### Full Workflow
Complete pipeline: GRASS Validation → Code Generation → Testing → Quality → Documentation
- Best for production tools
- Includes comprehensive documentation

### Prototype Workflow
All agents but minimal documentation (max 5 lines)
- Fast iteration for learning and experimentation
- Documentation placeholders for later expansion

### New Workflow
Focused on initial tool creation (GRASS + Code Generation)
- Quick start for new tool concepts
- Skips testing and documentation initially

## Usage Examples

### Starting a New Tool Workflow
```
@orchestrator start workflow --tool raster_clip --workflowType prototype
```

### Checking Workflow Status
```
@orchestrator status --workflowId workflow_001
```

### Canceling a Workflow
```
@orchestrator cancel --workflowId workflow_001
```

## Agent Sequence Logic

```javascript
const agentSequence = {
  full: [
    'grass_interaction',
    'code_generation',
    'test_agent',
    'quality_agent',
    'documentation_agent'
  ],
  prototype: [
    'grass_interaction',
    'code_generation',
    'test_agent',
    'quality_agent',
    'documentation_minimal'
  ],
  new: [
    'grass_interaction',
    'code_generation'
  ]
}
```

## Communication Protocol

### Input
- **toolName**: Name of the GRASS tool to develop
- **workflowType**: Type of workflow (full/prototype/new)
- **workflowId**: Optional custom identifier

### Output
- **Markdown Report**: Human-readable workflow summary
- **JSON Data**: Machine-readable results for chaining
- **Session Logs**: Detailed execution logs

### Example Output Structure
```json
{
  "success": true,
  "sessionId": "grass_agent_orchestrator_workflow_001_20250115",
  "results": {
    "workflowId": "workflow_001",
    "toolName": "raster_clip",
    "overallSuccess": true,
    "agents": [
      {
        "name": "grass_interaction",
        "success": true,
        "output": { "validated": true, "version": "8.4" }
      }
    ]
  }
}
```

## Error Handling

### Common Scenarios
- **Agent Failure**: Retry up to 2 times, log error, continue if non-critical
- **GRASS Not Found**: Halt workflow, provide installation guidance
- **Invalid Tool Name**: Prompt for clarification
- **Timeout**: Auto-retry with exponential backoff

### Recovery Strategies
- **Partial Success**: Complete successful agents, flag failed ones
- **Rollback**: Clean up generated files on critical failures
- **Manual Intervention**: Prompt user for complex error resolution

## Performance Tracking

### Metrics Collected
- Total workflow duration
- Individual agent execution times
- Success/failure rates per agent
- Resource usage (memory, file operations)

### Monitoring Dashboard
```
Workflow Performance Summary
├── Total Time: 45.2s
├── Agents Executed: 5/5
├── Success Rate: 100%
└── Peak Memory: 127MB
```

## Integration Points

### OpenCode Tools
- Invoked via `@orchestrator` commands
- Returns structured data for further processing

### File System
- Reads: Previous agent outputs from `temp/agent_outputs/{workflow_id}/`
- Writes: Results to `temp/agent_outputs/{workflow_id}/orchestrator_{timestamp}.*`

### Other Agents
- Calls all specialized agents in sequence
- Passes workflow context and parameters
- Aggregates agent outputs into final report

## Configuration

### Default Settings
```javascript
{
  action: 'start',
  workflowType: 'full',
  maxRetries: 2,
  timeoutMinutes: 30
}
```

### Customization
- Workflow sequences can be extended
- Agent parameters can be modified
- Error handling strategies configurable

## Future Enhancements

### Planned Features
- Parallel agent execution for independent tasks
- Workflow templates for common tool types
- Integration with CI/CD pipelines
- Advanced error recovery with AI suggestions

### Extensibility
- Plugin system for custom workflow steps
- Agent discovery for dynamic workflows
- Performance optimization and caching

---
*Generated by Orchestrator Agent v1.0 - GRASS Multi-Agent Framework*