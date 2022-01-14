from collections import defaultdict
from copy import copy
import numpy as np
import matplotlib.pyplot as plt


def mirror(coords, axis, posn):        
    coord_to_flip = coords[axis]
    flipped = False
    if coord_to_flip > posn:
        flipped = True
        flipped_coord = coord_to_flip - 2*(coord_to_flip - posn)
        coords = (coords[0], flipped_coord) if axis == 1 else (flipped_coord, coords[1])
    return coords, flipped

def get_axis_to_change_and_posn(instr):
    axis_str, posn = instr.split("=")
    posn = int(posn)
    axis_to_change = 0 if axis_str == "x" else 1
    return axis_to_change, posn

def print_folded(coords):
    plt.scatter(*zip(*coords))
    plt.show()


def main():
    with open("input.txt", "r") as input:
        dots = defaultdict(int)
        for line in input:
            x,y = line.strip('\n').split(",")
            dot = (int(x),int(y))
            dots[dot] = 1
    with open("folds.txt", "r") as instructions:
        temp_dict = copy(dots)
        for line in instructions:
            fold = line.strip("\n")
            axis, posn = get_axis_to_change_and_posn(fold)

            for dot in dots:
                new_coords, mirrored = mirror(dot, axis, posn)
                if mirrored:
                    temp_dict.pop(dot)
                    if new_coords not in dots:
                        temp_dict[new_coords] = 1

            dots = temp_dict
            temp_dict = copy(dots)
        
            coords = list(dots.keys())
            coords.sort()
            print(coords)
    print_folded(list(dots.keys()))


if __name__ == "__main__":
    main()