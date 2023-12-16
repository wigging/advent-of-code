"""
Part 2 of Day 6 for Advent of Code 2023.
https://adventofcode.com/2023/day/6
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
    for line in get_line(text_file):
        if line.startswith("Time:"):
            s = line.split()
            t = [x for x in s[1:]]
            time = int("".join(t))
        if line.startswith("Distance:"):
            s = line.split()
            d = [x for x in s[1:]]
            record = int("".join(d))

    wins = 0

    for t in range(1, time):
        speed = t
        duration = time - t
        distance = speed * duration

        if distance > record:
            wins += 1

    print(f"{time = }\n{record = }")
    print(f"Part 2 answer -> {wins}")


def main():
    run_part2("input.txt")


if __name__ == "__main__":
    main()
