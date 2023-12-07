from math import sqrt, floor, ceil

input_times = [[7, 15, 30], [46, 68, 98, 66], [71530], [46689866]]
input_distances = [[9, 40, 200], [358, 1054, 1807, 1080], [940200], [358105418071080]]
input_map = {
    "small": 0,
    "input": 1,
    "small2": 2,
    "input2": 3,
}

INPUT_TYPE = "input2"

times = input_times[input_map[INPUT_TYPE]]
distances = input_distances[input_map[INPUT_TYPE]]
product = 1

for time, distance in zip(times, distances):
    left_zero = (time - sqrt(pow(time, 2) - 4 * distance))/2
    right_zero = (time + sqrt(pow(time, 2) - 4 * distance))/2
    shortest = int(left_zero + 1) if ceil(left_zero) == left_zero else ceil(left_zero)
    longest = int(ceil(right_zero))
    product *= longest - shortest

print(product)