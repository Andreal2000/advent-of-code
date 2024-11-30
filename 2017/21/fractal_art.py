import os


def rotate(pattern):
    return ["".join(row) for row in zip(*pattern[::-1])]


def flip(pattern):
    return [row[::-1] for row in pattern]


def all_transforms(pattern):
    for _ in range(4):
        yield pattern
        yield flip(pattern)
        pattern = rotate(pattern)


def get_transforms(rules, pattern):
    for pattern in all_transforms(pattern):
        pattern = tuple(pattern)
        if pattern in rules:
            return rules[pattern]


def art_generator(input, iterations):
    input = input.strip().splitlines()
    rules = {}

    for line in input:
        pattern, result = line.split(" => ")
        pattern = pattern.split("/")
        result = result.split("/")
        rules[tuple(pattern)] = result

    grid = [".#.", "..#", "###"]

    for _ in range(iterations):
        size = len(grid)
        div = 2 if size % 2 == 0 else 3
        new_grid = []

        for y in range(0, size, div):
            new_row = []
            for x in range(0, size, div):
                pattern = [grid[y + dy][x : x + div] for dy in range(div)]
                new_row.append(get_transforms(rules, pattern))
            new_grid.extend(["".join(row) for row in zip(*new_row)])
        grid = new_grid

    return sum(row.count("#") for row in grid)


def part_one(input):
    return art_generator(input, 5)


def part_two(input):
    return art_generator(input, 18)


if __name__ == "__main__":
    input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()
    print(part_one(input))  # 160
    print(part_two(input))  # 2271537
