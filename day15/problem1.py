from collections import defaultdict
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
        grid = np.array(list(input.readline().strip()))
        for line in input:
            lineAsarray = np.array(list(line.strip()))
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


        print("Path score: ", self.distances[-1,-1])

        path_tracker = (self.grid.shape[0] - 1, self.grid.shape[1] - 1)
        path = []
        while path_tracker != (0,0):
            path.append(path_tracker)
            path_tracker = self.predecessors[path_tracker]
        path.append((0,0))
        path.reverse()
        print("Path:", path)



    def neighbours(self, point):
        y,x = point
        north = (y-1, x) if y > 0 else None
        east = (y, x+1) if x < self.grid.shape[0] - 1 else None
        south = (y+1, x) if y < self.grid.shape[1] - 1 else None
        west = (y, x-1) if x > 0 else None
        return [north, east, south, west]


def main():
    with open("input.txt", "r") as input:
        graph = Graph(input)
    print(graph)
    graph.dijkstra()

if __name__ == "__main__":
    main()