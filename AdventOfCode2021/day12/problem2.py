from copy import deepcopy

class Graph:

    def __init__(self, adjList):
        self.adjList = adjList
        self.numPaths = 0

    def countPaths(self):
        self.countPath("start", [], True)
        print(self.numPaths)

    def countPath(self, curr, visited, canDupe):
        nextCanDupe = canDupe
        adjs = self.adjList[curr]
        if curr == "end":
            self.numPaths += 1
            print(visited, curr)
            return
        if curr.islower() and curr in visited:
            if canDupe:
                nextCanDupe = False
            else:
                return
        if curr == "start" and curr in visited:
            return
        for adj in adjs:
            nextVisited = deepcopy(visited)
            nextVisited.append(curr)
            self.countPath(adj, nextVisited, nextCanDupe)

def main():
    adjList = {}
    with open("input.txt", "r") as input:
        for line in input:
            first, second = line.strip().split("-") 
            if first not in adjList: adjList[first] = [second]
            elif second not in adjList[first]: adjList[first].append(second)
            if second not in adjList: adjList[second] = [first]
            elif first not in adjList[second]: adjList[second].append(first)
    graph = Graph(adjList)
    graph.countPaths()

if __name__ == "__main__":
    main()