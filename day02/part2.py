"""
Part 2 of Day 2 for Advent of Code 2023.
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
    powers = []

    for line in get_line(text_file):
        subsets = line.split(": ")[1].split("; ")

        reds = []
        greens = []
        blues = []

        for subset in subsets:
            cubes = subset.split(", ")

            for cube in cubes:
                number = int(cube.split(" ")[0])
                color = cube.split(" ")[1]

                if color == "red":
                    reds.append(number)

                if color == "green":
                    greens.append(number)

                if color == "blue":
                    blues.append(number)

        power = max(reds) * max(greens) * max(blues)
        powers.append(power)

    print(f"Part 2 answer -> {sum(powers)}")


def main():
    run_part2("input.txt")


if __name__ == "__main__":
    main()
