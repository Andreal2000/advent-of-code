import os

directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
turn = {"L": -1, "R": 1}


def add(a, b): return tuple(map(sum, zip(a, b)))


def part_one(input):
    input = [(i[0], int(i[1:].strip(","))) for i in input.strip().split()]
    position = (0, 0)
    index = 0

    for i in input:
        index = (index + turn[i[0]]) % 4
        position = add(position, [d * i[1] for d in directions[index]])

    return sum(position)


def part_two(input):
    input = [(i[0], int(i[1:].strip(","))) for i in input.strip().split()]
    position = (0, 0)
    path = [(0, 0)]
    index = 0

    for i in input:
        index = (index + turn[i[0]]) % 4
        for _ in range(i[1]):
            position = add(position, directions[index])
            if position in path:
                return sum(position)
            else:
                path += [position]


if __name__ == "__main__":
    input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()
    print(part_one(input))  # 353
    print(part_two(input))  # 152
