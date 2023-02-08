import os

directions = {"^": (0, 1), "v": (0, -1), ">": (1, 0), "<": (-1, 0)}


def add(a, b): return tuple(map(sum, zip(a, b)))


def part_one(input):
    position = (0, 0)
    houses = [(0, 0)]

    for i in input:
        position = add(position, directions[i])
        houses.append(position)

    return len(set(houses))


def part_two(input):
    santa = (0, 0)
    robo = (0, 0)
    houses = [(0, 0)]

    for i in range(len(input)):
        if i % 2 == 0:
            santa = add(santa, directions[input[i]])
            houses.append(santa)
        else:
            robo = add(robo, directions[input[i]])
            houses.append(robo)

    return len(set(houses))


if __name__ == "__main__":
    input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()
    print(part_one(input))  # 2592
    print(part_two(input))  # 2360
