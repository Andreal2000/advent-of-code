import os
from functools import reduce
from itertools import combinations
from operator import mul


def part_one(input):
    input = list(map(int, input.strip().split("\n")))
    groups = 3
    weight = sum(input)/groups

    def splitter(packs, groups):
        if groups == 1:
            return [packs]
        for i in range(len(packs)):
            for j in [p for p in combinations(packs, i) if sum(p) == weight]:
                return [list(j)] + splitter(list(set(packs)-set(j)), groups-1)

    split = splitter(input, groups)

    return reduce(mul, split[0])


def part_two(input):
    input = list(map(int, input.strip().split("\n")))
    groups = 4
    weight = sum(input)/groups

    def splitter(packs, groups):
        if groups == 1:
            return [packs]
        for i in range(len(packs)):
            for j in [p for p in combinations(packs, i) if sum(p) == weight]:
                return [list(j)] + splitter(list(set(packs)-set(j)), groups-1)

    split = splitter(input, groups)

    return reduce(mul, split[0])


if __name__ == "__main__":
    input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()
    print(part_one(input))  # 11846773891
    print(part_two(input))  # 80393059
