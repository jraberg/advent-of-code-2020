import os
import re
from typing import List, Dict


def read_data(filename: str) -> List[str]:
    data_file = os.path.join("..", "inputs", filename)
    with open(data_file) as file:
        return file.readlines()


def parse_data(lines: str) -> None:
    rules: Dict[List] = {}
    for line in lines:
        master_bag, contained_bags = line.split(" bags contain ")
        contents = [re.sub(r' bags[,. ]', "", bag) for bag in contained_bags]
        print(f"MASTER: {master_bag}\nContents: {contained_bags}\nContents: {contents}")
        # rules = { *rules, { master_bag: contents } }
    return rules


# def parse_data(lines: str) -> None:
#     for line in lines:
#         aa = re.search(r"(?P<part>.+) bags contain (?P<anum>\d+) (?P<apart>.+), (?P<bnum>\d+) (?P<bpart>.+).$", line)
#         if aa:
#             print(aa.groupdict())


if __name__ == '__main__':
    d = read_data("day7.txt")
    print(parse_data(d))
