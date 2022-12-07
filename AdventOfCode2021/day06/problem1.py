class lanternfish:
    def __init__(self, time):
        self.timer = int(time, 10)
    
    def increaseAge(self):
        if self.timer == 0:
            self.timer = 6
            return lanternfish("8")
        else:
            self.timer -= 1
            return 
    def print(self):
        print(self.timer, end = "")


with open("input.txt", "r") as input:
    counts = input.readline().split(",")

fish = []
for f in counts:
    fish.append(lanternfish(f))

for day in range(256):
    # for f in fish:
    #     f.print()
    # print()
    newCount = 0
    for f in fish:
        new = f.increaseAge()
        if new:
            newCount += 1
    for i in range(newCount):
        fish.append(lanternfish("8"))

print(len(fish))


