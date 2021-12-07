class line:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2      

coords = []
with open("test.txt", "r") as input:
    for s in input:
        coord = s.replace(" -> ", ",").split(",")
        coords.append()
