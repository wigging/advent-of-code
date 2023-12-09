"""
Day 7 for Advent of Code 2023.
https://adventofcode.com/2023/day/7
"""
from collections import Counter
from operator import attrgetter


def get_line(text_file):
    """
    Yield a line from the text file.
    """
    with open(text_file) as file:
        for line in file:
            yield line.rstrip()


def get_value(card: str, part2=False) -> int:
    """
    Get numerical card value.
    """
    if card.isdigit():
        return int(card)
    else:
        if part2:
            j_value = 1
        else:
            j_value = 11
        value = {'A': 14, 'K': 13, 'Q': 12, 'J': j_value, 'T': 10}
        return value[card]


class Hand:

    def __init__(self, line: str, part2=False):
        hand, bid = line.split()
        self.hand = hand
        self.bid = int(bid)
        self.cards = tuple(get_value(card, part2) for card in hand)
        self.part2 = part2

    @property
    def rank(self):
        counter = Counter(self.cards)
        highest = max(counter.values())

        if self.part2:
            wilds = counter[1]
            del counter[1]
            highest = wilds
            if counter:
                highest += max(counter.values())

        if highest == 5:
            return 6        # Five of a kind
        elif highest == 4:
            return 5        # Four of a kind
        elif len(counter) == 2:
            return 4        # Full house
        elif highest == 3:
            return 3        # Three of a kind
        elif len(counter) == 3:
            return 2        # Two pair
        elif highest == 2:
            return 1        # One pair
        else:
            return 0        # High card

    def __repr__(self):
        return f'hand={self.hand} cards={self.cards} bid={self.bid} rank={self.rank}'


def run_part1(text_file):
    """
    Run the example or entire problem for part 1.
    """
    hands = []

    for line in get_line(text_file):
        hand = Hand(line)
        hands.append(hand)

    hands_sorted = sorted(hands, key=attrgetter('rank', 'cards'))
    total_winnings = 0

    for i in range(len(hands_sorted)):
        bid = hands_sorted[i].bid
        total_winnings += bid * (i + 1)

    # for hand in hands: print(hand)
    # print('')
    # for hand in hands_sorted: print(hand)
    # print('')

    print(f'Part 1 answer -> {total_winnings}')


def run_part2(text_file):
    """
    Run the example or entire problem for part 2.
    """
    hands = []

    for line in get_line(text_file):
        hand = Hand(line, part2=True)
        hands.append(hand)

    hands_sorted = sorted(hands, key=attrgetter('rank', 'cards'))
    total_winnings = 0

    for i in range(len(hands_sorted)):
        bid = hands_sorted[i].bid
        total_winnings += bid * (i + 1)

    # for hand in hands: print(hand)
    # print('')
    # for hand in hands_sorted: print(hand)
    # print('')

    print(f'Part 2 answer -> {total_winnings}')


def main():
    puzzle_input = "input/day07.txt"
    run_part1(puzzle_input)
    run_part2(puzzle_input)


if __name__ == "__main__":
    main()
