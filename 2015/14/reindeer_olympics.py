import os


def part_one(input):
    input = [y.split() for y in input.strip().split("\n")]

    def distance(deer):
        seconds = 2503
        v = int(deer[3])
        t = int(deer[6])
        r = int(deer[-2])
        start = ((seconds // (t+r)))
        start_distance = start * (v*t)
        end = seconds - (start * (t+r))
        end_distance = min(t, end) * v
        return start_distance + end_distance

    return max(map(distance, input))


def part_two(input):
    input = [y.split() for y in input.strip().split("\n")]
    seconds = 2503
    matrix = []
    scores = [0 for _ in range(len(input))]
    for deer in input:
        v = int(deer[3])
        t = int(deer[6])
        r = int(deer[-2])
        position = []
        while len(position) <= seconds:
            for _ in range(t):
                position += [(position[-1] if len(position) > 0 else 0) + v]
            position += [position[-1]]*r
        matrix += [position]

    matrix = matrix[:seconds]

    for i in range(seconds):
        first = max([x[i] for x in matrix])
        for x in range(len(matrix)):
            if matrix[x][i] == first:
                scores[x] += 1

    return max(scores)


if __name__ == "__main__":
    input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()
    print(part_one(input))  # 2660
    print(part_two(input))  # 1256
