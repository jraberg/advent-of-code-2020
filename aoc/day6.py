from collections import Counter
from functools import reduce
from os import path


def read_data(filename: str) -> str:
    file_name = path.join("..", "inputs", filename)
    with open(file_name) as file:
        return file.read()


def solve_day6_p1(raw: str) -> int:
    answers = [len(set(g.replace("\n", ""))) for g in raw.split("\n\n")]
    return reduce(lambda a, b: a + b, answers)


def solve_day6_p2(raw: str) -> int:
    groups_of_groups = [line.strip().split("\n") for line in raw.split("\n\n")]
    count_yes = []
    for groups in groups_of_groups:
        count_letters = Counter("".join([*groups]))
        all_yes = {x: count for x, count in count_letters.items() if count >= len(groups)}
        count_yes.append(len(all_yes))
    return reduce(lambda a, b: a + b, count_yes)


if __name__ == "__main__":
    raw_data = read_data("day6.txt")
    solution1 = solve_day6_p1(raw_data)
    print(f"Day6 - part1: {solution1}")

    solution2 = solve_day6_p2(raw_data)
    print(f"Day6 - part2: {solution2}")
