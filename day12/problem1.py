from queue import Queue

def countPaths(adjList):
    return

def bfs(adjList):
    visited = []
    worklist = Queue(maxsize = 0)
    for adj in adjList["start"]:
        worklist.put(adj)
    while not worklist.empty():
        curr = worklist.get()
        visited.append(curr)
    


def main():
    adjList = {}
    with open("small.txt", "r") as input:
        for line in input:
            first, second = line.strip().split("-") 
            if first not in adjList: adjList[first] = [second]
            elif second not in adjList[first]: adjList[first].append(second)
            if second not in adjList: adjList[second] = [first]
            elif first not in adjList[second]: adjList[second].append(first)
        print(adjList)
    bfs(adjList)



if __name__ == "__main__":
    main()