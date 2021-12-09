class vent:
    def __init__(self, x1, y1, x2, y2):
        # self.x1 = x1 if x1 <= x2 else x2
        # self.y1 = y1 if y1 <= y2 else y2
        # self.x2 = x2 if x2 > x1 else x1
        # self.y2 = y2 if y2 > y1 else y1
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        if x1 == x2: 
            self.orientation = "ver"
        elif y1 == y2:
            self.orientation = "hor" 
        else:
            self.orientation = "dia"

        self.delta_x = "pos" if x2 >= x1 else "neg"
        self.delta_y = "pos" if y2 >= y1 else "neg"

    def print(self):
        print(self.x1, ",", self.y1, " -> ", self.x2, ",", self.y2)

    def getCoords(self):
        coords = []
        if self.orientation == "ver":
            step_offset = 1 if self.delta_y == "pos" else -1
            for i in range(self.y1, self.y2 + step_offset, step_offset):
                coords.append((self.x1, i))
        elif self.orientation == "hor":
            step_offset = 1 if self.delta_x == "pos" else -1
            for i in range(self.x1, self.x2 + step_offset, step_offset):
                coords.append((i, self.y1))
        elif self.orientation == "dia":
            step_offset_x = 1 if self.delta_x == "pos" else -1
            step_offset_y = 1 if self.delta_y == "pos" else -1
            for x, y in zip(range(self.x1, self.x2 + step_offset_x, step_offset_x), range(self.y1, self.y2 + step_offset_y, step_offset_y)):
                coords.append((x, y))

        return coords

    def getOrientation(self):
        return self.orientation   


lines = []
with open("input.txt", "r") as input:
    for s in input:
        coord = s.replace(" -> ", ",").split(",")
        line = vent(int(coord[0], 10), int(coord[1],10), int(coord[2], 10), int(coord[3].strip(), 10))
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