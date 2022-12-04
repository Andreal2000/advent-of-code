import os
import hashlib


def part_one(input):
    i = 1
    while True:
        md5 = hashlib.md5((input + str(i)).encode()).hexdigest()
        if md5.startswith("0"*5):
            return i
        i += 1


def part_two(input):
    i = 1
    while True:
        md5 = hashlib.md5((input + str(i)).encode()).hexdigest()
        if md5.startswith("0"*6):
            return i
        i += 1


if __name__ == "__main__":
    input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()
    print(part_one(input))  # 254575
    print(part_two(input))  # 1038736
