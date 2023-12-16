"""
Part 1 of Day 8 for Advent of Code 2023.
https://adventofcode.com/2023/day/8
"""
import re


def get_line(text_file):
    """
    Yield a line from the text file.
    """
    with open(text_file) as file:
        for line in file:
            yield line.rstrip()


def run_part1(text_file):
    """
    Run the example or entire problem for part 1.
    """
    for line in get_line(text_file):
        instructions = [0 if c == "L" else 1 for c in line]
        break

    network = {}
    for line in get_line(text_file):
        if "=" in line:
            node, left, right = re.findall("[A-Z]+", line)
            network[node] = left, right

    steps = 0
    node = "AAA"
    finish = True
    while finish:
        for inst in instructions:
            if node == "ZZZ":
                finish = False
                break
            steps += 1
            node = network[node][inst]

    # print(f'{instructions = }')
    # print(f'{network = }')

    print(f"Part 1 answer -> {steps}")


def main():
    run_part1("input.txt")


if __name__ == "__main__":
    main()
