import os


def computer(input, mem):
    input = input.strip().splitlines()

    i = 0

    while 0 <= i < len(input):
        inst = input[i].split()
        if inst[0] == "cpy":
            x = int(inst[1]) if inst[1].isdecimal() else mem[inst[1]]
            mem[inst[2]] = x
            i += 1
        elif inst[0] == "inc":
            mem[inst[1]] += 1
            i += 1
        elif inst[0] == "dec":
            mem[inst[1]] -= 1
            i += 1
        elif inst[0] == "jnz":
            x = int(inst[1]) if inst[1].isdecimal() else mem[inst[1]]
            i += int(inst[2]) if x != 0 else 1

    return mem


def part_one(input):
    return computer(input, {"a": 0, "b": 0, "c": 0, "d": 0})["a"]


def part_two(input):
    return computer(input, {"a": 0, "b": 0, "c": 1, "d": 0})["a"]


if __name__ == "__main__":
    input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()
    print(part_one(input))  # 318020
    print(part_two(input))  # 9227674
