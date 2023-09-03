import os


def part_one(input):
    step = int(input.strip())
    buffer = [0]
    position = 0

    for i in range(1, 2018):
        buffer.insert(((position + step) % i)+1, i)
        position = buffer.index(i)

    return buffer[(position+1) % len(buffer)]


def part_two(input):
    step = int(input.strip())
    position = 0
    output = 0

    for i in range(1, (5*10**7)+1):
        position = ((position + step) % i)+1
        if (position == 1):
            output = i

    return output


if __name__ == "__main__":
    input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()
    print(part_one(input))  # 866
    print(part_two(input))  # 11995607
