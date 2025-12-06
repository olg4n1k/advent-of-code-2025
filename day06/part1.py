import sys
import re

from typing import List, Tuple
from collections.abc import Generator
from functools import reduce

def main() -> int:
    numbers, ops = _parse_input()

    problems = [[] for _ in range(len(ops))]
    for row in numbers:
        for i, x in enumerate(row):
            problems[i].append(x)

    result = 0
    for i, problem in enumerate(problems):
        result += _apply_op(problem, ops[i])

    print(f"Result: {result}")
    return 0


def _apply_op(problem: List[int], op: str) -> int:
    match op:
        case '+':
            return sum(problem)
        case '*':
            return reduce(lambda x, y: x * y, problem)
        case _:
            raise ValueError(f"Unsupported op: {op}")


def _parse_input() -> Tuple[List[List[int]], List[str]]:
    # filename = "test.txt"
    filename = "input.txt"
    with open(filename, encoding="utf-8") as file:
        data = file.read()
        num_data, _, op_data = data.strip().rpartition("\n")

        numbers = [[int(x) for x in re.findall(r"\d+", row)] for row in num_data.splitlines()]
        ops = [op for op in re.findall(r"[\+\*]", op_data)]
        return (numbers, ops)


if __name__ == '__main__':
    sys.exit(main())
