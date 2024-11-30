import os
import re
from collections import defaultdict


class particle:
    def __init__(self, id, data) -> None:
        self.id = id
        self.p = data[0:3]
        self.v = data[3:6]
        self.a = data[6:9]

    def __str__(self) -> str:
        p = ",".join(map(str, self.p))
        v = ",".join(map(str, self.v))
        a = ",".join(map(str, self.a))
        return f"{self.id} p=<{p}>, v=<{v}>, a=<{a}>"

    def update(self) -> None:
        for i in range(3):
            self.v[i] += self.a[i]
            self.p[i] += self.v[i]


def simulator(input, part_two=False):
    input = input.strip().splitlines()
    input = [
        particle(i, list(map(int, re.findall("-?\d+", p)))) for i, p in enumerate(input)
    ]

    for _ in range(1000):
        for p in input:
            p.update()

        if part_two:
            pos_dict = defaultdict(list)
            for p in input:
                pos_dict[tuple(p.p)].append(p)

            for _, v in pos_dict.items():
                if len(v) > 1:
                    for p in v:
                        input.remove(p)

    return len(input) if part_two else min(input, key=lambda p: sum(map(abs, p.p))).id


def part_one(input):
    return simulator(input)


def part_two(input):
    return simulator(input, True)


if __name__ == "__main__":
    input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()
    print(part_one(input))  # 344
    print(part_two(input))  # 404
