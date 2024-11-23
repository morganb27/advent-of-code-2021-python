import fileinput
import math

PUZZLE = fileinput.input().readline().strip()

CRABS = [int(crab) for crab in PUZZLE.split(",")]
RANGE = max(CRABS) * 2
PART_1, PART_2 = float("inf"), float("inf")

def treacher_whales(data):
    global PART_1, PART_2
    for position in range(RANGE):
        part_1_fuel = 0
        part_2_fuel = 0
        for crab in data:
            move = abs(crab - position)
            part_1_fuel += move
            part_2_fuel += int((move * (move + 1)) / 2)
        PART_1 = min(part_1_fuel, PART_1)
        PART_2 = min(part_2_fuel, PART_2)
    return PART_1

treacher_whales(CRABS)
print(f"Solution to part 1 is:{PART_1}")
print(f"Solution to part 2 is:{PART_2}")


