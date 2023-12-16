"""
Part 1 of Day 1 for Advent of Code 2023.
"""


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
    total = 0

    for line in get_line(text_file):
        digits = []

        for c in line:
            if c.isdigit():
                digits.append(c)

        cal_value = int(digits[0] + digits[-1])
        total += cal_value
        # print(f'{line} {digits=} {cal_value=}')

    print(f"Part 1 answer -> {total}")


def main():
    run_part1("input.txt")


if __name__ == "__main__":
    main()
