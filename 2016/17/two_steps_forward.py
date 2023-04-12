import os
import hashlib


def hash(input):
    open = ["b", "c", "d", "e", "f"]
    return [i in open for i in hashlib.md5((input).encode()).hexdigest()[:4]]


def find_paths(input):
    target = (3, 3)
    queue = [((0, 0), "")]
    directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
    paths = []
    while queue:
        for _ in range(len(queue)):
            position, path = queue.pop(0)

            if position == target:
                paths += [path]
                break

            for i, j in enumerate(hash(input + path)):
                next = tuple(map(sum, zip(position, directions[i])))
                if min(*next) >= 0 and max(*next) <= 3 and j:
                    queue.append((next, path + "UDLR"[i]))

    return paths


def part_one(input):
    return find_paths(input)[0]


def part_two(input):
    return len(find_paths(input)[-1])


if __name__ == "__main__":
    input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()
    print(part_one(input))  # DRRDRLDURD
    print(part_two(input))  # 618
