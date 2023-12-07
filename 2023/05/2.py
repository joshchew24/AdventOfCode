import argparse
import os
import sys

PUZZLE_INPUT = "input.txt"
EXAMPLE_INPUT = "small.txt"
MAX_INT = sys.maxsize

def main():
    in_file = PUZZLE_INPUT
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--test', action='store_true')
    if (parser.parse_args().test):
        in_file = EXAMPLE_INPUT
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, in_file)

    maps = []
    with open(file_path) as input:
        i = 0
        curr_map = num_range_map()
        for line in input.readlines():
            tokens = line.strip().split(" ")
            if len(tokens) == 1: continue
            if tokens[0] == "seeds:":
                seed_generator = get_seed_generator([int(x) for x in tokens[1:]])
            elif tokens[1] == "map:": # save the previous map and reset current map
                if curr_map.not_empty():
                    maps.append(curr_map)
                    curr_map = num_range_map()
            else: # this is a range line
                curr_map.add_range(num_range(*[int(x) for x in tokens]))
        # save the final map
        if curr_map.not_empty():
            maps.append(curr_map)
    
    print("maps are created")
    # print(f"seed generator: {seed_generator}")
    lowest_location = MAX_INT
    for seed in seed_generator:
        curr_val = seed
        for map in maps:
            curr_val = map.convert(curr_val)
        lowest_location = min(lowest_location, curr_val)
    print(lowest_location)
        
def get_seed_generator(seed_ranges: list[int]):
    seeds = []
    for (start, rng) in zip(seed_ranges[::2], seed_ranges[1::2]):
        for seed in range(start, start+rng):
            yield seed

class num_range:
    def __init__(self, dst, src, rng):
        self.dst = dst
        self.src = src
        self.rng = rng

    def __repr__(self):
        return f"<{self.dst} {self.src} {self.rng}>"
        # return f"dst range start: {self.dst}, src range start: {self.src}, range length: {self.rng}"

    def convert(self, num):
        if num in range(self.src, self.src + self.rng):
            return self.dst + (num - self.src)
        return -1

class num_range_map:
    def __init__(self):
        self.ranges = []
    def add_range(self, range):
        self.ranges.append(range)

    def convert(self, num):
        for range in self.ranges:
            if (result := range.convert(num)) > -1:
                return result
        return num
    
    def not_empty(self):
        return len(self.ranges) > 0

    def __repr__(self):
        return repr(self.ranges)

if __name__ == "__main__":
    main()