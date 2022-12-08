with open("advent_of_code_2022/data/day_8_input.txt", "r") as file:
    data = file.read().split("\n")

forest = [[int(tree) for tree in row] for row in data]

# Puzzle 1

hor = [
    [
        any(
            [
                all([row[i] > tree for tree in row[:i]]),
                all([row[i] > tree for tree in row[i + 1 :]]),
            ]
        )
        for i in range(len(row))
    ]
    for row in forest
]
forest_transpose = list(zip(*forest))
ver = zip(
    *[
        [
            any(
                [
                    all([row[i] > tree for tree in row[:i]]),
                    all([row[i] > tree for tree in row[i + 1 :]]),
                ]
            )
            for i in range(len(row))
        ]
        for row in forest_transpose
    ]
)
visible = [[h or v for h, v in zip(h_row, v_row)] for h_row, v_row in zip(hor, ver)]

result_1 = sum([visibility for row in visible for visibility in row])

print(f"Puzzle 1: {result_1}")

# Puzzle 2

hor_score = []

for row in forest:
    row_scores = []
    for i, pov in enumerate(row):
        l, r = 0, 0
        for tree in row[:i][::-1]:
            l += 1
            if tree >= pov:
                break
        for tree in row[i + 1 :]:
            r += 1
            if tree >= pov:
                break
        row_scores.append(l * r)
    hor_score.append(row_scores)

ver_score = []

for row in forest_transpose:
    row_scores = []
    for i, pov in enumerate(row):
        u, d = 0, 0
        for tree in row[:i][::-1]:
            u += 1
            if tree >= pov:
                break
        for tree in row[i + 1 :]:
            d += 1
            if tree >= pov:
                break
        row_scores.append(u * d)
    ver_score.append(row_scores)

ver_score = list(zip(*ver_score))

result_2 = max(
    [h * v for row_h, row_v in zip(hor_score, ver_score) for h, v in zip(row_h, row_v)]
)

print(f"Puzzle 1: {result_2}")
