from collections import deque

lefts = ("(", "[", "{", "<")
rights = (")", "]", "}", ">")
values = {
    ")" : 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

# returns corruption value of chunk
def checkChunkCorrupted(chunk):
    stack = deque()
    for c in chunk:
        # breakpoint()
        if c in lefts:
            stack.append(c)
        elif c in rights:
            curr = stack.pop()
            if rights.index(c) != lefts.index(curr):
                return values[c]
    return 0


with open("input.txt", "r") as input:
    lines = input.readlines()

sum = 0
for chunk in lines:
    sum += checkChunkCorrupted(chunk)

print(sum)