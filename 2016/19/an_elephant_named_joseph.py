import os


def part_one(input):
    input = int(input)
    elves = [1] * input
    i = 0

    while True:
        j = 1
        while elves[(i+j) % input] == 0:
            j += 1

        if elves[i % input] != 0:

            elves[i % input] += elves[(i+j) % input]
            elves[(i+j) % input] = 0
            j += 1

            if elves[i % input] == input:
                return (i % input) + 1
        i += j


def part_two(input):
    input = int(input)
    i = 1

    while i * 3 < input:
        i *= 3

    return input - i


if __name__ == "__main__":
    input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()
    print(part_one(input))  # 1834471
    print(part_two(input))  # 1420064
