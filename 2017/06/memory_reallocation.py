import os


def debugger(input, loop_size=False):
    input = list(map(int, input.strip().split("\t")))

    cycle = 0
    states = []

    while input not in states:
        states += [input.copy()]
        cycle += 1

        most_blocks = max(input)
        index = input.index(most_blocks)
        input[index] = 0

        for i in range(1, most_blocks+1):
            input[(index + i) % len(input)] += 1

    return len(states) - states.index(input) if loop_size else cycle


def part_one(input):
    return debugger(input)


def part_two(input):
    return debugger(input, loop_size=True)


if __name__ == "__main__":
    input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()
    print(part_one(input))  # 11137
    print(part_two(input))  # 1037
