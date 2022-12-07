from string import ascii_lowercase, ascii_uppercase

items = {}
for lowercase in list(ascii_lowercase):
    items.update({lowercase: ord(lowercase) - 96})
for uppercase in list(ascii_uppercase):
    items.update({uppercase: ord(uppercase) - 64 + 26})

def read_input(mode):
    lines = [] 
    with open(f"{mode}.txt") as input:
        for line in input:
            lines.append(line.strip())
    return lines

def solve(input):
    sum = 0
    for rucksack in input:
        seen = {}
        comp_1 = rucksack[:len(rucksack)//2]
        comp_2 = rucksack[len(rucksack)//2:]
        for item in comp_1:
            seen.update({item: None})
        for item in comp_2:
            try:
                seen[item]
                sum += items[item]
                break
            except KeyError as e:
                pass
    print(sum)

def get_score(comp):
    sum = 0
    for item in comp:
        sum += items[item]
    return sum


def main():
    read_input()
    solve()

if __name__ == "__main__":
    main()