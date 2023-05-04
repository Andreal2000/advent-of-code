import os


def part_one(input):
    input = list(map(int, list(input.strip())))
    length = len(input)
    return sum(input[i] for i in range(length)
               if input[i] == input[(i+1) % length])


def part_two(input):
    input = list(map(int, list(input.strip())))
    length = len(input)
    return sum(input[i] for i in range(length)
               if input[i] == input[(i+(length//2)) % length])


if __name__ == "__main__":
    input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()
    print(part_one(input))  # 1097
    print(part_two(input))  # 1188
