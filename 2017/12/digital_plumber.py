import os


def find_groups(input):
    input = list(map(str.split, input.strip().replace(",", "").splitlines()))
    input = {int(i[0]): list(map(int, i[2:])) for i in input}
    groups = {}

    while len(input) != 0:
        id = min(input.keys())
        seen = set([id])
        group = set()

        while len(seen) != 0:
            program = seen.pop()
            group.add(program)
            seen.update(i for i in input.pop(program) if i not in group)

        groups[id] = group

    return groups


def part_one(input):
    return len(find_groups(input)[0])


def part_two(input):
    return len(find_groups(input))


if __name__ == "__main__":
    input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()
    print(part_one(input))  # 175
    print(part_two(input))  # 213
