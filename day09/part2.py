"""
Part 2 of Day 9 for Advent of Code 2023.
https://adventofcode.com/2023/day/9
"""


def get_line(text_file):
    """
    Yield a line from the text file.
    """
    with open(text_file) as file:
        for line in file:
            yield line.rstrip()


def run_part2(text_file):
    """
    Run the example or entire problem for part 2.
    """
    values = []

    for line in get_line(text_file):
        hist = [int(x) for x in line.split()]

        hists = []
        hists.append(hist)

        while True:
            diff = [hists[-1][i+1] - hists[-1][i] for i in range(len(hists[-1]) - 1)]
            hists.append(diff)
            if all(v == 0 for v in hists[-1]):
                break

        # print('\n', hists)

        val = 0
        vals = []
        for h in hists[::-1]:
            # print(h)
            val = h[0] - val
            # print(val)
            vals.append(val)

        values.append(vals[-1])

    # print('\n', values)
    print(f'Part 2 answer -> {sum(values)}')


def main():
    run_part2("input.txt")


if __name__ == "__main__":
    main()
