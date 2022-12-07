import numpy as np

def checkNorth(point, prev):
    # if y is not at the top and prev is not above y and 
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


def calculateBasinScore(low_points):
    hi, mid, lo = 0, 0, 0
    for point in low_points:
        currBasin = calculateBasin(point[0], point[1])
        if currBasin > lo:
            if currBasin > mid:
                if currBasin > hi:
                    lo = mid
                    mid = hi
                    hi = currBasin
                else:
                    lo = mid
                    mid = currBasin
            else:
                lo = currBasin
    print(hi, mid, lo)
    return hi*mid*lo

# point is the current point to count. prev is the point used to reach current point
def calculateBasin(y, x):
    track[y, x] = 1
    if points[y, x] == 9:
        return 0
    north, east, south, west = 0, 0, 0, 0
    if y != 0 and track[y - 1, x] == 0:
        north = calculateBasin(y - 1, x)
    if x != points.shape[1] - 1 and track[y, x + 1] == 0:
        east = calculateBasin(y, x + 1)
    if y != points.shape[0] - 1 and track[y + 1, x] == 0:
        south = calculateBasin(y + 1, x)
    if x != 0 and track[y, x - 1] == 0:
        west = calculateBasin(y, x - 1)
    return 1 + north + east + south + west
    

with open("input.txt", "r") as input:
    points = np.array(list(map(int, list(input.readline().strip()))))
    for line in input:
        lineIntArr = list(map(int,list(line.strip())))
        points = np.vstack((points, lineIntArr))
    track = np.zeros(points.shape)

print(points)
low_points = []

for y in range(points.shape[0]):
    for x in range(points.shape[1]):
        if checkNeighbors(x, y):
            low_points.append((y, x))

print(calculateBasinScore(low_points))