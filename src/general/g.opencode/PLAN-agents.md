# PLAN-agents.md - Multi-Agent Workflow for GRASS GIS OpenCode Tools Development

## Overview
This plan outlines the implementation of a multi-agent workflow system to streamline the development, testing, and documentation of GRASS GIS OpenCode tools. The system consists of 7 specialized agents (including base framework and registry) coordinated by an orchestrator, enabling rapid prototyping and consistent methodology for geospatial tool development.

**Status**: Week 1 (Foundation) ✅ COMPLETED - All agents implemented with working orchestrator system ready for testing.

## Goals
- **Educational**: Learn multi-agent system design and orchestration
- **Practical**: Rapid iteration and prototyping of GRASS tools
- **Business**: Develop consistent methodology for geospatial AI consulting
- **Maintainable**: Extensible system for future GRASS workflows

## Architecture Overview

### Agent Roles & Responsibilities

#### 0. Agent Framework & Registry (Base Infrastructure)
**Purpose**: Shared utilities and agent discovery system
**Components**:
- **Agent Framework v1.0**: File communication, logging, performance tracking, error recovery
- **Agent Registry v1.0**: Agent discovery, versioning, capability mapping, health monitoring
**Responsibilities**:
- Provide common utilities for all agents
- Manage agent registration and status tracking
- Handle file-based communication protocols
- Track system-wide performance metrics

#### 1. Orchestrator Agent v1.0 (Core Coordinator)
**Purpose**: Manages the entire tool development workflow
**Responsibilities**:
- Parse user requests and determine workflow path
- Manage agent sequencing with error recovery
- Track overall performance metrics and progress
- Session management and naming conventions
- Trigger detection (OpenCode invocations, git hooks)
- Rapid iteration support (prototyping mode)
- Interactive prompts at major decision points

**Performance Tracking**: Total workflow time, agent success rates
**Error Recovery**: Medium - auto-retry common issues, log detailed context, prompt on critical failures
**Communication**: Reads previous agent outputs, writes workflow summary

#### 2. GRASS Interaction Agent v1.0 (Domain Expert)
**Purpose**: All GRASS GIS operations and validation
**Responsibilities**:
- Validate GRASS installations and paths
- Test GRASS commands and provide API references
- Recommend GRASS modules for new tools
- Handle GRASS-specific error messages

**Performance Tracking**: Command execution times
**Error Recovery**: Auto-retry network issues, detailed logging
**Communication**: Provides GRASS validation reports and recommendations

#### 3. Code Generation Agent v1.0 (Unified Creator)
**Purpose**: Generates new tool skeletons and implementations
**Responsibilities**:
- Generate Python scripts (core logic first, priority sequence)
- Generate TypeScript interfaces (OpenCode integration)
- Template selection based on tool type
- Configure common patterns (error handling, JSON output)
- Validate generated code syntax

**Performance Tracking**: Generation time, code complexity metrics
**Error Recovery**: Syntax validation, template issue logging
**Communication**: Writes generated code files + implementation notes
**Interactive Prompts**: "Accept generated Python script?" / "Modify TypeScript interface?"

#### 4. Test Agent v1.0 (Validator)
**Purpose**: Comprehensive testing automation
**Responsibilities**:
- Generate pytest test templates
- Run test suites with coverage reporting
- Mock GRASS operations for testing
- Integrate with Quality Agent for test validation

**Performance Tracking**: Execution time, coverage percentages
**Error Recovery**: Auto-fix common mock issues, detailed test failure logs
**Communication**: Test results and coverage reports

#### 5. Quality Agent v1.0 (Guardian)
**Purpose**: Code quality and standards enforcement
**Responsibilities**:
- Run ruff linting/formatting + PEP8 compliance for Python
- ESLint/Prettier for TypeScript
- GRASS coding conventions validation
- Suggest improvements and best practices

**Performance Tracking**: Scan time, issue counts, fix suggestions
**Error Recovery**: Auto-fix safe issues, suggest manual fixes for complex ones
**Communication**: Quality reports with actionable recommendations

#### 6. Documentation Agent v1.0 (Communicator)
**Purpose**: Documentation generation and maintenance
**Responsibilities**:
- Generate man pages, READMEs, examples
- Manage plan files (PLAN-g.region.md, PLAN-manpages.md, etc.)
- Track plan versions and suggest updates
- Extract documentation from code changes
- Maintain change logs and release notes
- Prototyping mode: Create minimal docs (max 5 lines) with expansion placeholders

**Performance Tracking**: Generation time, completeness metrics
**Error Recovery**: Fallback to templates on parsing failures
**Communication**: Updated documentation files + change summaries
**Interactive Prompts**: "Expand documentation now or later?"

### Communication Strategy
- **File-Based with Dual Formats**: Temp files persist for review/learning
  - Human-friendly: Markdown reports with sections, examples, explanations
  - Machine-friendly: JSON data structures for agent chaining
- **Location**: `temp/agent_outputs/{workflow_id}/`
- **Naming**: `{agent_name}_{timestamp}_{step}.md` and `{agent_name}_{timestamp}_{step}.json`
- **Cleanup**: Manual or on new workflow start (user preference)

### Session Management
- **Session Naming**: `grass_agent_{agent_name}_{workflow_id}_{timestamp}`
- **Persistence**: Stateless by default, optional file-based state for continuity
- **Logging**: Simple text logs in `logs/agent_{agent_name}_{session_id}.log`
  ```
  [2025-01-15 14:30:22] START: Code generation for tool 'raster_clip'
  [2025-01-15 14:30:25] DECISION: Selected template 'processing_tool'
  [2025-01-15 14:30:28] OUTPUT: Generated Python script (45 lines)
  [2025-01-15 14:30:30] END: Success (2.8s)
  ```

### Workflow Triggers
- **Primary**: OpenCode tool invocation (`@orchestrator start workflow --tool raster_clip`)
- **Secondary**: Git hooks (pre-commit quality checks), CLI commands
- **Interactive**: Step-by-step mode for learning/debugging

### Implementation Roadmap (3 weeks total)

#### Week 1: Foundation (4 days) ✅ COMPLETED
1. ✅ Create base agent framework with file communication utilities
2. ✅ Implement Orchestrator Agent with session management
3. ✅ Build GRASS Interaction Agent
4. ✅ Set up temp file structure, logging, and naming conventions
5. ✅ Create agent registration system
6. ✅ Implement stub agents for code generation, testing, quality, and documentation
7. ✅ Create comprehensive logging and dual-format communication system

**Week 1 Results**: Full multi-agent orchestration system operational with 7 agents. Ready for workflow testing and stub agent expansion.

#### Week 2: Specialized Agents (7 days) ✅ COMPLETED
1. ✅ Code Generation Agent (unified Python+TypeScript) - **COMPLETED**
2. ✅ Test Agent (real test generation) - **COMPLETED**
3. ✅ Quality Agent (real linting & analysis) - **COMPLETED**
4. ✅ Documentation Agent (with plan management) - **COMPLETED**
5. 🔄 Agent integration testing

**Week 2 Results**: All 6 agents now have real functionality instead of mock implementations. The system can generate actual code, tests, quality reports, and documentation. Ready for integration testing and workflow execution.

#### Week 3: Workflow Integration (5 days)
1. Wire orchestrator to call agent sequence
2. Add error recovery and rollback
3. Implement rapid prototyping mode
4. Create workflow trigger system

#### Week 4: Prototyping & Refinement (5 days)
1. Build 2-3 new GRASS tools using the agent workflow
2. Refine agents based on real usage
3. Apply learnings to refactor existing tools (g.region, g.mapset)
4. Documentation and training materials

### Success Metrics
- **Rapid Iteration**: New GRASS tools prototyped in <2 hours
- **Consistency**: Standardized development process across all tools
- **Quality**: All tools pass automated quality gates
- **Performance**: Track agent execution times, success rates, resource usage
- **Maintainability**: Agent system easily extensible for new workflows
- **Business Readiness**: Methodology supports client consulting engagements

### Educational Benefits
- Multi-Agent Orchestration
- File-Based Communication Design
- Workflow Design Patterns
- Session Management
- Rapid Prototyping Techniques
- Business Applications in Geospatial AI

### Technical Considerations
- **Versioning**: Each agent includes version metadata
- **Security**: Agents run in isolated environments
- **Scalability**: Plugin architecture for new agents
- **Monitoring**: Built-in performance tracking and logging
- **Error Recovery**: Medium granularity with detailed logging
- **Interactive Mode**: Prompts at decision points, logs for review

This plan provides a comprehensive framework for learning multi-agent systems while building practical GRASS GIS development capabilities.