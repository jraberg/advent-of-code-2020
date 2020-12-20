from aoc_2020.day4 import parse_raw, has_required_fields, is_valid_passport

P = """
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
"""


INVALID_PASSPORTS = """
eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007
"""

VALID_PASSPORTS = """
pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719
"""

def test_is_valid():
    assert True


def test_parse_raw():
    passports = parse_raw(P)
    assert len(passports) == 4
    assert {'ecl', 'eyr', 'hcl', 'byr', 'iyr', 'cid', 'hgt'}.difference(passports[0].keys()) == set()
    assert {'iyr', 'ecl', 'cid', 'eyr', 'pid', 'hcl', 'byr'}.difference(passports[1].keys()) == set()
    assert {'hcl', 'iyr', 'eyr', 'ecl', 'pid', 'byr', 'hgt'}.difference(passports[2].keys()) == set()
    assert {'hcl', 'eyr', 'pid', 'iyr', 'ecl', 'hgt'}.difference(passports[3].keys()) == set()


def test_passport_has_required_fields():
    passports = parse_raw(P)
    assert has_required_fields(passports[0])
    assert not has_required_fields(passports[1])
    assert has_required_fields(passports[2])
    assert not has_required_fields(passports[3])

def test_passports_valid():
    passports = parse_raw(VALID_PASSPORTS)
    for p in passports:
        assert is_valid_passport(p)


def test_passports_invalid():
    passports = parse_raw(INVALID_PASSPORTS)
    for p in passports:
        assert not is_valid_passport(p)
