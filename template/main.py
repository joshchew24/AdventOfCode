import argparse
import sys

PUZZLE_INPUT = "input.txt"
EXAMPLE_INPUT = "small.txt"

def main():
    in_file = PUZZLE_INPUT
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--test', action='store_true')
    if (parser.parse_args().test):
        in_file = EXAMPLE_INPUT
    
    with open(in_file) as input:
        lines = input.readlines()



if __name__ == "__main__":
    main()