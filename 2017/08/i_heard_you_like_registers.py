import os
import re


def measure_registers(input, highest_register=False):
    keys = re.findall(r'(\w+) (?:inc|dec) -?\d+ if (\w+)', input)
    registers = dict.fromkeys(set(a for b in keys for a in b), 0)
    highest = 0

    for i in map(str.split, input.strip().splitlines()):
        if eval(f"{registers[i[4]]} {i[5]} {i[6]}"):
            registers[i[0]] += int(i[2]) * (1 if i[1] == "inc" else -1)
            highest = max(highest, registers[i[0]])

    return highest if highest_register else max(registers.values())


def part_one(input):
    return measure_registers(input)


def part_two(input):
    return measure_registers(input, highest_register=True)


if __name__ == "__main__":
    input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()
    print(part_one(input))  # 5946
    print(part_two(input))  # 6026
