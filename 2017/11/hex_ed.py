import os


def distance(input, furthest=False):
    input = input.strip().split(",")
    q = r = s = 0
    path = [0]

    for i in input:
        if i == "n":
            r -= 1
            s += 1
        elif i == "ne":
            q += 1
            r -= 1
        elif i == "se":
            q += 1
            s -= 1
        elif i == "s":
            r += 1
            s -= 1
        elif i == "sw":
            q -= 1
            r += 1
        elif i == "nw":
            q -= 1
            s += 1

        path += [max(map(abs, [q, r, s]))]

    return max(path) if furthest else path[-1]


def part_one(input):
    return distance(input)


def part_two(input):
    return distance(input, furthest=True)


if __name__ == "__main__":
    input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()
    print(part_one(input))  # 643
    print(part_two(input))  # 1471
