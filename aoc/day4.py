from __future__ import annotations

import os
import re
from typing import Dict, List

Passport = Dict[str, str]
REQUIRED_FIELDS = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}


def read_data(filename: str) -> str:
    passports_file = os.path.join("..", "inputs", filename)
    with open(passports_file) as file:
        return file.read()


def parse_data(raw: str) -> List[Passport]:
    raw_passports = [p.strip().replace("\n", " ").split(" ") for p in raw.split("\n\n") if p.strip()]
    return [dict(zip([k.split(":")[0] for k in p], [v.split(":")[1] for v in p])) for p in raw_passports]


def has_required_fields(passport: Passport) -> bool:
    return REQUIRED_FIELDS.issubset(passport.keys())


def valid_height(height: str) -> bool:
    if height.endswith("cm"):
        hgt = height.replace("cm", "")
        try:
            return 150 <= int(hgt) <= 193
        except TypeError:
            return False
    elif height.endswith("in"):
        hgt = height.replace("in", "")
        try:
            return 59 <= int(hgt) <= 76
        except TypeError:
            return False
    return False


def is_valid_passport(p: Passport) -> bool:
    return all(
        [
            has_required_fields(p),
            1920 <= int(p.get("byr", -1)) <= 2002,
            2010 <= int(p.get("iyr", -1)) <= 2020,
            2020 <= int(p.get("eyr", -1)) <= 2030,
            valid_height(p.get("hgt", "")),
            re.match(r"^#[0-9a-f]{6}$", p.get("hcl", "")),
            p.get("ecl") in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
            re.match(r"^[0-9]{9}$", p.get("pid", "")),
        ]
    )


if __name__ == "__main__":
    parse_data(read_data("day4.txt"))
    solution1 = sum([has_required_fields(p) for p in parse_data(read_data("day4.txt"))])
    solution2 = sum([is_valid_passport(p) for p in parse_data(read_data("day4.txt"))])
    print(f"DAY4 - part 1 {solution1}")
    print(f"DAY4 - part 2 {solution2}")
