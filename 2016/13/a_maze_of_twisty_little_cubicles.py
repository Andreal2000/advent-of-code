import os


def is_wall(x, y, input):
    return bin(x*x + 3*x + 2*x*y + y + y*y + input).count("1") % 2 != 0


def part_one(input):
    input = int(input)
    target = (31, 39)
    queue = [(1, 1)]
    seen = set()
    steps = -1

    while queue:
        steps += 1
        for _ in range(len(queue)):
            x, y = queue.pop(0)
            seen.add((x, y))

            if (x, y) == target:
                return steps

            for i in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                next = tuple(map(sum, zip((x, y), i)))
                if (next not in seen
                        and min(*next) >= 0
                        and not is_wall(*next, input)):
                    queue.append(next)


def part_two(input):
    input = int(input)
    queue = [(1, 1)]
    seen = set()
    steps = -1

    while steps < 50:
        steps += 1
        for _ in range(len(queue)):
            x, y = queue.pop(0)
            seen.add((x, y))

            for i in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                next = tuple(map(sum, zip((x, y), i)))
                if (next not in seen
                        and min(*next) >= 0
                        and not is_wall(*next, input)):
                    queue.append(next)

    return len(seen)


if __name__ == "__main__":
    input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()
    print(part_one(input))  # 90
    print(part_two(input))  # 135
