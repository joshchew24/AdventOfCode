import argparse
import os

import numpy as np

PUZZLE_INPUT = "input.txt"
EXAMPLE_INPUT = "small.txt"

def main():
    parser = argparse.ArgumentParser(description='specifying no arguments will run with the puzzle input')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-f', '--file', help='specify an input file to test', default=PUZZLE_INPUT)
    group.add_argument('-t', '--test', dest='file', action='store_const', const=EXAMPLE_INPUT, help='test the instruction example')
    parser.add_argument('-p', '--pretty', action='store_true')
    args = parser.parse_args()
    in_file = args.file
    pretty = args.pretty
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, in_file)

    with open(file_path) as input:
        if pretty:
            rows = np.array([list(x) for x in input.read().splitlines()])
        else:
            rows = []
            for line in [list(line) for line in input.read().splitlines()]:
                rows.append([x == "#" for x in line])
            rows = np.array(rows)

        expanded = np.copy(rows)
        num_rows_added = 0
        comparator = "." if pretty else False
        for i, row in enumerate(rows):
            if np.all(row == comparator):
                expanded = np.insert(expanded, i + num_rows_added, row, axis=0)
                num_rows_added += 1
        cols = expanded.T
        num_cols_added = 0
        for i, col in enumerate(cols):
            if np.all(col == comparator):
                expanded = np.insert(expanded, i + num_cols_added, col, axis=1)
                num_cols_added += 1
        galaxies = list(zip(*np.where(expanded == "#"))) if pretty else list(zip(*np.where(expanded)))

        sum = 0
        galaxies = np.array(galaxies, dtype=int)
        for i, start in enumerate(galaxies):
            for end in galaxies[i:]:
                val = (max(end[1], start[1]) - min(end[1], start[1])) + (max(end[0], start[0]) - min(end[0], start[0]))
                # print(f"distance from {start} to {end} is {val}")
                sum += val
        print(sum)

if __name__ == "__main__":
    main()