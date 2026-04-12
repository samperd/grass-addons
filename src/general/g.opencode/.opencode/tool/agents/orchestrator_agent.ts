/**
 * Orchestrator Agent v1.0
 * Core coordinator for GRASS GIS multi-agent workflow system
 * Manages agent sequencing, error recovery, and progress tracking
 */

import { tool } from '@open-code/tools';
import { AgentFramework, createMarkdownReport, withErrorRecovery } from './base/agent_framework';
import { execSync } from 'child_process';

export default tool({
  description: "Orchestrates multi-agent workflow for GRASS GIS tool development",
  args: {
    action: tool.schema.string().default('start').describe('Workflow action: start, status, cancel'),
    toolName: tool.schema.string().optional().describe('Name of the GRASS tool to develop'),
    workflowType: tool.schema.string().default('full').describe('Workflow type: full, prototype, new'),
    workflowId: tool.schema.string().optional().describe('Custom workflow ID for tracking'),
  },
  async execute(args) {
    const framework = new AgentFramework('orchestrator', args.workflowId);
    const context = framework.getContext();

    framework.log(`Starting orchestrator session: ${context.sessionId}`);

    try {
      switch (args.action) {
        case 'start':
          return await runWorkflow(framework, args);
        case 'status':
          return await getWorkflowStatus(framework, args.workflowId);
        case 'cancel':
          return await cancelWorkflow(framework, args.workflowId);
        default:
          throw new Error(`Unknown action: ${args.action}`);
      }
    } catch (error) {
      framework.log(`Workflow failed: ${error}`, 'ERROR');
      const summary = await framework.generateSummary(false, { error: error.message });
      await framework.writeMarkdownReport(summary, 'error');
      await framework.writeJsonData({ success: false, error: error.message });

      return {
        success: false,
        message: `Workflow failed: ${error.message}`,
        sessionId: context.sessionId
      };
    }
  }
});

async function runWorkflow(framework: AgentFramework, args: any) {
  const { toolName, workflowType } = args;
  const context = framework.getContext();

  if (!toolName) {
    throw new Error('toolName is required for workflow execution');
  }

  framework.log(`Starting ${workflowType} workflow for tool: ${toolName}`);

  // Determine agent sequence based on workflow type
  const agentSequence = getAgentSequence(workflowType);

  const results = {
    workflowId: context.workflowId,
    toolName,
    workflowType,
    agents: [] as any[],
    overallSuccess: true,
    startTime: new Date().toISOString()
  };

  // Execute agents in sequence
  for (const agent of agentSequence) {
    try {
      framework.log(`Executing agent: ${agent.name}`);

      const agentResult = await withErrorRecovery(
        () => executeAgent(agent, { toolName, workflowId: context.workflowId }),
        `Agent ${agent.name}`,
        2 // max retries
      );

      results.agents.push({
        name: agent.name,
        success: true,
        output: agentResult,
        timestamp: new Date().toISOString()
      });

      framework.log(`Agent ${agent.name} completed successfully`);

    } catch (error) {
      framework.log(`Agent ${agent.name} failed: ${error}`, 'ERROR');

      results.agents.push({
        name: agent.name,
        success: false,
        error: error.message,
        timestamp: new Date().toISOString()
      });

      results.overallSuccess = false;

      // For prototype mode, continue with other agents
      // For full mode, stop on first failure
      if (workflowType === 'full') {
        break;
      }
    }
  }

  results.endTime = new Date().toISOString();

  // Generate summary report
  const summary = generateWorkflowSummary(results);
  await framework.writeMarkdownReport(summary);
  await framework.writeJsonData(results);

  framework.log(`Workflow completed: ${results.overallSuccess ? 'SUCCESS' : 'PARTIAL'}`);

  return {
    success: results.overallSuccess,
    message: `Workflow ${results.overallSuccess ? 'completed successfully' : 'completed with errors'}`,
    sessionId: context.sessionId,
    results
  };
}

function getAgentSequence(workflowType: string): Array<{ name: string; command: string }> {
  const baseAgents = [
    { name: 'grass_interaction', command: 'grass_interaction_agent' },
    { name: 'code_generation', command: 'code_generation_agent' },
    { name: 'test_generation', command: 'test_agent' },
    { name: 'quality_check', command: 'quality_agent' }
  ];

  // Add documentation agent based on workflow type
  if (workflowType === 'full') {
    baseAgents.push({ name: 'documentation', command: 'documentation_agent' });
  } else if (workflowType === 'prototype') {
    // Minimal documentation for prototyping
    baseAgents.push({ name: 'documentation_minimal', command: 'documentation_agent --minimal' });
  }

  return baseAgents;
}

async function executeAgent(agent: { name: string; command: string }, params: any): Promise<any> {
  // For now, simulate agent execution
  // In full implementation, this would invoke actual OpenCode tools or run subprocesses

  const { toolName, workflowId } = params;

  // Simulate different agent behaviors
  switch (agent.name) {
    case 'grass_interaction':
      return {
        validated: true,
        recommendedModules: ['g.region', 'r.clip'],
        grassVersion: '8.4'
      };

    case 'code_generation':
      return {
        pythonGenerated: true,
        typescriptGenerated: true,
        files: [`grass_${toolName}.py`, `grass_${toolName}.ts`]
      };

    case 'test_generation':
      return {
        testsGenerated: true,
        coverage: 85,
        testFiles: [`test_grass_${toolName}.py`]
      };

    case 'quality_check':
      return {
        passed: true,
        issues: 0,
        suggestions: []
      };

    case 'documentation':
    case 'documentation_minimal':
      const isMinimal = agent.name.includes('minimal');
      return {
        docsGenerated: true,
        files: [`PLAN-${toolName}.md`, `README-${toolName}.md`],
        minimalMode: isMinimal,
        linesGenerated: isMinimal ? 5 : 50
      };

    default:
      throw new Error(`Unknown agent: ${agent.name}`);
  }
}

async function getWorkflowStatus(framework: AgentFramework, workflowId?: string): Promise<any> {
  // Read workflow status from files
  const status = await framework.readAgentOutput('orchestrator', workflowId);

  if (!status) {
    return { message: 'No active workflow found' };
  }

  return {
    workflowId: status.workflowId,
    status: status.overallSuccess ? 'completed' : 'failed',
    agentsCompleted: status.agents?.length || 0,
    lastUpdate: status.endTime || status.startTime
  };
}

async function cancelWorkflow(framework: AgentFramework, workflowId?: string): Promise<any> {
  framework.log(`Cancelling workflow: ${workflowId || 'current'}`);

  // In a real implementation, this would signal running agents to stop
  // For now, just log the cancellation

  return {
    success: true,
    message: `Workflow cancellation requested`,
    workflowId: workflowId || 'current'
  };
}

function generateWorkflowSummary(results: any): string {
  const sections = {
    'Workflow Overview': `
- **Tool**: ${results.toolName}
- **Type**: ${results.workflowType}
- **Status**: ${results.overallSuccess ? '✅ SUCCESS' : '❌ PARTIAL'}
- **Duration**: ${calculateDuration(results.startTime, results.endTime)}
- **Agents Executed**: ${results.agents.length}
`,

    'Agent Results': results.agents.map((agent: any) =>
      `### ${agent.name}
- **Status**: ${agent.success ? '✅ Success' : '❌ Failed'}
- **Timestamp**: ${agent.timestamp}
${agent.success ? `- **Output**: ${JSON.stringify(agent.output, null, 2)}` : `- **Error**: ${agent.error}`}
`
    ).join('\n'),

    'Next Steps': results.overallSuccess ?
      'All agents completed successfully. Review generated files and iterate as needed.' :
      'Some agents failed. Review error logs and rerun failed components.'
  };

  return createMarkdownReport('GRASS Tool Development Workflow Summary', sections);
}

function calculateDuration(start: string, end: string): string {
  const startTime = new Date(start).getTime();
  const endTime = new Date(end).getTime();
  const durationMs = endTime - startTime;

  if (durationMs < 1000) {
    return `${durationMs}ms`;
  } else if (durationMs < 60000) {
    return `${(durationMs / 1000).toFixed(1)}s`;
  } else {
    return `${Math.floor(durationMs / 60000)}m ${Math.floor((durationMs % 60000) / 1000)}s`;
  }
}