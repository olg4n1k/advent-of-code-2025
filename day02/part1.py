import sys
import re
import math


def main() -> int:
    ranges = _parse_input()
    
    result = 0
    for (a, b) in ranges:
        for x in range(a, b+1):
            if _is_invalid(x):
                result += x

    print(f"Result: {result}")
    return 0

def _is_invalid(x):
    length = math.floor(math.log10(x)) + 1
    d = int(math.pow(10, length // 2))

    return (length % 2 == 0) and (x % d == x // d)


def _parse_input():
    # filename = "test.txt"
    filename = "input.txt"
    with open(filename, encoding="utf-8") as file:
        data = file.readline()
        matches = re.findall(r"(\d+)\-(\d+)", data)
        return [(int(m[0]), int(m[1])) for m in matches]


if __name__ == '__main__':
    sys.exit(main())
