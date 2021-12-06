with open("test.txt", "r") as input:
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
    fishCounts[f] = fishCounts[f] + 1
    
print(fishCounts)

newCounts = fishCounts.copy()
for i in range(18):
    print(fishCounts)
    for c in fishCounts:
        if c == 0:
            newCounts[8] = fishCounts[c]
        else:
            newCounts[str(int(c, 10) - 1)] = fishCounts[c]
    fishCounts = newCounts.copy()
    for c in fishCounts:
        fishCounts[c] = newCounts[c]
        newCounts[c] = 0
sum = 0
for c in fishCounts:
    sum += fishCounts[c]

print(sum)
# fish = []
# for f in counts:
#     fish.append(int(f, 10))
# del counts

# for day in range(256):
#     newCount = 0
#     for i in range(len(fish)):
#         if fish[i] == 0:
#             fish[i] = 6
#             newCount += 1
#         else:
#             fish[i] -= 1
#     for i in range(newCount):
#         fish.append(8)

# print(len(fish))


