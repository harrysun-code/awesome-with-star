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

def fetch_url(url, retries=5, delay=2):
    """Fetch URL content using curl with retry logic."""
    for attempt in range(retries):
        try:
            result = subprocess.run(
                ['curl', '-s', '--connect-timeout', '30', '--max-time', '120', url],
                capture_output=True,
                text=True,
                encoding='utf-8'
            )
            if result.returncode == 0 and result.stdout:
                return result.stdout
            elif attempt < retries - 1:
                print(f"    Retry {attempt+1}/{retries}...")
                time.sleep(delay * (attempt + 1))
        except Exception as e:
            if attempt < retries - 1:
                print(f"    Retry {attempt+1}/{retries}...")
                time.sleep(delay * (attempt + 1))
    return None

def get_github_token():
    """
    从配置文件加载 GitHub Token。
    
    配置文件样式说明：
    - 在脚本同级目录创建名为 github_token.json 的文件
    - 文件内容格式：{"token": "your_github_personal_access_token"}
    - 请将此文件添加到 .gitignore 中，避免提交到代码仓库
    - 如果没有配置文件或 token 为空，API 请求将以未认证方式进行（有速率限制）
    """
    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'github_token.json')
    try:
        with open(config_path, 'r') as f:
            config = json.load(f)
            token = config.get('token', '').strip()
            if token:
                return token
            else:
                print("Warning: github_token.json 中 token 为空，API 请求将未认证")
                return ''
    except FileNotFoundError:
        print("Warning: 未找到 github_token.json 配置文件，API 请求将未认证")
        return ''
    except json.JSONDecodeError:
        print("Warning: github_token.json 格式错误，API 请求将未认证")
        return ''
    except Exception as e:
        print(f"Warning: 读取 token 文件时出错: {e}")
        return ''

def get_readme_content(owner, repo, retries=5):
    """
    获取仓库 README 内容，优先使用 GitHub API，失败则 fallback 到 raw 方式。
    如果返回 404 则不更新，直接返回 None。
    """
    token = get_github_token()
    api_url = f"https://api.github.com/repos/{owner}/{repo}/readme"

    # 第一步：优先使用 GitHub API 获取
    for attempt in range(retries):
        try:
            cmd = ['curl', '-s', '--connect-timeout', '30', '--max-time', '120']
            if token:
                cmd.extend(['-H', f'Authorization: token {token}'])
            cmd.extend(['-H', 'Accept: application/vnd.github.v3+json'])
            cmd.append(api_url)

            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                encoding='utf-8'
            )

            if result.returncode == 0 and result.stdout:
                try:
                    data = json.loads(result.stdout)
                    # 检查是否是 404 错误
                    if isinstance(data, dict) and data.get('message') == 'Not Found':
                        print(f"404 - 仓库不存在或无 README，跳过更新", end=' ')
                        return None
                    # 正常获取到 README 内容（base64 编码）
                    if 'content' in data:
                        content = base64.b64decode(data['content']).decode('utf-8', errors='ignore')
                        return content
                except json.JSONDecodeError:
                    pass

            if attempt < retries - 1:
                print(f"    API 重试 {attempt+1}/{retries}...")
                time.sleep(2 * (attempt + 1))
        except Exception as e:
            if attempt < retries - 1:
                print(f"    API 重试 {attempt+1}/{retries}...")
                time.sleep(2 * (attempt + 1))

    # 第二步：API 获取失败，fallback 到 raw 方式
    print("API 获取失败，尝试 raw 方式...", end=' ')
    urls_to_try = [
        f"https://raw.githubusercontent.com/{owner}/{repo}/main/README.md",
        f"https://raw.githubusercontent.com/{owner}/{repo}/master/README.md",
        f"https://raw.githubusercontent.com/{owner}/{repo}/HEAD/README.md",
    ]

    for url in urls_to_try:
        content = fetch_url(url, retries=retries)
        if content:
            # 检查是否是 404 页面内容
            if "404: Not Found" in content or "404 Not Found" in content:
                continue
            return content

    # 所有方式都失败，且确认是 404 则不更新
    print("404 或获取失败，跳过更新", end=' ')
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

def process_readme_with_stars(content):
    """Process README content to add star badges to all GitHub project links."""
    lines = content.split('\n')
    processed_lines = []

    # Pattern to match [name](https://github.com/owner/repo)
    link_pattern = r'\[([^\]]+)\]\(https://github\.com/([^)]+)\)'

    for line in lines:
        # Skip badge lines
        if 'img.shields.io' in line:
            processed_lines.append(line)
            continue

        new_line = line

        # Find all GitHub links in this line
        matches = list(re.finditer(link_pattern, line))

        # Process matches in reverse order to preserve positions
        for match in reversed(matches):
            name = match.group(1).strip()
            path = match.group(2).strip()

            # Skip if already has badge
            if 'img.shields.io' in line[match.start():match.end()]:
                continue

            # Skip sub-links
            if '#' in path:
                continue

            # Create star badge
            badge = f"[![GitHub stars](https://img.shields.io/github/stars/{path}?style=flat)](https://github.com/{path}/stargazers)"

            # Insert badge after the link
            insert_pos = match.end()
            new_line = new_line[:insert_pos] + " " + badge + new_line[insert_pos:]

        processed_lines.append(new_line)

    return '\n'.join(processed_lines)

def main():
    base_dir = Path(__file__).resolve().parent
    awesome_dir = base_dir / 'awesome'
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

    # Save the original README with star badges
    print("Processing main README with star badges...")
    processed_main_readme = process_readme_with_stars(main_readme_content)
    # Save to awesome directory
    with open(awesome_dir / 'sindresorhus-awesome-original.md', 'w', encoding='utf-8') as f:
        f.write(processed_main_readme)
    # Save to root README.md
    with open(base_dir / 'README.md', 'w', encoding='utf-8') as f:
        f.write(processed_main_readme)
    print("Main README saved to README.md and awesome/sindresorhus-awesome-original.md")

    print("Parsing projects from README...")
    projects = parse_awesome_readme(main_readme_content)
    print(f"Found {len(projects)} projects")

    # Get stars for each project and download READMEs
    all_projects = projects.copy()
    processed_paths = {p['path'] for p in projects}

    print("Downloading project READMEs...")
    success_count = 0
    fail_count = 0

    for i, project in enumerate(projects):
        print(f"  [{i+1}/{len(projects)}] {project['path']}...", end=' ', flush=True)

        # Download README with retry
        readme_content = get_readme_content(project['owner'], project['repo'], retries=5)
        if readme_content:
            safe_name = project['repo']
            readme_path = awesome_dir / f"{safe_name}.md"
            with open(readme_path, 'w', encoding='utf-8') as f:
                # Add title and star badge at the top
                f.write(f"# {project['name']}\n\n")
                f.write(f"[![GitHub stars](https://img.shields.io/github/stars/{project['path']}?style=flat)](https://github.com/{project['path']}/stargazers)\n\n")
                # Add star badges to all project links in the README
                processed_content = process_readme_with_stars(readme_content)
                f.write(processed_content)

            print(f"OK", flush=True)
            success_count += 1

            # Extract nested projects
            nested_projects = process_nested_readme(readme_content, processed_paths)
            for np in nested_projects:
                if np['path'] not in processed_paths:
                    all_projects.append(np)
                    processed_paths.add(np['path'])
        else:
            print(f"FAILED", flush=True)
            fail_count += 1

        # Rate limiting
        time.sleep(0.5)

    print(f"\nDone! Success: {success_count}, Failed: {fail_count}")

if __name__ == '__main__':
    main()
