"""Script to initialize a new day for Advent of Code.
This script will basically grab the input and puzzle clue
from the Advent of Code website.

If user specifies a year and day, this script will create
the files pertaining to that day and year.

Note: This script is being provided as a courtesy and is simply
an example of using the AocMod class for a command-line utility.
While the functionality is correct here and the CLI can be utilized
in a user's local install, it is recommended to perform any
desired tweaks to ensure proper functionality.

Author: David Eyrich
"""

import argparse
import importlib.metadata
import os

from aoc_mod.utilities import AocMod, AocModError

LOCAL_PUZZLE_FILEPATH = "challenges/{YEAR}/day{DAY}"

cur_file = os.path.abspath(__file__)
cur_file_parent = os.path.dirname(cur_file)
DEFAULT_FILE_TEMPLATE = f"{cur_file_parent}/data/templates/solution_template.py"


def create_solution_file(filename_in: str, filename_out: str, year: int, day: int):
    """read in the template solution file and replace instances of "{YEAR}"
    and "{DAY}" with the corresponding year and day arguments

    :param filename_in: path to the input file
    :type filename_in: str
    :param filename_out: path to the output file
    :type filename_out: str
    :param year: year that was entered
    :type year: int
    :param day: day that was entered
    :type day: int
    :raises AocModError: if an error occurs with file operations
    """

    try:
        with open(filename_in, "r", encoding="utf-8") as f_in:
            data = f_in.read()

        data_w_year = data.replace("{YEAR}", f"{year}")
        data_w_year_day = data_w_year.replace("{DAY}", f"{day}")

        with open(filename_out, "w", encoding="utf-8") as f_out:
            f_out.write(data_w_year_day)
    except (OSError, TypeError) as err:
        raise AocModError("unable to create solution template file") from err


def setup_challenge_day_template(
    aoc_mod: AocMod,
    year: int,
    day: int,
    output_root_dir: str = "",
    template_path: str = "",
):
    """set up a template folder named "challenges/{year}/day{day}" that contains
    the puzzle input (.txt), instructions (.md) and a template solution file, if
    specified

    :param year: year of the AoC puzzle
    :type year: int
    :param day: day of the AoC puzzle
    :type day: int
    :param output_root_dir: path to be prepended to the template folder,
        defaults to the current directory
    :type output_root_dir: str, optional
    :param template_path: path to a template file to use for solution code,
        defaults to ""
    :type template_path: str, optional
    """

    # set output directory path (prepend root_dir, if specified)
    main_path = LOCAL_PUZZLE_FILEPATH.format(YEAR=year, DAY=day)
    if output_root_dir:
        day_path = output_root_dir.strip("/") + "/" + main_path
    else:
        day_path = main_path

    # set individual file paths
    solution_path = ""
    input_path = f"{day_path}/input_{day}.txt"
    instructions_path = f"{day_path}/instructions_{year}_{day}.md"

    # set solution file path, if entered
    if template_path:
        _, ext = os.path.splitext(template_path)
        if ext:
            solution_path = f"{day_path}/day{day}{ext}"

    # attempt to get puzzle input and instructions
    input_data = ""

    os.system(f"mkdir -p {day_path}")

    # create the solution template, input, and instruction files
    if not os.path.exists(input_path):
        try:
            input_data = aoc_mod.get_puzzle_input(year, day)
        except AocModError as err:
            print(f"Failed to get puzzle input for {year}, Day {day} ({err})")

        if input_data:
            with open(input_path, "w", encoding="utf-8") as f:
                f.write(input_data)
            print(f"{year}, Day {day} input file created: {input_path}")
    else:
        print(f"{year}, Day {day} input file already exists.")

    if not os.path.exists(instructions_path):
        instructions = aoc_mod.get_puzzle_instructions(year, day)
        if instructions:
            with open(instructions_path, "w", encoding="utf-8") as f:
                f.write(instructions)
            print(f"{year}, Day {day} instructions file created: {instructions_path}")
    else:
        print(f"{year}, Day {day} instruction file already exists.")

    if not os.path.exists(solution_path):
        try:
            create_solution_file(template_path, solution_path, year, day)
            print(f"{year}, Day {day} solution file created: {solution_path}")
        except AocModError:
            print("Failed to create solution template file.")
    else:
        print(f"{year}, Day {day} solution file already exists.")


def file_exists(filepath: str) -> str:
    """verify that a file exists for argparse argument

    :param filepath: path to the file
    :type filepath: str
    :raises argparse.ArgumentTypeError: raise if file doesn't exist or
        filepath is not a file
    :return: filepath, once verified
    :rtype: str
    """
    if not os.path.exists(filepath):
        raise argparse.ArgumentTypeError(f"Error: file '{filepath}' does not exist")
    if not os.path.isfile(filepath):
        raise argparse.ArgumentTypeError(f"Error: '{filepath}' is not a file")
    return filepath


def directory_exists(dir_path: str) -> str:
    """verify that a directory exists for an argparse argument

    :param dir_path: path to directory
    :type dir_path: str
    :raises argparse.ArgumentTypeError: raise if directory doesn't exist or
        dir_path is not a directory
    :return: dir_path, once verified
    :rtype: str
    """
    if not os.path.exists(dir_path):
        raise argparse.ArgumentTypeError(
            f"Error: directory '{dir_path}' does not exist"
        )
    if not os.path.isdir(dir_path):
        raise argparse.ArgumentTypeError(f"Error: '{dir_path}' is not a directory")
    return dir_path


def parse_arguments() -> tuple[argparse.Namespace, list[str]]:
    """create an argument parser and parse user args

    :return: parser.parse_known_args() return value
    :rtype: tuple[Type[argparse.Namespace], list[str]]
    """

    ### define the basic parser object ###

    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument(
        "--version",
        action="version",
        version=f"aoc-mod version {importlib.metadata.version('aoc-mod')}",
    )
    parser.add_argument(
        "-y",
        "--year",
        type=int,
        help="year of the puzzle",
    )
    parser.add_argument(
        "-d",
        "--day",
        type=int,
        help="day of the puzzle",
    )
    parser.add_argument(
        "-s",
        "--session-id",
        type=str,
        help="session-id from an authenticated Advent of Code browser session",
    )

    subparsers = parser.add_subparsers(required=True)

    ### define setup arguments ###

    setup_parser = subparsers.add_parser(
        "setup", help="setup challenge files for AoC puzzle"
    )
    setup_parser.add_argument(
        "-t",
        "--template",
        type=file_exists,
        default=DEFAULT_FILE_TEMPLATE,
        help="path to a code template file",
    )
    setup_parser.add_argument(
        "-o",
        "--output-root-dir",
        type=directory_exists,
        help="root path where the 'challenges' folder structure will be created",
    )

    ### define submission arguments ###

    submit_parser = subparsers.add_parser(
        "submit", help="submit answer for an AoC puzzle"
    )
    submit_parser.add_argument(
        "-a", "--answer", type=int, help="answer to submit", required=True
    )
    submit_parser.add_argument(
        "-p",
        "--part",
        choices=[1, 2],
        type=int,
        help="part A = 1; part B = 2",
        required=True,
    )

    return parser.parse_known_args()


def interactive():
    """Entry-point to the aoc-mod program"""

    known_opts, _ = parse_arguments()

    # create an AOCMod class instance
    try:
        aoc_mod = AocMod(session_id=known_opts.session_id)
    except AocModError as err:
        print(f"Error: could not initialize AocMod ({err})")
        exit(1)

    # parse the year and day
    if known_opts.year is not None and known_opts.day is not None:
        year = known_opts.year
        day = known_opts.day
    else:
        year = aoc_mod.curr_time.tm_year
        day = aoc_mod.curr_time.tm_mday

    print(f"Year: {year}\tDay: {day}")

    # if we are submitting, let's do it, otherwise we'll setup the template
    if "answer" in known_opts and "part" in known_opts:
        print(f"Answer: {known_opts.answer}\tLevel: {known_opts.part}")

        # attempt to submit the answer
        try:
            aoc_mod.submit_answer(year, day, known_opts.part, known_opts.answer)
        except AocModError as err:
            print(f"Failed to submit puzzle answer ({err})")

    else:
        setup_challenge_day_template(
            aoc_mod,
            year,
            day,
            output_root_dir=known_opts.output_root_dir,
            template_path=known_opts.template,
        )
