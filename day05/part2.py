import sys
import re

from typing import List, Tuple
from sortedcontainers import SortedKeyList

def main() -> int:
    ranges, _ = _parse_input()

    index = _build_index(ranges)

    result = sum([b - a + 1 for (a,b) in index])

    print(f"Result: {result}")
    return 0


def _build_index(ranges: List[Tuple[int, int]])-> SortedKeyList[Tuple[int, int]]:
    index = SortedKeyList(key=lambda x: x[0])
    for next_range in ranges:
        a, b = next_range
        i = index.bisect_right(next_range)

        # Check overlap on the left
        if i > 0:
            # a0 <= a
            a0, b0 = index[i - 1]
            if a <= b0:
                # Merge with left
                del index[i - 1]
                i = i - 1
                a = a0
                b = max(b, b0)
        
        index.add((a, b))

        # Now index i has range (_, b)
        # Check overlaps on the right
        while i + 1 < len(index):
            a1, b1 = index[i + 1]
            if a1 > b:
                # No more overlaps
                break

            if b1 > b:
                # Extend current range to b1
                b = max(b, b1)
                del index[i]
                index.add((a, b))
            del index[i + 1]

    return index



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
