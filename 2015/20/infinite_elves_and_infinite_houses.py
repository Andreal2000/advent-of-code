import os


def find_house(input, houses):
    for i in range(len(houses)):
        if houses[i] >= input:
            return i


def part_one(input):
    input = int(input)
    houses = [0] * (input//10+1)

    for i in range(1, input//10+1):
        for j in range(i, input//10+1, i):
            houses[j] += i*10

    return find_house(input, houses)


def part_two(input):
    input = int(input)
    houses = [0] * (input//11+1)

    for i in range(1, input//10+1):
        for j in range(i, i*50+1 if i*50+1 < len(houses) else len(houses), i):
            houses[j] += i*11

    return find_house(input, houses)


if __name__ == "__main__":
    input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()
    print(part_one(input))  # 786240
    print(part_two(input))  # 831600
