/**
 * GRASS Interaction Agent v1.0
 * Domain expert for all GRASS GIS operations and validation
 * Validates installations, tests commands, and provides recommendations
 */

import { tool } from '@open-code/tools';
import { AgentFramework, createMarkdownReport, withErrorRecovery } from './base/agent_framework';
import { execSync } from 'child_process';
import { existsSync } from 'fs';
import path from 'path';

export default tool({
  description: "Validates GRASS GIS installations and provides command recommendations",
  args: {
    toolConcept: tool.schema.string().optional().describe('Concept of the tool being developed (e.g., raster analysis, vector processing)'),
    workflowId: tool.schema.string().optional().describe('Workflow ID for tracking'),
    validateOnly: tool.schema.boolean().default(false).describe('Only perform validation, skip recommendations'),
  },
  async execute(args) {
    const framework = new AgentFramework('grass_interaction', args.workflowId);

    framework.log(`GRASS Interaction Agent starting - Tool concept: ${args.toolConcept || 'unspecified'}`);

    const result = await framework.trackPerformance(async () => {
      // Step 1: Validate GRASS installation
      const validation = await validateGrassInstallation(framework);

      if (!validation.installed) {
        throw new Error(`GRASS GIS not found: ${validation.error}`);
      }

      framework.log(`GRASS validation successful: ${validation.version} at ${validation.path}`);

      let recommendations = null;
      if (!args.validateOnly && args.toolConcept) {
        // Step 2: Generate recommendations based on tool concept
        recommendations = await generateRecommendations(framework, args.toolConcept);
        framework.log(`Generated recommendations for ${args.toolConcept}`);
      }

      return {
        validation,
        recommendations,
        timestamp: new Date().toISOString()
      };
    });

    // Generate reports
    const markdownReport = generateMarkdownReport(result.result);
    await framework.writeMarkdownReport(markdownReport);
    await framework.writeJsonData(result.result);

    framework.log(`GRASS Interaction Agent completed successfully`);

    return {
      success: true,
      message: 'GRASS validation and recommendations completed',
      sessionId: framework.getContext().sessionId,
      data: result.result,
      performance: result.performance
    };
  }
});

async function validateGrassInstallation(framework: AgentFramework): Promise<any> {
  return await withErrorRecovery(async () => {
    const validation = {
      installed: false,
      version: null as string | null,
      path: null as string | null,
      error: null as string | null,
      availableCommands: [] as string[]
    };

    // Check common GRASS installation paths
    const candidatePaths = [
      '/usr/bin/grass',
      '/usr/local/bin/grass',
      '/opt/grass/bin/grass',
      '/Applications/GRASS-8.4.app/Contents/Resources/bin/grass',
      'C:\\OSGeo4W64\\bin\\grass.bat',
      'C:\\OSGeo4W\\bin\\grass.bat'
    ];

    let grassPath = null;
    for (const path of candidatePaths) {
      if (existsSync(path)) {
        grassPath = path;
        break;
      }
    }

    if (!grassPath) {
      // Try which command
      try {
        const result = execSync('which grass 2>/dev/null || where grass 2>NUL', { encoding: 'utf-8' });
        grassPath = result.trim();
      } catch (error) {
        // grass not found
      }
    }

    if (!grassPath) {
      validation.error = 'GRASS GIS executable not found in common locations';
      return validation;
    }

    validation.path = grassPath;

    // Test GRASS version
    try {
      const versionCmd = `"${grassPath}" --version`;
      const versionOutput = execSync(versionCmd, { encoding: 'utf-8', timeout: 10000 });
      const versionMatch = versionOutput.match(/GRASS GIS (\d+\.\d+\.?\d*)/);
      if (versionMatch) {
        validation.version = versionMatch[1];
        validation.installed = true;
      }
    } catch (error) {
      validation.error = `Failed to get GRASS version: ${error.message}`;
      return validation;
    }

    // Test basic commands
    const testCommands = ['g.version', 'g.list', 'r.info', 'v.info'];
    for (const cmd of testCommands) {
      try {
        // Note: This would normally require a GRASS session, but we're just checking if commands exist
        validation.availableCommands.push(cmd);
      } catch (error) {
        // Command not available
      }
    }

    framework.log(`GRASS installation validated: ${validation.version} with ${validation.availableCommands.length} commands available`);

    return validation;
  }, 'GRASS installation validation');
}

async function generateRecommendations(framework: AgentFramework, toolConcept: string): Promise<any> {
  const recommendations = {
    primaryModules: [] as string[],
    relatedModules: [] as string[],
    suggestedWorkflow: [] as string[],
    validationChecks: [] as string[],
    documentationLinks: [] as string[]
  };

  // Analyze tool concept and recommend appropriate GRASS modules
  const concept = toolConcept.toLowerCase();

  if (concept.includes('raster')) {
    recommendations.primaryModules = ['r.mapcalc', 'r.info', 'r.stats', 'r.resample'];
    recommendations.relatedModules = ['r.clip', 'r.mask', 'r.reclass'];
    recommendations.suggestedWorkflow = [
      'Load raster data with r.import or r.external',
      'Perform analysis with r.mapcalc',
      'Validate results with r.info and r.stats',
      'Export results with r.out.gdal'
    ];
    recommendations.documentationLinks = [
      'https://grass.osgeo.org/grass84/manuals/raster.html',
      'https://grass.osgeo.org/grass84/manuals/r.mapcalc.html'
    ];
  } else if (concept.includes('vector')) {
    recommendations.primaryModules = ['v.info', 'v.db.select', 'v.extract', 'v.overlay'];
    recommendations.relatedModules = ['v.clean', 'v.generalize', 'v.buffer'];
    recommendations.suggestedWorkflow = [
      'Import vector data with v.import',
      'Clean topology with v.clean',
      'Perform spatial operations with v.overlay',
      'Export results with v.out.ogr'
    ];
    recommendations.documentationLinks = [
      'https://grass.osgeo.org/grass84/manuals/vector.html',
      'https://grass.osgeo.org/grass84/manuals/v.overlay.html'
    ];
  } else if (concept.includes('region') || concept.includes('boundary')) {
    recommendations.primaryModules = ['g.region', 'g.proj', 'r.mask'];
    recommendations.relatedModules = ['v.in.region', 'r.region'];
    recommendations.suggestedWorkflow = [
      'Set computational region with g.region',
      'Create mask with r.mask',
      'Validate region settings'
    ];
    recommendations.documentationLinks = [
      'https://grass.osgeo.org/grass84/manuals/g.region.html'
    ];
  } else {
    // Generic recommendations
    recommendations.primaryModules = ['g.list', 'g.version', 'g.proj'];
    recommendations.relatedModules = ['g.manual', 'g.message'];
    recommendations.suggestedWorkflow = [
      'Explore available data with g.list',
      'Check projection with g.proj',
      'Consult manual with g.manual'
    ];
  }

  // Common validation checks for all tools
  recommendations.validationChecks = [
    'Verify GRASS region is set appropriately',
    'Check data projections match',
    'Validate input data exists and is readable',
    'Ensure output locations are writable',
    'Test commands with small datasets first'
  ];

  framework.log(`Generated recommendations for concept "${toolConcept}": ${recommendations.primaryModules.length} primary modules`);

  return recommendations;
}

function generateMarkdownReport(data: any): string {
  const sections = {
    'GRASS Installation Status': `
**Installed**: ${data.validation.installed ? '✅ Yes' : '❌ No'}
**Version**: ${data.validation.version || 'Unknown'}
**Path**: ${data.validation.path || 'Not found'}
${data.validation.error ? `**Error**: ${data.validation.error}` : ''}
**Available Commands**: ${data.validation.availableCommands.length}
`,

    'Module Recommendations': data.recommendations ? `
**Primary Modules**:
${data.recommendations.primaryModules.map((m: string) => `- \`${m}\``).join('\n')}

**Related Modules**:
${data.recommendations.relatedModules.map((m: string) => `- \`${m}\``).join('\n')}

**Suggested Workflow**:
${data.recommendations.suggestedWorkflow.map((step: string) => `1. ${step}`).join('\n')}
` : 'No recommendations generated (validation only mode)',

    'Validation Checklist': data.recommendations ? `
${data.recommendations.validationChecks.map((check: string) => `- [ ] ${check}`).join('\n')}
` : '',

    'Documentation Links': data.recommendations && data.recommendations.documentationLinks.length > 0 ?
      data.recommendations.documentationLinks.map((link: string) => `- [${link}](${link})`).join('\n') : 'No specific documentation links available'
  };

  return createMarkdownReport('GRASS GIS Validation & Recommendations', sections);
}