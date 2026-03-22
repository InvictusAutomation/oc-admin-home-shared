#!/usr/bin/env python3
"""
Scrapling Web Scraper - 网页数据抓取

使用 Scrapling 框架进行网页数据抓取
"""

import sys
import json

def try_import_scrapling():
    """检查 Scrapling 是否已安装"""
    try:
        from scrapling import __version__
        return True
    except ImportError:
        return False


def install_scrapling():
    """安装 Scrapling"""
    import subprocess
    result = subprocess.run(
        [sys.executable, "-m", "pip", "install", "scrapling"],
        capture_output=True,
        text=True
    )
    return result.returncode == 0


def scrape_with_fetcher(url: str, fetcher_type: str = "auto"):
    """
    使用 Scrapling 抓取网页
    
    Args:
        url: 目标URL
        fetcher_type: fetcher类型 - "static", "dynamic", "stealthy", "auto"
    
    Returns:
        dict: 抓取结果
    """
    if not try_import_scrapling():
        return {
            "error": "Scrapling not installed",
            "install_hint": "pip install scrapling"
        }
    
    try:
        if fetcher_type == "static":
            from scrapling.fetchers import Fetcher
            page = Fetcher.fetch(url)
        elif fetcher_type == "dynamic":
            from scrapling.fetchers import DynamicFetcher
            page = DynamicFetcher.fetch(url, headless=True)
        elif fetcher_type == "stealthy":
            from scrapling.fetchers import StealthyFetcher
            page = StealthyFetcher.fetch(url, headless=True)
        else:
            # 自动选择
            from scrapling.fetchers import StealthyFetcher
            page = StealthyFetcher.fetch(url, headless=True)
        
        return {
            "success": True,
            "url": url,
            "fetcher_type": fetcher_type,
            "html": page.text[:5000],  # 限制长度
            "status_code": getattr(page, 'status_code', 200)
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "url": url
        }


def extract_elements(html: str, selector: str):
    """提取元素"""
    try:
        from scrapling import ParselSelector
        selector_obj = ParselSelector(text=html)
        elements = selector_obj.css(selector).getall()
        return {"elements": elements}
    except Exception as e:
        return {"error": str(e)}


def main():
    if len(sys.argv) < 2:
        print(json.dumps({
            "error": "Usage: scrapler.py <url> [fetcher_type]",
            "fetcher_types": ["static", "dynamic", "stealthy", "auto"]
        }))
        sys.exit(1)
    
    url = sys.argv[1]
    fetcher_type = sys.argv[2] if len(sys.argv) > 2 else "auto"
    
    result = scrape_with_fetcher(url, fetcher_type)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
