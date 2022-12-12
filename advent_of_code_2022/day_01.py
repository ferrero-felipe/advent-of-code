with open("advent_of_code_2022/data/day_01_input.txt", "r") as file:
    data = file.read()

# Puzzle 1

result_1 = max(map(sum, map(lambda elf: map(int, elf.split("\n")), data.split("\n\n"))))

print(f"Puzzle 1: {result_1}")

# Puzzle 2

result_2 = sum(
    sorted(
        map(sum, map(lambda elf: map(int, elf.split("\n")), data.split("\n\n"))),
        reverse=True,
    )[:3]
)

print(f"Puzzle 2: {result_2}")
