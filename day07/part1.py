import sys
import re

from typing import List, Tuple, Set

def main() -> int:
    n, (i_s, j_s), splitters = _parse_input()

    beams = {j_s}
    result = 0
    for i in range(i_s, n):
        next = set()
        for j_b in beams:
            if (i, j_b) in splitters:
                result += 1
                if j_b > 0:
                    next.add(j_b - 1)
                if j_b < n - 1:
                    next.add(j_b + 1)
            else:
                next.add(j_b)
        beams = next

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
