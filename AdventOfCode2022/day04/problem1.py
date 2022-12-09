from collections import namedtuple

def read_input(mode):
    elves = []
    Elf = namedtuple("Elf", ["bot", "top"])
    with open(f"{mode}.txt") as input:
        for line in input:
            e1, e2 = line.split(",")
            e1_bot, e1_top = e1.split("-")
            e2_bot, e2_top = e2.split("-")
            elf1 = Elf(int(e1_bot), int(e1_top))
            elf2 = Elf(int(e2_bot), int(e2_top))
            elves.append((elf1, elf2))
    return elves

def solve(input):
    sum = 0
    for pair in input:
        e1, e2 = pair
        if (e1.bot <= e2.bot and e2.top <= e1.top) or (e2.bot <= e1.bot and e1.top <= e2.top):
            sum += 1
    print(sum)

def main():
    solve(read_input(sys.argv[1]))

if __name__ == "__main__":
    main()