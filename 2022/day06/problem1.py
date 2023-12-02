import sys

def read_input(mode):
    lines = []
    with open(f"{mode}.txt") as input:
        for line in input:
            lines.append(line)
    return lines

def solve(input):
    for line in input:
        prev_3 = []
        index = 0
        for c in line:
            index += 1
            if len(prev_3) > 3:
                prev_3.pop(0)
            while c in prev_3:              # pop until list has no dupes of c
                while prev_3[0] != c:
                    prev_3.pop(0)
                else:                       # also pop the most recent dupe
                    prev_3.pop(0)
            if len(prev_3) == 3:
                print(index)
                break
            prev_3.append(c)

def main():
    solve(read_input(sys.argv[1]))

if __name__ == "__main__":
    main()