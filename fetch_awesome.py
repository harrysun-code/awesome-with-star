#!/usr/bin/env python3
"""
Script to fetch sindresorhus/awesome README, extract projects, get star counts,
and download all project READMEs to awesome directory.
"""

import os
import re
import json
import time
import datetime
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
    如果遇到 API 频次限制，会等待足够时间后重试。
    """
    token = get_github_token()
    api_url = f"https://api.github.com/repos/{owner}/{repo}/readme"

    # 第一步：优先使用 GitHub API 获取
    # 用 -D /dev/stderr 把响应头输出到 stderr，body 输出到 stdout
    # 避免 curl -i 在 HTTP/2 连接中输出多个头块导致解析失败
    for attempt in range(retries):
        try:
            cmd = ['curl', '-s', '--connect-timeout', '30', '--max-time', '120', '-D', '/dev/stderr']
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

            if result.returncode == 0:
                # stderr 是响应头，stdout 是 body
                header_text = result.stderr
                body_text = result.stdout

                if not header_text:
                    if attempt < retries - 1:
                        print(f"    API 重试 {attempt+1}/{retries}...", flush=True)
                        time.sleep(2 * (attempt + 1))
                    continue

                # 解析响应头（可能有多组，取最后一组）
                # HTTP/2 连接可能有多个头块，取最后一个有效的
                header_blocks = re.split(r'\r?\n\r?\n', header_text.strip())
                headers = {}
                status_line = ''
                for block in header_blocks:
                    block_lines = block.strip().split('\n')
                    if block_lines and block_lines[0].startswith('HTTP/'):
                        status_line = block_lines[0]
                        headers = {}
                        for line in block_lines[1:]:
                            if ':' in line:
                                key, value = line.split(':', 1)
                                headers[key.strip().lower()] = value.strip()

                # 检查 HTTP 状态码
                http_code = int(status_line.split()[1]) if len(status_line.split()) > 1 else 0

                # 解析 rate limit reset 时间
                reset_seconds = None
                if 'x-ratelimit-reset' in headers:
                    reset_timestamp = int(headers['x-ratelimit-reset'])
                    now = int(datetime.datetime.now(datetime.timezone.utc).timestamp())
                    reset_seconds = reset_timestamp - now + 5  # 多等5秒缓冲

                # 检查是否是 403 限流
                if http_code == 403:
                    if reset_seconds and reset_seconds > 0:
                        print(f"    [API 频次限制] 需等待 {reset_seconds} 秒后重试...", flush=True)
                        time.sleep(reset_seconds)
                        continue
                    else:
                        # 可能是其他 403 错误，继续重试
                        if attempt < retries - 1:
                            print(f"    API 403 错误，重试 {attempt+1}/{retries}...", flush=True)
                            time.sleep(5 * (attempt + 1))
                            continue

                # 检查是否是 404 错误
                if http_code == 404:
                    print(f"404 - 仓库不存在或无 README，跳过更新", end=' ', flush=True)
                    return None

                # 正常响应
                if http_code == 200 and body_text:
                    try:
                        data = json.loads(body_text)
                        # 正常获取到 README 内容（base64 编码）
                        if 'content' in data:
                            content = base64.b64decode(data['content']).decode('utf-8', errors='ignore')
                            return content
                    except json.JSONDecodeError:
                        pass

            if attempt < retries - 1:
                print(f"    API 重试 {attempt+1}/{retries}...", flush=True)
                time.sleep(2 * (attempt + 1))
        except Exception as e:
            if attempt < retries - 1:
                print(f"    API 异常，重试 {attempt+1}/{retries}...", flush=True)
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

            # 处理带 # 的链接，去掉 # 部分获取真实仓库路径
            if '#' in path:
                path = path.split('#')[0]
                if not path or '/' not in path:
                    continue

            # 跳过非仓库路径
            last_part = path.split('/')[-1]
            if last_part in ('issues', 'pulls', 'wiki', 'actions', 'releases', 'discussions'):
                continue

            # Create star badge
            badge = f"[![GitHub stars](https://img.shields.io/github/stars/{path}?style=flat)](https://github.com/{path}/stargazers)"

            # Insert badge after the link
            insert_pos = match.end()
            new_line = new_line[:insert_pos] + " " + badge + new_line[insert_pos:]

        processed_lines.append(new_line)

    return '\n'.join(processed_lines)

def add_source_marker(content, owner, repo):
    """
    在 README 内容顶部添加来源标记，指向原始 GitHub 项目。
    """
    source_url = f"https://github.com/{owner}/{repo}"
    marker = f"> 来源：[{owner}/{repo}]({source_url})\n\n"
    return marker + content

def process_main_readme(content, downloaded_projects):
    """
    处理 sindresorhus/awesome 的 README：
    1. 为所有 GitHub 项目链接添加 star 标
    2. 将有本地文件的链接改写为指向 awesome 目录下的本地文件
    downloaded_projects: dict, key = 仓库路径(owner/repo), value = 本地文件名
    """
    lines = content.split('\n')
    processed_lines = []
    link_pattern = r'\[([^\]]+)\]\(https://github\.com/([^)]+)\)'

    for line in lines:
        # Skip badge lines
        if 'img.shields.io' in line:
            processed_lines.append(line)
            continue

        new_line = line
        matches = list(re.finditer(link_pattern, line))

        # Process matches in reverse order to preserve positions
        for match in reversed(matches):
            name = match.group(1).strip()
            path = match.group(2).strip()

            # Skip if already has badge
            if 'img.shields.io' in line[match.start():match.end()]:
                continue

            # 处理带 # 的链接，去掉 # 部分获取真实仓库路径
            clean_path = path.split('#')[0]
            if not clean_path or '/' not in clean_path:
                continue

            # 跳过非仓库路径
            last_part = clean_path.split('/')[-1]
            if last_part in ('issues', 'pulls', 'wiki', 'actions', 'releases', 'discussions'):
                continue

            # 创建 star 标
            badge = f"[![GitHub stars](https://img.shields.io/github/stars/{clean_path}?style=flat)](https://github.com/{clean_path}/stargazers)"

            # 检查是否有本地文件，有则改写链接指向本地文件
            if clean_path in downloaded_projects:
                local_file = downloaded_projects[clean_path]
                new_link = f'[{name}](./awesome/{local_file}) {badge}'
                new_line = new_line[:match.start()] + new_link + new_line[match.end():]
            else:
                # 没有本地文件，只添加 star 标
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

    print("Parsing projects from README...")
    projects = parse_awesome_readme(main_readme_content)
    print(f"Found {len(projects)} projects")

    # 第一步：下载所有项目 README，并记录成功下载的项目
    print("Downloading project READMEs...")
    success_count = 0
    fail_count = 0
    downloaded_projects = {}  # 记录成功下载的项目: {owner/repo: 本地文件名}

    for i, project in enumerate(projects):
        print(f"  [{i+1}/{len(projects)}] {project['path']}...", end=' ', flush=True)

        # Download README with retry
        readme_content = get_readme_content(project['owner'], project['repo'], retries=5)
        if readme_content:
            safe_name = project['repo']
            readme_path = awesome_dir / f"{safe_name}.md"
            with open(readme_path, 'w', encoding='utf-8') as f:
                # 添加标题
                f.write(f"# {project['name']}\n\n")
                # 添加来源标记
                f.write(add_source_marker('', project['owner'], project['repo']))
                # 添加 star 标
                f.write(f"[![GitHub stars](https://img.shields.io/github/stars/{project['path']}?style=flat)](https://github.com/{project['path']}/stargazers)\n\n")
                # 为 README 中的所有 GitHub 项目链接添加 star 标
                processed_content = process_readme_with_stars(readme_content)
                f.write(processed_content)

            print(f"OK", flush=True)
            success_count += 1
            downloaded_projects[project['path']] = f"{safe_name}.md"
        else:
            print(f"FAILED", flush=True)
            fail_count += 1

        # Rate limiting
        time.sleep(0.5)

    print(f"\nDownloaded: {success_count}, Failed: {fail_count}")

    # 第二步：处理主 README（添加 star 标 + 改写链接指向本地文件 + 添加来源标记）
    print("Processing main README...")
    processed_main_readme = process_main_readme(main_readme_content, downloaded_projects)
    processed_main_readme = add_source_marker(processed_main_readme, 'sindresorhus', 'awesome')

    # 保存到 awesome 目录和根目录
    with open(awesome_dir / 'sindresorhus-awesome-original.md', 'w', encoding='utf-8') as f:
        f.write(processed_main_readme)
    with open(base_dir / 'README.md', 'w', encoding='utf-8') as f:
        f.write(processed_main_readme)
    print("Main README saved to README.md and awesome/sindresorhus-awesome-original.md")

if __name__ == '__main__':
    main()
