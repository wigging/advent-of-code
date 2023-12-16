"""
Part 1 of Day 2 for Advent of Code 2023.
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
    max_number = {'red': 12, 'green': 13, 'blue': 14}
    possible_games = []

    for line in get_line(text_file):

        game = line.split(': ')[0]
        game_id = int(game.split(' ')[1])
        game_possible = True

        subsets = line.split(': ')[1].split('; ')

        for subset in subsets:

            cubes = subset.split(', ')

            for cube in cubes:
                number = int(cube.split(' ')[0])
                color = cube.split(' ')[1]

                if number > max_number[color]:
                    game_possible = False

        if game_possible:
            possible_games.append(game_id)

    print(f'Part 1 answer -> {sum(possible_games)}')


def main():
    run_part1('input.txt')


if __name__ == '__main__':
    main()
