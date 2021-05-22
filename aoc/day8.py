from __future__ import annotations

import os
from typing import List

JMP = "jmp"

ACC = "acc"

NOP = "nop"


def read_data(filename: str) -> List:
    the_file = os.path.join("..", "inputs", filename)
    with open(the_file, encoding="utf-8") as file:
        return file.read().splitlines()


def parse_data(lines: List) -> List:
    return [line.split() for line in lines]


def run_ops(op_list: List) -> int:
    acc = 0
    i = 0
    used_ops = [False for i in op_list]
    while (i < len(op_list)) and (not used_ops[i]):
        op, arg = op_list[i][0], int(op_list[i][1])
        if op == NOP:
            used_ops[i] = True
            i += 1
        elif op == ACC:
            acc += arg
            used_ops[i] = True
            i += 1
        elif op == JMP:
            used_ops[i] = True
            i += arg
    return acc


def solve_day8_p1(op_list: List[str]) -> int:
    return run_ops(op_list)


def solve_day8_p2(op_list: List[str]) -> int:
    return run_ops(op_list)


if __name__ == '__main__':
    op_list = read_data("day8.txt")
    solution1 = solve_day8_p1(parse_data(op_list))
    print(f"Day8 - part 1: {solution1}")
    solution2 = solve_day8_p2(parse_data(op_list))
    print(f"Day8 - part 2: {solution2}")
