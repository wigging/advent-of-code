"""
Part 1 of Day 10 for Advent of Code 2023.
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
        available_directions = pipe_types[grid[i][j]]

        for direction in available_directions:
            di, dj, opposite = directions[direction]
            new_i, new_j = i + di, j + dj

            if not (0 <= new_i < len(grid) and 0 <= new_j < len(grid[new_i])):
                continue

            target = grid[new_i][new_j]

            if target not in pipe_types or opposite not in pipe_types[target]:
                continue

            traversal_queue.append(((new_i, new_j), distance + 1))

            print(f"  Moving {direction}, New position: ({new_i}, {new_j})")

    return encountered_places


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


def run_part1(text_file):
    """
    Run the example or entire problem for part 1.
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
    max_distance = max(encountered_places.values())

    print("\nMax Distance:", max_distance)

    # print("\nGrid Visualization with Distances:")
    # plot_grid(grid, encountered_places)


def main():
    run_part1("input.txt")


if __name__ == "__main__":
    main()
