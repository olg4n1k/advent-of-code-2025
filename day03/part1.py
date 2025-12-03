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


def _get_max_joltage(bank: List[int]) -> int:
    first = 0
    for i in range(len(bank) - 1):
        if bank[i] > bank[first]:
            first = i

    return bank[first]*10 + max(bank[first + 1:])


def _parse_input() -> List[List[int]]:
    # filename = "test.txt"
    filename = "input.txt"
    with open(filename, encoding="utf-8") as file:
        data = file.readlines()
        return [[int(ch) for ch in line.strip()] for line in data]


if __name__ == '__main__':
    sys.exit(main())
