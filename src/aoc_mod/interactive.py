"""Script to initialize a new day for Advent of Code.
This script will basically grab the input and puzzle clue
from the Advent of Code website.

If user specifies a year and day, this script will create
the files pertaining to that day and year.

Author: David Eyrich
"""

import argparse
import importlib.metadata
import os

from aoc_mod.utilities import AocMod, AocModError

LOCAL_PUZZLE_FILEPATH = "challenges/{YEAR}/day{DAY}"


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
    except OSError as err:
        raise AocModError("unable to create solution template file") from err


def setup_challenge_day_template(
    year: int,
    day: int,
    output_root_dir: str = "",
    template_path: str = "",
) -> int:
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
    :return: -1 for failure, 0 for success
    :rtype: int
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
    instructions = ""
    try:
        aoc_mod = AocMod()

        input_data = aoc_mod.get_puzzle_input(year, day)
        instructions = aoc_mod.get_puzzle_instructions(year, day)
    except AocModError as err:
        print(f"Failed to get puzzle input or instructions for {year}, Day {day}")
        print(f"Error received: {err}")
        return -1

    os.system(f"mkdir -p {day_path}")

    # create the solution template, input, and instruction files
    if not os.path.exists(input_path):
        with open(input_path, "w", encoding="utf-8") as f:
            f.write(input_data)
        print(f"{year}, Day {day} input file created: {input_path}")

    if not os.path.exists(instructions_path):
        with open(instructions_path, "w", encoding="utf-8") as f:
            f.write(instructions)
        print(f"{year}, Day {day} instructions file created: {instructions_path}")

    if not os.path.exists(solution_path):
        try:
            create_solution_file(template_path, solution_path, year, day)
            print(f"{year}, Day {day} solution file created: {solution_path}")
        except AocModError:
            print("Failed to create solution template file.")
    else:
        print(f"{year}, Day {day} solution file already exists.")

    return 0


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

    subparsers = parser.add_subparsers(required=True)

    ### define setup arguments ###

    subparsers.add_parser("setup", help="Initiate the setup of the files for AoC.")

    ### define submission arguments ###

    submit_parser = subparsers.add_parser(
        "submit", help="Initiate a submission of the answer for an AoC problem."
    )
    submit_parser.add_argument(
        "-a", "--answer", type=int, help="Answer to submit.", required=True
    )
    submit_parser.add_argument(
        "-p",
        "--part",
        choices=[1, 2],
        type=int,
        help="Part A = 1; Part B = 2",
        required=True,
    )

    return parser.parse_known_args()


def interactive():
    """Entry-point to the aoc-mod program"""

    known_opts, _ = parse_arguments()

    # create an AOCMod class instance
    aoc_mod = AocMod()

    # parse the year and day
    if known_opts.year is not None and known_opts.day is not None:
        year = known_opts.year
        day = known_opts.day
    else:
        year = aoc_mod.curr_time.tm_year
        day = aoc_mod.curr_time.tm_mday

    print(f"Year: {year}, Day: {day}")

    # if we are submitting, let's do it, otherwise we'll setup the template
    if "answer" in known_opts and "part" in known_opts:
        print(f"Answer: {known_opts.answer}, Level: {known_opts.part}")

        aoc_mod.submit_answer(year, day, known_opts.part, known_opts.answer)
    else:
        setup_challenge_day_template(year, day)
