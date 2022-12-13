import os
from functools import reduce


def part_one(input):
    input = [i.split() for i in input.replace(",", "").strip().split("\n")]
    input = [[int(i[2]), int(i[4]), int(i[6]), int(i[8])]
             for i in input]
    teaspoons = 100
    ratios = []

    def generate_ratios(ingredients, r=[]):
        if ingredients == 1:
            ratios.append(r + [teaspoons - sum(r)])
        else:
            for i in range(0, teaspoons + 1 - sum(r)):
                generate_ratios(ingredients-1, r + [i])

    generate_ratios(len(input))

    def score(ratio):
        score = [0]*len(input[0])
        for i in range(len(score)):
            for x in range(len(input)):
                score[i] += ratio[x] * input[x][i]
            if score[i] <= 0:
                return 0
        return reduce(lambda x, y: x*y, score)

    return max(map(score, ratios))


def part_two(input):
    input = [i.split() for i in input.replace(",", "").strip().split("\n")]
    input = [[int(i[2]), int(i[4]), int(i[6]), int(i[8]), int(i[10])]
             for i in input]
    teaspoons = 100
    ratios = []

    def generate_ratios(ingredients, r=[]):
        if ingredients == 1:
            ratios.append(r + [teaspoons - sum(r)])
        else:
            for i in range(0, teaspoons + 1 - sum(r)):
                generate_ratios(ingredients-1, r + [i])

    generate_ratios(len(input))

    def score(ratio):
        score = [0]*len(input[0])
        for i in range(len(score)):
            for x in range(len(input)):
                score[i] += ratio[x] * input[x][i]
            if score[i] <= 0:
                return 0
        return reduce(lambda x, y: x*y, score[:-1]) if score[-1] == 500 else 0

    return max(map(score, ratios))


if __name__ == "__main__":
    input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()
    print(part_one(input))  # 18965440
    print(part_two(input))  # 15862900
