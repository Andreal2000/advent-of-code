import os
from functools import reduce
from itertools import groupby
from operator import mul


def balance(input, target=[]):
    def find_ready(microchips):
        grouped = groupby(sorted(microchips), key=lambda x: x[0])
        return [i for i in
                [(k, sorted([i[-1] for i in g])) for k, g in grouped]
                if len(i[1]) == 2]

    input = [i.split() for i in input.strip().splitlines()]
    bots = {" ".join(i[:2]): (" ".join(i[5:7]), " ".join(i[10:12]))
            for i in input if len(i) == 12}
    microchips = [(" ".join(i[4:6]), int(i[1])) for i in input if len(i) == 6]

    ready = find_ready(microchips)
    while ready != []:
        for r in ready:
            if target != [] and r[1] == sorted(target):
                return int(r[0].split()[1])

            [microchips.remove(x) for x in list(zip([r[0]] * 2, r[1]))]
            [microchips.append(x) for x in list(zip(bots[r[0]], r[1]))]

        ready = find_ready(microchips)

    return microchips


def part_one(input):
    return balance(input, target=[61, 17])


def part_two(input):
    return reduce(mul, [i[1] for i in balance(input)
                        if i[0] in [f"output {r}" for r in range(3)]])


if __name__ == "__main__":
    input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()
    print(part_one(input))  # 27
    print(part_two(input))  # 13727
