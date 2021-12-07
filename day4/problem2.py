class BingoBoard:
    # rowContainer = []
    def __init__(self):
        self.rowContainer = []
        self.lines = [0]*10         # 0-4 are vertical, 5-9 are horizontal
        self.seen = []
        self.winningScore = 0
    def print(self):
        for row in self.rowContainer:
            print(row)
    def contains(self, num):
        if self.isWinner():
            return False
        for y in range(5):
            for x in range(5):
                if num == self.rowContainer[y][x]:
                    self.count(num, x,y)
                    return True
    def isWinner(self):
        for c in self.lines:
            if c == 5:
                if self.winningScore == 0:
                    self.winningScore = self.sumUnmarked() * int(self.seen[-1], 10)      # if haven't won yet, update
                return True
    def count(self, num, x, y):
        self.lines[x] += 1
        self.lines[y+5] += 1
        self.seen.append(num)
    def sumUnmarked(self):
        sum = 0
        for row in self.rowContainer:
            for n in row:
                if not self.seen.count(n):
                    sum += int(n,10)
        return sum

    
boards = []
draw = []
with open("input.txt", "r") as input:
    draw = input.readline().split(",")
    line = input.readline()

    while(line):
        board = BingoBoard()
        for i in range(5):
            row = input.readline().split()
            board.rowContainer.append(row)
        boards.append(board)
        
        line = input.readline()

dupes = boards.copy()
for num in draw:
    for count, board in enumerate(boards):
        if board.contains(num):
            if board.isWinner():
                lastWinner = count
                dupes.remove(board)

choice = boards[lastWinner]
choice.print()
print(choice.winningScore)
            

    
