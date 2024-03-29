import os
from like_a_rogue import part_one, part_two

input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()


def test_part_one():
    assert part_one(input) == 1989


def test_part_two():
    assert part_two(input) == 19999894
