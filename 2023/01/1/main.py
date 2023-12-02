import re

number_match = r'\d'

sum = 0
with open("input.txt") as input:
    for line in input.readlines():
        calibration_string = line.strip()
        calibration_numbers = re.findall(number_match, calibration_string)
        number = calibration_numbers[0] + calibration_numbers[-1]
        sum += int(number)
    
print(sum)


