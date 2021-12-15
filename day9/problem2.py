import numpy as np
import pdb

def checkNorth(x,y):
    if y == 0:
        return True
    else:
        return points[y - 1, x] > points[y, x]
def checkEast(x,y):
    if x == points.shape[1] - 1:
        return True
    else:
        return points[y, x + 1] > points[y, x]
def checkSouth(x,y):
    if y == points.shape[0] - 1:
        return True
    else:
        return points[y + 1, x] > points[y, x]
def checkWest(x,y):
    if x == 0:
        return True
    else:
        return points[y, x - 1] > points[y, x]

def checkNeighbors(x,y):
    return checkNorth(x,y) and checkEast(x,y) and checkSouth(x,y) and checkWest(x,y)

def calculateRisk(low_points):
    sum = 0
    for point in low_points:
        sum += int(point) + 1
    return sum


with open("input.txt", "r") as input:
    points = np.array(list(input.readline().strip()))
    for line in input:
        lineAsArray = np.array(list(line.strip()))
        points = np.vstack((points, lineAsArray))

print(points)
low_points = []

for y in range(points.shape[0]):
    for x in range(points.shape[1]):
        # breakpoint()
        if checkNeighbors(x, y):
            # pdb.set_trace()
            # breakpoint()
            low_points.append(points[y,x])

print(calculateRisk(low_points))

# ideas:
# classify each point as seen or unseen when searching
# iterate through every point, ignoring seen
# if unseen, mark as seen
# every time a 9 is encountered, halt this iteration and restart start from the left on the next row
# add each non-9 to current basin
# seems difficult to determine verticality of basin. QUALIFY STOP CONDITIONS FOR EACH ITERATION:
    # save rightmost 9 index of previous row
    # if any non-9 encountered, must continue search
    # else, if no non-9 encountered before index of rightmost 9 of previous row, STOP

# mark each 9
# 