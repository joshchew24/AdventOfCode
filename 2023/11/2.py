import argparse
import os

import numpy as np

PUZZLE_INPUT = "input.txt"
EXAMPLE_INPUT = "small.txt"

EXPANSION_FACTOR = 10

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
            rows = np.array([list(line) for line in input.read().splitlines()])
        else:
            rows = []
            for line in [list(line) for line in input.read().splitlines()]:
                rows.append([x == "#" for x in line])
            rows = np.array(rows)

    
    galaxies = list(zip(*np.where(rows == "#"))) if pretty else list(zip(*np.where(rows)))
    print(galaxies)
    comparator = "." if pretty else False
    empty_y = 0
    for row in rows:
        if np.all(row == comparator):
            for i, galaxy in enumerate(galaxies):
                galaxy_y, galaxy_x = galaxy
                if galaxy_y > empty_y:
                    galaxies[i] = (galaxy_y + EXPANSION_FACTOR - 1, galaxy_x)
            empty_y += EXPANSION_FACTOR - 1
        else:
            empty_y += 1
    empty_x = 0
    for col in rows.T:
        if np.all(col == comparator):
            for i, galaxy in enumerate(galaxies):
                galaxy_y, galaxy_x = galaxy
                if galaxy_x > empty_x:
                    galaxies[i] = (galaxy_y, galaxy_x + EXPANSION_FACTOR - 1)
            empty_x += EXPANSION_FACTOR - 1
        else:
            empty_x += 1
    print(galaxies)
    sum = 0
    for i, start in enumerate(galaxies):
        for end in galaxies[i:]:
            val = (max(end[1], start[1]) - min(end[1], start[1])) + (max(end[0], start[0]) - min(end[0], start[0]))
            sum += val
    print(sum)

if __name__ == "__main__":
    main()