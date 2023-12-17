import argparse
import os
import sys

PUZZLE_INPUT = "input.txt"
EXAMPLE_INPUT = "small.txt"

def main():
    in_file = PUZZLE_INPUT
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--test', action='store_true', help='test the instruction example')
    parser.add_argument('-f', '--file', help='specify an input file to test')
    args = parser.parse_args()
    if (args.test):
        in_file = EXAMPLE_INPUT
    elif (args.file):
        in_file = args.file
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, in_file)

    with open(file_path) as input:
        lines = input.readlines()
        print(lines)



if __name__ == "__main__":
    main()