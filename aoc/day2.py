from __future__ import annotations

import os
import re
from typing import List, NamedTuple


class Password(NamedTuple):
    password: str
    low: int
    high: int
    letter: str

    def is_valid(self) -> bool:
        return self.low <= self.password.count(self.letter) <= self.high

    def is_valid2(self) -> bool:
        return (self.password[self.low - 1] == self.letter[0]) ^ (self.password[self.high - 1] == self.letter)

    @staticmethod
    def parse(line: str) -> Password:
        pattern = re.compile(r"(?P<low>\d+)-(?P<high>\d+) (?P<letter>\w): (?P<password>\w+)")
        matches = pattern.search(line).groupdict()
        return Password(matches["password"], int(matches["low"]), int(matches["high"]), matches["letter"])


def read_data() -> List[Password]:
    password_file = os.path.join(".", "inputs", "day2.txt")
    with open(password_file) as file:
        return [Password.parse(line) for line in file]


if __name__ == "__main__":
    passwords = read_data()
    print("Part 1", sum(p.is_valid() for p in passwords))
    print("Part 2", sum(p.is_valid2() for p in passwords))
