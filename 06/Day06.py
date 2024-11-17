import fileinput
from collections import Counter

PUZZLE = fileinput.input().readline().strip()
RESULT = None
RANGE = 256
STATE = Counter()

def lanternfish(data):
    global RESULT, STATE
    FISH = list(map(int, data.split(",")))
    
    for f in FISH:
        STATE[f] += 1
    
    for _ in range(RANGE):
        next_state = Counter()
        for age, count in STATE.items():
            if age == 0:
                next_state[6] += count
                next_state[8] += count
            elif count > 0:
                next_state[age - 1] += count
        STATE = next_state
    RESULT = sum(STATE.values())
    


lanternfish(PUZZLE)
print(f"Solution is: {RESULT}")
        