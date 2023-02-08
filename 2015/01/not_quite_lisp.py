import os


def part_one(input):
    return sum(map(lambda x: (1 if x == "(" else -1), input))


def part_two(input):
    floor = 0
    for i in range(len(input)):
        floor += (1 if input[i] == "(" else -1)
        if floor == -1:
            return i + 1


if __name__ == "__main__":
    input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()
    print(part_one(input))  # 138
    print(part_two(input))  # 1771
