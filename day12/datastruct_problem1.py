class Graph:
    def __init__(self):
        self.adjList = {}

    # def addVertex(self, edge):

class Node:
    def __init__(self, key):
        self.key = key
        self.visited = False

    def __repr__(self):
        return str(self.key)

def main():
    adjList = {}
    trackingList = {}
    with open("small.txt", "r") as input:
        for line in input:
            first, second = line.strip().split("-") 

            startNode = Node(first)
            destNode = Node(second)
            if first not in trackingList:
                adjList[startNode] = [destNode]
                trackingList[first] = [second]
            elif second not in trackingList[first]: 
                adjList[startNode].append(destNode)
                trackingList[first].append(second)
            if second not in trackingList: 
                adjList[destNode] = [startNode]
                trackingList[second] = [first]
            elif first not in trackingList[destNode]: 
                adjList[destNode].append(startNode)
                trackingList[second].append(first)
        print(adjList)


if __name__ == "__main__":
    main()