from collections import deque

lefts = ("(", "[", "{", "<")
rights = (")", "]", "}", ">")
corruption_values = {
    ")" : 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}
completion_values = {
    ")" : 1,
    "]": 2,
    "}": 3,
    ">": 4
}

class chunk:

    def __init__(self, chunk):
        self.chunk = chunk
        self.stack = deque()
        self.completionString = ""

    # return corruption value of chunk
    def getCorruptionValue(self):
        for c in self.chunk:
            if c in lefts:
                self.stack.append(c)
            elif c in rights:
                curr = self.stack.pop()
                if rights.index(c) != lefts.index(curr):
                    return corruption_values[c]
        return 0
    
    # get completion string of chunk
    def getCompletionString(self):
        completionString = ""
        while self.stack:
            rem = self.stack.pop()
            completionString += rights[lefts.index(rem)]

        self.completionString = completionString
        return completionString

    def getCompletionScore(self):
        result = 0
        for c in self.completionString:
            result *= 5
            result += completion_values[c]
        return result


with open("input.txt", "r") as input:
    lines = input.readlines()

sum = 0
incompletes = lines.copy()
scores = []
for line in lines:
    currChunk = chunk(line)

    if currChunk.getCorruptionValue() > 0:
        incompletes.remove(line)
    else:
        print(line.strip() + currChunk.getCompletionString())
        scores.append(currChunk.getCompletionScore())

scores.sort()
print(scores[len(scores)//2])