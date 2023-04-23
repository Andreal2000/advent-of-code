import os


def part_one(input):
    input = [tuple(map(int, i.split("-"))) for i in input.strip().splitlines()]
    input = sorted(input)

    ip = 0
    for i in input:
        if i[0] <= ip <= i[1]:
            ip = i[1] + 1

    return ip


def part_two(input):
    input = [tuple(map(int, i.split("-"))) for i in input.strip().splitlines()]
    input = sorted(input)

    output = [input.pop(0)]
    for i in input:
        if i[0] > output[-1][1]:
            output += [i]
        elif i[0] > output[-1][0] and i[1] > output[-1][1]:
            output[-1] = (output[-1][0], i[1])

    ip = 0
    for i in range(1, len(output)):
        ip += (output[i][0] - output[i-1][1]) - 1

    return ip


if __name__ == "__main__":
    input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()
    print(part_one(input))  # 14975795
    print(part_two(input))  # 101
