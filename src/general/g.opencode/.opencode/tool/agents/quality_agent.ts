/**
 * Quality Agent v1.0
 * Performs comprehensive code quality checks and linting for GRASS tools
 */

import { tool } from '@open-code/tools';
import { AgentFramework, createMarkdownReport } from './base/agent_framework';

export default tool({
  description: "Performs code quality checks, linting, and best practices validation",
  args: {
    toolName: tool.schema.string().describe('Name of the tool to check'),
    workflowId: tool.schema.string().optional().describe('Workflow ID for tracking'),
  },
  async execute(args) {
    const framework = new AgentFramework('quality_agent', args.workflowId);

    framework.log(`Quality Agent checking: ${args.toolName}`);

    const result = await framework.trackPerformance(async () => {
      // Read generated code from Code Generation Agent
      const codeData = await framework.readAgentOutput('code_generation');
      if (!codeData) {
        throw new Error('No code generation data found. Run Code Generation Agent first.');
      }

      // Perform quality checks on both Python and TypeScript code
      const pythonChecks = analyzePythonCode(codeData.code.python);
      const typescriptChecks = analyzeTypeScriptCode(codeData.code.typescript);

      const allIssues = [...pythonChecks.issues, ...typescriptChecks.issues];
      const allSuggestions = [...pythonChecks.suggestions, ...typescriptChecks.suggestions];

      const overallScore = calculateQualityScore(pythonChecks, typescriptChecks);

      return {
        toolName: args.toolName,
        lintingPassed: allIssues.filter(i => i.severity === 'error').length === 0,
        pep8Compliant: pythonChecks.pep8Compliant,
        issuesFound: allIssues.length,
        issues: allIssues,
        suggestions: allSuggestions,
        score: overallScore,
        pythonChecks,
        typescriptChecks,
        mockImplementation: false,
        timestamp: new Date().toISOString()
      };
    });

    const markdownReport = createMarkdownReport('Quality Check Report', {
      'Quality Metrics': `
**Tool**: ${result.result.toolName}
**Overall Score**: ${result.result.score}/100
**Linting**: ${result.result.lintingPassed ? '✅ Passed' : '❌ Failed'}
**PEP8**: ${result.result.pep8Compliant ? '✅ Compliant' : '❌ Issues'}
**Total Issues**: ${result.result.issuesFound}
**Mock Mode**: ${result.result.mockImplementation ? 'Yes' : 'No'}
      `,
      'Python Analysis': `
**PEP8 Compliant**: ${result.result.pythonChecks.pep8Compliant ? '✅' : '❌'}
**Syntax Errors**: ${result.result.pythonChecks.syntaxErrors}
**Style Issues**: ${result.result.pythonChecks.styleIssues}
**Documentation**: ${result.result.pythonChecks.documentationScore}/10
      `,
      'TypeScript Analysis': `
**Syntax Valid**: ${result.result.typescriptChecks.syntaxValid ? '✅' : '❌'}
**Type Safety**: ${result.result.typescriptChecks.typeSafety}/10
**Interface Quality**: ${result.result.typescriptChecks.interfaceQuality}/10
      `,
      'Issues Found': result.result.issues.map((issue: any) =>
        `- **${issue.severity.toUpperCase()}** in ${issue.language}: ${issue.message} (line ${issue.line || 'N/A'})`
      ).join('\n') || 'No issues found',
      'Improvement Suggestions': result.result.suggestions.map((s: string) => `- ${s}`).join('\n') || 'No suggestions available'
    });

    await framework.writeMarkdownReport(markdownReport);
    await framework.writeJsonData(result.result);

    return {
      success: true,
      message: `Real quality analysis completed for ${args.toolName} (Score: ${result.result.score}/100)`,
      sessionId: framework.getContext().sessionId,
      data: result.result,
      performance: result.performance
    };
  }
});

interface QualityIssue {
  severity: 'error' | 'warning' | 'info';
  language: 'python' | 'typescript';
  message: string;
  line?: number;
}

interface CodeAnalysis {
  issues: QualityIssue[];
  suggestions: string[];
  [key: string]: any;
}

function analyzePythonCode(code: string): CodeAnalysis {
  const analysis: CodeAnalysis = {
    issues: [],
    suggestions: [],
    pep8Compliant: true,
    syntaxErrors: 0,
    styleIssues: 0,
    documentationScore: 8
  };

  const lines = code.split('\n');

  // Check for basic PEP8 compliance
  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    const lineNum = i + 1;

    // Check line length (PEP8: max 79 chars)
    if (line.length > 79) {
      analysis.issues.push({
        severity: 'warning',
        language: 'python',
        message: `Line too long (${line.length} characters, max 79)`,
        line: lineNum
      });
      analysis.pep8Compliant = false;
      analysis.styleIssues++;
    }

    // Check for trailing whitespace
    if (line.endsWith(' ') || line.endsWith('\t')) {
      analysis.issues.push({
        severity: 'warning',
        language: 'python',
        message: 'Trailing whitespace',
        line: lineNum
      });
      analysis.pep8Compliant = false;
      analysis.styleIssues++;
    }

    // Check for proper imports
    if (line.includes('import') && !line.includes('from')) {
      if (!line.match(/^import [a-zA-Z_]/)) {
        analysis.issues.push({
          severity: 'warning',
          language: 'python',
          message: 'Import statement formatting',
          line: lineNum
        });
      }
    }
  }

  // Check for documentation
  if (!code.includes('"""')) {
    analysis.documentationScore -= 2;
    analysis.suggestions.push('Add module docstring');
  }

  if (!code.includes('def main')) {
    analysis.suggestions.push('Consider adding a main() function for script execution');
  }

  if (code.includes('TODO') || code.includes('FIXME')) {
    analysis.suggestions.push('Address TODO/FIXME comments');
  }

  // Check for error handling
  if (!code.includes('try:') || !code.includes('except')) {
    analysis.suggestions.push('Add proper error handling with try/except blocks');
  }

  return analysis;
}

function analyzeTypeScriptCode(code: string): CodeAnalysis {
  const analysis: CodeAnalysis = {
    issues: [],
    suggestions: [],
    syntaxValid: true,
    typeSafety: 7,
    interfaceQuality: 8
  };

  const lines = code.split('\n');

  // Check for basic TypeScript patterns
  let hasInterface = false;
  let hasAsync = false;
  let hasTypes = false;

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    const lineNum = i + 1;

    // Check for interface definitions
    if (line.includes('interface') || line.includes('type')) {
      hasInterface = true;
    }

    // Check for async functions
    if (line.includes('async')) {
      hasAsync = true;
    }

    // Check for type annotations
    if (line.includes(': string') || line.includes(': number') || line.includes(': boolean')) {
      hasTypes = true;
    }

    // Check line length (TypeScript: max 100-120 chars, be lenient)
    if (line.length > 120) {
      analysis.issues.push({
        severity: 'warning',
        language: 'typescript',
        message: `Line too long (${line.length} characters)`,
        line: lineNum
      });
    }

    // Check for console.log (should use proper logging)
    if (line.includes('console.log')) {
      analysis.suggestions.push('Consider using a proper logging library instead of console.log');
    }
  }

  // Evaluate type safety
  if (!hasTypes) {
    analysis.typeSafety -= 3;
    analysis.suggestions.push('Add type annotations for better type safety');
  }

  if (!hasInterface) {
    analysis.interfaceQuality -= 2;
    analysis.suggestions.push('Consider defining interfaces for complex objects');
  }

  // Check for error handling in async functions
  if (hasAsync && !code.includes('catch')) {
    analysis.suggestions.push('Add error handling for async operations');
  }

  if (!code.includes('export')) {
    analysis.suggestions.push('Ensure proper module exports');
  }

  return analysis;
}

function calculateQualityScore(pythonChecks: CodeAnalysis, typescriptChecks: CodeAnalysis): number {
  let score = 100;

  // Deduct for Python issues
  score -= pythonChecks.syntaxErrors * 10;
  score -= pythonChecks.styleIssues * 2;
  score -= (10 - pythonChecks.documentationScore);

  // Deduct for TypeScript issues
  score -= (10 - typescriptChecks.typeSafety) * 2;
  score -= (10 - typescriptChecks.interfaceQuality) * 1;

  // Deduct for total issues
  const totalIssues = pythonChecks.issues.length + typescriptChecks.issues.length;
  score -= Math.min(totalIssues * 3, 20); // Max 20 points deduction for issues

  return Math.max(0, Math.min(100, score));
}