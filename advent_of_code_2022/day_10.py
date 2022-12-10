with open("advent_of_code_2022/data/day_10_input.txt", "r") as file:
    data = file.read().split("\n")

# Puzzle 1
V = 1
register = []

for command in data:
    register.append(V)
    if command.startswith("addx"):
        _, value = command.split()
        register.append(V)
        V += int(value)

strengths = []
for i in [20, 60, 100, 140, 180, 220]:
    strengths.append(i * register[i - 1])

result_1 = sum(strengths)
print(f"Puzzle 1: {result_1}")

# Puzzle 2
_length = 40
_height = 6

screen = [[" " for _ in range(_length)] for _ in range(_height)]
line = 0
for cursor, sprite_pos in enumerate(register):
    if cursor // _length > line:
        line += 1
    cursor %= _length
    sprite = [False for _ in range(_length)]
    for i in range(sprite_pos - 1, sprite_pos + 2):
        if 0 <= i < _length:
            sprite[i] = True
    if sprite[cursor]:
        screen[line][cursor] = "█"
print("Puzzle 2:")
print("\n".join(map(lambda line: "".join(line), screen)))

# PZGPKPEB

# ███  ████  ██  ███  █  █ ███  ████ ███
# █  █    █ █  █ █  █ █ █  █  █ █    █  █
# █  █   █  █    █  █ ██   █  █ ███  ███
# ███   █   █ ██ ███  █ █  ███  █    █  █
# █    █    █  █ █    █ █  █    █    █  █
# █    ████  ███ █    █  █ █    ████ ███
