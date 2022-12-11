import sys
import numpy as np

def read_input(mode):
    with open(f"{mode}.txt") as input:
        # test = list(map(lambda x: (int(x), False), input.readline().strip()))
        # breakpoint()
        trees = np.array(list(map(lambda x: (int(x), False), input.readline().strip())), dtype='i,b')
        for line in input:
            line_as_array = np.array(list(map(lambda x: (int(x), False), line.strip())), dtype='i,b')
            trees = np.vstack((trees, line_as_array))
    return trees

def solve(input):
    visible = 0
    north_vis, input = check_north(input)
    east_vis, input = check_east(input)
    south_vis, input = check_south(input)
    west_vis, input = check_west(input)
    visible += north_vis + east_vis + south_vis + west_vis
    print(visible)

def check_north(input):
    sum = 0
    for x in range(0, input.shape[1]):
        tallest = -1
        for y in range(0, input.shape[0]):
            curr = input[y,x][0]
            if curr > tallest:
                tallest = curr
                if not input[y,x][1]:
                    input[y,x] = (curr, True)
                    sum += 1
    return sum, input

def check_south(input):
    sum = 0
    for x in range(0, input.shape[1]):
        tallest = -1
        for y in range(input.shape[0]-1, 0-1, -1):
            curr = input[y,x][0]
            if curr > tallest:
                tallest = curr
                if not input[y,x][1]:
                    input[y,x] = (curr, True)
                    sum += 1
    return sum, input

def check_west(input):
    sum = 0
    for y in range(0, input.shape[0]):
        tallest = -1
        for x in range(0, input.shape[1]):
            curr = input[y,x][0]
            if curr > tallest:
                tallest = curr
                if not input[y,x][1]:
                    input[y,x] = (curr, True)
                    sum += 1
    return sum, input

def check_east(input):
    sum = 0
    for y in range(0, input.shape[0]):
        tallest = -1
        for x in range(input.shape[1]-1, 0-1, -1):
            curr = input[y,x][0]
            if curr > tallest:
                tallest = curr
                if not input[y,x][1]:
                    input[y,x] = (curr, True)
                    sum += 1
    return sum, input

def main():
    solve(read_input(sys.argv[1]))

if __name__ == "__main__":
    main()