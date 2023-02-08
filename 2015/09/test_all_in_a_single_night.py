import os
from all_in_a_single_night import part_one, part_two

input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()


def test_part_one():
    assert part_one(input) == 117


def test_part_two():
    assert part_two(input) == 909
