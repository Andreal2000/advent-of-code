import os
import re


def part_one(input):
    def abba(input):
        for i in range(1, len(input)-2):
            if input[i] == input[i+1] and \
               input[i-1] == input[i+2] and \
               input[i-1] != input[i]:
                return True
        return False

    input = input.strip().splitlines()
    input = [i for i in input
             if not any([abba(j) for j in re.findall(r"\[.*?\]", i)])]
    input = [any([abba(j) for j in re.split(r"\[.*?\]", i)]) for i in input]

    return sum(input)


def part_two(input):
    def ssl(input):
        supernet = " ".join(re.split(r"\[.*?\]", input))
        hypernet = "".join(re.findall(r"\[.*?\]", input))
        for s in range(1, len(supernet)-1):
            if supernet[s-1] == supernet[s+1] and \
               supernet[s] != supernet[s-1] and \
               supernet[s:s+2] + supernet[s] in hypernet:
                return True
        return False

    return sum(map(ssl, input.strip().splitlines()))


if __name__ == "__main__":
    input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()
    print(part_one(input))  # 105
    print(part_two(input))  # 258
