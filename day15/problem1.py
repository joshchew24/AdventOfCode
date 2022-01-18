from collections import defaultdict
import heapq
import numpy as np

class PriorityQueue:

    def __init__(self, list):
        self.queue = list
        heapq.heapify(queue)

class Graph:
    
    def __init__(self, input):
        grid = np.array(list(input.readline().strip()))
        for line in input:
            lineAsArray = np.array(list(line.strip()))
            grid = np.vstack((grid, lineAsArray))
        grid = grid.astype(int)        
        
        self.grid = grid
        self.labelled = np.zeros(grid.shape, dtype=bool)
        self.distances = np.ones(grid.shape) * np.inf
        self.predecessors = np.empty(grid.shape, dtype=tuple)

    def __str__(self):
        return str(self.grid)

    def dijkstra(self):

        curr = (0, 0)
        self.labelled[curr] = True
        self.distances[curr] = 0
        self.predecessors[curr] = curr

        worklist = []
        worklist.append((self.distances[curr], (1, 0)))#########!!!!!!!!!!!!!!!!!!!!!!!!!!
        worklist.append((1, (0, 1)))
        heapq.heapify(worklist)

        curr_to_v_edge_weight = self.grid[curr]
        shortest_path_to_curr = self.distances[curr]

        neighbours = self.neighbours(curr)
        for v in neighbours:
            if not v: continue
            if self.labelled[v]: continue
            curr_distance_to_v = shortest_path_to_curr + curr_to_v_edge_weight
            if curr_distance_to_v < self.distances[v]:
                self.distances[v] = curr_to_v_edge_weight
            heapq.heappush(worklist, (self.distances[v], v))

        # print(self.labelled)
        # print(self.distances)
        # print(self.predecessors)
        # print(d)
        



    def neighbours(self, point):
        x,y = point
        north = (x, y-1) if y > 0 else None
        east = (x+1, y) if x < self.grid.shape[1] - 1 else None
        south = (x, y+1) if y < self.grid.shape[0] - 1 else None
        west = (x-1, y) if x > 0 else None
        return [north, east, south, west]


def main():
    with open("small.txt", "r") as input:
        graph = Graph(input)
    print(graph)
    graph.dijkstra()

if __name__ == "__main__":
    main()