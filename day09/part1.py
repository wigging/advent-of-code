"""
Part 1 of Day 9 for Advent of Code 2023.
https://adventofcode.com/2023/day/9
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
    value = 0

    for line in get_line(text_file):
        hist = [int(x) for x in line.split()]

        hists = []
        hists.append(hist)

        while True:
            diff = [hists[-1][i + 1] - hists[-1][i] for i in range(len(hists[-1]) - 1)]
            hists.append(diff)
            if all(v == 0 for v in hists[-1]):
                break

        for h in hists[::-1]:
            value += h[-1]

    print(f"Part 1 answer -> {value}")


def main():
    run_part1("input.txt")


if __name__ == "__main__":
    main()
