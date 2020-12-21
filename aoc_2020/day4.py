from __future__ import annotations

import os
import re
from typing import Dict, List

Passport = Dict[str, str]
REQUIRED_FIELDS = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

def parse(raw: str) -> Passport:
    lines = raw.strip().split('\n')
    lines = [line.strip() for line in lines if line.strip()]

    # return dict([tuple(cunck.split(':')) for line in lines for cunck in line.split(' ')])
    passport = {}
    for line in lines:
        for record in line.split(' '):
            key, value = record.split(':')
            passport[key] = value
    return passport


def parse_raw(raw: str) -> List[Passport]:
    passports = [parse(passport) for passport in raw.split('\n\n') if passport.strip()]
    return passports


def has_required_fields(passport: Passport) -> bool:
    return REQUIRED_FIELDS.issubset(passport.keys())


def read_data() -> str:
    passports_file = os.path.join('..','data', 'day4alt.txt')
    lines: List[str]
    with open(passports_file) as file:
        return file.read()


def valid_height(height: str):
    if height.endswith('cm'):
        hgt = height.replace('cm', '')
        try:
            return 150 <= int(hgt) <= 190
        except:
            return False
    elif height.endswith('in'):
        hgt = height.replace('in', '')
        try:
            return 59 <= int(hgt) <= 76
        except:
            return False
    return False


def is_valid_passport(p: Passport):
    return all([
        has_required_fields(p),
        1920 <= int(p.get('byr', -1)) <= 2002,
        2010 <= int(p.get('iyr', -1)) <= 2020,
        2020 <= int(p.get('eyr', -1)) <= 2030,
        valid_height(p.get('hgt', '')),
        re.match(r'^#[0-9a-f]{6}$', p.get('hcl', '')),
        p.get('ecl') in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
        re.match(r'^[0-9]{9}$', p.get('pid', ''))
    ])


if __name__ == '__main__':
    print(sum([has_required_fields(p) for p in parse_raw(read_data())]))
    print(sum([is_valid_passport(p) for p in parse_raw(read_data())]))
