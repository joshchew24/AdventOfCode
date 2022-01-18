from collections import defaultdict
from copy import copy
import heapq
import numpy as np

class PriorityQueue:

    def __init__(self, list):
        self.queue = list
        heapq.heapify(self.queue)
    
    def push(self, elem):
        heapq.heappush(self.queue, elem)

    def pop(self):
        return heapq.heappop(self.queue)

    def __str__(self):
        return str(self.queue)

    def empty(self):
        return len(self.queue) == 0

class Graph:
    
    def __init__(self, input):
        # breakpoint()
        grid = np.array(list(input[0]))
        flag = True
        for line in input:
            if flag: 
                flag = False
                continue
            lineAsarray = np.array(list(line))
            grid = np.vstack((grid, lineAsarray))
        grid = grid.astype(int)        
        
        self.grid = grid
        self.labelled = np.zeros(grid.shape, dtype=bool)
        self.distances = np.ones(grid.shape) * np.inf
        self.predecessors = np.empty(grid.shape, dtype=tuple)

    def __str__(self):
        return str(self.grid)
    def __repr__(self):
        return str(self.grid)

    def dijkstra(self):

        curr = (0, 0)
        self.labelled[curr] = True
        self.distances[curr] = 0
        self.predecessors[curr] = curr

        worklist = []
        worklist.append((self.distances[curr], curr))
        worklist = PriorityQueue(worklist)
        

        while not worklist.empty():
            # breakpoint()
            shortest_path_to_curr, curr = worklist.pop()
            curr_to_v_edge_weight = self.grid[curr]
            self.labelled[curr] = True

            # if curr == (3,6):
            #     breakpoint()

            neighbours = self.neighbours(curr)
            for v in neighbours:
                # if v == (4,6) or v == (4,7) or v == (3,7):
                #     breakpoint()
                if not v: continue
                if self.labelled[v]: continue
                curr_distance_to_v = shortest_path_to_curr + curr_to_v_edge_weight
                if curr_distance_to_v < self.distances[v]:
                    self.distances[v] = curr_distance_to_v
                    self.predecessors[v] = curr
                    worklist.push((self.distances[v], v))


        # print("Path score: ", self.distances[-1,-1])

        path_tracker = (self.grid.shape[0] - 1, self.grid.shape[1] - 1)
        path = []
        sum = 0
        while path_tracker != (0,0):
            sum += self.grid[path_tracker]
            path.append(path_tracker)
            path_tracker = self.predecessors[path_tracker]
        path.append((0,0))
        path.reverse()
        # print("Path:", path)
        print("Path Score:", sum)



    def neighbours(self, point):
        y,x = point
        north = (y-1, x) if y > 0 else None
        east = (y, x+1) if x < self.grid.shape[0] - 1 else None
        south = (y+1, x) if y < self.grid.shape[1] - 1 else None
        west = (y, x-1) if x > 0 else None
        return [north, east, south, west]

def biggify(input):
    # breakpoint()
    big_grid = []
    row = []
    for line in input:
        line = line.strip()
        chars = [int(char) for char in line]
        new_line = copy(line)
        new_chars = copy(chars)
        for i in range(4):
            chars = new_chars
            new_chars = []
            for char in chars:
                new_line += str(add(char))
                new_chars.append(add(char))
        big_grid.append(new_line)
        row.append(new_line)
    
   
    for i in range(4):
        temp = []
        for line in row:
            new_line = ""
            new_line = new_line.join([str(add(int(char))) for char in line])
            big_grid.append(new_line)
            temp.append(new_line)
        row = temp

    return big_grid
    
    


def add(num):
    return num + 1 if num < 9 else 1

def main():
    with open("input.txt", "r") as input:
        input = biggify(input)
        graph = Graph(input)
    graph.dijkstra()

if __name__ == "__main__":
    main()