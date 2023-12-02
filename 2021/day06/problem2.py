with open("input.txt", "r") as input:
    counts = input.readline().split(",")

fishCounts = {
    "0": 0,
    "1": 0,
    "2": 0,
    "3": 0,
    "4": 0,
    "5": 0,
    "6": 0,
    "7": 0,
    "8": 0
}

for f in counts:
    fishCounts[f] += 1
    
print(fishCounts)

newCounts = fishCounts.copy()
for i in range(256):
    print(fishCounts)
    for c in fishCounts:
        if c == "0":
            newCounts["8"] = fishCounts[c]
            newCounts["6"] = fishCounts[c]
        elif c == "7":
            newCounts[str(int(c, 10) - 1)] += fishCounts[c]
        else:
            newCounts[str(int(c, 10) - 1)] = fishCounts[c]
    fishCounts = newCounts.copy()
    for c in fishCounts:
        newCounts[c] = 0
sum = 0
for c in fishCounts:
    sum += fishCounts[c]

print(sum)