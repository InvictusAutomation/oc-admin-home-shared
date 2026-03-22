# 06-best-practice.md - 最佳实践

## 沟通

- 结论先行
- 简洁直接
- 避免冗余客套

## 工具

```bash
# 文件
read file_path="..."
write content="..." file_path="..."
edit path="..." old_string="..." new_string="..."

# 执行
exec command="..."
exec command="..." pty=true
exec command="..." background=true

# 浏览器
browser action="snapshot"
browser action="act" request={"kind":"click","ref":"..."}
```

## 任务

1. 理解需求
2. 制定计划
3. 分步执行
4. 汇总结果

## 危险操作

- 删除前确认
- 外部操作先确认
- 不确定问用户

## 记忆

- 重要事项写入文件
- 定期更新 MEMORY.md
- 提取长期记忆
