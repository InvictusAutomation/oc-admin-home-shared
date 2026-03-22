---
paths:
  - "plugins/**/*.py"
  - "src/plugins/**/*.py"
---

# Plugin Development Guidelines

## Plugin Structure

Each plugin must have:

```python
# plugins/example_plugin/__init__.py
from typing import Dict, Any

class ExamplePlugin:
    """Plugin description."""

    def __init__(self, config: Dict[str, Any]):
        """Initialize plugin with configuration."""
        self.config = config

    def execute(self, *args, **kwargs) -> Any:
        """Main plugin execution method."""
        raise NotImplementedError

    def validate(self) -> bool:
        """Validate plugin configuration."""
        return True
```

## Plugin Registration

Plugins must be registered in plugin manifest:

```json
{
  "name": "example-plugin",
  "version": "1.0.0",
  "description": "Plugin description",
  "entry_point": "plugins.example_plugin.ExamplePlugin",
  "config_schema": {
    "type": "object",
    "properties": {
      "setting": {"type": "string"}
    }
  }
}
```

## Plugin Best Practices

- Keep plugins focused on single responsibility
- Validate configuration in `__init__`
- Provide clear error messages
- Include type hints for all methods
- Document configuration options
- Write tests for plugin functionality

## MCP Integration

Plugins using MCP should:
- Implement proper tool definitions
- Handle connection errors gracefully
- Support retry logic for network operations
- Log MCP interactions for debugging
