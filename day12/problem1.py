def countPaths(adjList):
    return
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
    countPaths(adjList)



if __name__ == "__main__":
    main()