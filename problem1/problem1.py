with open("input.txt", "r") as input:
    lines = input.readlines()

prev = int(lines[0])
print(prev)
numMore = 0
numLess = 0
print(lines)
for i in lines:
    i = int(i)
    if i > prev:
        numMore += 1
    if i < prev:
        numLess +=1
    prev = i

print(numMore + numLess)
print(numMore)
print(numLess)