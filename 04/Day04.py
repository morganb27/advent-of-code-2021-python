import fileinput
from itertools import chain
from collections import Counter

PUZZLE = [line.strip() for line in fileinput.input()]

NUMBERS = [number for number in PUZZLE[0].split(",")]
BOARDS = [[list(map(int, row.split())) for row in board.splitlines()] for board in "\n".join(PUZZLE[1:]).split("\n\n")]


WINNING_BOARDS = set()

def giant_squid(numbers, boards, isPartTwo = False):
    TRACK = [[] for _ in range(len(BOARDS))]
    global WINNING_BOARDS
    for num in numbers:
        for x, board in enumerate(boards):
            for row in range(len(board)):
                for col in range(len(board[0])):
                    if int(num) == board[row][col]:
                        TRACK[x].append((row, col))
                        if is_winning_board(TRACK[x]):
                            WINNING_BOARDS.add(x)
                            if not isPartTwo:
                                return int(num) * calculate_unmarked_numbers(TRACK, board, x)
                            else:
                                if len(WINNING_BOARDS) == len(BOARDS):
                                    return int(num) * calculate_unmarked_numbers(TRACK, board, x)
                                

def is_winning_board(board):
    X = Counter([x for x, _ in board])
    Y = Counter([y for _, y in board])
    if any(value == 5 for value in chain(X.values(), Y.values())):
        return True
    return False

def calculate_unmarked_numbers(track, board, position):
    sum = 0
    for row in range(len(board)):
        for col in range(len(board[0])):
            if (row, col) not in track[position]:
                sum += board[row][col]
    return sum


print(f"Solution to part 1 is: {giant_squid(NUMBERS, BOARDS)}")
print(f"Solution to part 2 is: {giant_squid(NUMBERS, BOARDS, True)}")
