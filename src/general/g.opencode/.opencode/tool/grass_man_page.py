"""
GRASS Manual Page Retrieval Tool

Downloads GRASS GIS manual pages, converts to Markdown with metadata,
updates local links, and implements caching with MAX_AGE.

Copyright (c) 2026 David Sampson
"""

import sys
import os
import json
import re
from datetime import datetime, timedelta
from pathlib import Path
import requests
from bs4 import BeautifulSoup
import html2text
import yaml

# Add tool directory to path for import
sys.path.insert(0, os.path.dirname(__file__))
import config

def search_candidates(description):
    """Search GRASS-COMMANDS.md for command candidates matching description."""
    commands_file = os.path.join(os.path.dirname(__file__), '..', '..', 'GRASS-COMMANDS.md')
    if not os.path.exists(commands_file):
        return []

    with open(commands_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Tokenize description
    keywords = set(description.lower().split())

    candidates = []
    lines = content.split('\n')
    i = 0
    while i < len(lines):
        line = lines[i]
        # Look for [command](command.html)
        match = re.match(r'\[(\w+(?:\.\w+)*)\]\((\w+(?:\.\w+)*)\.html\)', line.strip())
        if match:
            cmd = match.group(1)
            # Description is on line i+2 (after empty line)
            desc = lines[i+2].strip() if i+2 < len(lines) else ""
            # Score based on keyword matches
            score = sum(1 for kw in keywords if kw in cmd.lower() or kw in desc.lower())
            if score > 0:
                candidates.append({
                    'command': cmd,
                    'description': desc,
                    'score': score
                })
            i += 3  # Skip empty and description lines
        else:
            i += 1

    # Sort by score descending
    candidates.sort(key=lambda x: x['score'], reverse=True)
    return candidates[:10]  # Top 10

def is_cache_stale(file_path, max_age_days):
    """Check if cached file is stale."""
    if not os.path.exists(file_path):
        return True
    mtime = datetime.fromtimestamp(os.path.getmtime(file_path))
    return datetime.now() - mtime > timedelta(days=max_age_days)

def download_manual_page(page_name, output_dir='man-pages'):
    """Download, process, and save manual page."""
    os.makedirs(output_dir, exist_ok=True)
    md_path = os.path.join(output_dir, f'{page_name}.md')

    # Check cache
    if not is_cache_stale(md_path, config.GRASS_MAN_PAGE_MAX_AGE_DAYS):
        print(json.dumps({'status': 'cached', 'file': md_path}))
        return

    # Download HTML
    url = f'https://grass.osgeo.org/grass84/manuals/{page_name}.html'
    try:
        response = requests.get(url)
        response.raise_for_status()
        html_content = response.text
    except requests.RequestException as e:
        print(json.dumps({'error': f'Failed to download {url}: {str(e)}'}))
        sys.exit(1)

    # Parse and update links
    soup = BeautifulSoup(html_content, 'html.parser')
    for a in soup.find_all('a', href=True):
        href = a['href']
        # Match GRASS manual links
        match = re.search(r'(?:https?://grass\.osgeo\.org/grass\d+/manuals/)?(\w+(?:\.\w+)*)\.html$', href)
        if match:
            local_page = match.group(1)
            a['href'] = f'{output_dir}/{local_page}.md'

    updated_html = str(soup)

    # Extract metadata
    title = soup.find('title').get_text() if soup.find('title') else page_name
    author_meta = soup.find('meta', attrs={'name': 'Author'})
    author = author_meta['content'] if author_meta else 'GRASS Development Team'

    # Extract latest change
    latest_change = None
    for p in soup.find_all('p'):
        text = p.get_text()
        if 'Latest change:' in text:
            latest_change = text.split('Latest change:')[1].strip()
            break

    # Extract tags
    keywords_meta = soup.find('meta', attrs={'name': 'keywords'})
    tags = keywords_meta['content'].split(', ') if keywords_meta else []

    # Date created from copyright
    copyright_text = None
    for text in soup.stripped_strings:
        if '©' in text:
            copyright_text = text
            break
    date_created = copyright_text.split('-')[0].strip('© ') if copyright_text else 'Unknown'

    date_downloaded = datetime.now().isoformat()

    # Convert to Markdown
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = True
    h.body_width = 0
    markdown_content = h.handle(updated_html)

    # Create YAML header
    metadata = {
        'title': title,
        'author': author,
        'date_created': date_created,
        'date_downloaded': date_downloaded,
        'latest_change': latest_change,
        'source_url': url,
        'tags': tags
    }
    yaml_header = yaml.dump(metadata, default_flow_style=False).strip()
    full_content = f'---\n{yaml_header}\n---\n\n{markdown_content}'

    # Save
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(full_content)

    print(json.dumps({'status': 'downloaded', 'file': md_path}))

def main():
    if len(sys.argv) < 2:
        print("Usage: python grass_man_page.py <description> [selected_page]")
        sys.exit(1)

    description = sys.argv[1]
    selected_page = sys.argv[2] if len(sys.argv) > 2 else None

    if selected_page:
        # Download mode
        download_manual_page(selected_page)
    else:
        # Search mode
        candidates = search_candidates(description)
        print(json.dumps(candidates))

if __name__ == "__main__":
    main()