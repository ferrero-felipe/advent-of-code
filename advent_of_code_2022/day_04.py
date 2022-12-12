with open("advent_of_code_2022/data/day_04_input.txt", "r") as file:
    data = file.read()

data = list(
    map(
        lambda pair: [
            [int(digit) for digit in elf.split("-")] for elf in pair.split(",")
        ],
        data.split("\n"),
    )
)

# Puzzle 1

sections = [[set(range(*(elf[0], elf[-1] + 1))) for elf in pair] for pair in data]

result_1 = sum(
    [
        1 if (pair[0].issubset(pair[1]) or pair[1].issubset(pair[0])) else 0
        for pair in sections
    ]
)

print(f"Puzzle 1: {result_1}")

# Puzzle 2

result_2 = sum([1 if len(pair[0].intersection(pair[1])) else 0 for pair in sections])

print(f"Puzzle 2: {result_2}")
