class BingoBoard:
    # rowContainer = []
    def __init__(self):
        self.rowContainer = []
        self.lines = [0]*10         # 0-4 are vertical, 5-9 are horizontal
        self.seen = []
    def print(self):
        for row in self.rowContainer:
            print(row)
    def contains(self, num):
        for y in range(5):
            for x in range(5):
                if num == self.rowContainer[y][x]:
                    self.count(num, x,y)
    def isWinner(self):
        for c in self.lines:
            if c == 5:
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
draw = ""
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

for num in draw:
    for board in boards:
        board.contains(num)
        if board.isWinner():
            print(board.sumUnmarked() * int(num, 10))
            exit()
            
