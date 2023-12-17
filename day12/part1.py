"""
Part 1 of Day 12 for Advent of Code 2023.
https://adventofcode.com/2023/day/12
"""
import logging
from functools import cache


def get_line(input_file):
    """Yield a line from the puzzle input which is a text file."""
    with open(input_file) as file:
        for line in file:
            yield line.rstrip()


@cache
def find_springs(row, nums):
    """Find number of spring arrangements for the row."""
    if not nums:
        return "#" not in row

    row_len = len(row)
    group_len = nums[0]

    if row_len - sum(nums) - len(nums) + 1 < 0:
        return 0

    has_holes = any(row[x] == "." for x in range(group_len))

    if row_len == group_len:
        return 0 if has_holes else 1

    can_use = not has_holes and (row[group_len] != "#")

    if row[0] == "#":
        r = row[group_len + 1 :].lstrip(".")
        n = tuple(nums[1:])
        return find_springs(r, n) if can_use else 0

    skip = find_springs(row[1:].lstrip("."), nums)

    if not can_use:
        return skip

    return skip + find_springs(row[group_len + 1 :].lstrip("."), tuple(nums[1:]))


def run_part1(input_file):
    """Run the example or entire problem for part 1."""
    total = 0

    for line in get_line(input_file):
        row, nums = line.split()
        nums = tuple(int(n) for n in nums.split(","))
        s = find_springs(row, nums)
        total += s
        logging.debug(f"{row = }\n{nums = }\n{s = }")

    print("Total arrangements =", total)


def main():
    # logging.basicConfig(format="%(levelname)s:\n%(message)s\n", level=logging.DEBUG)
    # run_part1("input_ex.txt")

    logging.basicConfig(format="%(levelname)s:\n%(message)s\n", level=logging.INFO)
    run_part1("input.txt")



if __name__ == "__main__":
    main()
