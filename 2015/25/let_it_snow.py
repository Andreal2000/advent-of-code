import os


def part_one(input):
    input = [int(input.strip().split()[x][:-1]) for x in [-3, -1]]

    previous = 20151125

    for _ in range(sum(range(sum(input) - 1)) + input[1] - 1):
        previous = (previous * 252533) % 33554393

    return previous


if __name__ == "__main__":
    input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()
    print(part_one(input))  # 9132360
