import os


def look_and_say(input, times):
    for _ in range(times):
        n = 1
        out = ""
        for i in range(1, len(input)):
            if input[i-1] != input[i]:
                out += str(n) + input[i-1]
                n = 1
            else:
                n += 1
        input = out + str(n) + input[-1]

    return len(input)


def part_one(input):
    return look_and_say(input, 40)


def part_two(input):
    return look_and_say(input, 50)


if __name__ == "__main__":
    input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()
    print(part_one(input))  # 329356
    print(part_two(input))  # 4666278
