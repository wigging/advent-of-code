"""
Part 1 of Day 13 for Advent of Code 2023.
https://adventofcode.com/2023/day/13
"""
import logging


def find_mirror_index(grid):
    """Find index of mirror location."""
    for i in range(1, len(grid)):
        top_half = grid[:i][::-1]
        bottom_half = grid[i:]
        n = min(len(top_half), len(bottom_half))

        logging.debug(f"{top_half = }\n{bottom_half = }")
        logging.debug(f"{top_half[:n] = }\n{bottom_half[:n] = }")

        if top_half[:n] == bottom_half[:n]:
            return i

    return 0


def run_part1(input_file):
    """Run the example or entire problem for part 1."""
    with open(input_file) as file:
        blocks = file.read().split("\n\n")

    answer = 0

    for block in blocks:
        grid = block.splitlines()
        logging.debug(grid)

        row_index = find_mirror_index(grid)
        answer += row_index * 100

        transpose_grid = list(zip(*grid))
        column_index = find_mirror_index(transpose_grid)
        answer += column_index

        logging.debug(f"{row_index = }\n{column_index = }\n")

    print(f"Part 1 answer -> {answer}")


def main():
    # logging.basicConfig(format="%(levelname)s:\n%(message)s\n", level=logging.DEBUG)
    # run_part1("input_ex.txt")

    logging.basicConfig(format="%(levelname)s:\n%(message)s\n", level=logging.INFO)
    run_part1("input.txt")


if __name__ == "__main__":
    main()
