import os
from doesnt_he_have_intern_elves_for_this import part_one, part_two


input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()


def test_part_one():
    assert part_one(input) == 255


def test_part_two():
    assert part_two(input) == 55
