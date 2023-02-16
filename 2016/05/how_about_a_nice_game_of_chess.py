import os
import hashlib


def hash(input):
    i = 1
    while True:
        md5 = hashlib.md5((input + str(i)).encode()).hexdigest()
        if md5.startswith("0" * 5):
            yield md5
        i += 1


def part_one(input):
    generator = hash(input)
    return "".join([next(generator)[5] for _ in range(8)])


def part_two(input):
    generator = hash(input)
    output = ["_"] * 8

    while "_" in output:
        code = next(generator)
        index = int(code[5]) if code[5].isdigit() else -1

        if 0 <= index <= 7 and output[index] == "_":
            output[index] = code[6]

    return "".join(output)


if __name__ == "__main__":
    input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()
    print(part_one(input))  # d4cd2ee1
    print(part_two(input))  # f2c730e5
