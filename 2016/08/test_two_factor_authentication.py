import os
from two_factor_authentication import part_one, part_two

input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()


def test_part_one():
    assert part_one(input) == 123


def test_part_two():
    output = [" ██  ████ ███  █  █ ███  ████ ███    ██ ███   ███ ",
              "█  █ █    █  █ █  █ █  █    █ █  █    █ █  █ █    ",
              "█  █ ███  ███  █  █ █  █   █  ███     █ █  █ █    ",
              "████ █    █  █ █  █ ███   █   █  █    █ ███   ██  ",
              "█  █ █    █  █ █  █ █    █    █  █ █  █ █       █ ",
              "█  █ █    ███   ██  █    ████ ███   ██  █    ███  "]

    assert part_two(input) == "\n".join(output)
