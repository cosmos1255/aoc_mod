# Changelog

All notable changes to AOC-Mod will be documented in this file.

## [0.2.5] - 2025-11-21

### Fixed

- Dependencies unnecessary for actually running the tool have been removed.

## [0.2.4] - 2025-11-16

### Added

- Timeouts of 120 seconds between HTTP requests to the Advent of Code website. This was added to ensure that the community guidelines are met properly.

### Documentation

- Updated README with information about new timeout features and outlining the caching of puzzle input and instructions per puzzle day.

## [0.2.2] - 2025-11-16

### Changed

- Decided to remove the command-line argument for session ID as it's just better practice to set the environment variable rather than running each CLI command with the session ID exposed in the terminal.
- Error print outs in the CLI are more descriptive now.

### Fixed

- Issue with solution file creation where the solution template would be created with an extra period before the extension.
- Argument parsing was corrected to include CLI inputs like `aoc-mod setup -y [year] -d [day]`. Before, this command would have resulted in a failure because by default, non-subparser commands must precede subparser commands. Now we parse commands twice (once with parse_known_args() and a second time with parse_args(unknown, known)) to ensure that we parse all available arguments.

### Documentation

- Updated README to include information about running the CLI (this is also included elsewhere but the README will probably be viewed more often than the readthedocs page.)

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
