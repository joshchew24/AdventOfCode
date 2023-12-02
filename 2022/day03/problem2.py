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
    input_iter = iter(input)
    for elf in input_iter:
        e1 = elf
        e2 = next(input_iter, None)
        e3 = next(input_iter, None)
        seen_in_one = {}
        union_1_2 = {}
        for item in e1:
            seen_in_one.update({item: None})
        for item in e2:
            try:
                seen_in_one[item]
                union_1_2.update({item: None})
            except KeyError as e:
                pass
        for item in e3:
            try:
                union_1_2[item]
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
    solve(read_input(sys.argv[1]))

if __name__ == "__main__":
    main()