import os
import re


def part_one(input):
    input = re.sub(r'!.', "", input)
    input = re.sub(r'<.*?>', "", input)
    input = input.replace(",", "")

    total_score = score = 0

    for i in input:
        if i == "{":
            score += 1
        elif i == "}":
            total_score += score
            score -= 1

    return total_score


def part_two(input):
    input = re.sub(r'!.', "", input)
    input = re.findall(r'<.*?>', input)
    return sum(len(i)-2 for i in input)


if __name__ == "__main__":
    input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()
    print(part_one(input))  # 15922
    print(part_two(input))  # 7314
