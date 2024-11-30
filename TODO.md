# AOC_MOD library feature update

## Description

AOC_MOD is intended to be a one-size-fits-all library module for Advent of Code projects to use. Essentially, this library will be loaded and instantiated and will provide vast numbers of functions to assist in the import of daily problem input as well as submission of answers.

## Library structure and components

### Features - 0.1.*

- ~~puzzle instruction parser to grab the day's puzzle instructions from the Advent of Code website and parse as needed~~
- ~~puzzle input data parser to grab the day's problem input for parsing~~
- ~~ability to submit the puzzle input and raise exceptions as needed for useful feedback to the developer~~
- ~~read from the Linux and Windows environment variables to get the session_id and user_agent~~
- ~~better data validation (i.e. ensuring that functions like `get_puzzle_input` accept integer values regardless)~~

### Features - Planned

- Windows support for creating challenge files.
- More file templates to include languages like C/C++, Java, etc.
- readthedocs website to explain installation and use of the module
