lines = []
with open("input.txt", "r") as input:
    for line in input:
        lines.append(line.strip("\n"))

gamma = ""

oxygen = lines.copy()
carbon = lines.copy()
for i in range(len(lines[0])):
    oxygen0 = 0
    oxygen1 = 0
    carbon0 = 0
    carbon1 = 0
    topFreq = ""
    botFreq = ""
    # print(oxygen)
    # print(carbon)
    for n in lines:
        if n[i] == "0":
            if n in oxygen:
                oxygen0 += 1
            if n in carbon:
                carbon0 += 1
        elif n[i] == "1":
            if n in oxygen:
                oxygen1 += 1
            if n in carbon:
                carbon1 += 1
    if oxygen0 > oxygen1:
        topFreq = "0"
    else:
        topFreq = "1"
    if carbon0 > carbon1:
        botFreq = "1"
    else:
        botFreq = "0"
    # print("i:", i, "topFreq: ", topFreq)
    for n in lines:
        # print(lines)
        # print("curr: ", n[i], "", n)
        if (n in oxygen) and (n[i] != topFreq) and (len(oxygen) > 1):
            oxygen.remove(n)
        if (n in carbon) and (n[i] != botFreq) and (len(carbon) > 1):
            carbon.remove(n)
        # if n[i] == topFreq:
        #     print("123")
        #     carbon.remove(n)

# print(oxygen)
# print(carbon)
# oxygenint = int(oxygen[0], 2)
# print(oxygenint)
lifeSupport = int(oxygen[0], 2) * int(carbon[0], 2)
print(lifeSupport)