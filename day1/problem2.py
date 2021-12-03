lines = []
with open("input.txt", "r") as input:
    for line in input:
        lines.append(int(line))

A = lines.pop(0)
B = lines.pop(0)
C = lines.pop(0)
numMore = 0
numLess = 0

for i in lines:
    prev = A + B + C
    curr = B + C + i
    if curr > prev:
        numMore += 1
    if curr < prev:
        numLess +=1
    A = B
    B = C
    C = i

print(numMore + numLess)
print(numMore)
print(numLess)