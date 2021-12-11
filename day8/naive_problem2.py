import naive_sev_seg_disp as ssd

# count the number of digits that use a unique number of segments (1, 4, 7, 8)
# seg count for: 0  1  2  3  4  5  6  7  8  9
digitSegCount = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
a = [0,-1, 2, 3,-1, 5, 6, 7, 8, 9]
b = [0,-1,-1,-1, 4, 5, 6,-1, 8, 9]
c = [0, 1, 2, 3, 4,-1,-1, 7, 8, 9]
d = [-1,-1,2, 3, 4, 5, 6,-1, 8, 9]
e = [0,-1, 2,-1,-1,-1, 6,-1, 8, -1]
f = [0, 1,-1, 3, 4, 5, 6, 7, 8, 9]
g = [0,-1, 2, 3,-1, 5, 6,-1, 8, 9]

# 5 and 6 use F but not C


def isUnique(digit):
    return len(digit) == digitSegCount[1] or len(digit) == digitSegCount[4] or len(digit) == digitSegCount[7] or len(digit) == digitSegCount[8]

def solveThree(fives):
    three = None
    for i in range(3):
        first = False
        second = False
        if fives[0][0] in fives[1] or fives[0][0] in fives[2]:
            first = True
        if fives[0][1] in fives[1] or fives[0][0] in fives[2]:
            second = True
        if first and second:
            three = fives[0]
        fives.append(fives.pop(0))
    # print(three)
    return three

        
                    
            


def solveSegments(inputArr):
    fiveSegDigs = []
    sixSegDigs = []
    # one, four, seven, eight = ""
    for dig in inputArr:
        if len(dig) == 5:
            fiveSegDigs.append(dig)
        elif len(dig) == 6:
            sixSegDigs.append(dig)
        elif len(dig) == 2:
            one = dig
        elif len(dig) == 4:
            four = dig
        elif len(dig) == 3:
            seven = dig
        elif len(dig) == 7:
            eight = dig
    
    fives = fiveSegDigs.copy()
    comm = ssd.findComm(fives)
    fives = list(map(list, fives))
    for c in comm:
        for dig in fives:
            if c in dig:
                dig.remove(c)
    # threeID = ""
    # threeID = threeID.join(solveThree(fives))
    threeID = solveThree(fives)
    print(threeID)
    three = ""
    for elem in fiveSegDigs:
        # print(elem)
        flag = True
        for char in threeID:
            if char not in elem:
                flag = False
                # print(elem)
                # three = elem
        if flag:
            three = elem
    return three

lines = []
with open("normal.txt", "r") as input:
    for line in input:
        display = line.split(" | ")
        display[1] = display[1].strip("\n")
        display[0] = display[0].split(" ")
        display[1] = display[1].split(" ")
        lines.append(display)
    
# print(lines)
count = 0
for display in lines:
    print(solveSegments(display[0]))
