import sys
import re
import math

from typing import List, Set, Tuple
from functools import cache

def main() -> int:
    boxes = _parse_input()
    n = len(boxes)

    distances = []
    for i in range(n):
        for j in range(i + 1, n):
            (x_i,y_i,z_i) = boxes[i]
            (x_j,y_j,z_j) = boxes[j]
            d = math.sqrt(math.pow(x_i - x_j, 2) + math.pow(y_i - y_j, 2) + math.pow(z_i - z_j, 2))
            distances.append((i,j,d))

    distances.sort(key = lambda t: t[2])

    circuits = [{i} for i in range(n)]
    for (i,j,_) in distances[:1000]:
        circuit = next(filter(lambda c: i in c, circuits))
        if j not in circuit:
            other_circuit = next(filter(lambda c: j in c, circuits))
            circuits.remove(other_circuit)
            circuit.update(other_circuit)

    sizes = sorted(len(c) for c in circuits)
    result = sizes[-1] * sizes[-2] * sizes[-3]

    print(f"Result: {result}")
    return 0


def _parse_input() -> List[Tuple[int,int,int]]:
    # filename = "test.txt"
    filename = "input.txt"
    with open(filename, encoding="utf-8") as file:
        data = file.readlines()

        regex = re.compile(r"(\d+),(\d+),(\d+)\s*")
        def parse_box(line: str) -> Tuple[int,int,int]:
            match = regex.fullmatch(line)
            return (int(match.group(1)), int(match.group(2)), int(match.group(3)))

        return [parse_box(line) for line in data]


if __name__ == '__main__':
    sys.exit(main())
