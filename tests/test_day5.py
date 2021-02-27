from aoc.day5 import parse_column, parse_row, read_data, solve_day5_p1, solve_day5_p2


def test_parse_row() -> None:
    assert parse_row("FBFBBFFRLR"[:-3]) == 44
    assert parse_row("BFFFBBFRRR"[:-3]) == 70
    assert parse_row("FFFBBBFRRR"[:-3]) == 14
    assert parse_row("BBFFBBFRLL"[:-3]) == 102


def test_parse_column() -> None:
    assert parse_column("FBFBBFFRLR"[-3:]) == 5
    assert parse_column("BFFFBBFRRR"[-3:]) == 7
    assert parse_column("FFFBBBFRRR"[-3:]) == 7
    assert parse_column("BBFFBBFRLL"[-3:]) == 4


def test_valid_result_part1() -> None:
    solution = solve_day5_p1(read_data("day5.txt"))
    assert solution == 978


def test_valid_result_part2() -> None:
    solution = solve_day5_p2(read_data("day5.txt"))
    assert solution == 727
