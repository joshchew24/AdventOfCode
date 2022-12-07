from collections import defaultdict
import sys


def main():
    with open("input.txt", "r") as input:
        poly_template = input.readline().strip()
        # print(poly_template)
        input.readline()
        pair_rules = defaultdict(str)
        for line in input:
            line = line.strip()
            pair, output = line.split(" -> ")
            pair_rules[pair] = output
    # print(pair_rules)
    for i in range(10):
        idx0 = 0
        idx1 = 1
        temp = poly_template[idx0]
        while idx1 in range(len(poly_template)):
            # breakpoint()
            char0 = poly_template[idx0]
            char1 = poly_template[idx1]
            temp += pair_rules[char0 + char1]
            temp += char1
            idx0 += 1
            idx1 += 1
        poly_template = temp
    counts = defaultdict(int)
    for c in poly_template:
        counts[c] += 1
    min = sys.maxsize
    max = 0
    for val in counts.values():
        if val < min:
            min = val
        if val > max:
            max = val
    print(max-min)
        


if __name__ == "__main__":
    main()