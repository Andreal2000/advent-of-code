import os
from itertools import permutations


def find_routes(input):
    numbers = []
    for i in [input.index(str(i)) for i in range(8)]:
        row = len(input.splitlines()[0]) + 1
        numbers += [(i//row, i - (row * (i//row)))]

    routes = [[0]*8 for _ in range(8)]
    for k in range(8):
        queue = [numbers[k]]
        steps = -1
        maze = [list(i) for i in input.strip().splitlines()]
        while queue:
            steps += 1
            for _ in range(len(queue)):
                x, y = queue.pop(0)
                if maze[x][y] not in [".", "#"]:
                    routes[k][int(maze[x][y])] = steps

                maze[x][y] = "#"
                for i in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                    next = tuple(map(sum, zip((x, y), i)))
                    if (next not in queue
                            and min(*next) >= 0
                            and next[0] < len(maze)
                            and next[1] < len(maze[0])
                            and maze[next[0]][next[1]] != "#"):
                        queue.append(next)

    return routes


def part_one(input):
    routes = find_routes(input)
    return min([(routes[0][p[0]] +
                sum([routes[p[i]][p[i+1]] for i in range(len(p)-1)]))
                for p in permutations(range(1, 8)) if p < p[::-1]])


def part_two(input):
    routes = find_routes(input)
    return min([(routes[0][p[0]] + routes[p[-1]][0] +
                sum([routes[p[i]][p[i+1]] for i in range(len(p)-1)]))
                for p in permutations(range(1, 8)) if p < p[::-1]])


if __name__ == "__main__":
    input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()
    print(part_one(input))  # 412
    print(part_two(input))  # 664
