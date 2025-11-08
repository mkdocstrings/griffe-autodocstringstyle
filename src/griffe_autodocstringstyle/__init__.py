"""griffe-autodocstringstyle package.

Set docstring style to 'auto' for external packages.
"""

from __future__ import annotations

from griffe_autodocstringstyle._internal.extension import AutoDocstringStyleExtension

__all__: list[str] = ["AutoDocstringStyleExtension"]
