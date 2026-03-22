# Python Code Style for CodeBuddy

## General Guidelines

- Follow PEP 8 style guide
- Use 4-space indentation
- Max line length: 100 characters
- Use type hints for all public APIs

## Naming Conventions

- Classes: `PascalCase` (e.g., `PluginManager`)
- Functions/methods: `snake_case` (e.g., `load_plugin`)
- Constants: `UPPER_SNAKE_CASE` (e.g., `MAX_RETRIES`)
- Private members: prefix with `_` (e.g., `_internal_method`)

## Imports

- Use absolute imports from project root
- Group imports: stdlib → third-party → local
- One import per line
- Sort imports alphabetically within groups

Example:
```python
# Standard library
import os
from pathlib import Path

# Third-party
import numpy as np
from sklearn.model_selection import train_test_split

# Local
from src.core import PluginManager
from src.utils import load_config
```

## Docstrings

Use Google-style docstrings:

```python
def process_data(data: pd.DataFrame, threshold: float = 0.5) -> pd.DataFrame:
    """Process input data with threshold filtering.

    Args:
        data: Input DataFrame to process
        threshold: Minimum value threshold (default: 0.5)

    Returns:
        Processed DataFrame with filtered values

    Raises:
        ValueError: If data is empty or threshold is invalid
    """
```

## Error Handling

- Use specific exception types
- Always include context in error messages
- Log errors before re-raising
- Use custom exceptions for domain errors
