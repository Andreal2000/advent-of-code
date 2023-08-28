import os


def part_one(input):
    input = [list(map(int, i.split(": "))) for i in input.strip().splitlines()]
    return sum(i[0]*i[1] for i in input if not i[0] % (2*i[1]-2))


def part_two(input):
    input = [list(map(int, i.split(": "))) for i in input.strip().splitlines()]
    delay = 0

    while True:
        for i in input:
            if not (i[0]+delay) % (2*i[1]-2):
                break
            if i == input[-1]:
                return delay
        delay += 1


if __name__ == "__main__":
    input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()
    print(part_one(input))  # 2384
    print(part_two(input))  # 3921270
