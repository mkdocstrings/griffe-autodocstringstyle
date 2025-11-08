"""Test extension."""

from __future__ import annotations

import griffe


def test_extension() -> None:
    """Load self and external package, assert styles."""
    self_api = griffe.load("griffe_autodocstringstyle", extensions=griffe.load_extensions("griffe_autodocstringstyle"))
    assert self_api.docstring
    assert self_api.docstring.parser is None

    pytest_api = griffe.load("pytest", extensions=griffe.load_extensions("griffe_autodocstringstyle"))
    assert pytest_api.docstring
    assert pytest_api.docstring.parser is griffe.Parser.auto


def test_exclude_option() -> None:
    """Excluded packages are untouched."""
    pytest_api = griffe.load(
        "pytest",
        extensions=griffe.load_extensions({"griffe_autodocstringstyle": {"exclude": ["pytest"]}}),
    )
    assert pytest_api.docstring
    assert pytest_api.docstring.parser is None
