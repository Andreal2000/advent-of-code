import os

target = {"children": 3,
          "cats": 7,
          "samoyeds": 2,
          "pomeranians": 3,
          "akitas": 0,
          "vizslas": 0,
          "goldfish": 5,
          "trees": 3,
          "cars": 2,
          "perfumes": 1}


def part_one(input):
    input = input.replace(":", "").replace(",", "").splitlines()

    for i in input:
        i = i.split()
        if (all([target[i[x*2]] == int(i[x*2+1]) for x in range(1, 4)])):
            return int(i[1])


def part_two(input):
    input = input.replace(":", "").replace(",", "").splitlines()

    for i in input:
        i = i.split()
        out = [False]*3
        for x in range(1, 4):
            if i[x*2] in ["cats", "trees"]:
                out[x-1] = target[i[x*2]] < int(i[x*2+1])
            elif i[x*2] in ["pomeranians", "goldfish"]:
                out[x-1] = target[i[x*2]] > int(i[x*2+1])
            else:
                out[x-1] = target[i[x*2]] == int(i[x*2+1])
        if (all(out)):
            return int(i[1])


if __name__ == "__main__":
    input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()
    print(part_one(input))  # 40
    print(part_two(input))  # 241
