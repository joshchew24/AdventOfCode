with open("input.txt", "r") as input:
    lines = input.readlines()

posX = 0
posY = 0

for l in lines:
    move = l.split()
    direction = move[0]
    magnitude = int(move[1])
    if direction == "forward":
        posX += magnitude
    if direction == "up":
        posY -= magnitude
    if direction == "down":
        posY += magnitude
print("Horizontal Position: ",  posX)
print("Depth: ",  posY)
print("Solution:", posX*posY)