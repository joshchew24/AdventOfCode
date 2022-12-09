def read_input(mode):
    lines = [] 
    with open(f"{mode}.txt") as input:
        for line in input:
            lines.append(line.strip())
    return lines

def solve(input):
    elves = []
    elf = 0
    for line in input:
        if len(line) > 0:
            elf += int(line)
        else:
            elves.append(elf)
            elf = 0
    print(sum(sorted(elves, reverse=True)[:3]))
   
def main():
    solve(read_input(sys.argv[1]))

if __name__ == "__main__":
    main()