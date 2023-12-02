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
    
    # initial pair_count set up from poly template
    pair_counts = defaultdict(int)
    idx0 = 0
    idx1 = 1
    while idx1 in range(len(poly_template)):
            char0 = poly_template[idx0]
            char1 = poly_template[idx1]
            pair_counts[char0 + char1] += 1
            idx0 += 1
            idx1 += 1

    letter_counts = defaultdict(int)
    num_iterations = 40
    for i in range(num_iterations):
        # breakpoint()
        pair_counts_temp = defaultdict(int)
        for pair, count in pair_counts.items():
            char0 = pair[0]
            char1 = pair[1]
            insert = pair_rules[pair]
            pair_counts_temp[char0 + insert] += count
            pair_counts_temp[insert + char1] += count
        pair_counts = pair_counts_temp.copy()

    # only count char0 to avoid double counting letters. after the outer loop, add 1 to the final character in original poly_temp to account for only counting the first char in each pair
    for pair, count in pair_counts.items():
        # breakpoint()
        char0 = pair[0]
        char1 = pair[1]
        letter_counts[char0] += count
    letter_counts[poly_template[-1]] += 1
    
    min = sys.maxsize
    max = 0
    for val in letter_counts.values():
        if val < min:
            min = val
        if val > max:
            max = val
    print(max-min)

if __name__ == "__main__":
    main()