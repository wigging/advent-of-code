"""
Part 1 of Day 11 for Advent of Code 2023.
https://adventofcode.com/2023/day/11
"""
import logging


def get_line(input_file):
    """Yield a line from the puzzle input which is a text file."""
    with open(input_file) as file:
        for line in file:
            yield line.rstrip()


def make_grid(input_file, display=False):
    """Make a grid (list of lists) of the galaxies and empty space."""
    grid = []

    for line in get_line(input_file):
        grid.append([c for c in line])

    if display:
        for g in grid:
            print(g)
        print('')

    return grid


def run_part1(input_file, display_grid=False):
    """Run the example or entire problem for part 1."""
    grid = make_grid(input_file, display=display_grid)

    # Indices of rows and columns with no galaxies
    empty_rows = [i for i, row in enumerate(grid) if all(c == "." for c in row)]
    empty_cols = [j for j, col in enumerate(zip(*grid)) if all(c == "." for c in col)]
    logging.debug(f"{empty_rows = }\n{empty_cols = }")

    # Indices of rows and columns (i, j) of the galaxies
    galaxies = []
    for i, row in enumerate(grid):
        for j, c in enumerate(row):
            if c == "#":
                galaxies.append((i, j))
    logging.debug(f"{galaxies = }")

    total_length = 0

    for i, (gal_row, gal_col) in enumerate(galaxies):
        for gal_row2, gal_col2 in galaxies[:i]:
            for row in range(min(gal_row2, gal_row), max(gal_row2, gal_row)):
                total_length += 2 if row in empty_rows else 1

            for col in range(min(gal_col2, gal_col), max(gal_col2, gal_col)):
                total_length += 2 if col in empty_cols else 1

    print("Total length =", total_length)


def main():
    # logging.basicConfig(format="%(levelname)s:\n%(message)s\n", level=logging.DEBUG)
    # run_part1("input_ex.txt", display_grid=True)

    logging.basicConfig(format="%(levelname)s:\n%(message)s\n", level=logging.INFO)
    run_part1("input.txt")


if __name__ == "__main__":
    main()
