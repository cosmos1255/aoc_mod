# Changelog

All notable changes to AOC-Mod will be documented in this file.

## [Unreleased]

## [0.1.2] - 2024-11-30

### Added

- Better versioning with `importlib.metadata` to place the version in only the pyproject.toml and then distribute it throughout the project, notably to `interactive.py`'s `--version` option.

### Changed

- Updated library functions perform better parsing of integer values like year or day and not leaving it up to the user to figure it out.

### Documentation

- Added better comments throughout the code.

### Fixed

- Bug when running `aoc-mod` without input would throw an AttributeError exception.

## [0.1.1] - 2024-11-30

### Added

- New instructions to the README.md for use of AOC-Mod as a library.
- New tests to run the python package installation.

### Fixed

- Bug when installing the aoc-mod distribution. No files were present during the installation.

### Changed

- Release to PyPi only runs when pushed to the main branch (through a pull request).

## [0.1.0] - 2024-11-29

### Added

- Ability to read a user-provided session ID and User Agent from the Linux/Windows environment variables.
- Users are able to submit their puzzle solutions directly to Advent of Code (once authenticated) and receive verbatim output from the site within the terminal.
- Users can pull puzzle instructions and write these instructions to a Markdown file for readability within their project repos.
- Users can pull puzzle input data and begin parsing while solving.
- An interactive command line utility has been created that supports creating template files and interfacing with the puzzle submission functionality.
- Added unit/integration tests.
- Updated the README.md.
