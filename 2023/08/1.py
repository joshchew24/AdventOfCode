import argparse
import os

from itertools import cycle

PUZZLE_INPUT = "input.txt"
EXAMPLE_INPUT = "small.txt"

def main():
    parser = argparse.ArgumentParser(description='specifying no arguments will run with the puzzle input')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-f', '--file', help='specify an input file to test', default=PUZZLE_INPUT)
    group.add_argument('-t', '--test', dest='file', action='store_const', const=EXAMPLE_INPUT, help='test the instruction example')
    in_file = parser.parse_args().file
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, in_file)

    with open(file_path) as input:
        directions = cycle([direction == "R" for direction in input.readline().strip()]) # left is false, right is true
        input.readline()
        nodes = {}
        for node in input.readlines():
            curr, children = node.strip().split(" = ")
            left, right = children.strip("()").split(", ")
            child_tuple = (left, right)
            nodes[curr] = child_tuple
    curr_node = "AAA"
    num_moves = 0
    while curr_node != "ZZZ":
        direction = next(directions)
        curr_node = nodes[curr_node][direction]
        num_moves += 1
    print(num_moves)
        



if __name__ == "__main__":
    main()