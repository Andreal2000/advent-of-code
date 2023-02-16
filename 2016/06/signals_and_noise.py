import os
from itertools import groupby


def message(input, fun):
    input = input.strip().splitlines()
    input = [sorted([i[r] for i in input]) for r in range(len(input[0]))]
    input = [fun(groupby(i), key=lambda x: len(list(x[1])))[0] for i in input]
    return "".join(input)


def part_one(input):
    return message(input, max)


def part_two(input):
    return message(input, min)


if __name__ == "__main__":
    input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()
    print(part_one(input))  # gyvwpxaz
    print(part_two(input))  # jucfoary
