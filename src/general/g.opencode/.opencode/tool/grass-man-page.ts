import { tool } from "@opencode-ai/plugin"
import { execSync } from "child_process"
import * as fs from "fs"
import * as path from "path"

export default tool({
  description: "Retrieve and convert GRASS GIS manual pages to Markdown format with local link updates and caching.",
  args: {
    description: tool.schema.string().optional().describe("Description of the GRASS tool to search for"),
    selected_page: tool.schema.string().optional().describe("Specific manual page to download (e.g., g.region)"),
  },
  async execute(args) {
    const scriptPath = path.resolve('.opencode/tool/grass_man_page.py')
    const venvPython = path.resolve('venv/bin/python3')

    if (args.selected_page) {
      // Download mode
      const cmd = `"${venvPython}" "${scriptPath}" "" "${args.selected_page}"`
      try {
        const result = execSync(cmd, { encoding: 'utf-8', cwd: process.cwd() })
        const output = JSON.parse(result.trim())
        return output
      } catch (error) {
        throw new Error(`Download failed: ${error.message}`)
      }
    } else if (args.description) {
      // Search mode
      const cmd = `"${venvPython}" "${scriptPath}" "${args.description}"`
      try {
        const result = execSync(cmd, { encoding: 'utf-8', cwd: process.cwd() })
        const candidates = JSON.parse(result.trim())
        if (candidates.length === 0) {
          return "No matching manual pages found. Try a different description."
        }
        // Present options
        const options = candidates.map((c: any, idx: number) => ({
          index: idx + 1,
          command: c.command,
          description: c.description
        }))
        return {
          message: "Select a manual page to download:",
          options: options
        }
      } catch (error) {
        throw new Error(`Search failed: ${error.message}`)
      }
    } else {
      throw new Error("Provide either a description to search or a selected_page to download.")
    }
  },
})