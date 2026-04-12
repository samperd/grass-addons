import { tool } from "@opencode-ai/plugin"
import { execSync } from "child_process"
import * as path from "path"

export default tool({
  description: "Manage GRASS mapsets with simple keyword interpretation (e.g., 'list mapsets').",
  args: {
    action: tool.schema.string().describe("Action to perform, e.g., 'list mapsets' or 'print current mapset'"),
  },
  async execute(args) {
    const scriptPath = path.resolve('.opencode/tool/grass_g_mapset.py')
    const venvPython = path.resolve('venv/bin/python3')

    const cmd = `"${venvPython}" "${scriptPath}" "${args.action}"`
    try {
      const result = execSync(cmd, { encoding: 'utf-8', cwd: process.cwd() })
      const output = JSON.parse(result.trim())
      return output
    } catch (error) {
      throw new Error(`Execution failed: ${error.message}`)
    }
  },
})