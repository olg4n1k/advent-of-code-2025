import sys
import re

from typing import List, Tuple
from collections.abc import Generator

def main() -> int:
    grid = _parse_input()
    n = len(grid) # square grid

    result = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j]:
                adj_count = sum([1 if grid[x][y] else 0 for (x,y) in _get_adjacent(n, i, j)])
                if adj_count < 4:
                    result += 1

    print(f"Result: {result}")
    return 0


def _get_adjacent(n: int, x: int, y: int) -> Generator[Tuple[int, int]]:
    if x > 0:
        yield (x - 1, y)
        if y > 0:
            yield (x - 1, y - 1)
        if y < n - 1:
            yield (x - 1, y + 1)
    if x < n - 1:
        yield (x + 1, y)
        if y > 0:
            yield (x + 1, y - 1)
        if y < n - 1:
            yield (x + 1, y + 1)
    if y > 0:
        yield (x, y - 1)
    if y < n - 1:
        yield (x, y + 1)


def _parse_input() -> List[List[bool]]:
    # filename = "test.txt"
    filename = "input.txt"
    with open(filename, encoding="utf-8") as file:
        data = file.readlines()
        return [[ch == '@' for ch in line.strip()] for line in data]


if __name__ == '__main__':
    sys.exit(main())
