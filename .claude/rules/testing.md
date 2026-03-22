# Testing Conventions

## Test Structure

- Place tests in `tests/` directory
- Mirror source structure in test files
- Name test files: `test_<module>.py`
- Use descriptive test function names

## Test Naming

Follow pattern: `test_<function>_<scenario>_<expected>`

Examples:
```python
def test_load_plugin_valid_path_returns_plugin():
    """Test that loading a plugin with valid path returns plugin instance."""

def test_load_plugin_invalid_path_raises_error():
    """Test that loading plugin with invalid path raises FileNotFoundError."""
```

## Test Organization

```python
import pytest
from src.core import PluginManager

class TestPluginManager:
    """Tests for PluginManager class."""

    @pytest.fixture
    def manager(self):
        """Create PluginManager instance for tests."""
        return PluginManager()

    def test_load_plugin_success(self, manager):
        """Test successful plugin loading."""
        plugin = manager.load_plugin("test_plugin")
        assert plugin is not None
```

## Coverage Requirements

- Aim for >80% code coverage
- Focus on critical paths and edge cases
- Use `pytest --cov=src tests/` to check coverage

## Testing Best Practices

- Use fixtures for shared setup
- Mock external dependencies
- Test one thing per test
- Keep tests independent
- Use parametrize for similar test cases

Example:
```python
@pytest.mark.parametrize("input,expected", [
    ("valid", True),
    ("invalid", False),
    ("", False),
])
def test_validate_input(input, expected):
    assert validate(input) == expected
```
