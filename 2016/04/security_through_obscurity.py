import os


def part_one(input):
    input = [i for i in input.strip().splitlines()]
    input = list(map(lambda x: x.split("-"), input))
    input = [("".join(i[:-1]), int(i[-1][:-7]), i[-1][-6:-1]) for i in input]

    def check(args):
        name, sector, checksum = args
        letters = {}
        for i in name:
            letters.setdefault(i, 0)
            letters.update({i: letters.get(i) - 1})

        output = [i[0] for i in sorted(letters.items(), key=lambda x: x[::-1])]

        return sector if "".join(output[:5]) == checksum else 0

    return sum(map(check, input))


def part_two(input):
    input = [i for i in input.strip().splitlines()]
    input = [(i[:-11].split("-"), int(i[-10:-7])) for i in input]
    target = "north"

    def shift(word, sector):
        return "".join([chr((ord(ch) + sector - 97) % 26 + 97) for ch in word])

    for i in input:
        if " ".join([shift(word, i[1]) for word in i[0]]).startswith(target):
            return i[1]


if __name__ == "__main__":
    input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()
    print(part_one(input))  # 361724
    print(part_two(input))  # 482
