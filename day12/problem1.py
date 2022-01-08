class Graph:
    def __init__(self):
        self.adjList = {}

    # def addVertex(self, edge):

class Node:
    def __init__(self, key):
        self.key = key
        self.visited = False

def main():
    adjList = {}
    with open("small.txt", "r") as input:
        for line in input:
            first, second = line.strip().split("-") 
            if first not in adjList:
                adjList[first] = [second]
            else:
                if second not in adjList[first]: adjList[first].append(second)
            if second not in adjList:
                adjList[second] = [first]
            else:
                if first not in adjList[second]: adjList[second].append(first)
        print(adjList)


if __name__ == "__main__":
    main()