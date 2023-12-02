"""
Day 1 for Advent of Code 2023.
"""


def get_lines(text_file):
    """
    Return a list of all lines in a text file.
    """
    lines = []

    with open(text_file) as file:
        for line in file:
            lines.append(line.rstrip())

    return lines


def run_part1(text_file):
    """
    Run the example or entire problem for part 1.
    """
    lines = get_lines(text_file)
    total = 0

    for line in lines:
        digits = []

        for c in line:
            if c.isdigit():
                digits.append(c)

        cal_value = int(digits[0] + digits[-1])
        total += cal_value
        # print(f'{line} {digits=} {cal_value=}')

    print(f'Part 1 answer -> {total}')


def run_part2(text_file):
    """
    Run the example or entire problem for part 2.
    """
    lines = get_lines(text_file)
    total = 0
    words = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
             'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

    for line in lines:
        digits = []

        for idx, c in enumerate(line):
            if c.isdigit():
                digits.append(c)
            else:
                for w in words:
                    if line[idx:].startswith(w):
                        digits.append(words[w])

        cal_value = int(digits[0] + digits[-1])
        total += cal_value
        # print(f'{line} {digits=} {cal_value=}')

    print(f'Part 2 answer -> {total}')


def main():
    run_part1('input/day01.txt')
    run_part2('input/day01.txt')


if __name__ == '__main__':
    main()