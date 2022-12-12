with open("advent_of_code_2022/data/day_09_input.txt", "r") as file:
    data = list(map(lambda x: x.split(), file.read().split("\n")))

# Puzzle 1

head, tail = [0, 0], [0, 0]
visited = [(0, 0)]

move = {
    "R": lambda x, y: [x + 1, y],
    "L": lambda x, y: [x - 1, y],
    "U": lambda x, y: [x, y + 1],
    "D": lambda x, y: [x, y - 1],
}


def follow(head, tail):
    delta_x = head[0] - tail[0]
    delta_y = head[1] - tail[1]

    if abs(delta_x) >= 2:
        direction = "R" if delta_x > 0 else "L"
        tail = move[direction](*tail)
        if abs(delta_y) >= 1:
            direction = "U" if delta_y > 0 else "D"
            tail = move[direction](*tail)
    elif abs(delta_y) >= 2:
        direction = "U" if delta_y > 0 else "D"
        tail = move[direction](*tail)
        if abs(delta_x) >= 1:
            direction = "R" if delta_x > 0 else "L"
            tail = move[direction](*tail)

    return tail


for direction, qtty in data:
    for _ in range(int(qtty)):
        head = move[direction](*head)
        tail = follow(head, tail)
        visited.append(tuple(tail))

result_1 = len(set(visited))

print(f"Puzzle 1: {result_1}")

# Puzzle 2

rope = [[0, 0] for _ in range(10)]

visited = [(0, 0)]


for direction, qtty in data:
    for _ in range(int(qtty)):
        rope[0] = move[direction](*rope[0])
        for i in range(1, len(rope)):
            rope[i] = follow(rope[i - 1], rope[i])
            matrix = [["." for _ in range(10)] for _ in range(10)]
        visited.append(tuple(rope[-1]))

result_2 = len(set(visited))

print(f"Puzzle 2: {result_2}")
