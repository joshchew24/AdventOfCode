import argparse
import os

from itertools import groupby

PUZZLE_INPUT = "input.txt"
EXAMPLE_INPUT = "small.txt"

def main():
    parser = argparse.ArgumentParser(description='specifying no arguments will run with the puzzle input')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-f', '--file', help='specify an input file to test', default=PUZZLE_INPUT)
    group.add_argument('-t', '--test', dest='file', action='store_const', const=EXAMPLE_INPUT, help='test the instruction example')
    args = parser.parse_args()
    in_file = args.file
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, in_file)

    with open(file_path) as input:
        lines = input.read().splitlines()
    solve(lines)

def solve(lines):
    sum = 0
    for line in lines:
        sum += get_num_arrangements(line)
    print(sum)

def get_num_arrangements(line):
    conditions, broken_groups = line.split(" ")
    broken_groups = [int(group) for group in broken_groups.split(",")]
    condition_groups = groupby(conditions)
    first_broken_group_length = broken_groups[0]
    for condition, length in condition_groups:
        if condition == "#":
            if length == first_broken_group_length
    print([(condition, len(list(length))) for condition, length in condition_groups])

    print(broken_groups)
    return 0



if __name__ == "__main__":
    main()