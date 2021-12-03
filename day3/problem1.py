lines = []
with open("input.txt", "r") as input:
    for line in input:
        lines.append(bin(int(line, 2)))

# print(lines)

for i in lines:

    print(i)
    i >> 1
    print(i)