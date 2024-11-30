"""Advent of Code 2023, Day: 1
Link: https://adventofcode.com/2023/day/1"""

from aoc_mod import AOCMod

def parse_input(raw_input):
    # parse the input data
    input_data = raw_input.decode("utf-8").splitlines()
    return input_data


def part_a(parsed_input):
    print("Part A")
    return 0


def part_b(parsed_input):
    print("Part B")
    return 0
    

def main():

    # set up aoc_mod
    aoc_mod = AOCMod()

    print("2023:Day1")
    parsed_input = parse_input(aoc_mod.get_puzzle_input(2023, 1))
    instructions = aoc_mod.get_puzzle_instructions(2023, 1)
    
    with open("instructions_2023_1.md", "w", encoding="utf-8") as f:
        f.write(instructions)

    # uncomment below to submit part A
    # aoc_mod.submit_answer(2023, 1, 1, part_a(parsed_input))

    # uncomment below to submit part B
    # aoc_mod.submit_answer(2023, 1, 2, part_b(parsed_input))


if __name__ == "__main__":
    main()