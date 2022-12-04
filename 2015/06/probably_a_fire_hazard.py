import os


def part_one(input):
    matrix = [[False]*1000 for i in range(1000)]
    def turn_on(i): return True
    def turn_off(i): return False
    def toggle(i): return not i

    operations = {"on": turn_on, "off": turn_off, "toggle": toggle}

    for i in input.strip().split("\n"):
        i = i.split(" ")
        o = i[-4]
        a = i[-3].split(",")
        b = i[-1].split(",")

        for x in range(int(a[0]), int(b[0])+1):
            for y in range(int(a[1]), int(b[1])+1):
                matrix[x][y] = operations[o](matrix[x][y])

    return sum([x for y in matrix for x in y])


def part_two(input):
    matrix = [[0]*1000 for i in range(1000)]
    def turn_on(i): return i+1
    def turn_off(i): return i-1 if i > 0 else 0
    def toggle(i): return i+2

    operations = {"on": turn_on, "off": turn_off, "toggle": toggle}

    for i in input.strip().split("\n"):
        i = i.split(" ")
        o = i[-4]
        a = i[-3].split(",")
        b = i[-1].split(",")

        for x in range(int(a[0]), int(b[0])+1):
            for y in range(int(a[1]), int(b[1])+1):
                matrix[x][y] = operations[o](matrix[x][y])

    return sum([x for y in matrix for x in y])


if __name__ == "__main__":
    input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()
    print(part_one(input))  # 377891
    print(part_two(input))  # 14110788
