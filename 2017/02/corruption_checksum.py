import os


def part_one(input):
    input = [list(map(int, i.split())) for i in input.strip().splitlines()]
    return sum(max(i) - min(i) for i in input)


def part_two(input):
    input = [list(map(int, i.split())) for i in input.strip().splitlines()]
    return sum([x//y for y in i for x in i if x != y and x % y == 0][0]
               for i in input)


if __name__ == "__main__":
    input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()
    print(part_one(input))  # 47623
    print(part_two(input))  # 312
