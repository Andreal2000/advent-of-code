import os
from functools import reduce


def part_one(input):
    return reduce(lambda x, y: x + (1 if y == "(" else -1), input, 0)


def part_two(input):
    floor = 0
    for i in range(len(input)):
        floor += (1 if input[i] == "(" else -1)
        if floor == -1:
            return i + 1


if __name__ == "__main__":
    input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()
    print(part_one(input))  # 138
    print(part_two(input))  # 1771
