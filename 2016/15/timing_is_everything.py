import os


def kinetic_sculpture(input):
    input = input.replace(".", "").strip()
    input = [(i[3], i[-1]) for i in map(str.split, input.splitlines())]
    input = [list(map(int, i)) for i in input]
    discs = [i[1] for i in input]
    solution = [-(i+1) % input[i][0] for i in range(len(input))]
    time = 0

    while discs != solution:
        discs = [(discs[i]+1) % input[i][0] for i in range(len(input))]
        time += 1

    return time


def part_one(input):
    return kinetic_sculpture(input)


def part_two(input):
    input += "Disc #7 has 11 positions; at time=0, it is at position 0.\n"
    return kinetic_sculpture(input)


if __name__ == "__main__":
    input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()
    print(part_one(input))  # 317371
    print(part_two(input))  # 2080951
