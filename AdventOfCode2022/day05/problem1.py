import re

solve_stacks = [
    list("DTRBJLWG"),
    list("SWC"),
    list("RZTM"),
    list("DTCHSPV"),
    list("GPTLDZ"),
    list("FBRZJQCD"),
    list("SBDJMFTR"),
    list("LHRBTVM"),
    list("QPDSV"),
]
test_stacks = [
    list("ZN"),
    list("MCD"),
    list("P"),
]

def read_input(mode):
    lines = []
    with open(f"{mode}.txt") as input:
        for line in input:
            lines.append(line)
    return lines

def solve(input):
    mode = input.pop(0).strip()
    if mode == "test":
        stacks = test_stacks
    elif mode == "solve":
        stacks = solve_stacks
    else: 
        print(mode)
        return

    for instruction in input:
        trash, qty = re.search("move\s\d*", instruction).group().split(" ")
        trash, src = re.search("from\s\d*", instruction).group().split(" ")
        trash, dst = re.search("to\s\d*", instruction).group().split(" ")

        qty = int(qty)
        src = int(src) - 1
        dst = int(dst) - 1

        while qty > 0:
            stacks[dst].append(stacks[src].pop())
            qty -= 1
    
    tops = ""
    for stack in stacks:
        tops += stack.pop()
    print(tops)

def main():
    read_input()
    solve()

if __name__ == "__main__":
    main()