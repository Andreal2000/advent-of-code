import os


def part_one(input):
    input = input.strip().split("\n")

    def decode_string(string): return bytes(
        string, "utf-8").decode("unicode_escape")

    return sum(map(lambda x: len(x) - (len(decode_string(x)) - 2), input))


def part_two(input):
    input = input.strip().split("\n")

    def encode_string(string):
        return string.replace("\\", "\\\\").replace('"', '\\"')

    return sum(map(lambda x: len(encode_string(x)) + 2 - len(x), input))


if __name__ == "__main__":
    input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()
    print(part_one(input))  # 1333
    print(part_two(input))  # 2046
