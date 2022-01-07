import sys
import functools
def find_mode(counts):
    mode = 0                                # mode
    mode_n = 0                              # number of occurrences
    for posn, count in counts.items():
        if count > mode_n:
            mode = int(posn, 10)
            mode_n = count
    return mode
def find_mean(counts):
    sum = 0                                # sum
    n = 0                                  # number of occurrences
    for posn, count in counts.items():
        sum += int(posn,10)*count
        n += count
    return sum/n
def find_median(counts):
    max, min = find_max_min(counts)
    return (max-min)/2
def find_max_min(counts):
    max = 0                                # sum
    min = sys.maxsize                      # number of occurrences
    for posn in counts.keys():
        if int(posn, 10) > max:
            max = int(posn, 10)
        if int(posn, 10) < min:
            min = int(posn, 10)
    return max, min

def brute_force(counts):
    max, min = find_max_min(counts)
    minFuel = sys.maxsize
    for i in range(min, max):
        sum = getSumDiff(counts, i)
        if sum < minFuel:
            minFuel = sum
            sum = 0
    return minFuel

def getSumDiff(counts, n):
    sum = 0
    for i in counts:
        sum += abs(int(i,10) - n)*counts[i]
    return sum

def binary_search(counts, lo, hi):
    if (hi - lo) != 0:
        mid = (hi + lo)/2
        lef_mid = getSumDiff(counts, (lo + mid)/2)
        rig_mid = getSumDiff(counts, (mid + hi)/2)
        if lef_mid < rig_mid:
            lef = lo
            rig = mid
        else:
            lef = mid
            rig = hi
        return binary_search(counts, lef, rig)
    else:
        return getSumDiff(counts, hi)

with open("input.txt", "r") as input:
    crabs = input.readline().split(",")

counts = {}
for c in crabs:
    counts[c] =  1 + counts.setdefault(c, 0)

print(brute_force(counts))
min, max = find_max_min(counts)
print(binary_search(counts, min, max))

