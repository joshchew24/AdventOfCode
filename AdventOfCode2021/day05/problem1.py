class vent:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1 if x1 <= x2 else x2
        self.y1 = y1 if y1 <= y2 else y2
        self.x2 = x2 if x2 > x1 else x1
        self.y2 = y2 if y2 > y1 else y1
        if x1 == x2: 
            self.orientation = "ver"
        elif y1 == y2:
            self.orientation = "hor" 
        else:
            self.orientation = "dia"

    def print(self):
        print(self.x1, ",", self.y1, " -> ", self.x2, ",", self.y2)

    def getCoords(self):
        coords = []
        if self.orientation == "ver":
            for i in range(self.y1, self.y2 + 1):
                coords.append((self.x1, i))
        elif self.orientation == "hor":
            for i in range(self.x1, self.x2 + 1):
                coords.append((i, self.y1))
        return coords

    def getOrientation(self):
        return self.orientation   


lines = []
with open("input.txt", "r") as input:
    for s in input:
        coord = s.replace(" -> ", ",").split(",")
        line = vent(int(coord[0], 10), int(coord[1],10), int(coord[2], 10), int(coord[3].strip(), 10))
        if line.getOrientation() == "hor" or line.getOrientation() == "ver":
            lines.append(line)

coords = {}
for line in lines:
    for coord in line.getCoords():
            coords[coord] = coords.setdefault(coord, 0) + 1

count = 0
for coord in coords:
    if coords[coord] >= 2:
        count += 1

print(count)
