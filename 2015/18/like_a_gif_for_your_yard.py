import os
import copy


def part_one(input):
    input = ([[False]*102] +
             [[False] + [c == "#" for c in i] + [0]
             for i in input.strip().split("\n")] +
             [[False]*102])

    tmp = copy.deepcopy(input)
    for _ in range(100):
        for x in range(1, 101):
            for y in range(1, 101):
                neighbors = sum(input[x-1][y-1:y+2] +
                                input[x][y-1:y+2:2] +
                                input[x+1][y-1:y+2])

                if input[x][y]:
                    tmp[x][y] = neighbors in [2, 3]
                else:
                    tmp[x][y] = neighbors == 3

        input = copy.deepcopy(tmp)

    return sum([x for y in input for x in y])


def part_two(input):
    input = ([[False]*102] +
             [[False] + [c == "#" for c in i] + [0]
             for i in input.strip().split("\n")] +
             [[False]*102])

    for x in [1, 100]:
        for y in [1, 100]:
            input[x][y] = True

    tmp = copy.deepcopy(input)
    for _ in range(100):
        for x in range(1, 101):
            for y in range(1, 101):
                if not (x in [1, 100] and y in [1, 100]):
                    neighbors = sum(input[x-1][y-1:y+2] +
                                    input[x][y-1:y+2:2] +
                                    input[x+1][y-1:y+2])

                    if input[x][y]:
                        tmp[x][y] = neighbors in [2, 3]
                    else:
                        tmp[x][y] = neighbors == 3

        input = copy.deepcopy(tmp)

    return sum([x for y in input for x in y])


if __name__ == "__main__":
    input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()
    print(part_one(input))  # 821
    print(part_two(input))  # 886
