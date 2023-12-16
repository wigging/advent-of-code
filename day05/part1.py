"""
Part 1 of Day 5 for Advent of Code 2023.
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
        if line.startswith("seeds:"):
            seeds = [int(x) for x in re.findall("[0-9]+", line)]
            print(f"{seeds = }")
            continue

        if "map:" in line:
            mapped = [False for _ in seeds]
            # print(f'\n{" " + line + " ":*^40}')
            # print(f'{mapped = }')
            # print(f'... {line.split(" ")[0]}')
            continue

        the_map = [int(x) for x in re.findall("[0-9]+", line)]

        if len(the_map) > 0:
            # print(f'{seeds = }')
            # print(f'{the_map = }')

            dest = the_map[0]
            src = the_map[1]
            length = the_map[2]

            for i in range(len(seeds)):
                seed = seeds[i]
                is_mapped = mapped[i]
                if (seed >= src) and (seed < (src + length)) and (is_mapped is False):
                    seeds[i] = dest + (seed - src)
                    mapped[i] = True

            # print(f'{mapped = }')
            # print(f'{seeds = }\n')

    print(f"{seeds = }")
    print(f"Part 1 answer -> {min(seeds)}\n")


def main():
    run_part1("input.txt")


if __name__ == "__main__":
    main()
