# Advent of Code Module

A library for Advent of Code containing utilities to use while solving problems!

If any issues or bugs are discovered, please submit an issue and I'll fix it!

## Installation with Poetry

The build system has been updated to utilize poetry for installation, building, and dependency management. To install/build locally, install the poetry build system through `pipx`.

```sh
# install pipx
sudo apt install pipx

# install poetry
pipx install poetry
```

Once poetry is installed, the following commands can be used to install, build, and run unit tests locally.

```sh
# install the library
poetry install

# build a wheel
poetry build

# run the tests
poetry run pytest
```

Formatting and linting is also available through `ruff`.

```sh
# run a linter check
poetry run ruff check

# run a linter check and correct issues
poetry run ruff check --fix

# format the code
poetry run ruff format
```

## Documentation

The documentation is managed and built using Sphinx through the Poetry build system. To build the documentation and open it, run the following commands:

```bash
poetry run sphinx-build -M html docs/source/ docs/build/
firefox docs/build/html/index.html
```
