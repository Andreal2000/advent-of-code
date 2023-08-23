import os
import math


def part_one(input):
    input = int(input)
    i = 1
    n = 0

    while i < input:
        n += 1
        i += n * 8

    return n + abs((input - i) % (2 * n) - n) if input > 1 else 0


def part_two(input):
    input = int(input)

    def add(a, b): return tuple(map(sum, zip(a, b)))

    directions = ((0, 1), (-1, 0), (0, -1), (1, 0))
    index = 3

    dim = math.ceil(math.sqrt(input))
    dim = dim if dim % 2 else dim + 1
    grid = [[0]*dim for _ in range(dim)]
    position = [int(dim/2)]*2
    grid[position[0]][position[1]] = 1

    while grid[position[0]][position[1]] <= input:
        next = add(position, directions[(index+1) % 4])

        if grid[next[0]][next[1]] == 0:
            index = (index+1) % 4

        x, y = position = add(position, directions[index])
        grid[x][y] = sum(sum(grid[x+i][y-1:y+2]) for i in range(-1, 2))

    return grid[position[0]][position[1]]


if __name__ == "__main__":
    input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()
    print(part_one(input))  # 552
    print(part_two(input))  # 330785
