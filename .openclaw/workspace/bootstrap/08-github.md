# 08-github.md - GitHub

## GitHub App（所有操作都用这个）

| 信息 | 值 |
|------|-----|
| App ID | Your App ID |
| Installation ID | Your Installation ID |
| PEM | ~/.ssh/github-app.pem |

## 获取 Token

```python
import base64, json, time, subprocess, requests

header = {"alg": "RS256", "typ": "JWT"}
payload = {"iss": "Your App ID", "iat": int(time.time()), "exp": int(time.time()) + 600}

def b64url(d):
    s = json.dumps(d, separators=(',', ':'))
    return base64.urlsafe_b64encode(s.encode()).decode().rstrip('=')

h, p = b64url(header), b64url(payload)
sig = subprocess.check_output(f"echo -n '{h}.{p}' | openssl dgst -sha256 -sign ~/.ssh/github-app.pem -binary", shell=True)
s = base64.urlsafe_b64encode(sig).decode().rstrip('=')
jwt = f"{h}.{p}.{s}"

resp = requests.post("https://api.github.com/app/installations/Your Installation ID/access_tokens",
    headers={"Authorization": f"Bearer {jwt}", "Accept": "application/vnd.github+json", "Content-Type": "application/json"},
    json={"permissions": {"administration": "write", "contents": "write"}})
print(resp.json()["token"])
```

## 常用操作

```python
import requests

# 用上面获取的 token
token = "Your GitHub Token"

# 读取仓库内容
requests.get("https://api.github.com/repos/InvictusAutomation/oc-admin-home/contents",
    headers={"Authorization": f"token {token}"})

# 创建仓库
requests.post("https://api.github.com/orgs/InvictusAutomation/repos",
    headers={"Authorization": f"token {token}"}, json={"name": "new-repo-opclw", "private": True})

# 重命名仓库
requests.patch("https://api.github.com/repos/InvictusAutomation/old-name",
    headers={"Authorization": f"token {token}"}, json={"name": "new-name"})

# 创建 issue
requests.post("https://api.github.com/repos/InvictusAutomation/repo/issues",
    headers={"Authorization": f"token {token}"}, json={"title": "Bug"})
```

## Git Push

Git push 用 SSH 密钥（不是 GitHub App）：
```bash
git remote set-url origin git@github.com:InvictusAutomation/repo.git
git push origin main
```

### ~/home/admin 维护规则

- **不 pull**，直接修改提交就 push
- push 失败 → 推送到新分支（ocft1, ocft2...）
- remote 必须是 oc-admin-home

### 本地仓库丢失

如需开发某仓库但本地找不到：

```bash
cd ~/.openclaw/workspace/projects/
git clone git@github.com:InvictusAutomation/<repo-name>.git
```

## 问题

- Bad credentials → IP 被封锁 → `curl -s ifconfig.me` → 让用户加白名单
