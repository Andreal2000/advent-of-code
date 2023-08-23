import os
from spiral_memory import part_one, part_two

input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()


def test_part_one():
    assert part_one(input) == 552


def test_part_two():
    assert part_two(input) == 330785
