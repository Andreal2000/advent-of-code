import os
from knot_hash import part_one, part_two

input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()


def test_part_one():
    assert part_one(input) == 11413


def test_part_two():
    assert part_two(input) == "7adfd64c2a03a4968cf708d1b7fd418d"
