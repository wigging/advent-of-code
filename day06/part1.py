"""
Part 1 of Day 6 for Advent of Code 2023.
https://adventofcode.com/2023/day/6
"""
import math


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
        if line.startswith("Time:"):
            s = line.split()
            times = [int(x) for x in s[1:]]
            print(f"{times = }")
        if line.startswith("Distance:"):
            s = line.split()
            records = [int(x) for x in s[1:]]
            print(f"{records = }")

    wins = []

    for i in range(len(times)):
        time = times[i]
        record = records[i]
        win = 0

        for t in range(1, time):
            speed = t
            duration = time - t
            distance = speed * duration

            if distance > record:
                win += 1

        wins.append(win)

    ans = math.prod(wins)

    print(f"{wins = }")
    print(f"Part 1 answer -> {ans}\n")


def main():
    run_part1("input.txt")


if __name__ == "__main__":
    main()
