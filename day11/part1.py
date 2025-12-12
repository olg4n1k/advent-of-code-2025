import sys
import re
import math


from collections import deque

def main() -> int:
    devices = _parse_input()

    start = "you"
    end = "out"
    result = _calc_paths_dfs(devices, end, start)

    print(f"Result: {result}")
    return 0


def _calc_paths_dfs(devices: dict[str, set[str]], end: str, current: str) -> int:
    if current == end:
        return 1

    return sum(_calc_paths_dfs(devices, end, output) for output in devices[current])


def _parse_input() -> dict[str, set[str]]:
    # filename = "test.txt"
    filename = "input.txt"
    with open(filename, encoding="utf-8") as file:
        data = file.readlines()

        line_regex = re.compile(r"(\w+)\:((?: \w+)+)\s*")
        def parse_line(line: str) -> tuple[str, set[str]]:
            line_match = line_regex.fullmatch(line)

            device = line_match.group(1)
            outputs_str = line_match.group(2).strip()
            outputs = set(s for s in outputs_str.split(' '))

            return (device, outputs)

        return {k:v for (k, v) in (parse_line(line) for line in data)}


if __name__ == '__main__':
    sys.exit(main())
