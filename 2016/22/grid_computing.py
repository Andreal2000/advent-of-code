import os
import re


def part_one(input):
    regex = r"/dev/grid/node-x(\d+)-y(\d+) +(\d+)T +(\d+)T +(\d+)T +(\d+)%"
    input = [tuple(map(int, i)) for i in re.findall(regex, input)]

    used = sorted(input, key=lambda x: x[3])
    avail = sorted(input, key=lambda x: x[4], reverse=True)
    pairs = []
    for i in used:
        if i[3] != 0:
            for j in avail:
                if i[3] > j[4] or i == j:
                    break
                else:
                    pairs += [tuple([i[:2], j[:2]])]

    return len(pairs)


def part_two(input):
    regex = r"/dev/grid/node-x(\d+)-y(\d+) +(\d+)T +(\d+)T +(\d+)T +(\d+)%"
    input = [tuple(map(int, i)) for i in re.findall(regex, input)]

    data = [[0]*(input[-1][0] + 1) for _ in range(input[-1][1] + 1)]
    for i in input:
        data[i[1]][i[0]] = i[2:]

    steps = 0
    empty = min(input, key=lambda x: x[3])
    position = list(empty[:2][::-1])

    while data[position[0]-1][position[1]][1] <= empty[4]:
        position[0] -= 1
        steps += 1

    while data[position[0]-1][position[1]][1] > empty[4]:
        position[1] -= 1
        steps += 1

    position[0] -= 2
    steps += 2

    return steps + position[0] - position[1] + (len(data[0])-2)*6 + 1


if __name__ == "__main__":
    input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()
    print(part_one(input))  # 967
    print(part_two(input))  # 205
