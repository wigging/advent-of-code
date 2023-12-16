"""
Part 2 of Day 3 for Advent of Code 2023.
"""
import re
from collections import defaultdict


def get_lines(text_file):
    """
    Get lines from the text file.
    """
    lines = []
    with open(text_file) as file:
        for line in file:
            lines.append(line.rstrip())

    return lines


def run_part2(text_file):
    """
    Run the example or entire problem for part 2.
    """
    lines = get_lines(text_file)

    # Store locations of symbols
    symbols = {}

    for sy, line in enumerate(lines):
        for sx, c in enumerate(line):
            if c not in ".0123456789":
                symbols[(sx, sy)] = c

    # Sum the gear ratios
    part_numbers = defaultdict(list)
    gear_ratios_sum = 0

    for y, line in enumerate(lines):
        matches = re.finditer("[0-9]+", line)
        for m in matches:
            for sx, sy in symbols:
                if (m.start() - 1 <= sx <= m.end()) and (y - 1 <= sy <= y + 1):
                    part_number = int(m.group())
                    part_numbers[(sx, sy)].append(part_number)

    for pos, parts in part_numbers.items():
        if len(parts) == 2 and symbols[pos] == "*":
            gear_ratio = parts[0] * parts[1]
            gear_ratios_sum += gear_ratio

    print(f"Part 2 answer -> {gear_ratios_sum}")


def main():
    run_part2("input.txt")


if __name__ == "__main__":
    main()
