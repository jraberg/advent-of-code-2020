from aoc_2020.day2 import Password

PASSWORDS = [
    '1-3 a: abcde',
    '1-3 b: cdefg',
    '2-9 c: ccccccccc']


def test_is_valid():
    assert Password.parse(PASSWORDS[0]).is_valid()
    assert not Password.parse(PASSWORDS[1]).is_valid()
    assert Password.parse(PASSWORDS[2]).is_valid()


def test_is_valid2():
    assert Password.parse(PASSWORDS[0]).is_valid2()
    assert not Password.parse(PASSWORDS[1]).is_valid2()
    assert not Password.parse(PASSWORDS[2]).is_valid2()
