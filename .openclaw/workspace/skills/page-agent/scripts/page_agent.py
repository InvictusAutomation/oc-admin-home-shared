#!/usr/bin/env python3
"""
Page Agent - 网页自动化脚本

利用 OpenClaw browser 工具进行网页自动化操作
"""

import json
import re
import sys

def parse_instruction(instruction: str) -> dict:
    """解析自然语言指令"""
    instruction = instruction.lower()
    
    # 点击操作
    if any(kw in instruction for kw in ['点击', '点击', 'click', 'press']):
        action_type = 'click'
        # 尝试提取目标元素
        match = re.search(r'(.+?)(?:按钮|链接|元素)', instruction)
        target = match.group(1) if match else None
        return {'action': 'click', 'target': target}
    
    # 填写操作
    elif any(kw in instruction for kw in ['填写', '填入', '输入', 'fill', 'type']):
        action_type = 'fill'
        # 提取字段名和值
        fill_match = re.search(r'把(.+?)填写?为(.+)', instruction)
        if fill_match:
            field = fill_match.group(1)
            value = fill_match.group(2)
            return {'action': 'fill', 'field': field, 'value': value}
        return {'action': 'fill', 'field': None, 'value': None}
    
    # 抓取操作
    elif any(kw in instruction for kw in ['抓取', '获取', '提取', 'scrape', 'extract']):
        action_type = 'scrape'
        return {'action': 'scrape', 'target': None}
    
    # 导航操作
    elif any(kw in instruction for kw in ['打开', '访问', ' navigate', 'go to']):
        action_type = 'navigate'
        url_match = re.search(r'(https?://[^\s]+)', instruction)
        if url_match:
            return {'action': 'navigate', 'url': url_match.group(1)}
        return {'action': 'navigate', 'url': None}
    
    # 导出操作
    elif any(kw in instruction for kw in ['导出', 'export', 'download']):
        action_type = 'export'
        format_match = re.search(r'导出为(.+)', instruction)
        fmt = format_match.group(1) if format_match else 'json'
        return {'action': 'export', 'format': fmt}
    
    return {'action': 'unknown', 'instruction': instruction}


def generate_browser_commands(parsed: dict) -> list:
    """生成 browser 工具命令"""
    commands = []
    
    if parsed['action'] == 'click':
        commands.append({
            'kind': 'click',
            'selector': f'[text*="{parsed.get("target", "")}"]'
        })
    
    elif parsed['action'] == 'fill':
        commands.append({
            'kind': 'fill',
            'selector': f'[name="{parsed.get("field", "")}"]',
            'value': parsed.get('value', '')
        })
    
    elif parsed['action'] == 'navigate':
        commands.append({
            'kind': 'navigate',
            'url': parsed.get('url', '')
        })
    
    return commands


def main():
    if len(sys.argv) < 2:
        print(json.dumps({
            'error': 'Usage: page_agent.py <instruction>'
        }))
        sys.exit(1)
    
    instruction = sys.argv[1]
    parsed = parse_instruction(instruction)
    commands = generate_browser_commands(parsed)
    
    print(json.dumps({
        'instruction': instruction,
        'parsed': parsed,
        'commands': commands
    }))


if __name__ == '__main__':
    main()
