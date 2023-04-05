import os


def generate_checksum(input, disk):
    while len(input) < disk:
        input = input + "0" + "".join("01"[i == "0"] for i in input[::-1])

    checksum = list(map(int, input[:disk]))

    while (len(checksum) % 2) == 0:
        checksum = [sum(checksum[i:i+2]) != 1
                    for i in range(0, len(checksum), 2)]

    return "".join(map(str, map(int, checksum)))


def part_one(input):
    return generate_checksum(input, 272)


def part_two(input):
    return generate_checksum(input, 35651584)


if __name__ == "__main__":
    input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()
    print(part_one(input))  # 11111000111110000
    print(part_two(input))  # 10111100110110100
