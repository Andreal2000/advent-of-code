import os
import re
import json


def part_one(input):
    return sum(map(int, re.sub("[^-0-9]", " ", input.strip()).split()))


def part_two(input):
    input = json.loads(input)

    def count(j):
        out = 0
        for i in j:
            if type(i) == int:
                out += i
            if type(i) == list:
                out += count(i)
            if type(i) == dict:
                out += 0 if "red" in i.values() else count(i.values())
        return out

    return count(input)


if __name__ == "__main__":
    input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()
    print(part_one(input))  # 191164
    print(part_two(input))  # 87842
