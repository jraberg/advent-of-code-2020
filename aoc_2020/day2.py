from __future__ import annotations

import os
from typing import NamedTuple, List


class Password(NamedTuple):
    password: str
    least: int
    most: int
    letter: str

    def is_valid(self):
        return self.least <= self.password.count(self.letter) <= self.most

    def is_valid2(self):
        return (self.password[self.least - 1] == self.letter[0]) ^ (self.password[self.most - 1] == self.letter)

    @staticmethod
    def parse(line: str) -> Password:
        policy, letter, password = line.strip().split()
        letter = letter[0]
        least, most = [int(a) for a in policy.split('-')]
        return Password(password, least, most, letter)


def read_data() -> List[str]:
    password_file = os.path.join('data', 'day2.txt')
    with open(password_file) as file:
        return [Password.parse(l) for l in file]


if __name__ == '__main__':
    passwords = read_data()
    print(sum(p.is_valid() for p in passwords))
    print(sum(p.is_valid2() for p in passwords))
