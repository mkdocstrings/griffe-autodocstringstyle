from __future__ import annotations

import re
from typing import Any

import griffe

_external = re.compile("/(.venv|site-packages)/")


class AutoDocstringStyleExtension(griffe.Extension):
    """Set `auto` docstring style on external packages."""

    def __init__(self, exclude: list[str] | None = None) -> None:
        """Initialize the extension.

        Parameters:
            exclude: Package names to exclude.
        """
        self._exclude = set(exclude or ())

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
