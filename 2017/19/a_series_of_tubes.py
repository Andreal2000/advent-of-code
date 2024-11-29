import os
import re


def add(a, b):
    return tuple(map(sum, zip(a, b)))


def diagram(input, part_two=False):
    input = input.splitlines()
    position = (0, input[0].index("|"))
    direction = (1, 0)
    letters = ""
    steps = -1

    while True:
        current = input[position[0]][position[1]]
        steps += 1
        if current in ["|", "-"]:
            position = add(position, direction)
        elif current == "+":
            next_direction = tuple(reversed(direction))
            next_position = add(position, next_direction)
            next = input[next_position[0]][next_position[1]]
            if re.match("[\w|-]", next):
                direction = next_direction
                position = next_position
            else:
                direction = tuple(-i for i in next_direction)
                position = add(position, direction)
        elif current.isalpha():
            letters += current
            position = add(position, direction)
        else:
            return steps if part_two else letters


def part_one(input):
    return diagram(input)


def part_two(input):
    return diagram(input, part_two=True)


if __name__ == "__main__":
    input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()
    print(part_one(input))  # AYRPVMEGQ
    print(part_two(input))  # 16408
