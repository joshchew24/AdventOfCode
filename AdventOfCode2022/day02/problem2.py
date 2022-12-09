def read_input(mode):
    lines = [] 
    with open(f"{mode}.txt") as input:
        for line in input:
            lines.append(line.strip())
    return lines

def solve(input):
    score = 0
    for line in input:
        opp, outcome = line.split(" ")
        score += get_score(opp, outcome)
    print(score)

score_map = {
    "C_WRAP": 3,
    "A": 1,
    "B": 2,
    "C": 3,
    "A_WRAP": 1,
}
indices = {
    "A": 1,
    "B": 2,
    "C": 3,
}
def get_score(opp, outcome):
    if outcome == "X":
        score = list(score_map.values())[indices[opp] - 1]
    elif outcome == "Y":
        score = list(score_map.values())[indices[opp]] + 3
    elif outcome == "Z":
        score = list(score_map.values())[indices[opp] + 1] + 6
    return score

def main():
    solve(read_input(sys.argv[1]))

if __name__ == "__main__":
    main()