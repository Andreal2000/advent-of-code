import os
from no_time_for_a_taxicab import part_one, part_two

input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()


def test_part_one():
    assert part_one(input) == 353


def test_part_two():
    assert part_two(input) == 152
