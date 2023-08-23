import os


def is_valid(passphrase, validator):
    for x in range(len(passphrase)):
        for y in range(x+1, len(passphrase)):
            if validator(passphrase[x], passphrase[y]):
                return False
    return True


def part_one(input):
    def is_valid_one(passphrase):
        return is_valid(passphrase, lambda x, y: x in y)

    return sum(map(is_valid_one, map(str.split, input.strip().splitlines())))


def part_two(input):
    def is_valid_two(passphrase):
        return is_valid(passphrase, lambda x, y: sorted(x) == sorted(y))

    return sum(map(is_valid_two, map(str.split, input.strip().splitlines())))


if __name__ == "__main__":
    input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()
    print(part_one(input))  # 383
    print(part_two(input))  # 265
