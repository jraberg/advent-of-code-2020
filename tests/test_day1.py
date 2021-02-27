from functools import reduce

from aoc.day1 import read_data, solve_day1_part1, solve_day1_part2


def test_valid_result_part1() -> None:
    expenses = read_data()
    solution = reduce(lambda a, b: a * b, solve_day1_part1(expenses))
    assert solution == 712075


def test_valid_result_part2() -> None:
    expenses = read_data()
    solution = reduce(lambda a, b: a * b, solve_day1_part2(expenses))
    assert solution == 145245270
