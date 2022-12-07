with open("input.txt", "r") as input:
    lines = input.readlines()

posX = 0
posY = 0
aim = 0

for l in lines:
    move = l.split()
    direction = move[0]
    magnitude = int(move[1])
    if direction == "forward":
        posX += magnitude
        posY += aim*magnitude
        print(aim*magnitude)
    if direction == "up":
        aim -= magnitude
    if direction == "down":
        aim += magnitude
print("Horizontal Position: ",  posX)
print("Depth: ",  posY)
print("Solution:", posX*posY)