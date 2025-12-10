import sys
import re
import math

from typing import List, Set, Tuple
from functools import cache
from collections.abc import Generator

def main() -> int:
    tiles = _parse_input()

    result = max(s for s in _calc_areas(tiles))
    print(f"Result: {result}")
    return 0


def _calc_areas(tiles: List[Tuple[int,int]]) -> Generator[int]:
    for i, (x_i, y_i) in enumerate(tiles):
        for j in range(i+1, len(tiles)):
            (x_j, y_j) = tiles[j]
            yield (abs(x_i - x_j) + 1) * (abs(y_i - y_j) + 1)


def _parse_input() -> List[Tuple[int,int]]:
    # filename = "test.txt"
    filename = "input.txt"
    with open(filename, encoding="utf-8") as file:
        data = file.readlines()

        regex = re.compile(r"(\d+),(\d+)\s*")
        def parse_box(line: str) -> Tuple[int,int]:
            match = regex.fullmatch(line)
            return (int(match.group(1)), int(match.group(2)))

        return [parse_box(line) for line in data]


if __name__ == '__main__':
    sys.exit(main())
