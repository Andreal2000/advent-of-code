import os
from i_was_told_there_would_be_no_math import part_one, part_two


input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()


def test_part_one():
    assert part_one(input) == 1586300


def test_part_two():
    assert part_two(input) == 3737498
