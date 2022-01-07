import numpy as np
from queue import Queue

class dumbos:
    def __init__(self, input):
        # read first line
        self.points = np.array([int(c) for c in input.readline().strip()])
        # read rest of lines
        for line in input:
            lineAsArray = np.array([int(c) for c in line.strip()])
            self.points = np.vstack((self.points, lineAsArray))
        self.queue = Queue(maxsize = 0)
        self.numFlashes = 0

    def step(self):
        self.addOne() 
        self.enqueueToFlash()  
        self.enqueueProcessLoop()
       
    def doSteps(self, numSteps):
        while numSteps:
            print(self)
            print("number of steps left:", numSteps)
            self.step()
            numSteps -= 1
        print(self)

    def addOne(self):
        self.points = np.vectorize(lambda x : x + 1)(self.points)    
    
    def enqueueToFlash(self):
        toFlash = np.where(self.points > 9)
        xs = toFlash[1]
        ys = toFlash[0]
        for x, y in zip(xs, ys):                # can't directly loop through toFlash tuple. this extracts each array and zips them for the loop
            self.queue.put((y,x))

    def processQueue(self):
        while not self.queue.empty():
            curr = self.queue.get()
            if self.points[curr] == 0: continue
            if self.points[curr] > 9:
                self.flash(curr)
            else:
                self.points[curr] += 1

    def flash(self, curr):
        self.points[curr] = 0
        self.numFlashes += 1
        self.enqueueNeighbours(curr)

    def enqueueNeighbours(self, curr):
        col, row = curr
        for x in range(col - 1, col + 2):
            if x < 0 or x >= self.points.shape[1]: continue
            for y in range(row - 1, row + 2):
                if y < 0 or y >= self.points.shape[0]: continue
                if x == col and y == row: continue
                self.queue.put((x, y))
            
    
    def enqueueProcessLoop(self):
        while not self.queue.empty():
            self.processQueue()
            self.enqueueToFlash()

    def printQ(self):
        print(list(self.queue.queue))

    def __str__(self):
        return str(self.points)






def main():
    with open("input.txt", "r") as input:
        board = dumbos(input)
        board.doSteps(100)
        print(board.numFlashes)


if __name__ == "__main__":
    main()