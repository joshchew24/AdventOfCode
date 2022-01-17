from collections import defaultdict
from queue import Queue
import numpy as np

class Graph:
    
    def __init__(self, input):
        grid = np.array(list(input.readline().strip()))
        for line in input:
            lineAsArray = np.array(list(line.strip()))
            grid = np.vstack((grid, lineAsArray))
        grid = grid.astype(int)        
        
        self.grid = grid
        self.visited = np.zeros(grid.shape)
    
    def __str__(self):
        return str(self.grid)

    def bfs(self):
        worklist = Queue(maxsize = 0)
        for y, row in enumerate(self.grid):
            for x, elem in enumerate(row):
                print(self.neighbours(x, y))
        
    def neighbours(self, x, y):
        north = (x, y-1) if y > 0 else None
        east = (x+1, y) if x < self.grid.shape[1] - 1 else None
        south = (x, y+1) if y < self.grid.shape[0] - 1 else None
        west = (x-1, y) if x > 0 else None
        return north, east, south, west


def main():
    with open("small.txt", "r") as input:
        graph = Graph(input)
    print(graph)
    graph.bfs()

if __name__ == "__main__":
    main()