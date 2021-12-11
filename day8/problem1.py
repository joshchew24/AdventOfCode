# count the number of digits that use a unique number of segments (1, 4, 7, 8)
# seg count for: 0  1  2  3  4  5  6  7  8  9
digitSegCount = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

lines = []
with open("input.txt", "r") as input:
    for line in input:
        display = line.split(" | ")
        display[1] = display[1].strip("\n")
        display[0] = display[0].split(" ")
        display[1] = display[1].split(" ")
        # display = tuple(display)                            # maybe don't bother converting to tuple?
        lines.append(display)
    
# print(lines)
count = 0
for display in lines:
    print(display)
    for output in display[1]:
        if len(output) == digitSegCount[1] or len(output) == digitSegCount[4] or len(output) == digitSegCount[7] or len(output) == digitSegCount[8]:
            # print(output)
            count += 1
print(count)