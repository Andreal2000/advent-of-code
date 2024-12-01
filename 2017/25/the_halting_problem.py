import os
import re
from collections import defaultdict


class State:
    def __init__(self, setup):
        self.name = setup[0]

        false_write = int(setup[1])
        false_move = -1 if setup[2] == "left" else 1
        false_next = setup[3]

        true_write = int(setup[4])
        true_move = -1 if setup[5] == "left" else 1
        true_next = setup[6]

        self.instructions = (
            (false_write, false_move, false_next),
            (true_write, true_move, true_next),
        )

    def next_state(self, tape, cursor):
        if tape[cursor] == 0:
            tape[cursor] = self.instructions[0][0]
            cursor += self.instructions[0][1]
            return (self.instructions[0][2], cursor)
        else:
            tape[cursor] = self.instructions[1][0]
            cursor += self.instructions[1][1]
            return (self.instructions[1][2], cursor)


def part_one(input):
    regex = (
        r"In state (.):\n"
        r"  If the current value is 0:\n"
        r"    - Write the value (.)\.\n"
        r"    - Move one slot to the (.+)\.\n"
        r"    - Continue with state (.)\.\n"
        r"  If the current value is 1:\n"
        r"    - Write the value (.)\.\n"
        r"    - Move one slot to the (.*)\.\n"
        r"    - Continue with state (.)\."
    )

    states_setup = re.findall(regex, input)

    input = input.strip().splitlines()
    begin_state = input[0].split()[-1][0]
    steps = int(input[1].split()[-2])

    tape = defaultdict(int)
    cursor = 0
    state = begin_state
    states = {}

    for s in states_setup:
        states[s[0]] = State(s)

    for _ in range(steps):
        state, cursor = states[state].next_state(tape, cursor)

    return sum(tape.values())


if __name__ == "__main__":
    input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()
    print(part_one(input))  # 633
