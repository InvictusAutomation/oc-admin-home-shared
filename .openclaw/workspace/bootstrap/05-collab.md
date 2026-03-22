# 05-collab.md - 协作链路

## 协作模式

| 模式 | 描述 |
|------|------|
| Main Session | 直接与用户交互 |
| Sub-agent | 后台任务 |
| Isolated Session | 独立环境 |

## 工具

```bash
# 启动子代理
sessions_spawn agentId="..." task="..."

# 跨会话消息
sessions_send sessionKey="..." message="..."

# 会话管理
sessions_list
sessions_history sessionKey="..."
```

## 节点

```bash
nodes action="camera_snap" node="..."
nodes action="screen_record" node="..."
nodes action="location_get" node="..."
```
