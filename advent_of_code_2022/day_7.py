with open("advent_of_code_2022/data/day_7_input.txt", "r") as file:
    data = file.read().split("\n")


class Object:
    def __init__(self, name, type, size=0):
        self.name = name
        self.children = []
        self.type = type
        self.size = size

    def set_parent(self, parent):
        self.parent = parent
        parent.add_children(self)

    def __repr__(self) -> str:
        return f"<{self.type.capitalize()} {self.name}>"


class Dir(Object):
    def __init__(self, name):
        super().__init__(name, type="dir")

    def add_children(self, child):
        self.children.append(child)

    def get_child(self, child_name):
        for child in self.children:
            if child.name == child_name:
                return child

    def get_size(self):
        size = 0
        for child in self.children:
            if child.type == "file":
                size += child.size
            elif child.type == "dir":
                size += child.get_size()
        return size


class File(Object):
    def __init__(self, name, size):
        super().__init__(name, "file", size)


root = Dir("/")
cwd = root

all_dirs = [root]

for line in data[1:]:
    if not line.startswith("$"):
        cond, path = line.split()
        if cond == "dir":
            dir = Dir(path)
            dir.set_parent(cwd)
            all_dirs.append(dir)
        else:
            file = File(path, int(cond))
            file.set_parent(cwd)
    elif line.startswith("$ cd"):
        _, _, path = line.split()
        if path == "..":
            if cwd.name != "/":
                cwd = cwd.parent
        else:
            cwd = cwd.get_child(path)

# Puzzle 1

result_1 = sum(
    filter(lambda size: size <= 100000, [dir.get_size() for dir in all_dirs])
)

print(f"Puzzle 1: {result_1}")

# Puzzle 2

total_size = 70000000
available = total_size - root.get_size()
needed_space = 30000000
result_2 = min(
    filter(
        lambda size: available + size >= needed_space,
        [dir.get_size() for dir in all_dirs],
    )
)

print(f"Puzzle 2: {result_2}")
