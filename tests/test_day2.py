from aoc.day2 import Password, read_data

PASSWORDS = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]


def test_is_valid() -> None:
    assert Password.parse(PASSWORDS[0]).is_valid()
    assert not Password.parse(PASSWORDS[1]).is_valid()
    assert Password.parse(PASSWORDS[2]).is_valid()


def test_is_valid2() -> None:
    assert Password.parse(PASSWORDS[0]).is_valid2()
    assert not Password.parse(PASSWORDS[1]).is_valid2()
    assert not Password.parse(PASSWORDS[2]).is_valid2()


def test_valid_result_part1() -> None:
    passwords = read_data()
    solution = sum(p.is_valid() for p in passwords)
    assert solution == 447


def test_valid_result_part2() -> None:
    passwords = read_data()
    solution = sum(p.is_valid2() for p in passwords)
    assert solution == 249
