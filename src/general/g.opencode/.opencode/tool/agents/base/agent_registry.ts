/**
 * Agent Registry v1.0
 * Centralized registry for all agents in the GRASS multi-agent system
 * Provides discovery, versioning, and capability information
 */

export interface AgentInfo {
  name: string;
  version: string;
  description: string;
  capabilities: string[];
  dependencies: string[];
  status: 'active' | 'inactive' | 'stub';
}

export class AgentRegistry {
  private static agents: Map<string, AgentInfo> = new Map();

  static register(agent: AgentInfo): void {
    this.agents.set(agent.name, agent);
    console.log(`Agent registered: ${agent.name} v${agent.version}`);
  }

  static getAgent(name: string): AgentInfo | undefined {
    return this.agents.get(name);
  }

  static getAllAgents(): AgentInfo[] {
    return Array.from(this.agents.values());
  }

  static getActiveAgents(): AgentInfo[] {
    return this.getAllAgents().filter(agent => agent.status === 'active');
  }

  static getAgentsByCapability(capability: string): AgentInfo[] {
    return this.getAllAgents().filter(agent =>
      agent.capabilities.includes(capability)
    );
  }

  static getAgentHealth(): { total: number; active: number; stub: number } {
    const agents = this.getAllAgents();
    return {
      total: agents.length,
      active: agents.filter(a => a.status === 'active').length,
      stub: agents.filter(a => a.status === 'stub').length
    };
  }
}

// Register core agents
AgentRegistry.register({
  name: 'orchestrator',
  version: '1.0',
  description: 'Core coordinator for multi-agent workflows',
  capabilities: ['orchestration', 'workflow-management', 'error-recovery'],
  dependencies: [],
  status: 'active'
});

AgentRegistry.register({
  name: 'grass_interaction',
  version: '1.0',
  description: 'GRASS GIS installation validation and module recommendations',
  capabilities: ['grass-validation', 'module-recommendation', 'api-reference'],
  dependencies: ['orchestrator'],
  status: 'active'
});

AgentRegistry.register({
  name: 'code_generation',
  version: '1.0',
  description: 'Automated generation of Python and TypeScript code for GRASS tools',
  capabilities: ['python-generation', 'typescript-generation', 'template-selection'],
  dependencies: ['orchestrator', 'grass_interaction'],
  status: 'active'
});

AgentRegistry.register({
  name: 'test_agent',
  version: '1.0',
  description: 'Automated test generation and execution for GRASS tools',
  capabilities: ['test-generation', 'test-execution', 'coverage-analysis'],
  dependencies: ['orchestrator', 'code_generation'],
  status: 'active'
});

AgentRegistry.register({
  name: 'quality_agent',
  version: '1.0',
  description: 'Code quality checking with linting, PEP8, and best practices',
  capabilities: ['linting', 'pep8-compliance', 'code-review'],
  dependencies: ['orchestrator'],
  status: 'active'
});

AgentRegistry.register({
  name: 'documentation_agent',
  version: '1.0',
  description: 'Documentation generation and plan management',
  capabilities: ['doc-generation', 'plan-management', 'readme-creation'],
  dependencies: ['orchestrator'],
  status: 'active'
});

export default AgentRegistry;