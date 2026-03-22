# 12-skillhub.md - SkillHub

## 安装

```bash
curl -fsSL https://skillhub-1251783334.cos.ap-guangzhou.myqcloud.com/install/install.sh | bash
```

安装后重启 Gateway：

```bash
openclaw gateway restart
```

## CLI

```bash
skillhub --help
```

位置：`~/.local/bin/skillhub`

## 插件

位置：`~/.openclaw/extensions/skillhub`

配置：`~/.openclaw/openclaw.json`

```json
{
  "plugins": {
    "entries": {
      "skillhub": {
        "enabled": true
      }
    }
  }
}
```

## 使用

安装后可直接用自然语言安装技能：

```
安装 xxx 技能
```
