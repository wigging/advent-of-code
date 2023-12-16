"""
Part 1 of Day 4 for Advent of Code 2023.
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
    points = 0

    for line in get_line(text_file):
        win = line.split(": ")[1].split(" | ")[0]
        hand = line.split(": ")[1].split(" | ")[1]

        win_nums = [int(m) for m in re.findall("[0-9]+", win)]
        hand_nums = [int(m) for m in re.findall("[0-9]+", hand)]
        matches = set(win_nums) & set(hand_nums)

        if len(matches) > 0:
            p = 0
            for m in matches:
                if p == 0:
                    p += 1
                else:
                    p *= 2

            points += p

    print(f"Part 1 answer -> {points}")


def main():
    run_part1("input.txt")


if __name__ == "__main__":
    main()
