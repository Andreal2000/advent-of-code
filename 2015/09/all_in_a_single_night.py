import os
from itertools import permutations


def part_one(input):
    input = input.strip().split("\n")
    dimension = len({i.split(" ")[x] for i in input for x in [0, 3]})
    matrix = [[0]*dimension for i in range(dimension)]

    it = iter(input)
    for x in range(dimension):
        for y in range(x+1, dimension):
            matrix[x][y] = matrix[y][x] = int(next(it).split(" ")[-1])

    return min([sum([matrix[p[i]][p[i+1]] for i in range(len(p)-1)])
                for p in permutations(range(dimension)) if p < p[::-1]])


def part_two(input):
    input = input.strip().split("\n")
    dimension = len({i.split(" ")[x] for i in input for x in [0, 3]})
    matrix = [[0]*dimension for i in range(dimension)]

    it = iter(input)
    for x in range(dimension):
        for y in range(x+1, dimension):
            matrix[x][y] = matrix[y][x] = int(next(it).split(" ")[-1])

    return max([sum([matrix[p[i]][p[i+1]] for i in range(len(p)-1)])
                for p in permutations(range(dimension)) if p < p[::-1]])


if __name__ == "__main__":
    input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()
    print(part_one(input))  # 117
    print(part_two(input))  # 909
