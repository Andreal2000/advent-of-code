import os
import re
import hashlib


def generate_key(input, key_stretching=False):
    index = 0
    keys = []
    triple = {}
    while len(keys) < 64:
        md5 = hashlib.md5((input + str(index)).encode()).hexdigest()

        if key_stretching:
            for _ in range(2016):
                md5 = hashlib.md5((md5).encode()).hexdigest()

        triple = {k: v for k, v in triple.items() if k + 1000 >= index}

        five = re.findall(r"(.)\1{4}", md5)
        if five != []:
            for k, v in triple.items():
                if v == five[0]:
                    keys += [k]

        three = re.findall(r"(.)\1{2}", md5)
        if three != []:
            triple[index] = three[0]

        index += 1

    return sorted(keys)[63]


def part_one(input):
    return generate_key(input)


def part_two(input):
    return generate_key(input, key_stretching=True)


if __name__ == "__main__":
    input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()
    print(part_one(input))  # 25427
    print(part_two(input))  # 22045
