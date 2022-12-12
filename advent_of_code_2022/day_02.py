with open("advent_of_code_2022/data/day_02_input.txt", "r") as file:
    data_raw = file.read()

data = list(map(lambda match: match.split(), data_raw.split("\n")))

# Puzzle 1

conv = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors",
    "X": "Rock",
    "Y": "Paper",
    "Z": "Scissors",
}

points = {"Rock": 1, "Paper": 2, "Scissors": 3}
wins = {"Rock": "Scissors", "Paper": "Rock", "Scissors": "Paper"}


def play(elf, you):
    result = 0
    if elf == you:
        result = 3
    elif wins[you] == elf:
        result = 6
    return result + points[you]


result_1 = sum(
    map(
        lambda match: play(*match),
        map(lambda match: map(lambda player: conv[player], match), data),
    )
)

print(f"Puzzle 1: {result_1}")

# Puzzle 2

outcome = {"X": "lose", "Y": "draw", "Z": "win"}


def choose(elf, outcome):
    if outcome == "draw":
        return elf
    elif outcome == "lose":
        return wins[elf]
    else:
        return {v: k for k, v in wins.items()}[elf]


result_2 = sum(
    map(
        lambda match: play(match[0], choose(*match)),
        map(lambda match: (conv[match[0]], outcome[match[1]]), data),
    )
)

print(f"Puzzle 2: {result_2}")
