import argparse
import os
import sys

from collections import Counter
from typing import Tuple

PUZZLE_INPUT = "input.txt"
EXAMPLE_INPUT = "small.txt"

cards = {
    "A": 0,
    "K": 1,
    "Q": 2,
    # "J": 3,
    "T": 4,
    "9": 5,
    "8": 6,
    "7": 7,
    "6": 8,
    "5": 9,
    "4": 10,
    "3": 11,
    "2": 12,
    "1": 13,
    "J": 14
}

hand_types = {
    "five": 0,
    "four": 1,
    "full": 2,
    "three": 3,
    "two pairs": 4,
    "one pair": 5,
    "high card": 6
}

def main():
    in_file = PUZZLE_INPUT
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--test', action='store_true')
    if (parser.parse_args().test):
        in_file = EXAMPLE_INPUT
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, in_file)

    hands_bids = []
    with open(file_path) as input:
        for line in input.readlines():
            hands_bids.append(line.strip().split(" "))
    sorted_hands_bids = sorted(hands_bids, key=rank_sort_key, reverse=True)
    result = 0
    for i, (hand, bid) in enumerate(sorted_hands_bids, start=1):
        result += i*int(bid)
    print(result)
    
def rank_sort_key(hand: Tuple[str, str]):
    return get_hand_type(hand[0]), tie_break_key(hand[0])

def get_hand_type(hand: str):
    card_counts = Counter(hand)

    if "J" in hand:
        wildcard_count = card_counts.pop("J")
        if wildcard_count == 5: return hand_types["five"]
        card_counts[card_counts.most_common(1)[0][0]] += wildcard_count
    
    three = False
    two = 0
    for count in card_counts.values():
        if (count == 5): return hand_types["five"]
        if (count == 4): return hand_types["four"]
        if (count == 3): three = True
        if (count == 2): two += 1
    if (three and two): return hand_types["full"]
    if (three): return hand_types["three"]
    if (two == 2): return hand_types["two pairs"]
    if (two == 1): 
        return hand_types["one pair"]
    return hand_types["high card"]

def tie_break_key(hand: str):
    return tuple(cards[card] for card in hand)

if __name__ == "__main__":
    main()