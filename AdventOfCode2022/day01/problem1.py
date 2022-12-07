def read_input(mode):
    lines = [] 
    with open(f"{mode}.txt") as input:
        for line in input:
            lines.append(line.strip())
    print(lines)


def solve():
    pass


def main():
    read_input()
    solve()


if __name__ == "__main__":
    main()