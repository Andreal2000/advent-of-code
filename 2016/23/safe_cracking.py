import os
import re


def computer(input, mem):
    regex = r"cpy (.) (.)\ninc (.)\ndec \2\njnz \2 -2\ndec (.)\njnz \4 -5\n"
    input = re.sub(regex, r"mul \1 \4 \3 \2\nnop\nnop\nnop\nnop\nnop\n", input)
    input = input.strip().splitlines()

    i = 0

    while 0 <= i < len(input):
        inst = input[i].split()
        if inst[0] == "mul":
            mem[inst[3]] = mem[inst[1]] * mem[inst[2]]
            mem[inst[2]] = 0
            mem[inst[4]] = 0
            i += 1
        elif inst[0] == "tgl" and 0 <= i + mem[inst[1]] < len(input):
            tgl = i + mem[inst[1]]
            tgl_inst = input[tgl].split()
            if tgl_inst[0] == "inc":
                input[tgl] = input[tgl].replace("inc", "dec")
            elif tgl_inst[0] == "dec":
                input[tgl] = input[tgl].replace("dec", "inc")
            elif tgl_inst[0] == "tgl":
                input[tgl] = input[tgl].replace("tgl", "inc")
            elif tgl_inst[0] == "cpy":
                input[tgl] = input[tgl].replace("cpy", "jnz")
            elif tgl_inst[0] == "jnz":
                input[tgl] = input[tgl].replace("jnz", "cpy")
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

    return mem


def part_one(input):
    return computer(input, {"a": 7, "b": 0, "c": 0, "d": 0})["a"]


def part_two(input):
    return computer(input, {"a": 12, "b": 0, "c": 0, "d": 0})["a"]


if __name__ == "__main__":
    input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()
    print(part_one(input))  # 10440
    print(part_two(input))  # 479007000
