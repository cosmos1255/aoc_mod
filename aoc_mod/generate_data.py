"""Script to initialize a new day for Advent of Code.
This script will basically grab the input and puzzle clue
from the Advent of Code website.

If user specifies a year and day, this script will create
the files pertaining to that day and year.

Author: David Eyrich
"""

import argparse
import os
import json
import logging
import time
import requests

from aoc_mod.helpers.file_templates import SINGLE_DAY_PYTHON_SCRIPT

logger = logging.getLogger(__name__)


def aoc_mod_parse_args():
    """Simple argparser."""

    args = argparse.ArgumentParser(add_help=True)

    args.add_argument(
        "-c",
        "--config",
        help="Configuration file containing session-id and user-agent (see readme for assistance).",
        required=True,
    )

    args.add_argument(
        "--debug", action="store_true", help="Enable debug print statements."
    )

    args.add_argument(
        "-y", help="Enter the year of the Advent of Code challenge you would like."
    )
    args.add_argument(
        "-d", help="Enter the day of the Advent of Code challenge you would like."
    )

    return args.parse_args()


def get_curr_time():
    """Returns the current time."""
    cur_time = time.time()
    return time.localtime(cur_time)


def parse_year_day(str_year, str_day):
    """Parses the current year and day to determine if it's
    valid. For example, not a date that hasn't occurred.

    @param str_year: year as a string
    @param str_day: day as a string

    @return tuple of (year, day) as ints"""

    cur_time = get_curr_time()
    min_year = 2015
    max_year = cur_time.tm_year

    int_year = int(str_year)
    int_day = int(str_day)

    # check for correct year
    if int_year < min_year or int_year > max_year:
        logger.error(
            "The year provided is either too early (before %s), or has not occurred yet. Please try again.",
            min_year,
        )
        exit(1)

    # check for correct day
    if int_day < 1 or int_day > 25:
        logger.error(
            "Improper day entered, Advent of Code runs from December 1st to 25th."
        )
        exit(1)

    # if we get here, we have a valid day and year
    return int_year, int_day


def grab_data(year, day, config_data):
    """Performs a get request to the adventofcode site for
    the current year and day.

    @param year - input year
    @param day - input day

    @return input_data response or None for failure"""

    aoc_url = f"https://adventofcode.com/{year}/day/{day}/input"

    # grab input data
    response = requests.get(
        url=aoc_url,
        cookies={
            "session": config_data["session-id"],
            "User-Agent": config_data["user-agent"],
        },
        timeout=5,
    )

    if response.status_code != 200:
        logger.error(
            "Request was invalid, received code: %d. Please check session-id and user-agent.",
            response.status_code,
        )
        exit(1)

    return response.content


def check_december():
    """Function to check if it is December or not. Also verifies
    the current day to check if we have passed Christmas.

    Returns:
        tuple: (current_year, current_day)
    """
    cur_time = get_curr_time()

    if cur_time.tm_mon != 12:
        logger.error(
            "It's not quite time for this script to be run. Please wait until December!"
        )
        exit(1)

    if cur_time.tm_mday > 25:
        logger.error(
            "Oh no! Christmas is over? Please select a day from December 1st to the 25th to receive data."
        )
        exit(1)

    # if we make it here, it is December 1st-25th of the proper year
    return cur_time.tm_year, cur_time.tm_mday


def main():
    """AOC_MOD start"""

    opts = aoc_mod_parse_args()

    if opts.debug:
        logging.basicConfig(level=logging.DEBUG)

    # open config file for reading
    with open(opts.config, "w", encoding="utf-8") as conf_file:
        config_data = json.loads(conf_file)
        if "session_id" not in config_data or "user_agent" not in config_data:
            logger.error(
                "Unable to find correct contents of config (session-id and user-agent)."
            )
            exit(1)

    # check for both year and day or generate our own
    if opts.y is not None and opts.d is not None:
        year, day = parse_year_day(opts.y, opts.d)
    elif opts.y is not None or opts.d is not None:
        logger.error("Both year and day are required to create challenge data.")
        exit(1)
    else:
        year, day = check_december()

    # grab the input data with the proper year and day
    data = grab_data(year, day, config_data)

    # create proper files to be used
    day_path = f"challenges/{year}/day{day}"

    os.system(f"mkdir -p {day_path}")

    soln_path = f"{day_path}/day{day}.py"
    input_path = f"{day_path}/day{day}_input.txt"

    if not os.path.exists(soln_path):
        with open(soln_path, "w", encoding="utf-8") as f_soln:
            if "author" in config_data:
                f_soln.write(
                    SINGLE_DAY_PYTHON_SCRIPT.format(
                        AUTHOR=config_data["author"],
                        YEAR=year,
                        DAY=day,
                        scripts_path_join="{scripts_path_join}",
                    )
                )
            else:
                f_soln.write(
                    SINGLE_DAY_PYTHON_SCRIPT.format(
                        AUTHOR="Anonymous",
                        YEAR=year,
                        DAY=day,
                        scripts_path_join="{scripts_path_join}",
                    )
                )

    else:
        logger.warning("%s, Day %s solution file already exists.", year, day)

    if not os.path.exists(input_path):
        with open(input_path, "wb") as f_input:
            f_input.write(data[:-1])
    else:
        logger.warning("%s, Day %s input file already exists.", year, day)


if __name__ == "__main__":
    main()
