# PLAN-manpages.md - Comprehensive Plan for grass-man-page OpenCode Tool

## Overview (Unchanged)
This plan outlines the implementation of the `grass-man-page` OpenCode tool, which allows users to search for GRASS GIS manual pages by description, select from ranked candidates, download HTML pages, convert them to Markdown with YAML metadata headers, update local links, and cache based on configurable age limits. The tool consists of a Python backend for processing and a TypeScript interface for OpenCode integration.

## Prerequisites (Unchanged)
- GRASS GIS 8.4 documentation (GRASS-COMMANDS.md for command reference).
- Python 3.8+ with virtual environment (venv) for dependencies.
- Node.js for TypeScript execution.
- OpenCode project setup (.opencode/tool/ directory).
- Libraries: beautifulsoup4, html2text, pyyaml, requests (install via pip in venv).

## Implementation Steps (Minor Updates for Consistency)
1. **Update Configuration**:
    - Add to `.opencode/tool/config.py`: `GRASS_MAN_PAGE_MAX_AGE_DAYS = 20`
    - Ensure config uses literal values for compatibility.
    - (New) Align output format with region tool: Default to JSON for structured responses (e.g., {"mode": "search", "candidates": [...]}).

2. **Create Python Script (.opencode/tool/grass_man_page.py)** (Minor Updates):
    - **Search Function**: Parse GRASS-COMMANDS.md with regex to find commands matching description keywords. Score and rank candidates by relevance.
    - **Download Function**: Fetch HTML from `https://grass.osgeo.org/grass84/manuals/{page}.html`, parse with BeautifulSoup for metadata (title, author, dates, tags), update links to local paths, convert to Markdown, add YAML header, save to `man-pages/{page}.md`.
    - **Caching**: Check file mtime; skip download if < MAX_AGE_DAYS old. (New) Use JSON output for consistency with region tool.
    - Modes: Search (output JSON candidates) or Download (process and save, return JSON status).
    - Error handling for missing files, failed downloads, parsing issues.

3. **Create TypeScript Tool (.opencode/tool/grass-man-page.ts)** (Minor Updates):
    - Use OpenCode plugin API with args: `description` (search) and `selected_page` (download).
    - Execute Python script via `execSync` using venv Python path.
    - (New) Parse JSON output; present search options or return download status in JSON format.

4. **Set Up Storage** (Unchanged):
    - Create `man-pages/` directory for Markdown files.

5. **Install Dependencies** (Unchanged):
    - `source venv/bin/activate && pip install beautifulsoup4 html2text pyyaml requests`

## Testing Plan (Minor Updates)
- **Python Unit Tests**: Mock searches, downloads, HTML parsing, caching; (New) test JSON output.
- **TS Integration**: Test OpenCode calls, JSON handling.
- **E2E**: Search "region" → select g.region → verify download, Markdown format, YAML header, link updates, caching.

## Key Features (Unchanged)
- **Search & Ranking**: Keyword-based matching from GRASS-COMMANDS.md.
- **Metadata Extraction**: YAML header with title, author (GRASS Development Team), date_created (from copyright), date_downloaded (current), latest_change (from HTML), source_url, tags (from keywords).
- **Link Updates**: Replace GRASS manual links with `man-pages/*.md`.
- **Caching**: Age-based (20 days default); re-download if stale.

## Considerations (Minor Updates)
- **Performance**: Subprocess overhead mitigated by caching.
- **Robustness**: Fallbacks for missing data; validate paths.
- **Extensibility**: Easy to add more metadata or sources.
- **Tradeoffs**: Simple search vs. advanced NLP; HTML parsing vs. manual extraction.
- (New) **Alignment with Region Tool**: Use JSON for outputs to match the region tool's structured format.

## Lessons Learned (Unchanged)
- Config evaluation issues → Use literals.
- Path resolution → Absolute paths in TS.
- Dependency management → Venv for isolation.
- Regex for docs parsing → Robust for Markdown structure.
- Caching logic → mtime-based for simplicity.

This plan ensures a complete, tested tool. For implementation, switch to build mode.