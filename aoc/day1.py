import os
from functools import reduce
from typing import List

MAGIC_NUMBER = 2020


def read_data() -> List[int]:
    data_file = os.path.join("..", "inputs", "day1.txt")
    with open(data_file) as file:
        return [int(line) for line in file]


def solve_day1_part1(expenses: List[int]) -> List[int]:
    for i in expenses:
        for j in expenses[1:]:
            if i + j == MAGIC_NUMBER:
                return [i, j]
    return []


def solve_day1_part2(expenses: List[int]) -> List[int]:
    for i in expenses:
        for j in expenses[1:]:
            for k in expenses[2:]:
                if i + j + k == MAGIC_NUMBER:
                    return [i, j, k]
    return []


expenses = read_data()
solution1 = solve_day1_part1(expenses)
solution2 = solve_day1_part2(expenses)
print(f"DAY1 - part 1: {reduce(lambda a, b: a * b, solution1)}")
print(f"DAY1 - part 2: {reduce(lambda a, b: a * b, solution2)}")
