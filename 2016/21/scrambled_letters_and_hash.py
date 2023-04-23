import os
import re


def scrambler(input, password, undo=False):
    input = input.strip().splitlines()
    input = input[::-1] if undo else input
    password = list(password)

    for i in input:
        if args := re.findall(r"swap position (.) with position (.)", i):
            args = list(map(int, args[0]))
            temp = password[args[0]]
            password[args[0]] = password[args[1]]
            password[args[1]] = temp
        elif args := re.findall(r"swap letter (.) with letter (.)", i):
            args = [password.index(i) for i in args[0]]
            temp = password[args[0]]
            password[args[0]] = password[args[1]]
            password[args[1]] = temp
        elif args := re.findall(r"rotate (left|right) (.) step.?", i):
            args = [args[0][0], int(args[0][1])]
            rotate = args[1] if (args[0] == "left") ^ undo else -args[1]
            password = password[rotate:] + password[:rotate]
        elif args := re.findall(r"rotate based on position of letter (.)", i):
            index = password.index(args[0])
            if undo:
                rotate = index//2 + (1 if index % 2 == 1 or index == 0 else 5)
            else:
                rotate = - (index + (2 if index >= 4 else 1))
            password = password[rotate:] + password[:rotate]
        elif args := re.findall(r"reverse positions (.) through (.)", i):
            args = list(map(int, args[0]))
            password = (password[:args[0]] +
                        password[args[0]:args[1] + 1][::-1] +
                        password[args[1] + 1:])
        elif args := re.findall(r"move position (.) to position (.)", i):
            args = list(map(int, args[0]))
            args = args[::-1] if undo else args
            password.insert(args[1], password.pop(args[0]))

    return "".join(password)


def part_one(input):
    return scrambler(input, "abcdefgh")


def part_two(input):
    return scrambler(input, "fbgdceah", undo=True)


if __name__ == "__main__":
    input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()
    print(part_one(input))  # bfheacgd
    print(part_two(input))  # gcehdbfa
