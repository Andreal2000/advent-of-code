import os


def part_one(input):
    input = int(input)
    house = [0] * (input//10+1)

    for i in range(1, input//10+1):
        for j in range(i, input//10+1, i):
            house[j] += i*10

    for i in range(len(house)):
        if house[i] >= input:
            return i


def part_two(input):
    input = int(input)
    house = [0] * (input//11+1)

    for i in range(1, input//10+1):
        for j in range(i, i*50+1 if i*50+1 < len(house) else len(house), i):
            house[j] += i*11

    for i in range(len(house)):
        if house[i] >= input:
            return i


if __name__ == "__main__":
    input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()
    print(part_one(input))  # 786240
    print(part_two(input))  # 831600
