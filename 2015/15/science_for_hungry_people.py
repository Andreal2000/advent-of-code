import os
from functools import reduce
from operator import mul


def generate_ratios(ingredients):
    teaspoons = 100
    ratios = []

    def generate_ratios_helper(ingredients, r=[]):
        if ingredients == 1:
            ratios.append(r + [teaspoons - sum(r)])
        else:
            for i in range(0, teaspoons + 1 - sum(r)):
                generate_ratios_helper(ingredients-1, r + [i])

    generate_ratios_helper(ingredients)

    return ratios


def part_one(input):
    input = [i.split() for i in input.replace(",", "").strip().splitlines()]
    input = [[int(i[j]) for j in range(2, 9, 2)] for i in input]

    def score(ratio):
        score = [0]*len(input[0])
        for i in range(len(score)):
            for x in range(len(input)):
                score[i] += ratio[x] * input[x][i]
            if score[i] <= 0:
                return 0
        return reduce(mul, score)

    return max(map(score, generate_ratios(len(input))))


def part_two(input):
    input = [i.split() for i in input.replace(",", "").strip().splitlines()]
    input = [[int(i[j]) for j in range(2, 11, 2)] for i in input]

    def score(ratio):
        score = [0]*len(input[0])
        for i in range(len(score)):
            for x in range(len(input)):
                score[i] += ratio[x] * input[x][i]
            if score[i] <= 0:
                return 0
        return reduce(mul, score[:-1]) if score[-1] == 500 else 0

    return max(map(score, generate_ratios(len(input))))


if __name__ == "__main__":
    input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()
    print(part_one(input))  # 18965440
    print(part_two(input))  # 15862900
