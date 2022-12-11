import sys
import numpy as np

def read_input(mode):
    with open(f"{mode}.txt") as input:
        # (height, total score, n,e,s,w)
        trees = np.array(list(map(lambda x: (int(x), 1, 0,0,0,0), input.readline().strip())), dtype='i,i,i,i,i,i')
        for line in input:
            line_as_array = np.array(list(map(lambda x: (int(x), 1, 0,0,0,0), line.strip())), dtype='i,i,i,i,i,i')
            trees = np.vstack((trees, line_as_array))
    return trees

def solve(input):
    print_input(check_west(check_south(check_east(check_north(input)))))
    print(find_best_score(input))

def print_input(input):
    for y in range(0, input.shape[0]):
        print([f"{input[y,x][0]}: {input[y,x][1]}" for x in range(0, input.shape[1])])


def find_best_score(input):
    score = 0
    for row in input:
        for tree in row:
            score = max(score, tree[1])
    return score


# updates each tree in input with num trees visible when facing north from that posn
def check_north(input):
    for x in range(0, input.shape[1]):
        heights = {
            0:[],
            1:[],
            2:[],
            3:[],
            4:[],
            5:[],
            6:[],
            7:[],
            8:[],
            9:[],
        }
        for y in range(0, input.shape[0]):
            if y == 0:
                n_score = 0
            else:
                closest = 0
                for i in range(input[y,x][0], 10):
                    curr = heights[i]
                    if len(curr) == 0: continue
                    diff = y - curr[0][0]
                    if diff < y - closest:
                        closest = curr[0][0]
                n_score = y - closest
            heights[input[y,x][0]].insert(0, (y,x))
            input[y,x][1] *= n_score
            input[y,x][2] = n_score
    return input

def check_south(input):
    for x in range(0, input.shape[1]):
        heights = {
            0:[],
            1:[],
            2:[],
            3:[],
            4:[],
            5:[],
            6:[],
            7:[],
            8:[],
            9:[],
        }
        for y in range(input.shape[0]-1, 0-1, -1):
            if y == input.shape[0]-1:
                s_score = 0
            else:
                closest = input.shape[0] - 1
                for i in range(input[y,x][0], 10):
                    curr = heights[i]
                    if len(curr) == 0: continue
                    diff = curr[0][0] - y
                    if diff < closest - y:
                        closest = curr[0][0]
                s_score = closest - y
            heights[input[y,x][0]].insert(0, (y,x))
            input[y,x][1] *= s_score
            input[y,x][4] = s_score
    return input

def check_west(input):
    for y in range(0, input.shape[0]):
        heights = {
            0:[],
            1:[],
            2:[],
            3:[],
            4:[],
            5:[],
            6:[],
            7:[],
            8:[],
            9:[],
        }
        for x in range(0, input.shape[1]):
            if x == 0:
                w_score = 0
            else:
                closest = 0
                for i in range(input[y,x][0], 10):
                    curr = heights[i]
                    if len(curr) == 0: continue
                    diff = x - curr[0][1]
                    if diff < x - closest:
                        closest = curr[0][1]
                w_score = x - closest
            heights[input[y,x][0]].insert(0, (y,x))
            input[y,x][1] *= w_score
            input[y,x][5] = w_score
    return input

def check_east(input):
    for y in range(0, input.shape[0]):
        heights = {
            0:[],
            1:[],
            2:[],
            3:[],
            4:[],
            5:[],
            6:[],
            7:[],
            8:[],
            9:[],
        }
        for x in range(input.shape[1]-1, 0-1, -1):
            if x == input.shape[1]-1:
                e_score = 0
            else:
                closest = input.shape[1] - 1
                for i in range(input[y,x][0], 10):
                    curr = heights[i]
                    if len(curr) == 0: continue
                    diff = curr[0][1] - x
                    if diff < closest - x:
                        closest = curr[0][1]
                e_score = closest - x
            heights[input[y,x][0]].insert(0, (y,x))
            input[y,x][1] *= e_score
            input[y,x][3] = e_score
    return input

def main():
    solve(read_input(sys.argv[1]))

if __name__ == "__main__":
    main()