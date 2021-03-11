from aoc.day8 import solve_day8_p1, read_data, solve_day8_p2, parse_data


def test_basic_part1():
    solution = solve_day8_p1(parse_data(data))
    assert solution == 5


def test_basic_part2():
    solution = solve_day8_p2(parse_data(data))
    assert solution == 8


def test_day8_part1():
    solution = solve_day8_p1(read_data("day8.txt"))
    assert solution == 1684


data = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""
