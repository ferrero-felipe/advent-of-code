with open("advent_of_code_2022/data/day_6_input.txt", "r") as file:
    data = file.read()


def get_markers(input, len_marker):
    blocks = [
        (input[chr_pos - len_marker : chr_pos], chr_pos)
        for chr_pos in range(len_marker, len(input) + 1)
    ]
    return filter(lambda block: len(set(block[0])) == len_marker, blocks)


# Puzzle 1

result_1 = next(get_markers(data, 4))[1]

print(f"Puzzle 1: {result_1}")

# Puzzle 2

result_2 = next(get_markers(data, 14))[1]

print(f"Puzzle 2: {result_2}")
