import os
from functools import reduce
from operator import xor


def knot_hash(input):
    input = list(map(ord, input.strip())) + [17, 31, 73, 47, 23]
    hash = list(range(256))
    position = 0
    skip_size = 0

    for _ in range(64):
        for i in input:
            for p in range(i//2):
                tmp = hash[(position+p) % 256]
                hash[(position+p) % 256] = hash[(position+i-p-1) % 256]
                hash[(position+i-p-1) % 256] = tmp

            position = (position + i + skip_size) % 256
            skip_size += 1

    hash = [reduce(xor, hash[i:i+16]) for i in range(0, 256, 16)]
    return "".join(f"{i:02x}" for i in hash)


def part_one(input):
    input = input.strip()
    hashes = [knot_hash(f"{input}-{r}") for r in range(128)]
    return sum(sum(bin(int(i, base=16)).count("1") for i in h) for h in hashes)


def part_two(input):
    input = input.strip()
    geid = [knot_hash(f"{input}-{r}") for r in range(128)]
    grid = [list("".join(f"{int(i, base=16):04b}" for i in h)) for h in geid]
    grid = [list(map(int, i)) for i in grid]

    def clear_region(grid, x, y):
        grid[x][y] = 0
        for i in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            a, b = tuple(map(sum, zip((x, y), i)))
            if (min(a, b) >= 0 and max(a, b) <= 127 and grid[a][b] == 1):
                clear_region(grid, a, b)

    regions = 0
    for x in range(128):
        for y in range(128):
            if grid[x][y] == 1:
                clear_region(grid, x, y)
                regions += 1

    return regions


if __name__ == "__main__":
    input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()
    print(part_one(input))  # 8190
    print(part_two(input))  # 1134
