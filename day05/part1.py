import sys
import re

from typing import List, Tuple
from sortedcontainers import SortedKeyList

def main() -> int:
    ranges, products = _parse_input()

    index = SortedKeyList(ranges, key=lambda x: x[0])

    result = 0
    for product in products:
        if _is_fresh(index, product):
            # print(product)
            result += 1

    print(f"Result: {result}")
    return 0


def _is_fresh(index: SortedKeyList[Tuple[int, int]], product: int) -> bool:
    max_i = index.bisect_right((product, product))
    # First check if insertion point is (product, _) range
    if max_i < len(index):
        start, _ = index[max_i]
        if start == product:
            return True

    # Check all ranges to the left of insertion point
    for i in range(max_i - 1, -1, -1):
        _, end = index[i]
        if product <= end:
            return True

    return False


def _parse_input() -> Tuple[Tuple[int, int], List[int]]:
    # filename = "test.txt"
    filename = "input.txt"
    with open(filename, encoding="utf-8") as file:
        data = file.read()
        range_data, _, product_data = data.partition("\n\n")

        ranges = [(int(a), int(b)) for (a, _, b) in map(lambda s: s.partition("-"), range_data.splitlines())]
        products = [int(x) for x in product_data.splitlines()]
        return (ranges, products) 


if __name__ == '__main__':
    sys.exit(main())
