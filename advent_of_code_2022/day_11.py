from functools import reduce

with open("advent_of_code_2022/data/day_11_input.txt", "r") as file:
    data = file.read().split("\n\n")


class Monkey:
    def __init__(self, items, operation, test, true, false, relief=1) -> None:
        self.items = list(items)
        self.operation = operation
        self.test = test
        self.true = true
        self.false = false
        self.counter = 0
        self.relief = relief
        self.lcm = 1

    def set_lcm(self, lcm=1):
        self.lcm = lcm

    def _inspect(self, item):
        self.counter += 1
        old = item
        new = eval(self.operation)
        new //= self.relief
        new %= self.lcm
        return new

    def _test(self, item):
        return item % self.test == 0

    def _throw(self, item, monkeys):
        if self._test(item):
            monkeys[self.true].receive(item)
        else:
            monkeys[self.false].receive(item)

    def receive(self, item):
        self.items.append(item)

    def turn(self, monkeys):
        for _ in range(len(self.items)):
            item = self.items.pop(0)
            item = self._inspect(item)
            self._throw(item, monkeys)

    def total(self):
        return sum(self.items)


class MonkeyTroop:
    def __init__(self, monkeys) -> None:
        self.monkeys = monkeys
        self.set_lcm()

    def set_lcm(self):
        lcm = reduce(lambda a, b: a * b, [monkey.test for monkey in self.monkeys])
        for monkey in self.monkeys:
            monkey.set_lcm(lcm)

    def _round(self):
        for monkey in self.monkeys:
            monkey.turn(self)

    def rounds(self, num):
        for _ in range(num):
            self._round()

    def __iter__(self):
        return iter(self.monkeys)

    def __getitem__(self, __name: str) -> Monkey:
        return self.monkeys[__name]

    def business(self):
        return reduce(
            lambda a, b: a * b,
            sorted([monkey.counter for monkey in monkeys], reverse=True)[:2],
        )


monkeys_data = []
for monkey in data:
    items, operation, test, true, false = map(
        lambda line: line.split(":")[-1].strip(), monkey.split("\n")[1:]
    )
    items = tuple(map(int, items.split(",")))
    operation = operation.split("=")[-1].strip()
    test = int(test.split("by")[-1])
    true, false = tuple(
        map(lambda throw: int(throw.split("monkey")[-1]), [true, false])
    )
    monkeys_data.append((items, operation, test, true, false))


# Puzzle 1
monkeys = MonkeyTroop([Monkey(*monkey, relief=3) for monkey in monkeys_data])

monkeys.rounds(20)

result_1 = monkeys.business()

print(f"Puzzle 1: {result_1}")

# Puzzle 2

monkeys = MonkeyTroop([Monkey(*monkey) for monkey in monkeys_data])

monkeys.rounds(10000)

result_2 = monkeys.business()

print(f"Puzzle 2: {result_2}")


# Puzzle 1: 182293
# Puzzle 2: 54832778815
