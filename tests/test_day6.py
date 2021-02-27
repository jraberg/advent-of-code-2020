from aoc.day6 import read_data, solve_day6_p1, solve_day6_p2


def test_valid_result_part1() -> None:
    solution = solve_day6_p1(read_data("day6.txt"))
    assert solution == 6504


def test_valid_result_part2() -> None:
    solution = solve_day6_p2(read_data("day6.txt"))
    assert solution == 3351
