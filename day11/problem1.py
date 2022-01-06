import numpy as np

class dumbos:
    def __init__(self, input):
        # read first line
        self.points = np.array([int(c) for c in input.readline().strip()])
        # read rest of lines
        for line in input:
            lineAsArray = np.array([int(c) for c in line.strip()])
            self.points = np.vstack((self.points, lineAsArray))

    def step(self):
        self.addOne() 
        toFlash = self.getToFlash()
        while toFlash[0].size > 0:                  # it is presumed that the arrays in the toFlash tuple are the same size as they represent pairs of coordinates
            xs = toFlash[1]
            ys = toFlash[0]
            for x, y in zip(xs, ys):                # can't directly loop through toFlash tuple. this extracts each array and zips them for the loop
                self.flash(x,y)
            toFlash = self.getToFlash()

    def addOne(self):
        self.points = np.vectorize(lambda x : x + 1)(self.points)    
    
    def getToFlash(self):
        return np.where(self.points > 9)

    def flash(self, col, row):                      # handle all flashes. check for any new flashes. handle new flashes. repeat until no new flashes are triggered. then reset all > 9 to 0
        self.points[row, col] = 0
        self.incNeighbours(col, row)

    def incNeighbours(self, col, row):
        # breakpoint()
        for x in range(col - 1, col + 1):
            for y in range(row - 1, row + 1):
                if x < 0 or y < 0: continue
                if x == col and y == row: continue
                self.points[y, x] += 1

    def __str__(self):
        return str(self.points)






def main():
    with open("small.txt", "r") as input:
        board = dumbos(input)
        board.step()
        print(board)


if __name__ == "__main__":
    main()