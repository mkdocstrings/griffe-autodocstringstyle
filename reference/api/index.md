# griffe_autodocstringstyle

griffe-autodocstringstyle package.

Set docstring style to 'auto' for external packages.

Classes:

- **`AutoDocstringStyleExtension`** – Set auto docstring style on external packages.

## AutoDocstringStyleExtension

```
AutoDocstringStyleExtension(
    exclude: list[str] | None = None,
)
```

Bases: `Extension`

Set `auto` docstring style on external packages.

Parameters:

- **`exclude`** (`list[str] | None`, default: `None` ) – Package names to exclude.

Methods:

- **`on_instance`** – Set docstring style to auto on all external Griffe objects.

Source code in `src/griffe_autodocstringstyle/_internal/extension.py`

```
def __init__(self, exclude: list[str] | None = None) -> None:
    """Initialize the extension.

    Parameters:
        exclude: Package names to exclude.
    """
    self._exclude = set(exclude or ())
```

### on_instance

```
on_instance(*, obj: Object, **kwargs: Any) -> None
```

Set docstring style to `auto` on all external Griffe objects.

Parameters:

- **`obj`** (`Object`) – A Griffe object.
- **`**kwargs`** (`Any`, default: `{}` ) – Additional arguments.

Source code in `src/griffe_autodocstringstyle/_internal/extension.py`

```
def on_instance(self, *, obj: griffe.Object, **kwargs: Any) -> None:  # noqa: ARG002
    """Set docstring style to `auto` on all external Griffe objects.

    Parameters:
        obj: A Griffe object.
        **kwargs: Additional arguments.
    """
    if not obj.docstring or isinstance(obj.filepath, list) or obj.package.name in self._exclude:
        return
    filepath = obj.filepath.resolve().as_posix()
    if _external.search(filepath):
        obj.docstring.parser = griffe.Parser.auto
```
