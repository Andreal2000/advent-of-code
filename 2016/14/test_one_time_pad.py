import os
from one_time_pad import part_one, part_two

input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()


def test_part_one():
    assert part_one(input) == 25427


def test_part_two():
    assert part_two(input) == 22045
