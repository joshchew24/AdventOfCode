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

def findFrequencies(input):
    freq = {
        "a" : 0,
        "b" : 0,
        "c" : 0,
        "d" : 0,
        "e" : 0,
        "f" : 0,
        "g" : 0
    }
    for dig in input:
        for char in dig:
            freq[char] += 1
    return freq

def getNumValue(input):
    output = ""
    return digLetters.index(output.join(sorted(input)))