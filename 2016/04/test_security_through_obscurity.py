import os
from security_through_obscurity import part_one, part_two

input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()


def test_part_one():
    assert part_one(input) == 361724


def test_part_two():
    assert part_two(input) == 482
