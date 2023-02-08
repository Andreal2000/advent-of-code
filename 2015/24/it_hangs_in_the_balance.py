import os
from functools import reduce
from itertools import combinations
from operator import mul


def splitter(input, groups):
    input = list(map(int, input.strip().splitlines()))
    weight = sum(input)/groups

    def splitter_helper(packs, groups):
        if groups == 1:
            return [packs]
        for i in range(len(packs)):
            for j in [p for p in combinations(packs, i) if sum(p) == weight]:
                return [list(j)] + splitter_helper(set(packs)-set(j), groups-1)

    return splitter_helper(input, groups)


def part_one(input):
    return reduce(mul, splitter(input, 3)[0])


def part_two(input):
    return reduce(mul, splitter(input, 4)[0])


if __name__ == "__main__":
    input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()
    print(part_one(input))  # 11846773891
    print(part_two(input))  # 80393059
