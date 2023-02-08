import os
from itertools import permutations


def find_routes(input):
    input = input.strip().splitlines()
    dimension = len({i.split()[x] for i in input for x in [0, 3]})
    matrix = [[0]*dimension for _ in range(dimension)]

    it = iter(input)
    for x in range(dimension):
        for y in range(x+1, dimension):
            matrix[x][y] = matrix[y][x] = int(next(it).split()[-1])

    return ([sum([matrix[p[i]][p[i+1]] for i in range(len(p)-1)])
             for p in permutations(range(dimension)) if p < p[::-1]])


def part_one(input):
    return min(find_routes(input))


def part_two(input):
    return max(find_routes(input))


if __name__ == "__main__":
    input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()
    print(part_one(input))  # 117
    print(part_two(input))  # 909
