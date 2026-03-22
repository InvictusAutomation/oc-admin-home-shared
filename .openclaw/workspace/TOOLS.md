# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

## GitHub App

用于所有 GitHub 操作（API、仓库管理、代码推送等）：

| 信息 | 值 |
|------|-----|
| App ID | Your App ID |
| Installation ID | Your Installation ID |
| PEM 密钥 | ~/.ssh/github-app.pem |

**注意**：
- Git push 用 SSH 密钥 (`id_ed25519`)
- 所有 API 操作用 GitHub App（需先获取 token）

### 获取 Token

```python
# 生成 JWT → 获取 installation token
python3 << 'EOF'
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
EOF
```

## 研究项目

| 项目 | 仓库 |
|------|------|
| PageAgent 集成研究 | https://github.com/InvictusAutomation/page-agent-for-openclaw |
