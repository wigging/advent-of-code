"""
Day 2 for Advent of Code 2023.
"""


def get_lines(text_file):
    """
    Return a list of all lines in a text file.
    """
    lines = []

    with open(text_file) as file:
        for line in file:
            lines.append(line.rstrip())

    return lines


def run_part1(text_file):
    """
    Run the example or entire problem for part 1.
    """
    max_number = {'red': 12, 'green': 13, 'blue': 14}
    possible_games = []

    lines = get_lines(text_file)

    for line in lines:

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


def run_part2(text_file):
    """
    Run the example or entire problem for part 2.
    """
    powers = []
    lines = get_lines(text_file)

    for line in lines:
        subsets = line.split(': ')[1].split('; ')

        reds = []
        greens = []
        blues = []

        for subset in subsets:
            cubes = subset.split(', ')

            for cube in cubes:
                number = int(cube.split(' ')[0])
                color = cube.split(' ')[1]

                if color == 'red':
                    reds.append(number)

                if color == 'green':
                    greens.append(number)

                if color == 'blue':
                    blues.append(number)

        power = max(reds) * max(greens) * max(blues)
        powers.append(power)

    print(f'Part 2 answer -> {sum(powers)}')


def main():
    run_part1('input/day02.txt')
    run_part2('input/day02.txt')


if __name__ == '__main__':
    main()
