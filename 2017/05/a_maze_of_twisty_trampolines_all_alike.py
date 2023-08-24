import os


def interrupt(input, part_two=False):
    input = list(map(int, input.strip().splitlines()))
    index = 0
    steps = 0

    while index < len(input):
        extra = -1 if input[index] >= 3 and part_two else +1
        input[index] += extra
        index += input[index] - extra
        steps += 1

    return steps


def part_one(input):
    return interrupt(input)


def part_two(input):
    return interrupt(input, part_two=True)


if __name__ == "__main__":
    input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()
    print(part_one(input))  # 381680
    print(part_two(input))  # 29717847
