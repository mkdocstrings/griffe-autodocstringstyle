# SPDX-License-Identifier: ISC
#
# ISC License
#
# Copyright (c) 2024, Timothée Mazzucotelli and contributors
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

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
