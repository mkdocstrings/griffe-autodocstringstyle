# griffe-autodocstringstyle

[![documentation](https://img.shields.io/badge/docs-mkdocs-708FCC.svg?style=flat)](https://mkdocstrings.github.io/griffe-autodocstringstyle/)
[![gitpod](https://img.shields.io/badge/gitpod-workspace-708FCC.svg?style=flat)](https://gitpod.io/#https://github.com/mkdocstrings/griffe-autodocstringstyle)
[![gitter](https://badges.gitter.im/join%20chat.svg)](https://app.gitter.im/#/room/#griffe-autodocstringstyle:gitter.im)

Set docstring style to 'auto' for external packages.

## Installation

This project is available to sponsors only, through my Insiders program.
See Insiders [explanation](https://mkdocstrings.github.io/griffe-autodocstringstyle/insiders/)
and [installation instructions](https://mkdocstrings.github.io/griffe-autodocstringstyle/insiders/installation/).

## Usage

[Enable(https://mkdocstrings.github.io/griffe/guide/users/extending/#using-extensions)] the `griffe_autodocstringstyle` extension. Now all packages loaded from a virtual environment will have their docstrings parsed with the `auto` style (automatically guessing the docstring style).

Use the `exclude` option to pass package names that shouldn't be considered. This can be useful if you must first install your sources as a package before loading/documenting them (meaning they end up in the virtual environment too).

With MkDocs:

```yaml
plugins:
- mkdocstrings:
    handlers:
      python:
        options:
          extensions:
          - griffe_autodocstringstyle:
              # only useful if your sources can't be found
              # in the current working directory 
              exclude:
              - my_package
```
