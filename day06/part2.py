import sys
import re

from typing import List, Tuple
from collections.abc import Generator
from functools import reduce
from itertools import takewhile

def main() -> int:
    numbers, ops = _parse_input()

    result = 0
    for i, problem in enumerate(numbers):
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

         num_lines = num_data.splitlines()
         columns = ["" for _ in range(len(num_lines[0]))]
         for line in num_lines:
              for i, ch in enumerate(line):
                   columns[i] = columns[i] + ch
         columns = [column.strip() for column in columns]

         numbers = []
         current = []
         for column in columns:
              if column:
                   current.append(int(column))
              else:
                   numbers.append(current)
                   current = []
         numbers.append(current)

         ops = [op for op in re.findall(r"[\+\*]", op_data)]
         return (numbers, ops)


if __name__ == '__main__':
    sys.exit(main())
