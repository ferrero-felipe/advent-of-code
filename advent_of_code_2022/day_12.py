from string import ascii_lowercase
from networkx import DiGraph, shortest_path_length

with open("advent_of_code_2022/data/day_12_input.txt", "r") as file:
    data = file.read().split("\n")

data = [list(line) for line in data]

for y in range(len(data)):
    for x in range(len(data[y])):
        if data[y][x] == "S":
            start = (x, y)
            data[y][x] = "a"
        if data[y][x] == "E":
            finish = (x, y)
            data[y][x] = "z"

conv = {
    **{letter: value for value, letter in enumerate(ascii_lowercase)},
}
height_map = [[conv[pos] for pos in line] for line in data]

moves = {
    "up": lambda x, y: [x, y - 1],
    "down": lambda x, y: [x, y + 1],
    "left": lambda x, y: [x - 1, y],
    "right": lambda x, y: [x + 1, y],
}


def valide_coordinates(x, y, height_map=height_map):
    if x < 0:
        return False
    if y < 0:
        return False
    if y >= len(height_map):
        return False
    if x >= len(height_map[y]):
        return False
    return True


def posible_moves(x, y):
    destinations = []
    for move in moves.values():
        destinations.append(move(x, y))
    destinations = filter(lambda coord: valide_coordinates(*coord), destinations)
    return destinations


def connections(x, y, destinations, height_map=height_map):
    connections = []
    for dest in destinations:
        x_dest, y_dest = dest
        if height_map[y_dest][x_dest] - height_map[y][x] <= 1:
            connections.append(((x, y), (x_dest, y_dest)))
    return connections


G = DiGraph()

for y in range(len(data)):
    for x in range(len(data[y])):
        if height_map[y][x] == "S":
            start = (x, y)
        if height_map[y][x] == "E":
            finish = (x, y)
        edges = connections(x, y, posible_moves(x, y))
        for src, dest in edges:
            G.add_edge(src, dest)


# Puzzle 1

result_1 = shortest_path_length(G, start, finish)
print(f"Puzzle 1: {result_1}")

# Puzzle 2

a_squares = []
for y in range(len(data)):
    for x in range(len(data[y])):
        if height_map[y][x] == 0:
            a_squares.append((x, y))

lenghts = []
for a_start in a_squares:
    try:
        lenghts.append(shortest_path_length(G, a_start, finish))
    except:
        pass

result_2 = min(lenghts)

print(f"Puzzle 2: {result_2}")
