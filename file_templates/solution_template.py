"""Advent of Code {YEAR}, Day: {DAY}
Link: https://adventofcode.com/{YEAR}/day/{DAY}"""

import os
import re

from aoc_mod.utilities import AocMod


def get_year_and_day(filepath: str) -> tuple[int, int]:
    """utility function to get current year and day from the
    path to this file

    :param filepath: path to this file
    :type filepath: str
    :return: a tuple with (year, day) as int values
    :rtype: tuple[int, int]
    """
    head, day_folder = os.path.split(filepath)
    head, year_folder = os.path.split(head)

    # get the year from the year folder name
    year_num = int(year_folder)

    # extract the number from the challenge year's day folder name
    day_num = int(re.findall(r"\d+", day_folder)[0])

    return (year_num, day_num)


def parse_input(input_path: str) -> list[str]:
    """utility function to read in puzzle input and
    place it into a list of str values

    :param input_path: path to the input file
    :type input_path: str
    :return: a list of strings representing the input
    :rtype: list[str]
    """
    # read in input data from file
    with open(input_path, "r", encoding="utf-8") as f:
        raw_input = f.read()

    # parse the input data
    input_data = raw_input.splitlines()
    return input_data


def part_one(parsed_input: list[str]) -> dict[str, int]:
    """create the part one solution here

    :param parsed_input: list of strings from parsed input
    :type parsed_input: list[str]
    :return: a dictionary containing the result and a boolean
        where True will submit the part two result
    :rtype: dict[str, int]
    """
    print("Part One")
    output = dict(result=0, submit=False)

    return output


def part_two(parsed_input: list[str]) -> dict[str, int]:
    """create the part two solution here

    :param parsed_input: list of strings from parsed input
    :type parsed_input: list[str]
    :return: a dictionary containing the result and a boolean
        where True will submit the part two result
    :rtype: dict[str, int]
    """
    print("Part Two")
    output = dict(result=0, submit=False)

    return output


def main():
    """main driver function"""
    # set up aoc_mod
    aoc_mod = AocMod()

    # get current path to file
    current_path_to_file = os.path.dirname(os.path.abspath(__file__))

    # get the current year and day and then the input filepath
    year, day = get_year_and_day(current_path_to_file)
    input_path = current_path_to_file + f"/input_{day}.txt"

    print(f"{year}:Day{day}")

    # get the answer for part one
    answer_one = part_one(parse_input(input_path))

    # submit part one, if ready
    if answer_one["submit"]:
        result = aoc_mod.submit_answer(year, day, 1, answer_one["result"])

        # if we get the correct answer for part one, we'll retrieve the instructions for part two
        if "That's the right answer" in result:
            aoc_mod.get_puzzle_instructions(year, day)

    # get the answer for part two
    answer_two = part_two(parse_input(input_path))

    # submit part two, if ready
    if answer_two["submit"]:
        result = aoc_mod.submit_answer(year, day, 2, answer_two["result"])

        # if we get the correct answer for part two, we'll retrieve the rest of the instructions
        if "That's the right answer" in result:
            aoc_mod.get_puzzle_instructions(year, day)


if __name__ == "__main__":
    main()
