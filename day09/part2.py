import sys
import re
import math

from typing import List, Set, Tuple
from functools import cache
from collections.abc import Generator

def main() -> int:
    tiles = _parse_input()
    min_x = min(x for (x, _) in tiles)
    max_x = max(x for (x, _) in tiles)
    min_y = min(y for (y, y) in tiles)
    max_y = max(y for (_, y) in tiles)
    print(f"x: {min_x} to {max_x}, y: {min_y} to {max_y}")
    print(f"total tiles: {(max_x - min_x + 1)*(max_y - min_y + 1)}")

    (horizontal, vertical) = _get_lines(tiles, min_x, max_x, min_y, max_y)

    def _no_intersections(x_0: int, x_1: int, y_0: int, y_1: int) -> bool:
        # We expect that x_0 <= x_1 and y_0 <= y_1
        if x_0 == x_1 or y_0 == y_1:
            # No inner tiles to check
            return True

        for x in {x_0 + 1, x_1 - 1}:
            for y in range(y_0 + 1, y_1):
                for (x_2, x_3) in horizontal[y - min_y]:
                    if x_2 <= x and x <= x_3:
                        return False

        for y in {y_0 + 1, y_1 - 1}:
            for x in range(x_0 + 1, x_1):
                for (y_2, y_3) in vertical[x - min_x]:
                    if y_2 <= y and y <= y_3:
                        return False

        return True

    def _is_green(tile_0: Tuple[int, int], tile_1: Tuple[int, int]) -> bool:
        x_0, y_0 = tile_0
        x_1, y_1 = tile_1
        return _no_intersections(min(x_0, x_1), max(x_0, x_1), min(y_0, y_1), max(y_0, y_1))

    def _valid_areas() -> Generator[int]:
        for i, tile_i in enumerate(tiles[:-1]):
            for tile_j in tiles[i+1:]:
                if _is_green(tile_i, tile_j):
                    yield _calc_area(tile_i, tile_j)

    result = max(s for s in _valid_areas())
    print(f"Result: {result}")
    return 0


def _get_lines(
        tiles: List[Tuple[int, int]],
        min_x: int,
        max_x: int,
        min_y: int,
        max_y: int
) -> Tuple[List[Set[Tuple[int, int]]], List[Set[Tuple[int, int]]]]:
    vertical = [set() for _ in range(max_x - min_x + 1)]
    horizontal = [set() for _ in range(max_y - min_y + 1)]

    prev = tiles[-1]
    for current in tiles:
        (x_0, y_0) = prev
        (x_1, y_1) = current
        
        if x_0 == x_1:
            vertical[x_0 - min_x].add((min(y_0, y_1), max(y_0, y_1)))
        elif y_0 == y_1:
            horizontal[y_0 - min_y].add((min(x_0, x_1), max(x_0, x_1)))
        else:
            raise ValueError("Invalid tile sequence")

        prev = current

    return (horizontal, vertical)


def _calc_area(tile_i: Tuple[int, int], tile_j: Tuple[int, int]) -> int:
    (x_i, y_i) = tile_i
    (x_j, y_j) = tile_j
    return (abs(x_i - x_j) + 1) * (abs(y_i - y_j) + 1)


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
