import os


def two_factor(input):
    def rect(screen, a, b):
        for y in range(b):
            for x in range(a):
                screen[y][x] = True

    def rotate_row(screen, a, b):
        screen[a] = screen[a][-b:] + screen[a][:-b]

    def rotate_column(screen, a, b):
        for _ in range(b):
            prev = screen[-1][a]
            for i in range(6):
                curr = screen[i][a]
                screen[i][a] = prev
                prev = curr

    rotate = {"row": rotate_row, "column": rotate_column}
    screen = [[False] * 50 for _ in range(6)]
    input = [i.split() for i in input.strip().splitlines()]

    for i in input:
        if len(i) == 2:
            i = i[1].split("x")
            rect(screen, int(i[0]), int(i[1]))
        else:
            rotate[i[1]](screen, int(i[2][2:]), int(i[4]))

    return screen


def part_one(input):
    screen = two_factor(input)
    return sum([a for b in screen for a in b])


def part_two(input):
    screen = two_factor(input)
    translate = {False: " ", True: "█"}
    screen = "\n".join([''.join([translate[i] for i in r]) for r in screen])
    return screen


if __name__ == "__main__":
    input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()
    print(part_one(input))  # 123
    print(part_two(input))  # AFBUPZBJPS
