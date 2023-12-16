"""
Day 10 for Advent of Code 2023.
https://adventofcode.com/2023/day/10

This was taking too long to figure out so I went with the approach used by
BjornstadThomas on GitHub.
"""

from collections import deque


def get_line(text_file):
    """Yield a line from the text file."""
    with open(text_file) as file:
        for line in file:
            yield line.rstrip()


def find_start(grid):
    """Find the start S position."""
    start = None

    for i, row in enumerate(grid):
        for j, place in enumerate(row):
            if place == "S":
                start = (i, j)
                break
        if start:
            break

    return start


def find_places(start, grid, pipe_types, directions):
    """Find encountered places."""
    encountered_places = {}
    traversal_queue = deque([(start, 0)])

    while traversal_queue:
        current, distance = traversal_queue.popleft()

        if current in encountered_places:
            continue

        encountered_places[current] = distance

        print(f"Current position: {current}, Distance: {distance}")

        i, j = current

        for direction in pipe_types[grid[i][j]]:
            di, dj, opposite = directions[direction]
            new_i, new_j = i + di, j + dj

            if 0 <= new_i < len(grid) and 0 <= new_j < len(grid[new_i]):
                target = grid[new_i][new_j]

                if target in pipe_types and opposite in pipe_types[target]:
                    traversal_queue.append(((new_i, new_j), distance + 1))

    return encountered_places


def fill_loop_interior(grid, pipe_types, encountered_places):
    """Fill the interior of the loop."""
    for i, row in enumerate(grid):
        norths = 0
        for j, cell in enumerate(row):
            if (i, j) in encountered_places:
                if "n" in pipe_types[cell]:
                    norths += 1
            else:
                grid[i][j] = "I" if norths % 2 != 0 else "O"


def plot_grid(grid, encountered_places):
    """
    Plot the grid as shown below.
    .   .   .   .   .
    .   0   1   2   .
    .   1   .   3   .
    .   2   3   4   .
    .   .   .   .   .
    """
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if (i, j) in encountered_places:
                print(f"{encountered_places[(i, j)]:^4}", end="")
            else:
                print(f'{".":^4}', end="")
        print()


def run_part2(text_file):
    """
    Run the example or entire problem for part 2.
    """
    pipe_types = {
        "|": ["n", "s"],
        "-": ["w", "e"],
        "L": ["n", "e"],
        "J": ["n", "w"],
        "7": ["s", "w"],
        "F": ["s", "e"],
        "S": ["n", "s", "w", "e"],
    }

    directions = {
        "n": (-1, 0, "s"),
        "s": (1, 0, "n"),
        "w": (0, -1, "e"),
        "e": (0, 1, "w"),
    }

    grid = []

    for line in get_line(text_file):
        grid.append([c for c in line])

    start = find_start(grid)
    encountered_places = find_places(start, grid, pipe_types, directions)
    fill_loop_interior(grid, pipe_types, encountered_places)

    inside_count = sum(row.count("I") for row in grid)
    print("\nNumber of tiles inside the loop:", inside_count)


def main():
    puzzle_input = "input/day10.txt"
    run_part2(puzzle_input)


if __name__ == "__main__":
    main()
