import fileinput

PUZZLE = [line.strip() for line in fileinput.input()]

DIRECTION = {
    "forward": lambda x, y, steps: (x + steps, y),
    "down": lambda x, y, steps: (x, y - steps),
    "up": lambda x, y, steps: (x, y + steps)
}

DIRECTION_UPDATED = {
    "forward": lambda x, y, aim, steps: (x + steps, y + (steps*aim), aim),
    "down": lambda x, y, aim, steps: (x, y, aim + steps),
    "up": lambda x, y, aim, steps: (x, y, aim - steps)
}


def dive(data):
    X, Y = 0, 0
    for line in data:
        command, value = parse_instruction(line)
        X, Y = DIRECTION[command](X, Y, value)
    return abs(X * Y)

def dive_part_2(data):
    X, Y, AIM = 0, 0, 0
    for line in data:
        command, value = parse_instruction(line)
        X, Y, AIM = DIRECTION_UPDATED[command](X, Y, AIM, value)
    return X * Y


def parse_instruction(line):
    command, value = line.split()
    return command, int(value)

print(f"Solution to part 1 is: {dive(PUZZLE)}")
print(f"Solution to part 2 is: {dive_part_2(PUZZLE)}")