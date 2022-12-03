import os
from functools import reduce


def part_one(input):
    def paper(box):
        le, wi, he = map(int, box)
        sides = [le*wi, wi*he, he*le]
        return sum(sides)*2 + min(sides)

    return sum(map(paper, [i.split("x") for i in input.strip().split("\n")]))


def part_two(input):
    def ribbon(box):
        sides = list(map(int, box))
        return sum(sorted(sides)[:-1])*2 + reduce(lambda x, y: x*y, sides)

    return sum(map(ribbon, [i.split("x") for i in input.strip().split("\n")]))


if __name__ == "__main__":
    input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()
    print(part_one(input))  # 1586300
    print(part_two(input))  # 3737498
