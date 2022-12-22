import os
from itertools import product


def part_one(input):
    weapons = list(zip([8, 10, 25, 40, 74], range(4, 9), [0]*5))
    armors = list(zip([0, 13, 31, 53, 75, 102], [0]*6, range(6)))
    rings = list(zip([0, 25, 50, 100, 20, 40, 80],
                     [0, 1, 2, 3, 0, 0, 0],
                     [0, 0, 0, 0, 1, 2, 3]))

    items = list(product(weapons, armors, rings, rings))

    boss = [int(i.split()[-1]) for i in input.strip().split("\n")]
    m = 74+102+100+80

    for i in [[sum(z) for z in zip(*i)]
              for i in items
              if (i[2] != i[3] or sum(i[2]) == 0 or sum(i[3]) == 0)]:
        me_dmg = max(i[1] - boss[2], 1)
        boss_dmg = max(boss[1] - i[2], 1)
        if boss[0] // me_dmg <= 100 // boss_dmg:
            m = min(m, i[0])

    return m


def part_two(input):
    weapons = list(zip([8, 10, 25, 40, 74], range(4, 9), [0]*5))
    armors = list(zip([0, 13, 31, 53, 75, 102], [0]*6, range(6)))
    rings = list(zip([0, 25, 50, 100, 20, 40, 80],
                     [0, 1, 2, 3, 0, 0, 0],
                     [0, 0, 0, 0, 1, 2, 3]))

    items = list(product(weapons, armors, rings, rings))

    boss = [int(i.split()[-1]) for i in input.strip().split("\n")]
    m = 0

    for i in [[sum(z) for z in zip(*i)]
              for i in items
              if (i[2] != i[3] or sum(i[2]) == 0 or sum(i[3]) == 0)]:
        me_dmg = max(i[1] - boss[2], 1)
        boss_dmg = max(boss[1] - i[2], 1)
        if boss[0] // me_dmg > 100 // boss_dmg:
            m = max(m, i[0])

    return m


if __name__ == "__main__":
    input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()
    print(part_one(input))  # 91
    print(part_two(input))  # 158
