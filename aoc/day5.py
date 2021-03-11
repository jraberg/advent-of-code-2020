# Start by considering the whole range, rows 0 through 127.
# F means to take the lower half, keeping rows 0 through 63.
# B means to take the upper half, keeping rows 32 through 63.
# F means to take the lower half, keeping rows 32 through 47.
# B means to take the upper half, keeping rows 40 through 47.
# B keeps rows 44 through 47.
# F keeps rows 44 through 45.
# The final F keeps the lower of the two, row 44.
import os
from typing import List


def read_data(filename: str) -> List[str]:
    data_file = os.path.join(".", "inputs", filename)
    with open(data_file) as file:
        return [line.strip() for line in file.readlines()]


def parse_row(location: str, low: int = 0, high: int = 127) -> int:
    if high - low == 1:
        return low if location == "F" else high
    if location[0] == "F":
        high = low + int((high - low) / 2)
    elif location[0] == "B":
        low = low + int((high - low) / 2) + 1
    return parse_row(location[1:], low, high)


def parse_column(location: str) -> int:
    return int(location.replace("L", "0").replace("R", "1"), 2)


def get_seat_id(location: str) -> int:
    return parse_row(location[:-3]) * 8 + parse_column(location[-3:])


def get_seat_ids(locations: List[str]) -> List[int]:
    return [get_seat_id(line) for line in locations]


def solve_day5_p1(locations: List[str]) -> int:
    seat_ids = [get_seat_id(line) for line in locations]
    return max(seat_ids)


def solve_day5_p2(locations: List[str]) -> int:
    ids = get_seat_ids(locations)
    return [id + 1 for id in ids if id + 1 not in ids and id + 2 in ids][0]


if __name__ == "__main__":
    location_data = read_data("day5.txt")
    max_seat_id = solve_day5_p1(location_data)
    print(f"Day1 - part 1: {max_seat_id}")

    solution2 = solve_day5_p2(location_data)
    print(f"Day1 - part 2: {solution2}")
