import os


def part_one(input):
    input = input.strip().splitlines()
    mem = {chr(i): 0 for i in range(ord("a"), ord("h") + 1)}
    mul = 0

    i = 0

    while 0 <= i < len(input):
        inst = input[i].split()
        if inst[0] == "set":
            mem[inst[1]] = mem[inst[2]] if inst[2].isalpha() else int(inst[2])
            i += 1
        elif inst[0] == "sub":
            mem[inst[1]] -= mem[inst[2]] if inst[2].isalpha() else int(inst[2])
            i += 1
        elif inst[0] == "mul":
            mem[inst[1]] *= mem[inst[2]] if inst[2].isalpha() else int(inst[2])
            mul += 1
            i += 1
        elif inst[0] == "jnz":
            x = mem[inst[1]] if inst[1].isalpha() else int(inst[1])
            y = mem[inst[2]] if inst[2].isalpha() else int(inst[2])
            i += y if x != 0 else 1

    return mul


def part_two(_):
    h = 0
    for x in range(109900, 126900 + 1, 17):
        for i in range(2, x):
            if x % i == 0:
                h += 1
                break

    return h


if __name__ == "__main__":
    input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()
    print(part_one(input))  # 9409
    print(part_two(input))  # 913
