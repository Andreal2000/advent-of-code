import os


def part_one(input):
    input = [sorted(map(int, i.split())) for i in input.strip().splitlines()]
    return sum([sum(i[:-1]) > i[-1] for i in input])


def part_two(input):
    input = [list(map(int, i.split())) for i in input.strip().splitlines()]

    input = [sorted([input[i+x][y] for x in range(3)])
             for y in range(3)
             for i in range(0, len(input), 3)]

    return sum([sum(i[:-1]) > i[-1] for i in input])


if __name__ == "__main__":
    input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()
    print(part_one(input))  # 1032
    print(part_two(input))  # 1838
