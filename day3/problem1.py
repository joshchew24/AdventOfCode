lines = []
with open("input.txt", "r") as input:
    for line in input:
        lines.append(line.strip("\n"))

gamma = ""
for i in range(len(lines[0])):
    count0 = 0
    count1 = 0
    for n in lines:
        if n[i] == "0":
            count0 += 1
        elif n[i] == "1":
            count1 += 1
    if count0 > count1:
        gamma += "0"
    else:
        gamma += "1"

gamma = int(gamma, 2)
epsilon = gamma ^ 0b111111111111
print(gamma*epsilon)