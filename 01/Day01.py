import fileinput

PUZZLE = [int(line.strip()) for line in fileinput.input()]

def sonar_sweep(data):
    count = 0
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            count+=1
    return count

def sonar_sweep_part_two(data):
    count = 0
    for i in range(0, len(data) - 3, 1):
        first_window = data[i] + data[i+1] + data[i+2]
        second_window = data[i+1] + data[i+2] + data[i+3]
        if second_window > first_window:
            count += 1
    return count

print(f"Solution to part 1 is: {sonar_sweep(PUZZLE)}")
print(f"Solution to part 2 is: {sonar_sweep_part_two(PUZZLE)}")
