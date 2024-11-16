import fileinput
from collections import Counter

PUZZLE = [line.strip() for line in fileinput.input()]

PART_1 = Counter()
PART_2 = Counter()

def hydrothermal_venture(data):
    global PART_1
    global PART_2
    for line in data:
        left, right = line.split(" -> ")
        x1, y1 = map(int, left.split(","))
        x2, y2 = map(int, right.split(","))

        #Horizontal or vertical lines
        if x1 == x2 or y1 == y2:
            x1, x2 = sorted((x1, x2))
            y1, y2 = sorted((y1, y2))
            for x in range(int(x1), int(x2) + 1):
                for y in range(int(y1), int(y2) + 1):
                    PART_1[x, y] += 1
                    PART_2[x, y] += 1
        
        #Diagonal lines
        else:
            delta = abs(x1 - x2)
            for _ in range(delta + 1):
                PART_2[x1, y1] += 1
                if x1 < x2:
                    x1 += 1
                else: 
                    x1 -= 1
                if y1 < y2:
                    y1 += 1
                else: 
                    y1 -= 1
        
    

hydrothermal_venture(PUZZLE)
print(f"Solution to part 1 is: {sum(1 for v in PART_1.values() if v > 1)}")
print(f"Solutiont to part 2 is: {sum(1 for v in PART_2.values() if v > 1)}")

