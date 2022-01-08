class myGraph:

    def __init__(self):
        self.adjList = {}

    # def addVertex(self, edge):


def main():
    adjList = {}
    with open("small.txt", "r") as input:
        for line in input:
            first, second = line.strip().split("-") 
            if first not in adjList:
                adjList[first] = [second]
            else:
                adjList[first].append(second)

        print(adjList)


if __name__ == "__main__":
    main()