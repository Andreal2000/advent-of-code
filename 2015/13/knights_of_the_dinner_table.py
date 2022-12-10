import os
from itertools import permutations


def part_one(input):
    input = [y.split() for y in input.replace(".", "").strip().split("\n")]
    persons = sorted(list({i[x] for i in input for x in [0, 10]}))
    matrix = [[0]*len(persons) for _ in range(len(persons))]

    for i in input:
        x = persons.index(i[0])
        y = persons.index(i[10])
        v = matrix[x][y] + int(i[3]) * (-1 if i[2] == "lose" else 1)
        matrix[x][y] = matrix[y][x] = v

    return max([sum([matrix[p[i]][p[(i+1) % len(p)]]for i in range(len(p))])
                for p in permutations(range(len(persons))) if p < p[::-1]])


def part_two(input):
    text = [y.split() for y in input.replace(".", "").strip().split("\n")]
    persons = sorted(list({i[x] for i in text for x in [0, 10]}))
    template = "{} would gain 0 happiness units by sitting next to {}.\n"
    args = list(zip(["Andrea"] * len(persons), persons)) + \
        list(zip(persons, ["Andrea"] * len(persons)))
    me = (template*(len(persons))*2).format(*[x for y in args for x in y])
    return part_one(input + me)


if __name__ == "__main__":
    input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()
    print(part_one(input))  # 664
    print(part_two(input))  # 640
