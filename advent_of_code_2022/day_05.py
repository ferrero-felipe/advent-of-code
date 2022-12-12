from copy import deepcopy

with open("advent_of_code_2022/data/day_05_input.txt", "r") as file:
    data = file.read()
stacks, moves = data.split("\n\n")

stacks = stacks.split("\n")
stacks, columns = stacks[:-1], stacks[-1]

stacks = [
    [row[columns.index(col)] for row in stacks if row[columns.index(col)] != " "]
    for col in columns.strip().split()
    if col
]

moves = [
    [int(num) for num in command.split() if num.isnumeric()]
    for command in moves.split("\n")
]

# Puzzle 1

stacks_move = deepcopy(stacks)
for qtty, src, dest in moves:
    for _ in range(qtty):
        stacks_move[dest - 1] = [stacks_move[src - 1].pop(0)] + stacks_move[dest - 1]

result_1 = "".join([col[0] for col in stacks_move])

print(f"Puzzle 1: {result_1}")

# Puzzle 2

stacks_move = deepcopy(stacks)
for qtty, src, dest in moves:
    stacks_move[dest - 1] = stacks_move[src - 1][:qtty] + stacks_move[dest - 1]
    stacks_move[src - 1] = stacks_move[src - 1][qtty:]

result_2 = "".join([col[0] for col in stacks_move])

print(f"Puzzle 2: {result_2}")
