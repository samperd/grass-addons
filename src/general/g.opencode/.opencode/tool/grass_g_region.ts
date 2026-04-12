import { tool, question } from "@opencode-ai/plugin"
import { execSync } from "child_process"
import * as fs from "fs"
import * as path from "path"

export default tool({
  description: "Comprehensive GRASS region management: display, set, create regions, and manage boundaries/resolutions.",
  args: {
    gisbase: tool.schema.string().optional().describe("Path to GRASS GIS installation (GISBASE)"),
    gisdbase: tool.schema.string().optional().describe("Path to GRASS database (GISDBASE)"),
    project: tool.schema.string().optional().describe("GRASS project name"),
    mapset: tool.schema.string().optional().describe("GRASS mapset name"),
    flags: tool.schema.string().optional().describe("Flags for g.region command (leave empty for interactive menu)"),
    output_format: tool.schema.string().optional().describe("Output format: raw_text, parsed_dict, or json"),
    create_location: tool.schema.boolean().optional().describe("Whether to create a new location"),
    location_name: tool.schema.string().optional().describe("Name for new location"),
    epsg: tool.schema.number().optional().default(4326).describe("EPSG code for new location"),
    north: tool.schema.number().optional().describe("North bound for region"),
    south: tool.schema.number().optional().describe("South bound for region"),
    east: tool.schema.number().optional().describe("East bound for region"),
    west: tool.schema.number().optional().describe("West bound for region"),
    resolution: tool.schema.number().optional().describe("Resolution for region"),
  },
  async execute(args) {
    // Load config from Python export
    const configCmd = `python3 "${path.resolve('.opencode/tool/export_config.py')}"`
    let config
    try {
      const configOutput = execSync(configCmd, { encoding: 'utf-8', cwd: process.cwd() })
      config = JSON.parse(configOutput)
      if (config.error) {
        throw new Error(config.error)
      }
    } catch (error) {
      throw new Error(`Failed to load config: ${error.message}`)
    }

    // Interactive menu if no flags provided
    let flags = args.flags
    if (!flags) {
      const menuOptions = [
        { label: "Basic region info", description: "Print current region (-p)" },
        { label: "3D region info", description: "Print with 3D settings (-p3)" },
        { label: "Shell script style", description: "Print in key=value format (-g)" },
        { label: "Flat shell style", description: "One-line key=value format (-f)" },
        { label: "Lat/long format", description: "Geographic coordinates (-l)" },
        { label: "Extent only", description: "Print boundaries (-e)" },
        { label: "Center coordinates", description: "Print map center (-c)" },
        { label: "GMT style", description: "GMT format (-t)" },
        { label: "WMS style", description: "WMS format (-w)" },
        { label: "Resolution in meters", description: "Geodesic meters (-m)" },
        { label: "Convergence angle", description: "Grid vs true north (-n)" },
        { label: "Bounding box", description: "Lat/long on WGS84 (-b)" },
      ]
      const answers = await question({
        questions: [{
          question: "Select the type of region information to display:",
          header: "Region Info Menu",
          options: menuOptions,
          multiple: false
        }]
      })
      const selected = answers[0]
      switch (selected) {
        case "Basic region info": flags = "p"; break
        case "3D region info": flags = "p3"; break
        case "Shell script style": flags = "g"; break
        case "Flat shell style": flags = "f"; break
        case "Lat/long format": flags = "l"; break
        case "Extent only": flags = "e"; break
        case "Center coordinates": flags = "c"; break
        case "GMT style": flags = "t"; break
        case "WMS style": flags = "w"; break
        case "Resolution in meters": flags = "m"; break
        case "Convergence angle": flags = "n"; break
        case "Bounding box": flags = "b"; break
        default: flags = "p"
      }
    }

    // Apply defaults
    const gisbase = args.gisbase || config.GISBASE
    const gisdbase = args.gisdbase || config.GRASS_GISDBASE
    const project = args.project || config.GRASS_LOCATION
    const mapset = args.mapset || config.GRASS_MAPSET
    flags = flags || config.GRASS_REGIONS_FLAG
    const output_format = args.output_format || config.GRASS_REGIONS_OUTPUT_FORMAT

    // Validate paths
    if (!fs.existsSync(gisdbase)) {
      throw new Error(`GISDBASE path does not exist: ${gisdbase}`)
    }
    const mapsetPath = `${gisdbase}/${project}/${mapset}`
    if (!fs.existsSync(mapsetPath)) {
      throw new Error(`Mapset path does not exist: ${mapsetPath}. Failing gracefully.`)
    }

    // Construct and run command
    let command: string
    if (args.create_location) {
      if (!args.location_name || !args.north || !args.south || !args.east || !args.west) {
        throw new Error("For creating location, provide location_name, north, south, east, west")
      }
      command = `python3 .opencode/tool/grass_g_region.py create "${gisbase}" "${gisdbase}" "${args.location_name}" "${args.epsg || 4326}" "${args.north}" "${args.south}" "${args.east}" "${args.west}"`
    } else if (args.resolution) {
      // Set region
      if (!args.north || !args.south || !args.east || !args.west) {
        throw new Error("For setting region, provide north, south, east, west, resolution")
      }
      command = `python3 .opencode/tool/grass_g_region.py set "${gisbase}" "${gisdbase}" "${project}" "${mapset}" "${args.north}" "${args.south}" "${args.east}" "${args.west}" "${args.resolution}"`
    } else {
      // Query
      command = `python3 .opencode/tool/grass_g_region.py "${gisbase}" "${gisdbase}" "${project}" "${mapset}" "${flags}" "${output_format}"`
    }
    try {
      const result = execSync(command, { encoding: 'utf-8', cwd: process.cwd() })
      return result.trim()
    } catch (error) {
      throw new Error(`Command failed: ${error.message}`)
    }
  },
})