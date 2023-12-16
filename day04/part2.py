"""
Part 2 of Day 4 for Advent of Code 2023.
"""
import re


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
    scratchcards = []

    # Create scratchcards list with initial values of 1
    for _ in get_line(text_file):
        scratchcards.append(1)

    # Process scratchcard originals and copies
    for line in get_line(text_file):
        card = line.split(": ")[0].split()[1]
        card_number = int(card)

        win = line.split(": ")[1].split(" | ")[0]
        hand = line.split(": ")[1].split(" | ")[1]

        win_nums = [int(m) for m in re.findall("[0-9]+", win)]
        hand_nums = [int(m) for m in re.findall("[0-9]+", hand)]
        matches = set(win_nums) & set(hand_nums)

        n_matches = len(matches)

        for n in range(n_matches):
            scratchcards[card_number + 1 + n] += scratchcards[card_number]

    scratchcards_sum = sum(scratchcards)
    print(f"Part 2 answer -> {scratchcards_sum}")


def main():
    run_part2("input.txt")


if __name__ == "__main__":
    main()
