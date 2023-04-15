import os


def rogue(input, rows=40):
    tiles = [input.strip()]
    while len(tiles) < rows:
        current = f".{tiles[-1]}."
        next = ""
        for i in range(1, len(current) - 1):
            next += ".^"[current[i-1:i+2] in ["^^.", ".^^", "^..", "..^"]]
        tiles += [next]
    return "".join(tiles).count(".")


def part_one(input):
    return rogue(input)


def part_two(input):
    return rogue(input, rows=400000)


if __name__ == "__main__":
    input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()
    print(part_one(input))  # 1989
    print(part_two(input))  # 19999894
