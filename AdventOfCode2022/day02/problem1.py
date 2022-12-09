def read_input(mode):
    lines = [] 
    with open(f"{mode}.txt") as input:
        for line in input:
            lines.append(line.strip())
    return lines

def solve(input):
    score = 0
    for line in input:
        opp, you = line.split(" ")
        score += get_score(opp, you)
    print(score)

score_grid = [
    [4, 1, 7],              # rock ties rock, rock loses paper, rock wins scissor
    [8, 5, 2],              # paper beats rock, paper ties paper, paper loses scissor
    [3, 9, 6],              # scissor loses rock, scissor wins paper, scissor ties scissor
]
choice_map = {
    "A": 0,
    "B": 1,
    "C": 2,
    "X": 0,
    "Y": 1,
    "Z": 2,
}
def get_score(opp, you):
    return score_grid[choice_map[you]][choice_map[opp]]

def main():
    solve(read_input(sys.argv[1]))

if __name__ == "__main__":
    main()_ == "__main__":
    main()