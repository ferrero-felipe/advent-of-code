import string
from functools import reduce

with open("advent_of_code_2022/data/day_3_input.txt", "r") as file:
    data = file.read()
data = data.split("\n")

# Puzzle 1

values = {
    letter: i
    for i, letter in enumerate(string.ascii_lowercase + string.ascii_uppercase, 1)
}

result_1 = sum(
    map(
        lambda letter: values[letter],
        map(
            lambda rucksack: set(rucksack[: len(rucksack) // 2])
            .intersection(rucksack[len(rucksack) // 2 :])
            .pop(),
            data,
        ),
    )
)

print(f"Puzzle 1: {result_1}")

# Puzzle 2

result_2 = sum(
    map(
        lambda letter: values[letter],
        map(
            lambda set_3: set_3.pop(),
            map(
                lambda group: reduce(lambda a, b: set(a).intersection(set(b)), group),
                [data[i : i + 3] for i in range(0, len(data), 3)],
            ),
        ),
    )
)

print(f"Puzzle 2: {result_2}")
