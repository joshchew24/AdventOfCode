import sys
import re

def read_input(mode):
    lines = []
    with open(f"{mode}.txt") as input:
        for line in input:
            lines.append(line.strip())
    return lines    

def inc_clock(clock, reg_X):
    render_pixel(clock, reg_X)
    clock += 1
    return (clock)

def render_pixel(clock, reg_X):
    x_posn = clock%40
    if reg_X in range(x_posn-1, x_posn+2):
        render_pixel.screen += "#"
    else:
        render_pixel.screen += "."
    if x_posn == 39: render_pixel.screen += "\n"

render_pixel.screen = ""

def solve(input):
    clock = 0
    reg_X = 1
    for cmd in input:
        if cmd.strip() == "noop":
            clock = inc_clock(clock, reg_X)
            continue
        else:
            clock = inc_clock(clock, reg_X)
            trash, V = re.split("addx ", cmd)
            clock = inc_clock(clock, reg_X)
            reg_X += int(V)
    print(render_pixel.screen)

def main():
    solve(read_input(sys.argv[1]))

if __name__ == "__main__":
    main()