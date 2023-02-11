import os

moves = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}


def part_one(input):
    input = input.strip().splitlines()
    current = (1, 1)
    output = ""
    for i in input:
        for c in i:
            next = tuple(map(sum, zip(current, moves[c])))
            if all([0 <= next[i] <= 2 for i in range(2)]):
                current = next
        output += str(current[0]*3 + current[1] + 1)

    return output


def part_two(input):
    keypad = [["0", "0", "1", "0", "0"],
              ["0", "2", "3", "4", "0"],
              ["5", "6", "7", "8", "9"],
              ["0", "A", "B", "C", "0"],
              ["0", "0", "D", "0", "0"]]

    input = input.strip().splitlines()
    current = (2, 0)
    output = ""
    for i in input:
        for c in i:
            next = tuple(map(sum, zip(current, moves[c])))
            if (all([0 <= next[i] <= 4 for i in range(2)]) and
                    keypad[next[0]][next[1]] != "0"):
                current = next
        output += keypad[current[0]][current[1]]

    return output


if __name__ == "__main__":
    input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()
    print(part_one(input))  # 14894
    print(part_two(input))  # 26B96
