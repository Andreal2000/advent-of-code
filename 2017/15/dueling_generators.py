import os


def judge(input, pairs, criteria=(1, 1)):
    def generator(factor, previous, criteria=1):
        while True:
            previous = (previous * factor) % 2147483647
            if previous % criteria == 0:
                yield previous & 0xffff

    factors = (16807, 48271)
    previous = [int(i.split()[-1]) for i in input.strip().splitlines()]
    a, b = [generator(factors[i], previous[i], criteria[i]) for i in range(2)]

    return sum(next(a) == next(b) for _ in range(pairs))


def part_one(input):
    return judge(input, 4*10**7)


def part_two(input):
    return judge(input, 5*10**6, (4, 8))


if __name__ == "__main__":
    input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()
    print(part_one(input))  # 619
    print(part_two(input))  # 290
