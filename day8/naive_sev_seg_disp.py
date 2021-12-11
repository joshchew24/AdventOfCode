# seg count for: 0  1  2  3  4  5  6  7  8  9
digitSegCount = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
segLetters = ["a", "b", "c", "d", "e", "f", "g"]
digLetters = ["abcefg", "cf", "acdeg", "acdfg", "bcdf", "abdfg", "abdefg", "acf", "abcdefg", "abcdfg"]
fives = [2, 3, 5]
sixes = [0, 6, 9]
test = ["acdeg", "acdfg", "abdfg"]

# a = [0,    2, 3,    5, 6, 7, 8, 9]
# b = [0,          4, 5, 6,    8, 9]
# c = [0, 1, 2, 3, 4,       7, 8, 9]
# d = [      2, 3, 4, 5, 6,    8, 9]
# e = [0,    2,          6,    8]
# f = [0, 1,    3, 4, 5, 6, 7, 8, 9]
# g = [0,    2, 3,    5, 6,    8, 9]

a = [0,-1, 2, 3,-1, 5, 6, 7, 8, 9]
b = [0,-1,-1,-1, 4, 5, 6,-1, 8, 9]
c = [0, 1, 2, 3, 4,-1,-1, 7, 8, 9]
d = [-1,-1,2, 3, 4, 5, 6,-1, 8, 9]
e = [0,-1, 2,-1,-1,-1, 6,-1, 8, -1]
f = [0, 1,-1, 3, 4, 5, 6, 7, 8, 9]
g = [0,-1, 2, 3,-1, 5, 6,-1, 8, 9]
#              a, b, c, d, e, f, g
frequencies = [8, 6, 8, 7, 4, 9, 7]

segments = [a, b, c, d, e, f, g]

def findCommFive():
    commFive = []
    for seg in segments:
        comm = True
        for i in fives:
            # print(seg[i])
            if seg[i] == -1:
                # print(segLetters[segments.index(seg)])
                comm = False
        # print(segLetters[segments.index(seg)], comm)
        if comm:
            commFive.append(segLetters[segments.index(seg)])

# accepts list of segments in string format
def findComm(digits):
    if len(digits) == 0: return ""
    if len(digits) == 1: return list(digits[0])
    comm = set(digits[0])
    digits = map(set, digits)
    comm = comm.intersection(*digits)
    return comm

# print(findComm(test))
