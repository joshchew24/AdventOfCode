import sev_seg_disp as ssd

class Entry:
    def __init__(self, raw) -> None:
        self.input = raw[0]
        self.output = raw[1]    

    def __str__(self):
        return "Inputs: " + str(self.input) + " | " + "Outputs: " + str(self.output)

lines = []
with open("input.txt", "r") as input:
    for line in input:
        display = line.split(" | ")
        display[1] = display[1].strip("\n")
        display[0] = display[0].split(" ")
        display[1] = display[1].split(" ")
        lines.append(Entry(display))


sum = 0
for line in lines:
    # dictionary of input segment and the decoded segment it should map to
    translate = {}

    freqs = ssd.findFrequencies(line.input)

    segWithCountSeven = []
    segWithCountEight = []

    for seg, count in freqs.items():
        if count == 4:
            translate[seg] = "e"
        if count == 6:
            translate[seg] = "b"
        if count == 7:
            segWithCountSeven.append(seg)
        if count == 8:
            segWithCountEight.append(seg)
        if count == 9:
            translate[seg] = "f"
    four = None
    one = None
    for entry in line.input:
        if len(entry) == 4:
            four = entry
        if len(entry) == 2:
            one = entry
    if segWithCountSeven[0] in four:
        translate[segWithCountSeven[0]] = "d"
        translate[segWithCountSeven[1]] = "g"
    else: 
        translate[segWithCountSeven[0]] = "g"
        translate[segWithCountSeven[1]] = "d"
    
    if segWithCountEight[0] in one:
        translate[segWithCountEight[0]] = "c"
        translate[segWithCountEight[1]] = "a"
    else: 
        translate[segWithCountEight[0]] = "a"
        translate[segWithCountEight[1]] = "c"
    
    outputNumber = 0
    for digit in line.output:
        solvedOutput = ""
        for char in digit:
            solvedOutput += translate[char]
        outputNumber *= 10
        outputNumber += ssd.getNumValue(solvedOutput)
    sum += outputNumber

print(sum)