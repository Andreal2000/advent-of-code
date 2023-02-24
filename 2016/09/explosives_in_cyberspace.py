import os


def decompress(input, version=1):
    output = 0
    i = 0
    while i < len(input):
        if input[i] == "(":
            repeat = list(map(int, input[i+1:input.index(")", i)].split("x")))
            i += len(str(repeat)) - 1

            if version == 2:
                decompressed = decompress(input[i: i+repeat[0]], version=2)
            else:
                decompressed = repeat[0]

            output += decompressed * repeat[1]
            i += repeat[0]
        else:
            output += 1
            i += 1

    return output


def part_one(input):
    return decompress(input.strip())


def part_two(input):
    return decompress(input.strip(), version=2)


if __name__ == "__main__":
    input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()
    print(part_one(input))  # 115118
    print(part_two(input))  # 11107527530
