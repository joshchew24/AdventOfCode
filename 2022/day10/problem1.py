import sys
import re

def read_input(mode):
    lines = []
    with open(f"{mode}.txt") as input:
        for line in input:
            lines.append(line.strip())
    return lines    

def solve(input):
    
    def inc_clock(clock, sum):
        clock += 1
        if ((clock - 20) % 40) == 0:
            sum += reg_X*clock
        return (clock, sum)

    clock = 0
    reg_X = 1
    sum = 0
    for cmd in input:
        if cmd.strip() == "noop":
            clock, sum = inc_clock(clock, sum)
            continue
        else:
            clock, sum = inc_clock(clock, sum)
            trash, V = re.split("addx ", cmd)
            clock, sum = inc_clock(clock, sum)
            reg_X += int(V)
    print(sum)

def main():
    solve(read_input(sys.argv[1]))

if __name__ == "__main__":
    main()