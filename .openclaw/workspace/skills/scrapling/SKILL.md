---
name: scrapling
description: |
  网页数据抓取 - 使用 Scrapling 爬虫框架抓取任意网页。
  
  当用户需要以下操作时使用：
  - "抓取网页"、"爬取网站"
  - "分析这个网站"、"提取网站内容"
  - "绕过 Cloudflare"、"抓取动态页面"
  - "市场调研"、"竞品分析"
  - "抓取产品信息"、"提取论坛内容"
  
  特性：
  - 支持普通网页、JS渲染页面、反爬网站
  - Adaptive Parsing - 自动适应网站改版
  - 内置反检测能力
---

# Scrapling - 网页数据抓取

使用 Scrapling 框架进行网页数据抓取。

## 核心能力

### 三种 Fetcher

| 类型 | 用途 | 示例 |
|------|------|------|
| Fetcher | 普通网页 | `from scrapling.fetchers import Fetcher` |
| DynamicFetcher | JS渲染页面 | 需要浏览器的动态内容 |
| StealthyFetcher | 反爬网站 | Cloudflare等防护 |

### Adaptive Parsing

记录元素特征，网站改版后自动重新匹配：

```python
# 首次抓取
products = page.css(".product", auto_save=True)

# 网站改版后
products = page.css(".product", adaptive=True)
```

## 使用示例

### 示例 1：抓取普通网页

```python
from scrapling.fetchers import Fetcher

page = Fetcher.fetch("https://example.com")
title = page.css("title::text")
```

### 示例 2：抓取 JS 渲染页面

```python
from scrapling.fetchers import DynamicFetcher

page = DynamicFetcher.fetch("https://example.com", headless=True)
content = page.css(".content::text")
```

### 示例 3：绕过反爬

```python
from scrapling.fetchers import StealthyFetcher

page = StealthyFetcher.fetch("https://example.com", headless=True)
# 自动：伪装浏览器、模拟TLS指纹、绕过Cloudflare
```

## 应用场景

| 场景 | 说明 |
|------|------|
| 市场调研 | 自动抓取竞品网站、论坛讨论 |
| 技术情报 | 抓取GitHub、技术博客、行业新闻 |
| 内容提取 | 提取文章、产品信息、用户评论 |
| 监控告警 | 定时抓取网站变化 |

## 与 OpenClaw 集成

创建 Skill 后，AI 可以：
1. 判断需要网页数据
2. 自动调用抓取函数
3. 提取内容
4. 返回分析结果

实现自动化的"自己去互联网找答案"。
