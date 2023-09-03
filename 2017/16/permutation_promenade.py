import os
import re


def dance(input, cycles=1):
    input = re.findall(r'([spx])(\w*)/?(\w*)', input)
    programs = list(chr(i) for i in range(ord("a"), ord("p")+1))
    seen = {}
    for n in range(1, cycles+1):
        for i in input:
            if i[0] == "s":
                x = int(i[1])
                programs = programs[-x:] + programs[:-x]
            elif i[0] == "x":
                a = int(i[1])
                b = int(i[2])
                tmp = programs[a]
                programs[a] = programs[b]
                programs[b] = tmp
            elif i[0] == "p":
                a = programs.index(i[1])
                b = programs.index(i[2])
                tmp = programs[a]
                programs[a] = programs[b]
                programs[b] = tmp

        key = tuple(programs)
        if (key in seen) and ((10**9 - n) % (n - seen[key]) == 0):
            break

        seen[key] = n

    return "".join(programs)


def part_one(input):
    return dance(input)


def part_two(input):
    return dance(input, cycles=10**9)


if __name__ == "__main__":
    input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()
    print(part_one(input))  # glnacbhedpfjkiom
    print(part_two(input))  # fmpanloehgkdcbji
