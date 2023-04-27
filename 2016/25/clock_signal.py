import os
import re


def computer(input, mem):
    regex = r"cpy (.+) (.)\ninc (.)\ndec \2\njnz \2 -2\ndec (.)\njnz \4 -5\n"
    input = re.sub(regex, r"mul \1 \4 \3 \2\nnop\nnop\nnop\nnop\nnop\n", input)
    input = input.strip().splitlines()
    out = []
    i = 0

    while 0 <= i < len(input) and len(out) < 8:
        inst = input[i].split()
        if inst[0] == "out":
            out += [mem[inst[1]] if inst[1].isalpha() else int(inst[1])]
            i += 1
        elif inst[0] == "mul":
            x = mem[inst[1]] if inst[1].isalpha() else int(inst[1])
            mem[inst[3]] += x * mem[inst[2]]
            mem[inst[2]] = 0
            mem[inst[4]] = 0
            i += 1
        elif inst[0] == "cpy" and inst[2].isalpha():
            x = mem[inst[1]] if inst[1].isalpha() else int(inst[1])
            mem[inst[2]] = x
            i += 1
        elif inst[0] == "inc":
            mem[inst[1]] += 1
            i += 1
        elif inst[0] == "dec":
            mem[inst[1]] -= 1
            i += 1
        elif inst[0] == "jnz":
            x = mem[inst[1]] if inst[1].isalpha() else int(inst[1])
            y = mem[inst[2]] if inst[2].isalpha() else int(inst[2])
            i += y if x != 0 else 1
        else:
            i += 1

    return out


def part_one(input):
    signal = list(range(2))*4
    i = 0

    while computer(input, {"a": i, "b": 0, "c": 0, "d": 0}) != signal:
        i += 1
    return i


if __name__ == "__main__":
    input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()
    print(part_one(input))  # 158
