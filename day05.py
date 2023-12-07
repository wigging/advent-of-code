"""
Day 5 for Advent of Code 2023.
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

        if line.startswith('seeds:'):
            seeds = [int(x) for x in re.findall('[0-9]+', line)]
            print(f'{seeds = }')
            continue

        if 'map:' in line:
            mapped = [False for _ in seeds]
            # print(f'\n{" " + line + " ":*^40}')
            # print(f'{mapped = }')
            # print(f'... {line.split(" ")[0]}')
            continue

        the_map = [int(x) for x in re.findall('[0-9]+', line)]

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

    print(f'{seeds = }')
    print(f'Part 1 answer -> {min(seeds)}\n')


def run_part2(text_file):
    """
    Run the example or entire problem for part 2.
    """
    nxt = []

    for line in get_line(text_file):

        if line.startswith('seeds:'):
            seed_split = [x.split() for x in re.findall('[0-9]+ [0-9]+', line)]
            seed_tuple = [(int(x[0]), int(x[1])) for x in seed_split]
            seed_range = [(x[0], x[0] + x[1] - 1) for x in seed_tuple]
            print(f'{seed_range = }')
            continue

        if 'map:' in line:
            seed_range = nxt + seed_range
            nxt = []
            continue

        the_map = [int(x) for x in re.findall('[0-9]+', line)]
        aux = []

        if len(the_map) > 0:
            # print(f'{seeds = }')
            # print(f'{the_map = }')

            dest_start = the_map[0]
            src_start = the_map[1]
            length = the_map[2]
            src_end = src_start + length
            diff = dest_start - src_start

            for a, b in seed_range:

                # Before range
                # .....
                #       .....
                # After range
                #       .....
                # .....
                if (b < src_start) or (a >= src_end):
                    aux.append((a, b))
                    continue

                # Before with intersection
                # .....
                #    .....
                if a < src_start and b < src_end:
                    aux.append((a, src_start - 1))
                    nxt.append((src_start + diff, b + diff))
                    continue

                # After with intersection
                #    .....
                # .....
                if a < src_end and b >= src_end:
                    aux.append((a, src_end - 1))
                    nxt.append((src_end + diff, b + diff))
                    continue

                # Within range
                #    ......
                # ............
                if a >= src_start and b < src_end:
                    nxt.append((a + diff, b + diff))
                    continue

                # Larger range
                # ............
                #    ......
                if a < src_start and b >= src_end:
                    aux.append((a, src_start - 1))
                    aux.append((src_end, b))
                    nxt.append((src_start + diff, src_end + diff))
                    continue

            seed_range = aux

    seed_range = nxt + seed_range
    print(f'{seed_range = }')
    print(f'Part 2 answer -> {min(seed_range)[0]}')


def main():
    puzzle_input = 'input/day05.txt'
    run_part1(puzzle_input)
    run_part2(puzzle_input)


if __name__ == '__main__':
    main()
