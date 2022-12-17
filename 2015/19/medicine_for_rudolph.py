import os
import re


def part_one(input):
    input = input.strip().split("\n")
    medicine = input[-1]
    input = [i.split()[::2] for i in input[:-2]]
    molecules = set()

    for i in input:
        for m in [m.start() for m in re.finditer(i[0], medicine)]:
            molecules.add(medicine[:m] + medicine[m:].replace(*i, 1))

    return len(molecules)


def part_two(input):
    input = input.strip().split("\n")[-1]
    elements = len(re.findall("[A-Z]", input))
    rn_ar = len(re.findall("Rn|Ar", input))
    y = len(re.findall("Y", input))

    return elements - rn_ar - 2*y - 1


if __name__ == "__main__":
    input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()
    print(part_one(input))  # 576
    print(part_two(input))  # 207
