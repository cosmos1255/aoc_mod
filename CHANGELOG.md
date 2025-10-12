# Changelog

All notable changes to AOC-Mod will be documented in this file.

## [Unreleased]

## [0.2.1] - 2025-10-12

### Added

- Added documentation using Sphinx and deployed via readthedocs.
- Added support for custom, user-generated file templates (more info on [aoc_mod readthedocs](https://readthedocs.org/projects/aoc-mod/aoc_mod_usage.html)).
- Added ability to run the command-line utility (and all other library utilities) without an authenticated session-id. Without a session id, a user is unable to retrieve puzzle input or submit answers but can receive the first part of the Advent of Code instructions and setup their project challenge.
- Created a general AocModError exception class to make it easier for library users to detect errors.

### Changed

- Reorganized the project structure to make a bit more sense.
- Reworked the build system to use Poetry instead of SetupTools.
- Updated the Python template to be functioning source code rather than a string for better testing.
- Update testing to reflect new library changes.
- Replaced all instances of 'os.path' with 'pathlib.Path' objects for better path management

### Documentation

- Updated the README and created other documentation with Sphinx
- Added or updated function/class docstrings and other comments throughout the codebase

## [0.1.5] - 2024-11-30

### Added

- Better versioning with `importlib.metadata` to place the version in only the pyproject.toml and then distribute it throughout the project, notably to `interactive.py`'s `--version` option.
- New instructions to the README.md for use of AOC-Mod as a library.
- New tests to run the python package installation.
- Ability to read a user-provided session ID and User Agent from the Linux/Windows environment variables.
- Users are able to submit their puzzle solutions directly to Advent of Code (once authenticated) and receive verbatim output from the site within the terminal.
- Users can pull puzzle instructions and write these instructions to a Markdown file for readability within their project repos.
- Users can pull puzzle input data and begin parsing while solving.
- An interactive command line utility has been created that supports creating template files and interfacing with the puzzle submission functionality.
- Added unit/integration tests.
- Updated the README.md.

### Changed

- Existing file templates.
- Updated library functions perform better parsing of integer values like year or day and not leaving it up to the user to figure it out.
- Release to PyPi only runs when pushed to the main branch (through a pull request).

### Fixed

- Bug when running `aoc-mod` without input would throw an AttributeError exception.
- Bug when installing the aoc-mod distribution. No files were present during the installation.

### Documentation

- Added better comments throughout the code.
