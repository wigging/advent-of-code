"""
Day 8 for Advent of Code 2023.
https://adventofcode.com/2023/day/8
"""
import math
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
        instructions = [0 if c == 'L' else 1 for c in line]
        break

    network = {}
    for line in get_line(text_file):
        if '=' in line:
            node, left, right = re.findall('[A-Z]+', line)
            network[node] = left, right

    steps = 0
    node = 'AAA'
    finish = True
    while finish:
        for inst in instructions:
            if node == 'ZZZ':
                finish = False
                break
            steps += 1
            node = network[node][inst]

    # print(f'{instructions = }')
    # print(f'{network = }')

    print(f'Part 1 answer -> {steps}')


def get_instruction(instr: str):
    """
    here
    """
    instruction = [0 if c == 'L' else 1 for c in instr]
    while True:
        yield from instruction


def run_part2(text_file):
    """
    Run the example or entire problem for part 2.
    """
    for line in get_line(text_file):
        instructions = line
        break

    network = {}
    for line in get_line(text_file):
        if '=' in line:
            node, left, right = re.findall('[0-9A-Z]+', line)
            network[node] = left, right

    all_steps = []
    for node in filter(lambda x: x[-1] == 'A', network):
        # periods.append(solve(instr, net, node))

        steps = 0

        for i in get_instruction(instructions):
            if node[-1] == 'Z':
                all_steps.append(steps)
                break
            steps += 1
            node = network[node][i]

    least_steps = math.lcm(*all_steps)

    # print(f'{instructions = }')
    # print(f'{network = }')
    # print(f'{all_steps = }')

    print(f'Part 2 answer -> {least_steps}')


def main():
    puzzle_input = "input/day08.txt"
    run_part1(puzzle_input)
    run_part2(puzzle_input)


if __name__ == "__main__":
    main()
