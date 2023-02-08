import os
from like_a_gif_for_your_yard import part_one, part_two

input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()


def test_part_one():
    assert part_one(input) == 821


def test_part_two():
    assert part_two(input) == 886
