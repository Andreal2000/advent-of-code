import os
import re


def part_one(input):
    return min(re.findall(r'[a-z]+', input), key=input.count)


def part_two(input):
    root = part_one(input)
    input = input.replace(",", "").strip().splitlines()
    programs = {i[0]: [int(i[1][1:-1])] + i[3:] for i in map(str.split, input)}

    def get_weight(name):
        weights = list(map(get_weight, programs[name][1:]))
        wrong = sum(i[1] for i in weights)
        weights = [i[0] for i in weights]

        if len(set(weights)) > 1 and wrong == 0:
            balanced = max(weights, key=weights.count)
            unbalanced = min(weights, key=weights.count)
            name_unbalanced = programs[name][weights.index(unbalanced)+1]
            wrong = programs[name_unbalanced][0] + (balanced - unbalanced)

        return programs[name][0] + sum(weights), wrong

    return get_weight(root)[1]


if __name__ == "__main__":
    input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()
    print(part_one(input))  # azqje
    print(part_two(input))  # 646
