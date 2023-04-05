import os
from dragon_checksum import part_one, part_two

input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()


def test_part_one():
    assert part_one(input) == "11111000111110000"


def test_part_two():
    assert part_two(input) == "10111100110110100"
