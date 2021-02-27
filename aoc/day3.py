from __future__ import annotations

import os
from functools import reduce
from typing import List


def read_data(filename: str) -> List[str]:
    map_file = os.path.join("..", "inputs", filename)
    with open(map_file) as file:
        return [line.strip() for line in file.readlines()]


def walk_the_map(map: List[str], slope: List[int]) -> int:
    tree_count: int = 0
    col, row = 0, 0
    while row + slope[0] < len(map):
        row += slope[0]
        col += slope[1]
        if map[row][col % len(map[0])] == "#":
            tree_count += 1
    return tree_count


def solve_day3_p2(tree_map: List[str]) -> int:
    slopes = [[1, 1], [1, 3], [1, 5], [1, 7], [2, 1]]
    trees_by_slope = [walk_the_map(tree_map, s) for s in slopes]
    return reduce(lambda a, b: a * b, trees_by_slope)


def solve_day3_p1(tree_map: List[str]) -> int:
    return walk_the_map(tree_map, [1, 3])


if __name__ == "__main__":
    no_trees = solve_day3_p1(read_data("day3.txt"))
    print(f"DAY3 - part 1 # trees {no_trees}")

    solution2 = solve_day3_p2(read_data("day3.txt"))
    print(f"DAY3 - part 2 # trees {solution2}")
