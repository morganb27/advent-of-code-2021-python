import fileinput
from collections import Counter

PUZZLE = [line.strip() for line in fileinput.input()]

def binary_diagnostic(data):
    gamma, epsilon = "", ""
    for col in range(len(data[0])):
        binary_column = ""
        for row in range(len(data)):
            binary_column += data[row][col]
        counter = Counter(binary_column)
        most_common_bit, _ = counter.most_common(1)[0]
        least_common_bit, _ = counter.most_common()[-1]
        gamma += most_common_bit
        epsilon += least_common_bit
    return int(gamma, 2) * int(epsilon, 2)


def binary_diagnostic_part_two(data):
    oxygen, co2 = [line.strip() for line in data], [line.strip() for line in data]
    return int(calculate_oxygen_and_co2(oxygen, True), 2) * int(calculate_oxygen_and_co2(co2), 2)
    
        

def calculate_oxygen_and_co2(data, oxygen=False):
    for col in range(len(data[0])):
        binary_column = ""
        for row in range(len(data)):
            binary_column += data[row][col]
        counter = Counter(binary_column)
        most_common_bit = "1" if counter.most_common()[0][1] == counter.most_common()[-1][1] else counter.most_common(1)[0][0]
        least_common_bit = "0" if counter.most_common()[0][1] == counter.most_common()[-1][1] else counter.most_common()[-1][0]
        if oxygen:
            data = [x for x in data if x[col] == most_common_bit]
        else:
            data = [x for x in data if x[col] == least_common_bit]

        if len(data) == 1:
            return data[0]
    return data[0]


print(f"Solution to part 1 is: {binary_diagnostic(PUZZLE)}")
print(f"Solution to part 2 is: {binary_diagnostic_part_two(PUZZLE)}")