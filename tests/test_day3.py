from aoc.day3 import read_data, solve_day3_p1, solve_day3_p2, walk_the_map


def test_count_trees() -> None:
    slope = [1, 3]
    no_trees = walk_the_map(TEST_MAP, slope)
    assert no_trees == 7


def test_valid_result_part1() -> None:
    solution = solve_day3_p1(read_data("day3.txt"))
    assert solution == 220


def test_valid_result_part2() -> None:
    solution = solve_day3_p2(read_data("day3.txt"))
    assert solution == 2138320800


TEST_MAP = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#""".split(
    "\n"
)
