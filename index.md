# griffe-autodocstringstyle

Set docstring style to 'auto' for external packages.

## Installation

```
pip install griffe-autodocstringstyle
```

## Usage

[Enable](https://mkdocstrings.github.io/griffe/guide/users/extending/#using-extensions) the `griffe_autodocstringstyle` extension. Now all packages loaded from a virtual environment will have their docstrings parsed with the `auto` style (automatically guessing the docstring style).

Use the `exclude` option to pass package names that shouldn't be considered. This can be useful if you must first install your sources as a package before loading/documenting them (meaning they end up in the virtual environment too).

With MkDocs:

```
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

## Sponsors
