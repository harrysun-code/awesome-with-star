#!/usr/bin/env python3
"""
Script to fetch sindresorhus/awesome README, extract projects, get star counts,
and download all project READMEs to awesome directory.
"""

import os
import re
import json
import time
import subprocess
import base64
from pathlib import Path

def fetch_url(url):
    """Fetch URL content using curl."""
    try:
        result = subprocess.run(
            ['curl', '-s', '--connect-timeout', '30', '--max-time', '60', url],
            capture_output=True,
            text=True,
            encoding='utf-8'
        )
        if result.returncode == 0:
            return result.stdout
        return None
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

def get_github_stars(owner, repo):
    """Get GitHub stars for a repository using GraphQL API."""
    query = """
    {
      repository(owner: \"%s\", name: \"%s\") {
        stargazerCount
      }
    }
    """ % (owner, repo)

    try:
        result = subprocess.run(
            ['curl', '-s', '--connect-timeout', '30', '--max-time', '60',
             '-X', 'POST', '-H', 'Content-Type: application/json',
             '-H', 'Accept: application/vnd.github.v3+json',
             '-d', json.dumps({'query': query}),
             'https://api.github.com/graphql'],
            capture_output=True,
            text=True,
            encoding='utf-8'
        )
        if result.returncode == 0:
            data = json.loads(result.stdout)
            if 'data' in data and data['data'] and 'repository' in data['data']:
                return data['data']['repository']['stargazerCount']
    except Exception:
        pass

    # Fallback to REST API
    url = f"https://api.github.com/repos/{owner}/{repo}"
    data = fetch_url(url)
    if data:
        try:
            parsed = json.loads(data)
            return parsed.get('stargazers_count', 'N/A')
        except:
            pass

    return 'N/A'

def get_readme_content(owner, repo):
    """Get README content for a repository."""
    url = f"https://api.github.com/repos/{owner}/{repo}/readme"
    data = fetch_url(url)
    if data:
        try:
            parsed = json.loads(data)
            content = parsed.get('content', '')
            encoding = parsed.get('encoding', 'base64')
            if encoding == 'base64':
                return base64.b64decode(content).decode('utf-8', errors='ignore')
            return content
        except:
            pass
    return None

def parse_awesome_readme(content):
    """Parse awesome README and extract project links."""
    projects = []

    # Match links like [name](https://github.com/owner/repo)
    link_pattern = r'\[([^\]]+)\]\(https://github\.com/([^)]+)\)'

    seen = set()

    for match in re.finditer(link_pattern, content):
        name = match.group(1).strip()
        path = match.group(2).strip()

        if path in seen:
            continue
        seen.add(path)

        if '/' not in path:
            continue

        # Skip non-repo paths
        last_part = path.split('/')[-1]
        if last_part in ('issues', 'pulls', 'wiki', 'actions', 'releases', 'discussions'):
            continue

        # Skip sub-links (containing #) - but keep #readme style links to repos
        if '#' in path:
            # Remove #readme or #section suffix to get actual repo
            path = path.split('#')[0]
            if not path or '/' not in path:
                continue

        projects.append({
            'name': name,
            'path': path,
            'owner': path.split('/')[0],
            'repo': path.split('/')[1]
        })

    return projects

def process_nested_readme(content, existing_paths):
    """Process a downloaded README and extract projects from it."""
    projects = parse_awesome_readme(content)
    new_projects = [p for p in projects if p['path'] not in existing_paths]
    return new_projects

def format_stars(stars):
    """Format star count for display."""
    if stars == 'N/A':
        return 'N/A'
    if isinstance(stars, int):
        if stars >= 1000:
            return f"{stars:,}"
        return str(stars)
    return str(stars)

def main():
    awesome_dir = Path('/workspace/awesome')
    awesome_dir.mkdir(exist_ok=True)

    print("Fetching sindresorhus/awesome README...")
    main_readme_content = fetch_url(
        'https://raw.githubusercontent.com/sindresorhus/awesome/main/readme.md'
    )

    if not main_readme_content:
        print("Failed to fetch main README, trying master branch...")
        main_readme_content = fetch_url(
            'https://raw.githubusercontent.com/sindresorhus/awesome/master/readme.md'
        )

    if not main_readme_content:
        print("Failed to fetch sindresorhus/awesome README")
        return

    # Save the original README
    with open('/workspace/awesome/sindresorhus-awesome-original.md', 'w', encoding='utf-8') as f:
        f.write(main_readme_content)

    print("Parsing projects from README...")
    projects = parse_awesome_readme(main_readme_content)
    print(f"Found {len(projects)} projects")

    # Get stars for each project and download READMEs
    all_projects = projects.copy()
    processed_paths = {p['path'] for p in projects}

    print("Fetching star counts and project READMEs...")
    for i, project in enumerate(projects):
        print(f"  [{i+1}/{len(projects)}] {project['path']}...", end=' ', flush=True)

        # Get stars
        stars = get_github_stars(project['owner'], project['repo'])
        project['stars'] = stars
        print(f"{format_stars(stars)} stars", flush=True)

        # Download README
        readme_content = get_readme_content(project['owner'], project['repo'])
        if readme_content:
            safe_name = project['repo']
            readme_path = awesome_dir / f"{safe_name}.md"
            with open(readme_path, 'w', encoding='utf-8') as f:
                f.write(f"# {project['name']}\n\n")
                f.write(f"> Stars: {format_stars(stars)} | ")
                f.write(f"[GitHub](https://github.com/{project['path']})\n\n")
                f.write(readme_content)

            print(f"    Saved README to {readme_path}")

            # Extract nested projects and get their stars
            nested_projects = process_nested_readme(readme_content, processed_paths)
            for np in nested_projects:
                if np['path'] not in processed_paths:
                    all_projects.append(np)
                    processed_paths.add(np['path'])

        # Rate limiting
        time.sleep(0.3)

    # Update main README.md with projects
    print("\nUpdating main README.md...")
    with open('/workspace/README.md', 'w', encoding='utf-8') as f:
        f.write("# Information comes from [sindresorhus/awesome](https://github.com/sindresorhus/awesome)\n\n")
        f.write("## Projects\n\n")

        for project in projects:
            safe_name = project['repo']
            stars = project.get('stars', 'N/A')
            stars_str = format_stars(stars)
            f.write(f"- [{project['name']}](./awesome/{safe_name}.md) ")
            f.write(f"[![GitHub stars](https://img.shields.io/github/stars/{project['path']}?style=flat)]")
            f.write(f"(https://github.com/{project['path']}/stargazers) ")
            f.write(f"({stars_str} stars)\n")

    print("Done!")

if __name__ == '__main__':
    main()
