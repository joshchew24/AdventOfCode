with open("input.txt", "r") as input:
    lines = input.readlines()

prev = int(lines[0])
numMore = 0
numLess = 0

for i in lines:
    i = int(i)
    if i > prev:
        numMore += 1
    if i < prev:
        numLess +=1
    prev = i

print(numMore)
print(numLess)