import os
from functools import reduce
from operator import xor


def knot_hash_rounds(input, rounds=1):
    size = 256
    hash = list(range(size))
    position = 0
    skip_size = 0

    for _ in range(rounds):
        for i in input:
            for p in range(i//2):
                tmp = hash[(position+p) % size]
                hash[(position+p) % size] = hash[(position+i-p-1) % size]
                hash[(position+i-p-1) % size] = tmp

            position = (position + i + skip_size) % size
            skip_size += 1

    return hash


def part_one(input):
    hash = knot_hash_rounds(list(map(int, input.strip().split(","))))
    return hash[0] * hash[1]


def part_two(input):
    input = list(map(ord, input.strip())) + [17, 31, 73, 47, 23]
    hash = knot_hash_rounds(input, rounds=64)
    hash = [reduce(xor, hash[i:i+16]) for i in range(0, 256, 16)]
    return "".join(f"{i:02x}" for i in hash)


if __name__ == "__main__":
    input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()
    print(part_one(input))  # 11413
    print(part_two(input))  # 7adfd64c2a03a4968cf708d1b7fd418d
