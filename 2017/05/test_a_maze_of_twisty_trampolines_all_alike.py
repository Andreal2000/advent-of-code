import os
from a_maze_of_twisty_trampolines_all_alike import part_one, part_two

input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()


def test_part_one():
    assert part_one(input) == 381680


def test_part_two():
    assert part_two(input) == 29717847
