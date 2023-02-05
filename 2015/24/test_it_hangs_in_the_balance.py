import os
from it_hangs_in_the_balance import part_one, part_two


input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()


def test_part_one():
    assert part_one(input) == 11846773891


def test_part_two():
    assert part_two(input) == 80393059
