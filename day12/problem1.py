from queue import Queue
from collections import deque

class Graph:

    def __init__(self, adjList):
        self.adjList = adjList
        self.visited = []
        self.worklist = Queue(maxsize = 0)
        self.numPaths = 0
        # for adj in adjList["start"]:
        #     self.worklist.put(adj)

    def countPaths(self, curr, visited):
        adjs = self.adjList[curr]
        stack = deque()
        if curr == "end":
            self.numPaths += 1
            return
        if curr in visited: 
            return


def bfs(adjList):
    visited = []
    worklist = Queue(maxsize = 0)
    numPaths = 0
    for adj in adjList["start"]:
        worklist.put(adj)
    visited.append("start")
    # breakpoint()
    while not worklist.empty():
        curr = worklist.get()
        # if curr == "A": breakpoint()
        if curr == "end": 
            numPaths += 1
            visited = []
            continue
        if curr.islower(): 
            if curr not in visited:
                visited.append(curr)
            else:
                continue
        for adj in adjList[curr]:
            if adj not in visited:
                worklist.put(adj)

    print(numPaths)




def main():
    adjList = {}
    with open("small.txt", "r") as input:
        for line in input:
            first, second = line.strip().split("-") 
            if first not in adjList: adjList[first] = [second]
            elif second not in adjList[first]: adjList[first].append(second)
            if second not in adjList: adjList[second] = [first]
            elif first not in adjList[second]: adjList[second].append(first)
    bfs(adjList)



if __name__ == "__main__":
    main()