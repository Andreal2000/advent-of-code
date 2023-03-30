import os
import re
from itertools import combinations, groupby


def part_one(input):
    def is_valid_state(floor):
        return (len(set(type for _, type in floor)) < 2 or
                all((obj, 'generator') in floor
                    for (obj, type) in floor
                    if type == 'microchip'))

    def next_states(state):
        moves, elevator, floors = state

        possible_moves = (*combinations(floors[elevator], 2),
                          *combinations(floors[elevator], 1))

        for move in possible_moves:
            for direction in [-1, 1]:
                next_elevator = elevator + direction
                if not 0 <= next_elevator < len(floors):
                    continue

                next_floors = floors.copy()
                next_floors[elevator] = floors[elevator].difference(move)
                next_floors[next_elevator] = floors[next_elevator].union(move)

                if all([is_valid_state(next_floors[i]) for i
                        in [elevator, next_elevator]]):
                    yield (moves + 1, next_elevator, next_floors)

    input = [set(re.findall(r'(\w+)(?:-compatible)? (microchip|generator)', i))
             for i in input.splitlines()]

    seen = set()
    queue = [(0, 0, input)]

    while queue:
        state = queue.pop(0)
        moves, _, floors = state

        if not sum(map(len, floors[:-1])):
            return moves

        for next_state in next_states(state):
            _, elevator, floors = next_state
            key = (elevator,
                   tuple(tuple((k, len(list(g))) for k, g
                               in groupby(type for _, type in floor))
                         for floor in floors))

            if key not in seen:
                seen.add(key)
                queue.append(next_state)


def part_two(input):
    extra_parts = ["An elerium generator.",
                   "An elerium-compatible microchip.",
                   "A dilithium generator.",
                   "A dilithium-compatible microchip."]

    input = input.splitlines()
    input[0] = input[0].strip() + "".join(extra_parts)
    return part_one("\n".join(input))


if __name__ == "__main__":
    input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()
    print(part_one(input))  # 31
    print(part_two(input))  # 55
