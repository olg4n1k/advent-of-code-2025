import sys
import re

from typing import List

def main() -> int:
    banks = _parse_input()
    
    result = 0
    for bank in banks:
        joltage = _get_max_joltage(bank)
        result += joltage

    print(f"Result: {result}")
    return 0


def _get_max_joltage(bank: List[int], digits: int = 12) -> int:
    if digits == 1:
        return max(bank)

    next_i = 0
    next = bank[0]
    for i, value in enumerate(bank[1:-digits + 1]):
        if value > next:
            next_i = i + 1 
            next = value

    return next*pow(10, digits - 1) + _get_max_joltage(bank[next_i + 1:], digits - 1)


def _parse_input() -> List[List[int]]:
    # filename = "test.txt"
    filename = "input.txt"
    with open(filename, encoding="utf-8") as file:
        data = file.readlines()
        return [[int(ch) for ch in line.strip()] for line in data]


if __name__ == '__main__':
    sys.exit(main())
