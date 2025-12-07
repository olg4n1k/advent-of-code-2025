import sys
import re

from typing import List, Tuple, Set

def main() -> int:
    n, (i_s, j_s), splitters = _parse_input()

    beams = [1 if j == j_s else 0 for j in range(n)]
    for i in range(i_s, n):
        next = [0 for _ in range(n)]
        for j, paths in enumerate(beams):
            if (i, j) in splitters:
                if j > 0:
                    next[j - 1] += paths
                if j < n - 1:
                    next[j + 1] += paths
            else:
                next[j] += paths
        beams = next

    result = sum(beams)
    print(f"Result: {result}")
    return 0


def _parse_input() -> Tuple[int, Tuple[int, int], Set[Tuple[int, int]]]:
    # filename = "test.txt"
    filename = "input.txt"
    with open(filename, encoding="utf-8") as file:
        data = file.readlines()

        splitters = set()
        n = 0
        start = (-1, -1)
        for i, line in enumerate(data):
            n = len(line)
            for j, ch in enumerate(line.strip()):
                match ch:
                    case 'S':
                        start = (i, j)
                    case '^':
                        splitters.add((i, j))
                    case '.':
                        pass
                    case _:
                        raise ValueError(f"Unexpected character '{ch}'")
        return (n, start, splitters)


if __name__ == '__main__':
    sys.exit(main())
