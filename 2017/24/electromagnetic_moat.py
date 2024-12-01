import os


def bridges(components, start=0):
    result = []
    for i, component in enumerate(components):
        if start in component:
            next_start = component[0] if component[1] == start else component[1]
            next_components = components[:i] + components[i + 1 :]
            next_bridges = bridges(next_components, next_start)
            if next_bridges:
                for bridge in next_bridges:
                    result.append([component] + bridge)
            else:
                result.append([component])

    return result


def part_one(input):
    input = input.strip().splitlines()
    components = [tuple(map(int, line.split("/"))) for line in input]
    max_strength = 0

    for bridge in bridges(components):
        max_strength = max(max_strength, sum(sum(component) for component in bridge))

    return max_strength


def part_two(input):
    input = input.strip().splitlines()
    components = [tuple(map(int, line.split("/"))) for line in input]
    max_strength = 0
    max_length = 0

    for bridge in bridges(components):
        length = len(bridge)
        strength = sum(sum(component) for component in bridge)
        if length >= max_length:
            max_length = length
            max_strength = max(max_strength, strength)

    return max_strength


if __name__ == "__main__":
    input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()
    print(part_one(input))  # 1511
    print(part_two(input))  # 1471
