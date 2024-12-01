import os
from collections import defaultdict

directions = ((0, 1), (1, 0), (0, -1), (-1, 0))


def add(a, b):
    return tuple(map(sum, zip(a, b)))


def part_one(input):
    input = input.strip().splitlines()
    grid = defaultdict(lambda: ".")

    for y in range(len(input)):
        for x in range(len(input[0])):
            grid[(x, y)] = input[x][y]

    position = tuple([len(input[0]) // 2, len(input) // 2])
    direction = 3
    infected = 0

    for _ in range(10**4):
        if grid[position] == ".":
            direction = (direction - 1) % 4
            grid[position] = "#"
            infected += 1
            position = add(position, directions[direction])
        else:
            direction = (direction + 1) % 4
            grid[position] = "."
            position = add(position, directions[direction])

    return infected


def part_two(input):
    input = input.strip().splitlines()
    grid = defaultdict(lambda: ".")

    for y in range(len(input)):
        for x in range(len(input[0])):
            grid[(x, y)] = input[x][y]

    position = tuple([len(input[0]) // 2, len(input) // 2])
    direction = 3
    infected = 0

    for _ in range(10**7):
        current = grid[position]
        if current == ".":
            direction = (direction - 1) % 4
            grid[position] = "W"
            position = add(position, directions[direction])
        elif current == "W":
            grid[position] = "#"
            infected += 1
            position = add(position, directions[direction])
        elif current == "#":
            direction = (direction + 1) % 4
            grid[position] = "F"
            position = add(position, directions[direction])
        elif current == "F":
            direction = (direction + 2) % 4
            grid[position] = "."
            position = add(position, directions[direction])
            pass

    return infected


if __name__ == "__main__":
    input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()
    print(part_one(input))  # 5182
    print(part_two(input))  # 2512008
