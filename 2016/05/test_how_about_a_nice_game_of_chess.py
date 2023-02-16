import os
from how_about_a_nice_game_of_chess import part_one, part_two

input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()


def test_part_one():
    assert part_one(input) == "d4cd2ee1"


def test_part_two():
    assert part_two(input) == "f2c730e5"
