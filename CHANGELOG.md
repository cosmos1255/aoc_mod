# Changelog

All notable changes to AOC-Mod will be documented in this file.

## [Unreleased]

### Added

- New deployment test to TestPypi to ensure that we are good to go prior to actual release.

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
